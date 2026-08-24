#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["PyYAML"]
# ///
"""
Import a Goodreads CSV export into data/reading.yaml.

Usage:
    ci/goodreads_to_reading.py ~/Downloads/goodreads_library_export.csv
    ci/goodreads_to_reading.py export.csv --min-rating 4 --no-covers

Keeps only books on the "read" shelf whose rating is at least --min-rating.
Category placement and hand-written notes survive re-imports: books already
present in data/reading.yaml keep their category, series, note and cover, by
their Goodreads book id. New books land in the "Miscellaneous" category, and
book ids listed under "excluded" stay out of the page for good. Deleting a book
by hand and re-importing brings it back, so --exclude-missing turns every book
missing from the data file into an excluded one instead.

The CSV export carries no cover image, so each new book costs one request to
its public Goodreads page, whose og:image points at the cover on Amazon's CDN.
The same page names the series a book belongs to, so one request per series
also fills in the link under "series".
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

DATA_FILE = pathlib.Path(__file__).resolve().parent.parent / "data" / "reading.yaml"
SCHEMA_REF = "# yaml-language-server: $schema=../schemas/reading.json"
MISCELLANEOUS = "Miscellaneous"
BOOK_URL = "https://www.goodreads.com/book/show/{id}"
COVER_PATTERN = re.compile(r'<meta property="og:image" content="([^"]+)"')
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


def without_updated(text):
    """Drop the updated line, so it does not count as a change to the books."""
    kept = [line for line in text.splitlines() if not line.startswith("updated:")]
    return "\n".join(kept).strip()


def book_id(url):
    """Extract the Goodreads book id from a book URL."""
    match = re.search(r"/book/show/(\d+)", url or "")
    return match.group(1) if match else None


def read_existing(path):
    """Return (profile, updated, excluded, links, {book id: book}) from a file."""
    if not path.exists():
        return None, None, [], {}, {}
    data = yaml.safe_load(path.read_text()) or {}
    known = {}
    for category in data.get("categories") or []:
        for book in category.get("books") or []:
            key = book_id(book.get("url"))
            if key:
                known[key] = dict(book, category=category["name"])
    excluded = [str(key) for key in data.get("excluded") or []]
    links = {entry["name"]: entry["url"] for entry in data.get("series") or []}
    return data.get("profile"), data.get("updated"), excluded, links, known


def fetch_page(book):
    """Return the HTML of a book's public Goodreads page, or None."""
    request = urllib.request.Request(
        BOOK_URL.format(id=book["id"]), headers={"User-Agent": USER_AGENT}
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            status = response.status
            page = response.read().decode("utf-8", "replace")
    except (urllib.error.URLError, TimeoutError) as error:
        print("  {}: {}".format(book["title"], error), file=sys.stderr)
        return None
    if status != 200 or not page:
        print(
            "  {}: HTTP {}, {} bytes".format(book["title"], status, len(page)),
            file=sys.stderr,
        )
        return None
    return page


def series_url(page, name):
    """Return the series page URL named in a book page, or None."""
    for title, url in SERIES_PATTERN.findall(page or ""):
        # Goodreads writes curly apostrophes, the data file straight ones.
        if plain_text(json.loads('"{}"'.format(title))) == plain_text(name):
            return url
    return None


def fetch_series_urls(books, links, delay):
    """Fill in the link of every series that has none yet. Returns how many."""
    named = sorted({book["series"] for book in books if book.get("series")})
    added = 0
    for name in named:
        if links.get(name):
            continue
        volumes = [book for book in books if book.get("series") == name]
        print("series: {}".format(name))
        page = fetch_page(volumes[0])
        url = series_url(page, name)
        if url:
            links[name] = url
            added += 1
        else:
            print("  {}: no series page".format(name), file=sys.stderr)
        time.sleep(delay)
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


def render(profile, updated, excluded, links, categories):
    """Render the data file. This script owns the order, so no sort markers."""
    lines = [SCHEMA_REF]
    if profile:
        lines.append("profile: {}".format(quote(profile)))
    if updated:
        lines.append('updated: "{}"'.format(updated))
    if excluded:
        lines.append("excluded:")
        for key, title in sorted(excluded.items(), key=lambda item: item[1].casefold()):
            lines.append('  - "{}" # {}'.format(key, title))
    if links:
        lines.append("series:")
        for name in sorted(links, key=str.casefold):
            lines.append("  - name: {}".format(quote(name)))
            lines.append("    url: {}".format(quote(links[name])))
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
            lines.append("        url: {}".format(BOOK_URL.format(id=book["id"])))
            if book.get("series"):
                lines.append("        series: {}".format(quote(book["series"])))
            if book.get("cover"):
                lines.append("        cover: {}".format(quote(book["cover"])))
            if book.get("note"):
                lines.append("        note: {}".format(quote(book["note"])))
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

    profile, updated, excluded, links, known = read_existing(args.output)
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
        book["note"] = previous.get("note") if previous else None
        book["cover"] = previous.get("cover") if previous else None
        categories.setdefault(book["category"], []).append(book)

    stamp = [updated]

    def save():
        """Write the file, dating it only when the books themselves changed."""
        previous = args.output.read_text() if args.output.exists() else ""
        body = render(profile, None, dropped, links, categories)
        if without_updated(previous) != without_updated(body) or not stamp[0]:
            stamp[0] = datetime.date.today().isoformat()
        args.output.write_text(render(profile, stamp[0], dropped, links, categories))

    fetched = 0
    if not args.no_covers:
        fetched = add_covers(books, args.cover_delay, save)
        fetch_series_urls(books, links, args.cover_delay)

    save()
    covered = sum(1 for book in books if book.get("cover"))
    print(
        "wrote {} books in {} categories to {}"
        " ({} kept their category, series, note and cover; {} covers, {} fetched;"
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
