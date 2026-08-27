import contextlib
import csv
import io
import re
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from goodreads_to_books import (
    BOOKS_SORT,
    EXCLUDED_SORT,
    OVERRIDES_SORT,
    add_covers,
    apply_override,
    book_id,
    clean_title,
    fetch_series,
    main,
    marker,
    parse_export,
    quote,
    read_existing,
    render,
    series_url,
    series_works,
    without_updated,
)

SERIES_JSON = (
    '{"__typename":"Series","id":"kca://series/x",'
    '"title":"The Hitchhiker\u2019s Guide to the Galaxy",'
    '"webUrl":"https://www.goodreads.com/series/40957-x"}'
)

COLUMNS = [
    "Book Id",
    "Title",
    "Author",
    "My Rating",
    "Year Published",
    "Original Publication Year",
    "Exclusive Shelf",
]


@contextlib.contextmanager
def quiet():
    """Swallow the progress lines the importer prints."""
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(
        io.StringIO()
    ):
        yield


def write_export(directory, rows):
    """Write a Goodreads style CSV export holding the given rows."""
    path = Path(directory) / "export.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=COLUMNS)
        writer.writeheader()
        for row in rows:
            writer.writerow({column: row.get(column, "") for column in COLUMNS})
    return path


def row(book_id, title, rating="5.0", shelf="read", **extra):
    """Build one CSV row, so tests only spell out what they care about."""
    return dict(
        {
            "Book Id": book_id,
            "Title": title,
            "Author": "Ada Lovelace",
            "My Rating": rating,
            "Original Publication Year": "1999",
            "Exclusive Shelf": shelf,
        },
        **extra,
    )


class BookIdTest(unittest.TestCase):
    def test_reads_the_id_out_of_a_book_url(self):
        self.assertEqual(book_id("https://www.goodreads.com/book/show/4099"), "4099")

    def test_returns_none_without_a_usable_url(self):
        self.assertIsNone(book_id("https://example.com/4099"))
        self.assertIsNone(book_id(None))


class CleanTitleTest(unittest.TestCase):
    def test_drops_a_trailing_series_marker(self):
        self.assertEqual(clean_title("Dune (Dune, #1)"), "Dune")

    def test_keeps_parentheses_that_are_not_a_series(self):
        self.assertEqual(
            clean_title("Naked Statistics (Revised)"), "Naked Statistics (Revised)"
        )

    def test_drops_the_quotes_a_title_is_wrapped_in(self):
        self.assertEqual(
            clean_title('"Surely You\'re Joking, Mr. Feynman!": Adventures'),
            "Surely You're Joking, Mr. Feynman!: Adventures",
        )

    def test_keeps_quotes_inside_a_title(self):
        self.assertEqual(clean_title('Say "hi" to the world'), 'Say "hi" to the world')

    def test_normalizes_smart_quotes_and_spacing(self):
        self.assertEqual(clean_title("It\u2019s  Alive"), "It's Alive")


class QuoteTest(unittest.TestCase):
    def test_leaves_a_plain_string_alone(self):
        self.assertEqual(quote("The Martian"), "The Martian")

    def test_quotes_a_string_yaml_would_read_as_a_number(self):
        self.assertEqual(quote("1984"), '"1984"')

    def test_leaves_inner_double_quotes_unquoted(self):
        self.assertEqual(quote('Say "hi"'), 'Say "hi"')

    def test_uses_single_quotes_when_the_text_opens_with_a_double_quote(self):
        self.assertEqual(
            quote('"Surely You\'re Joking": Adventures'),
            "'\"Surely You''re Joking\": Adventures'",
        )


class WithoutUpdatedTest(unittest.TestCase):
    def test_removes_only_the_updated_line(self):
        text = 'profile: x\nupdated: "2026-01-01"\ncategories:\n'
        self.assertEqual(without_updated(text), "profile: x\ncategories:")


class ParseExportTest(unittest.TestCase):
    def test_keeps_read_books_above_the_rating_and_skips_the_rest(self):
        with tempfile.TemporaryDirectory() as directory:
            path = write_export(
                directory,
                [
                    row("1", "Kept"),
                    row("2", "Too low", rating="3.0"),
                    row("3", "Unread", shelf="to-read"),
                    row("4", "Excluded"),
                ],
            )

            books = parse_export(path, 5, ["4"])

            self.assertEqual([book["title"] for book in books], ["Kept"])
            self.assertEqual(books[0]["rating"], 5)
            self.assertEqual(books[0]["year"], 1999)

    def test_falls_back_to_the_publication_year(self):
        with tempfile.TemporaryDirectory() as directory:
            path = write_export(
                directory,
                [
                    row(
                        "1",
                        "No original year",
                        **{"Original Publication Year": "", "Year Published": "2008"},
                    )
                ],
            )

            self.assertEqual(parse_export(path, 5, [])[0]["year"], 2008)


class RenderTest(unittest.TestCase):
    def test_writes_every_field_it_was_given(self):
        book = {
            "id": "4099",
            "title": "The Pragmatic Programmer",
            "author": "Andy Hunt",
            "year": 1999,
            "rating": 5,
            "cover": "https://example.com/4099.jpg",
        }

        text = render(
            "https://example.com/me", "2026-01-02", {}, {}, {}, {"Technical": [book]}
        )

        self.assertEqual(
            text,
            "# yaml-language-server: $schema=../schemas/books.json\n"
            "profile: https://example.com/me\n"
            'updated: "2026-01-02"\n'
            "categories:\n"
            "  - name: Technical\n"
            "    books:\n"
            + marker(BOOKS_SORT, "      ") + "\n"
            "      - title: The Pragmatic Programmer\n"
            "        author: Andy Hunt\n"
            "        year: 1999\n"
            "        rating: 5\n"
            "        url: https://www.goodreads.com/book/show/4099\n"
            "        cover: https://example.com/4099.jpg\n"
            + marker("end", "        ") + "\n",
        )

    def test_sorts_categories_with_miscellaneous_last_and_books_by_year(self):
        def book(book_id, title, year=None):
            return {"id": book_id, "title": title, "author": "A", "year": year,
                    "rating": 4}

        text = render(
            None,
            None,
            {},
            {},
            {},
            {
                "Miscellaneous": [book("1", "Zebra")],
                "Technical": [
                    book("2", "older", 1999),
                    book("3", "newer", 2020),
                    book("4", "same year, later title", 1999),
                ],
                "Fiction": [book("5", "Novel")],
            },
        )

        self.assertEqual(
            [line for line in text.splitlines() if "name:" in line or "title:" in line],
            [
                "  - name: Fiction",
                "      - title: Novel",
                "  - name: Technical",
                "      - title: newer",
                "      - title: same year, later title",
                "      - title: older",
                "  - name: Miscellaneous",
                "      - title: Zebra",
            ],
        )

    def test_comments_the_excluded_ids_with_their_titles(self):
        text = render(None, None, {"7": "Zebra", "8": "Apple"}, {}, {}, {})

        # The markers come from the module: spelling them out here would let
        # the keep-sorted hook treat this expectation as a block to sort.
        self.assertEqual(
            text.splitlines()[1:6],
            [
                "excluded:",
                marker(EXCLUDED_SORT),
                '  - "8" # Apple',
                '  - "7" # Zebra',
                marker("end"),
            ],
        )

    def test_breaks_a_tie_on_the_title_with_the_id(self):
        text = render(
            None, None, {"58493107": "Goomics", "41810925": "Goomics"}, {}, {}, {}
        )

        self.assertEqual(
            [line for line in text.splitlines() if line.startswith("  - ")],
            ['  - "41810925" # Goomics', '  - "58493107" # Goomics'],
        )


class RenderOverridesTest(unittest.TestCase):
    def test_leads_each_entry_with_its_title_and_sorts_them(self):
        overrides = {
            "2": {"id": "2", "title": "Zebra", "url": "https://example.com/z"},
            "1": {"id": "1", "title": "Apple"},
        }

        text = render(None, None, {}, {}, overrides, {})

        self.assertEqual(
            text.splitlines()[1:8],
            [
                "overrides:",
                marker(OVERRIDES_SORT),
                "  - title: Apple",
                '    id: "1"',
                "  - title: Zebra",
                '    id: "2"',
                "    url: https://example.com/z",
            ],
        )
        self.assertEqual(text.splitlines()[8], marker("end", "    "))


class ReadExistingTest(unittest.TestCase):
    def test_returns_nothing_for_a_missing_file(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual(
                read_existing(Path(directory) / "absent.yaml"),
                (None, None, [], {}, {}, {}),
            )

    def test_reads_back_what_render_wrote(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "books.yaml"
            book = {
                "id": "4099",
                "title": "Book",
                "author": "Author",
                "year": None,
                "rating": 5,
                "cover": "https://example.com/c.jpg",
            }
            book["series"] = "Some Series"
            path.write_text(
                render(
                    "https://example.com/me",
                    "2026-01-02",
                    {"7": "Gone"},
                    {"Some Series": {"url": "https://example.com/s", "count": 4}},
                    {},
                    {"Technical": [book]},
                )
            )

            profile, updated, excluded, links, overrides, known = read_existing(path)

            self.assertEqual(profile, "https://example.com/me")
            self.assertEqual(updated, "2026-01-02")
            self.assertEqual(excluded, ["7"])
            self.assertEqual(
                links, {"Some Series": {"url": "https://example.com/s", "count": 4}}
            )
            self.assertEqual(known["4099"]["series"], "Some Series")
            self.assertEqual(known["4099"]["category"], "Technical")
            self.assertEqual(known["4099"]["cover"], "https://example.com/c.jpg")


class OverrideTest(unittest.TestCase):
    def test_replaces_only_the_fields_it_carries(self):
        book = {
            "id": "15779555",
            "title": "O Poderoso Chefao",
            "author": "Mario Puzo",
            "year": 1969,
            "rating": 5,
            "cover": "https://example.com/pt.jpg",
        }

        apply_override(
            book,
            {
                "id": "15779555",
                "title": "The Godfather",
                "url": "https://www.goodreads.com/book/show/22034",
                "cover": "https://example.com/en.jpg",
            },
        )

        self.assertEqual(book["title"], "The Godfather")
        self.assertEqual(book["url"], "https://www.goodreads.com/book/show/22034")
        self.assertEqual(book["cover"], "https://example.com/en.jpg")
        self.assertEqual(book["author"], "Mario Puzo")
        self.assertEqual(book["year"], 1969)

    def test_an_override_keeps_the_category_of_the_shelved_edition(self):
        with tempfile.TemporaryDirectory() as directory:
            export = write_export(directory, [row("15779555", "O Poderoso Chefao")])
            output = Path(directory) / "books.yaml"
            output.write_text(
                "# yaml-language-server: $schema=../schemas/books.json\n"
                "overrides:\n"
                '  - id: "15779555"\n'
                "    title: The Godfather\n"
                "    url: https://www.goodreads.com/book/show/22034\n"
                "categories:\n"
                "  - name: Fiction\n"
                "    books:\n"
                "      - title: The Godfather\n"
                "        author: Ada Lovelace\n"
                "        rating: 5\n"
                "        url: https://www.goodreads.com/book/show/22034\n"
            )
            argv = [
                "goodreads_to_books.py",
                str(export),
                "--output",
                str(output),
                "--no-covers",
            ]

            with patch("sys.argv", argv), quiet():
                main()
            text = output.read_text()

            self.assertIn("  - name: Fiction\n", text)
            self.assertNotIn("Miscellaneous", text)
            self.assertIn("        url: https://www.goodreads.com/book/show/22034\n", text)
            self.assertNotIn("O Poderoso Chefao", text)


class SeriesUrlTest(unittest.TestCase):
    def test_matches_a_name_whose_apostrophe_was_normalized(self):
        self.assertEqual(
            series_url(SERIES_JSON, "The Hitchhiker's Guide to the Galaxy"),
            "https://www.goodreads.com/series/40957-x",
        )

    def test_returns_none_for_another_series_or_an_empty_page(self):
        self.assertIsNone(series_url(SERIES_JSON, "Frontlines"))
        self.assertIsNone(series_url(None, "Frontlines"))


class FetchSeriesTest(unittest.TestCase):
    def test_only_fetches_what_a_series_is_missing(self):
        books = [
            {"id": "1", "title": "One", "series": "Known"},
            {"id": "2", "title": "Two", "series": "Fresh"},
            {"id": "3", "title": "Three"},
        ]
        links = {"Known": {"url": "https://example.com/known", "count": 3}}

        with patch("goodreads_to_books.fetch_page", return_value=SERIES_JSON) as page:
            with patch(
                "goodreads_to_books.fetch_url", return_value="8 primary works"
            ) as series_page:
                with patch(
                    "goodreads_to_books.series_url",
                    return_value="https://example.com/f",
                ):
                    with quiet():
                        added = fetch_series(books, links, 0)

        page.assert_called_once()
        series_page.assert_called_once()
        self.assertEqual(added, 1)
        self.assertEqual(
            links["Fresh"], {"url": "https://example.com/f", "count": 8}
        )
        self.assertEqual(
            links["Known"], {"url": "https://example.com/known", "count": 3}
        )

    def test_reads_the_work_count_off_a_series_page(self):
        self.assertEqual(series_works("7 primary works 9 total works"), 7)
        self.assertIsNone(series_works("no counts here"))
        self.assertIsNone(series_works(None))


class AddCoversTest(unittest.TestCase):
    def test_only_fetches_books_that_have_no_cover(self):
        books = [
            {"id": "1", "title": "Has one", "cover": "https://example.com/1.jpg"},
            {"id": "2", "title": "Needs one", "cover": None},
        ]

        with patch("goodreads_to_books.fetch_cover", return_value="c.jpg") as fetch:
            with quiet():
                fetched = add_covers(books, 0, lambda: None)

        fetch.assert_called_once()
        self.assertEqual(fetched, 1)
        self.assertEqual(books[1]["cover"], "c.jpg")

    def test_gives_up_once_goodreads_keeps_refusing(self):
        books = [{"id": str(i), "title": str(i), "cover": None} for i in range(20)]

        with patch("goodreads_to_books.fetch_cover", return_value=None) as fetch:
            with quiet():
                fetched = add_covers(books, 0, lambda: None)

        self.assertEqual(fetched, 0)
        self.assertEqual(fetch.call_count, 5)


class MainTest(unittest.TestCase):
    def test_imports_and_then_keeps_category_and_date(self):
        with tempfile.TemporaryDirectory() as directory:
            export = write_export(directory, [row("1", "First"), row("2", "Second")])
            output = Path(directory) / "books.yaml"
            argv = [
                "goodreads_to_books.py",
                str(export),
                "--output",
                str(output),
                "--no-covers",
            ]

            with patch("sys.argv", argv), quiet():
                main()
            first = output.read_text()

            self.assertIn("  - name: Miscellaneous\n", first)
            self.assertIn("updated:", first)

            edited = re.sub(
                r'^updated: ".*"$', 'updated: "2020-01-01"', first, flags=re.M
            )
            edited = edited.replace("  - name: Miscellaneous", "  - name: Fiction")
            output.write_text(edited)
            before = output.read_text()

            with patch("sys.argv", argv), quiet():
                main()

            self.assertEqual(output.read_text(), before)

    def test_leaves_excluded_books_out(self):
        with tempfile.TemporaryDirectory() as directory:
            export = write_export(directory, [row("1", "Kept"), row("2", "Dropped")])
            output = Path(directory) / "books.yaml"
            output.write_text(
                "# yaml-language-server: $schema=../schemas/books.json\n"
                "excluded:\n"
                '  - "2"\n'
                "categories: []\n"
            )
            argv = [
                "goodreads_to_books.py",
                str(export),
                "--output",
                str(output),
                "--no-covers",
            ]

            with patch("sys.argv", argv), quiet():
                main()
            text = output.read_text()

            self.assertIn("- title: Kept", text)
            self.assertNotIn("- title: Dropped", text)
            self.assertIn('  - "2" # Dropped', text)


if __name__ == "__main__":
    unittest.main()
