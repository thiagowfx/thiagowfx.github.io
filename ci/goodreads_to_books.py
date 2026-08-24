#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["PyYAML"]
# ///
"""
Import a Goodreads CSV export into data/books.yaml.

Usage:
    ci/goodreads_to_books.py ~/Downloads/goodreads_library_export.csv
    ci/goodreads_to_books.py export.csv --min-rating 4 --no-covers

Keeps only books on the "read" shelf whose rating is at least --min-rating.
Category placement survives re-imports: books already present in
data/books.yaml keep their category, series and cover, matched by
their Goodreads book id. New books land in the "Miscellaneous" category, and
book ids listed under "excluded" stay out of the page for good. Deleting a book
by hand and re-importing brings it back, so --exclude-missing turns every book
missing from the data file into an excluded one instead. An entry under
"overrides" replaces what the CSV says about one book, which is how a shelved
translation ends up pointing at the edition worth linking.

The CSV export carries no cover image, so each new book costs one request to
its public Goodreads page, whose og:image points at the cover on Amazon's CDN.
The same page names the series a book belongs to, so one request per series
fills in its link under "series", and one more reads how many primary works
the series holds, which is what the page shows next to a collapsed series.
Covers already in the data file are never fetched again, and the file is saved
as they arrive, so a run that Goodreads cuts short resumes where it stopped.
Goodreads answers with an AWS WAF challenge when it finds the requests too
frequent; this gives up after a few of those, and the next run picks up again.
"""

import argparse
import csv
import datetime
import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request

import yaml

DATA_FILE = pathlib.Path(__file__).resolve().parent.parent / "data" / "books.yaml"
SCHEMA_REF = "# yaml-language-server: $schema=../schemas/books.json"
MISCELLANEOUS = "Miscellaneous"
BOOK_URL = "https://www.goodreads.com/book/show/{id}"
COVER_PATTERN = re.compile(r'<meta property="og:image" content="([^"]+)"')
SERIES_WORKS_PATTERN = re.compile(r"([0-9]+) primary works")
SERIES_PATTERN = re.compile(
    r'\{"__typename":"Series","id":"[^"]*",'
    r'"title":"((?:[^"\\]|\\.)*)","webUrl":"([^"]*)"\}'
)
# Goodreads serves this placeholder for books with no cover.
COVER_PLACEHOLDER = "nophoto"
# Goodreads answers 202 with an empty body unless the agent looks like a browser.
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    " (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
COVER_DELAY_SECONDS = 3.0
# Consecutive failures that mean Goodreads is refusing us, not a missing cover.
COVER_FAILURE_LIMIT = 5
# How many new covers to collect before saving, so a cut-short run keeps them.
COVER_SAVE_EVERY = 10
# The fix-smartquotes prek hook rewrites these, so normalize them on import.
SMART_QUOTES = {"\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"'}
# Sorts the excluded ids by their title comment. Its own start marker is built
# at runtime, so the keep-sorted hook does not mistake it for one of its own.
EXCLUDED_SORT = "start case=no by_regex=" + r"\d\D\s(.*)$"


def marker(directive):
    """Render a keep-sorted comment for the data file."""
    return "  # keep-{} {}".format("sorted", directive)


def without_updated(text):
    """Drop the updated line, so it does not count as a change to the books."""
    kept = [line for line in text.splitlines() if not line.startswith("updated:")]
    return "\n".join(kept).strip()


def book_id(url):
    """Extract the Goodreads book id from a book URL."""
    match = re.search(r"/book/show/(\d+)", url or "")
    return match.group(1) if match else None


def read_existing(path):
    """Return (profile, updated, excluded, links, overrides, books) from a file."""
    if not path.exists():
        return None, None, [], {}, {}, {}
    data = yaml.safe_load(path.read_text()) or {}
    overrides = {str(entry["id"]): entry for entry in data.get("overrides") or []}
    # An override moves the entry's url, so map it back to the id in the CSV.
    shelved = {
        book_id(entry["url"]): key
        for key, entry in overrides.items()
        if entry.get("url")
    }
    known = {}
    for category in data.get("categories") or []:
        for book in category.get("books") or []:
            key = book_id(book.get("url"))
            key = shelved.get(key, key)
            if key:
                known[key] = dict(book, category=category["name"])
    excluded = [str(key) for key in data.get("excluded") or []]
    links = {
        entry["name"]: {
            field: entry[field] for field in ("url", "count") if field in entry
        }
        for entry in data.get("series") or []
    }
    return (
        data.get("profile"),
        data.get("updated"),
        excluded,
        links,
        overrides,
        known,
    )


def apply_override(book, override):
    """Replace what the CSV said about a book with the override's fields."""
    for field in ("title", "author", "year", "url", "cover"):
        if override.get(field) is not None:
            book[field] = override[field]
    return book


def fetch_url(url, label):
    """Return the HTML of a public Goodreads page, or None."""
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            status = response.status
            page = response.read().decode("utf-8", "replace")
    except (urllib.error.URLError, TimeoutError) as error:
        print("  {}: {}".format(label, error), file=sys.stderr)
        return None
    if status != 200 or not page:
        print(
            "  {}: HTTP {}, {} bytes".format(label, status, len(page)),
            file=sys.stderr,
        )
        return None
    return page


def fetch_page(book):
    """Return the HTML of a book's public Goodreads page, or None."""
    return fetch_url(
        book.get("url") or BOOK_URL.format(id=book["id"]), book["title"]
    )


def series_url(page, name):
    """Return the series page URL named in a book page, or None."""
    for title, url in SERIES_PATTERN.findall(page or ""):
        # Goodreads writes curly apostrophes, the data file straight ones.
        if plain_text(json.loads('"{}"'.format(title))) == plain_text(name):
            return url
    return None


def series_works(page):
    """Return how many primary works a series page lists, or None."""
    match = SERIES_WORKS_PATTERN.search(page or "")
    return int(match.group(1)) if match else None


def fetch_series(books, links, delay):
    """Fill in the link and size of every series that lacks them. Returns how many."""
    named = sorted({book["series"] for book in books if book.get("series")})
    added = 0
    for name in named:
        entry = links.setdefault(name, {})
        if not entry.get("url"):
            volumes = [book for book in books if book.get("series") == name]
            print("series link: {}".format(name))
            url = series_url(fetch_page(volumes[0]), name)
            time.sleep(delay)
            if url:
                entry["url"] = url
                added += 1
            else:
                print("  {}: no series page".format(name), file=sys.stderr)
        if entry.get("url") and not entry.get("count"):
            print("series size: {}".format(name))
            count = series_works(fetch_url(entry["url"], name))
            time.sleep(delay)
            if count:
                entry["count"] = count
            else:
                print("  {}: no work count".format(name), file=sys.stderr)
        if not entry:
            del links[name]
    return added


def fetch_cover(book):
    """Return the cover URL from a book's public Goodreads page, or None."""
    page = fetch_page(book)
    if not page:
        return None
    match = COVER_PATTERN.search(page)
    if not match or COVER_PLACEHOLDER in match.group(1):
        print("  {}: no cover".format(book["title"]), file=sys.stderr)
        return None
    return match.group(1)


def add_covers(books, delay, save):
    """Fill in the cover of every book that has none yet. Returns how many."""
    missing = [book for book in books if not book.get("cover")]
    fetched = 0
    failures = 0
    for index, book in enumerate(missing, 1):
        print("cover {}/{}: {}".format(index, len(missing), book["title"]))
        book["cover"] = fetch_cover(book)
        if book["cover"]:
            fetched += 1
            failures = 0
            if fetched % COVER_SAVE_EVERY == 0:
                save()
        else:
            failures += 1
        if failures >= COVER_FAILURE_LIMIT:
            print(
                "giving up after {} failures in a row; run again later to"
                " fetch the remaining {} covers".format(failures, len(missing) - index),
                file=sys.stderr,
            )
            break
        time.sleep(delay)
    return fetched


def excluded_titles(path, excluded):
    """Return {book id: title} for the excluded books, to comment the list."""
    titles = {}
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row["Book Id"] in excluded:
                titles[row["Book Id"]] = clean_title(row["Title"])
    for key in excluded:
        titles.setdefault(key, "unknown")
    return titles


def parse_export(path, min_rating, excluded):
    """Return the read, highly rated books from a Goodreads CSV export."""
    books = []
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row["Exclusive Shelf"] != "read":
                continue
            if row["Book Id"] in excluded:
                continue
            rating = int(float(row["My Rating"] or 0))
            if rating < min_rating:
                continue
            year = row["Original Publication Year"] or row["Year Published"]
            books.append(
                {
                    "id": row["Book Id"],
                    "title": clean_title(row["Title"]),
                    "author": plain_text(row["Author"]),
                    "year": int(float(year)) if year else None,
                    "rating": rating,
                }
            )
    return books


def plain_text(value):
    """Normalize smart quotes and collapse runs of whitespace."""
    for smart, plain in SMART_QUOTES.items():
        value = value.replace(smart, plain)
    return re.sub(r"\s+", " ", value).strip()


def clean_title(title):
    """Drop a trailing series marker, e.g. "Dune (Dune, #1)" -> "Dune"."""
    return plain_text(re.sub(r"\s*\([^()]*#\d+[^()]*\)\s*$", "", title))


def quote(value):
    """Quote a YAML scalar unless the plain style reads back as the same string."""
    text = str(value)
    try:
        parsed = yaml.safe_load("v: {}".format(text))["v"]
    except yaml.YAMLError:
        parsed = None
    if parsed != text:
        # Match how prettier quotes: single quotes when they need fewer escapes.
        if '"' in text:
            return "'{}'".format(text.replace("'", "''"))
        return '"{}"'.format(text.replace("\\", "\\\\"))
    return text


def render(profile, updated, excluded, links, overrides, categories):
    """Render the data file. This script owns the order, so no sort markers."""
    lines = [SCHEMA_REF]
    if profile:
        lines.append("profile: {}".format(quote(profile)))
    if updated:
        lines.append('updated: "{}"'.format(updated))
    if excluded:
        lines.append("excluded:")
        lines.append(marker(EXCLUDED_SORT))
        # Ties on the title fall back to the id, the way keep-sorted breaks them.
        for key, title in sorted(
            excluded.items(), key=lambda item: (item[1].casefold(), item[0])
        ):
            lines.append('  - "{}" # {}'.format(key, title))
        lines.append(marker("end"))
    if overrides:
        lines.append("overrides:")
        for key in sorted(overrides, key=lambda key: overrides[key]["title"].casefold()):
            entry = overrides[key]
            lines.append('  - id: "{}"'.format(key))
            for field in ("title", "author", "year", "url", "cover", "shelved"):
                if entry.get(field) is not None:
                    lines.append("    {}: {}".format(field, quote(entry[field])))
    if links:
        lines.append("series:")
        for name in sorted(links, key=str.casefold):
            lines.append("  - name: {}".format(quote(name)))
            lines.append("    url: {}".format(quote(links[name]["url"])))
            if links[name].get("count"):
                lines.append("    count: {}".format(links[name]["count"]))
    lines.append("categories:")
    ordered = sorted(categories, key=lambda n: (n == MISCELLANEOUS, n.casefold()))
    for name in ordered:
        lines.append("  - name: {}".format(quote(name)))
        lines.append("    books:")
        for book in sorted(categories[name], key=lambda b: b["title"].casefold()):
            lines.append("      - title: {}".format(quote(book["title"])))
            lines.append("        author: {}".format(quote(book["author"])))
            if book["year"]:
                lines.append("        year: {}".format(book["year"]))
            lines.append("        rating: {}".format(book["rating"]))
            url = book.get("url") or BOOK_URL.format(id=book["id"])
            lines.append("        url: {}".format(url))
            if book.get("series"):
                lines.append("        series: {}".format(quote(book["series"])))
            if book.get("cover"):
                lines.append("        cover: {}".format(quote(book["cover"])))
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", type=pathlib.Path, help="Goodreads CSV export")
    parser.add_argument(
        "--min-rating",
        type=int,
        default=5,
        choices=range(1, 6),
        help="lowest rating to import (default: 5)",
    )
    parser.add_argument(
        "--output", type=pathlib.Path, default=DATA_FILE, help="data file to write"
    )
    parser.add_argument(
        "--exclude",
        nargs="+",
        default=[],
        metavar="ID",
        help="Goodreads book ids to keep out of the page for good",
    )
    parser.add_argument(
        "--exclude-missing",
        action="store_true",
        help="also exclude every book the data file no longer lists",
    )
    parser.add_argument(
        "--no-covers",
        action="store_true",
        help="skip fetching covers for books that have none yet",
    )
    parser.add_argument(
        "--cover-delay",
        type=float,
        default=COVER_DELAY_SECONDS,
        help="seconds to wait between cover requests (default: {})".format(
            COVER_DELAY_SECONDS
        ),
    )
    args = parser.parse_args()

    if not args.csv.exists():
        sys.exit("error: no such file: {}".format(args.csv))

    profile, updated, excluded, links, overrides, known = read_existing(args.output)
    excluded = set(excluded) | set(args.exclude)
    if args.exclude_missing and known:
        excluded |= {
            book["id"]
            for book in parse_export(args.csv, args.min_rating, excluded)
            if book["id"] not in known
        }
    excluded = sorted(excluded)
    books = parse_export(args.csv, args.min_rating, excluded)
    dropped = excluded_titles(args.csv, excluded)
    if not books:
        sys.exit("error: no read books rated {} or higher".format(args.min_rating))

    categories = {}
    kept = 0
    for book in books:
        previous = known.get(book["id"])
        if previous:
            kept += 1
        book["category"] = previous["category"] if previous else MISCELLANEOUS
        book["series"] = previous.get("series") if previous else None
        book["cover"] = previous.get("cover") if previous else None
        # The override has the last word, even over what the file already held.
        if book["id"] in overrides:
            apply_override(book, overrides[book["id"]])
        categories.setdefault(book["category"], []).append(book)

    stamp = [updated]

    def save():
        """Write the file, dating it only when the books themselves changed."""
        previous = args.output.read_text() if args.output.exists() else ""
        body = render(profile, None, dropped, links, overrides, categories)
        if without_updated(previous) != without_updated(body) or not stamp[0]:
            stamp[0] = datetime.date.today().isoformat()
        args.output.write_text(
            render(profile, stamp[0], dropped, links, overrides, categories)
        )

    fetched = 0
    if not args.no_covers:
        fetched = add_covers(books, args.cover_delay, save)
        fetch_series(books, links, args.cover_delay)

    save()
    covered = sum(1 for book in books if book.get("cover"))
    print(
        "wrote {} books in {} categories to {}"
        " ({} kept their category, series and cover; {} covers, {} fetched;"
        " {} excluded)".format(
            len(books),
            len(categories),
            args.output,
            kept,
            covered,
            fetched,
            len(dropped),
        )
    )


if __name__ == "__main__":
    main()
