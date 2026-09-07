# ADR-0007: Full-Text Search

## Status

Accepted

## Date

2026-09-06

## Context

The blog's search widget (`layouts/partials/search-widget.html`) uses a JSON index
generated at build time (`layouts/_default/search.search.json`). The index currently
contains these fields per post:

- `title`
- `url`
- `date`
- `tags`
- `categories`
- `summary` (Hugo's `.Summary`, plainified and truncated to 150 characters)

Search matches against `title`, `tags`, and `summary` with simple substring matching
and wildcard support. This works well for finding posts by topic or tag, but fails
when users search for specific terms that only appear in the body text.

As of 2026-08-20, the index contains 1,300 English posts. It excludes the one
`rss_only` post. The generated file is 418,479 bytes (~409 KiB) and 115,022 bytes
(~112 KiB) when gzip-compressed.

The dedicated search page now also supports tag chips, a year range, sort order,
and URL state through `q`, `tag`, `from`, `to`, and `sort`. These additions do not
change which text fields are searchable.

## Decision

Adopt Option B, but store complete plain-text bodies in a separate JSON index.
The existing index keeps titles, tags, summaries, and metadata. Both search
interfaces use this smaller index by default. A checkbox loads the content index
and enables body matching.

The following options were evaluated:

### Option A: Add Truncated Content (500–1000 chars)

Add a `content` field with truncated plain text to the existing index.

```go-html-template
"content" ((.Content | plainify | truncate 1000) | default "")
```

- **Index size**: ~700 KB–1.2 MB (estimated)
- **Pros**: Minimal code change, covers intros/conclusions where key terms often appear
- **Cons**: Still misses terms deep in posts, arbitrary cutoff

### Option B: Add Full Content

Add the complete plain-text body to the index.

```go-html-template
"content" ((.Content | plainify) | default "")
```

- **Index size**: ~2–4 MB (estimated, depends on average post length)
- **Pros**: True full-text search, no missed terms
- **Cons**: Large payload on first search, slower client-side matching with substring scan over megabytes

### Option C: Dedicated Search Library

Replace the custom substring matcher with a purpose-built library:

- **[Pagefind](https://pagefind.app/)**: Static search index generated post-build.
  Pre-compressed WASM-based index, loads only relevant chunks (~50–100 KB typical).
  Minimal client-side JS. Used by many Hugo sites.
- **[Fuse.js](https://www.fusejs.io/)**: Fuzzy search in the browser. Still requires
  shipping the full index JSON, but supports typo tolerance and weighted scoring.

| Criteria         | Current  | Option A     | Option B   | Option C (Pagefind) |
| ---------------- | -------- | ------------ | ---------- | ------------------- |
| Index size       | ~409 KiB | ~700 KB–1 MB | ~2.5 MB    | ~50–100 KB chunks   |
| Body text search | No       | Partial      | Full       | Full                |
| Fuzzy matching   | No       | No           | No         | Yes                 |
| Build dependency | Hugo     | Hugo         | Hugo       | Hugo + Pagefind CLI |
| Code complexity  | Low      | Low          | Low        | Medium              |
| Load time impact | Minimal  | Moderate     | Noticeable | Minimal (chunked)   |

### Rationale

Full content guarantees that searches find terms anywhere in a post. Separating
content keeps the default transfer close to its previous size. It also keeps the
current filters, wildcard matching, URL state, and build process. Pagefind would
require a new build dependency and a rewrite of both search interfaces.

## Consequences

- Default search transfers the metadata index only. It is approximately 419 KiB,
  or 115 KiB compressed.
- Body search loads a second index. It is approximately 2.1 MiB, or 725 KiB
  compressed.
- Search finds terms in complete body text only after users enable body matching.
- Each index is cached after its first load.
- Search keeps its current substring and wildcard behavior.
- No new build dependency is required.
- Pagefind remains an option if index transfer or scan time becomes a problem.
