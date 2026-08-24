import contextlib
import csv
import io
import re
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from goodreads_to_reading import (
    add_covers,
    book_id,
    clean_title,
    fetch_series_urls,
    main,
    parse_export,
    quote,
    read_existing,
    render,
    series_url,
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
            "note": "Good one.",
        }

        text = render(
            "https://example.com/me", "2026-01-02", {}, {}, {"Technical": [book]}
        )

        self.assertEqual(
            text,
            "# yaml-language-server: $schema=../schemas/reading.json\n"
            "profile: https://example.com/me\n"
            'updated: "2026-01-02"\n'
            "categories:\n"
            "  - name: Technical\n"
            "    books:\n"
            "      - title: The Pragmatic Programmer\n"
            "        author: Andy Hunt\n"
            "        year: 1999\n"
            "        rating: 5\n"
            "        url: https://www.goodreads.com/book/show/4099\n"
            "        cover: https://example.com/4099.jpg\n"
            "        note: Good one.\n",
        )

    def test_sorts_categories_with_miscellaneous_last_and_books_by_title(self):
        def book(book_id, title):
            return {"id": book_id, "title": title, "author": "A", "year": None,
                    "rating": 4}

        text = render(
            None,
            None,
            {},
            {},
            {
                "Miscellaneous": [book("1", "Zebra")],
                "Technical": [book("2", "b title"), book("3", "A title")],
                "Fiction": [book("4", "Novel")],
            },
        )

        self.assertEqual(
            [line for line in text.splitlines() if "name:" in line or "title:" in line],
            [
                "  - name: Fiction",
                "      - title: Novel",
                "  - name: Technical",
                "      - title: A title",
                "      - title: b title",
                "  - name: Miscellaneous",
                "      - title: Zebra",
            ],
        )

    def test_comments_the_excluded_ids_with_their_titles(self):
        text = render(None, None, {"7": "Zebra", "8": "Apple"}, {}, {})

        self.assertEqual(
            text.splitlines()[1:4],
            ["excluded:", '  - "8" # Apple', '  - "7" # Zebra'],
        )


class ReadExistingTest(unittest.TestCase):
    def test_returns_nothing_for_a_missing_file(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual(
                read_existing(Path(directory) / "absent.yaml"),
                (None, None, [], {}, {}),
            )

    def test_reads_back_what_render_wrote(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "reading.yaml"
            book = {
                "id": "4099",
                "title": "Book",
                "author": "Author",
                "year": None,
                "rating": 5,
                "note": "Note.",
                "cover": "https://example.com/c.jpg",
            }
            book["series"] = "Some Series"
            path.write_text(
                render(
                    "https://example.com/me",
                    "2026-01-02",
                    {"7": "Gone"},
                    {"Some Series": "https://example.com/s"},
                    {"Technical": [book]},
                )
            )

            profile, updated, excluded, links, known = read_existing(path)

            self.assertEqual(profile, "https://example.com/me")
            self.assertEqual(updated, "2026-01-02")
            self.assertEqual(excluded, ["7"])
            self.assertEqual(links, {"Some Series": "https://example.com/s"})
            self.assertEqual(known["4099"]["series"], "Some Series")
            self.assertEqual(known["4099"]["category"], "Technical")
            self.assertEqual(known["4099"]["note"], "Note.")
            self.assertEqual(known["4099"]["cover"], "https://example.com/c.jpg")


class SeriesUrlTest(unittest.TestCase):
    def test_matches_a_name_whose_apostrophe_was_normalized(self):
        self.assertEqual(
            series_url(SERIES_JSON, "The Hitchhiker's Guide to the Galaxy"),
            "https://www.goodreads.com/series/40957-x",
        )

    def test_returns_none_for_another_series_or_an_empty_page(self):
        self.assertIsNone(series_url(SERIES_JSON, "Frontlines"))
        self.assertIsNone(series_url(None, "Frontlines"))


class FetchSeriesUrlsTest(unittest.TestCase):
    def test_only_fetches_series_without_a_link(self):
        books = [
            {"id": "1", "title": "One", "series": "Known"},
            {"id": "2", "title": "Two", "series": "Fresh"},
            {"id": "3", "title": "Three"},
        ]
        links = {"Known": "https://example.com/known"}

        with patch("goodreads_to_reading.fetch_page", return_value=SERIES_JSON) as page:
            with patch(
                "goodreads_to_reading.series_url", return_value="https://example.com/f"
            ):
                with quiet():
                    added = fetch_series_urls(books, links, 0)

        page.assert_called_once()
        self.assertEqual(added, 1)
        self.assertEqual(links["Fresh"], "https://example.com/f")


class AddCoversTest(unittest.TestCase):
    def test_only_fetches_books_that_have_no_cover(self):
        books = [
            {"id": "1", "title": "Has one", "cover": "https://example.com/1.jpg"},
            {"id": "2", "title": "Needs one", "cover": None},
        ]

        with patch("goodreads_to_reading.fetch_cover", return_value="c.jpg") as fetch:
            with quiet():
                fetched = add_covers(books, 0, lambda: None)

        fetch.assert_called_once()
        self.assertEqual(fetched, 1)
        self.assertEqual(books[1]["cover"], "c.jpg")

    def test_gives_up_once_goodreads_keeps_refusing(self):
        books = [{"id": str(i), "title": str(i), "cover": None} for i in range(20)]

        with patch("goodreads_to_reading.fetch_cover", return_value=None) as fetch:
            with quiet():
                fetched = add_covers(books, 0, lambda: None)

        self.assertEqual(fetched, 0)
        self.assertEqual(fetch.call_count, 5)


class MainTest(unittest.TestCase):
    def test_imports_and_then_keeps_category_note_and_date(self):
        with tempfile.TemporaryDirectory() as directory:
            export = write_export(directory, [row("1", "First"), row("2", "Second")])
            output = Path(directory) / "reading.yaml"
            argv = [
                "goodreads_to_reading.py",
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
            url = "        url: https://www.goodreads.com/book/show/1\n"
            edited = edited.replace(url, url + "        note: Mine.\n")
            output.write_text(edited)
            before = output.read_text()

            with patch("sys.argv", argv), quiet():
                main()

            self.assertEqual(output.read_text(), before)

    def test_leaves_excluded_books_out(self):
        with tempfile.TemporaryDirectory() as directory:
            export = write_export(directory, [row("1", "Kept"), row("2", "Dropped")])
            output = Path(directory) / "reading.yaml"
            output.write_text(
                "# yaml-language-server: $schema=../schemas/reading.json\n"
                "excluded:\n"
                '  - "2"\n'
                "categories: []\n"
            )
            argv = [
                "goodreads_to_reading.py",
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
