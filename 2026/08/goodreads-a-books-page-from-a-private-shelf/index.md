---
title: "goodreads: a books page from a private shelf"
url: https://perrotta.dev/2026/08/goodreads-a-books-page-from-a-private-shelf/
last_updated: 2026-09-29
---


[Previously]({{< ref "2025-03-18-goodreads" >}}).

**Problem statement**: I wanted a `/books` page with covers, but my Goodreads
shelf is private and the API has been dead since 2020.

```shell
% curl -sS "https://www.goodreads.com/review/list_rss/7873832?shelf=read" \
    -o /tmp/rss.txt -w "%{http_code}\n"
401
% head -c 42 /tmp/rss.txt
Sorry, that person's shelf is private
```

The CSV export needs no auth, no key, no scraping — one click under *My Books →
Import/Export*. It carries 1469 rows and everything worth rendering, except
covers:

```shell
% head -1 ~/Downloads/goodreads_library_export.csv | tr ',' '\n' | grep -ciE "cover|image"
0
```

So `ci/goodreads_to_books.py` reads the CSV, keeps the five-star `read` rows,
and writes `data/books.yaml` for Hugo to render:

```shell
% just goodreads-import
ci/goodreads_to_books.py ~/Downloads/goodreads_library_export.csv
wrote 101 books in 2 categories to ~/Workspace/perrotta.dev/data/books.yaml (101 kept their category, series, note and cover; 101 covers, 0 fetched; 63 excluded)
```

101 on display, 63 excluded: the 164 five-star rows, minus the textbooks and
language courses nobody needs a recommendation for.

Covers come from each book's public page — those stay readable even when the
shelf is not, and the `og:image` points straight at the CDN:

```shell
% curl -sL "https://www.goodreads.com/book/show/22034" |
    grep -o '<meta property="og:image" content="[^"]*"'
<meta property="og:image" content="https://m.media-amazon.com/images/S/compressed.photo.goodreads.com/books/1394988109i/22034.jpg"
```

Which lands in the data file, one fetch per book, ever:

```yaml
      - title: The Godfather
        author: Mario Puzo
        year: 1969
        rating: 5
        url: https://www.goodreads.com/book/show/22034
        cover: https://m.media-amazon.com/images/S/compressed.photo.goodreads.com/books/1394988109i/22034.jpg
```

That "ever" is the whole trick. Crawling 164 pages back to back gets an AWS WAF
challenge — HTTP 202 with an empty body — and it sticks around for a few
minutes:

```text
  Thinking, Fast and Slow: HTTP 202, 0 bytes
  Blindness: HTTP 202, 0 bytes
  Freakonomics + Superfreakonomics: HTTP 202, 0 bytes
giving up after 5 failures in a row; run again later to fetch the remaining 43 covers
```

So the importer treats a cover as a cache entry rather than a build step: three
seconds between requests, a save every ten covers, and a bail-out after five
consecutive failures. A blocked run keeps what it got, and the next run resumes:

```python
        book["cover"] = fetch_cover(book)
        if book["cover"]:
            fetched += 1
            failures = 0
            if fetched % COVER_SAVE_EVERY == 0:
                save()
```

Three runs, spaced by coffee, and every cover was in. Re-imports are now free —
`0 fetched` above — and idempotent, which matters because the CSV is the source
of truth for titles and ratings, while the YAML owns the curation:
categories, series names, notes, an `excluded` list for the books I don't want
on display, and an `overrides` list for when the shelved edition is not the one
worth linking:

```yaml
overrides:
  - id: "15779555"
    title: The Godfather
    url: https://www.goodreads.com/book/show/22034
```

That entry is the Brazilian translation of *The Godfather*. It is what I read,
but *O Poderoso Chefão* is not what I would recommend.

```shell
% git --no-pager show --stat --oneline 7c8785dbb4
7c8785dbb4 books: add fiction favorites
 data/books.yaml | 348 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 348 insertions(+)
```

Fiction first. Non-fiction is still sitting unstaged, which is its own kind of
review queue.

- - -

🤖 *Drafted with [`/bloggify`](https://github.com/thiagowfx/skills/blob/master/plugins/thiagowfx/skills/bloggify/SKILL.md).*

