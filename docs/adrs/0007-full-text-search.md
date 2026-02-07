# ADR-0007: Full-Text Search

## Status

Proposed

## Date

2026-02-07

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

The current index weighs ~331 KB (gzipped: ~60 KB) for ~1000 posts.

## Decision

Evaluate three approaches to adding body text search:

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
| Index size       | ~331 KB  | ~700 KB–1 MB | ~2–4 MB    | ~50–100 KB chunks   |
| Body text search | No       | Partial      | Full       | Full                |
| Fuzzy matching   | No       | No           | No         | Yes                 |
| Build dependency | Hugo     | Hugo         | Hugo       | Hugo + Pagefind CLI |
| Code complexity  | Low      | Low          | Low        | Medium              |
| Load time impact | Minimal  | Moderate     | Noticeable | Minimal (chunked)   |

### Recommendation

Option C (Pagefind) is the strongest candidate if full-text search is desired.
It provides full body search with smaller transferred payloads than even the current
index, and adds fuzzy matching. The trade-off is an additional build step
(`pagefind --site public` after `hugo`).

Option A is the pragmatic middle ground if the goal is incremental improvement
without new dependencies.

No change has been made yet — this ADR captures the analysis for future reference.

## Consequences

### If Option A or B is adopted

- Search index grows, increasing initial load time for first search interaction
- Client-side search becomes slower as substring matching scales linearly with content size
- No new build dependencies

### If Option C (Pagefind) is adopted

- New build dependency (`pagefind` CLI) added to `just build`
- Search widget HTML/JS would be replaced with Pagefind's UI or API
- Index is pre-chunked and compressed, so load time may actually decrease
- Fuzzy matching improves search UX (typo tolerance, stemming)
- Current search features (tag/category filtering, wildcard matching, URL sync) would
  need to be re-implemented or adapted to Pagefind's API

### If no change is made

- Users cannot find posts by body content — only title, tags, and first 150 chars
- The current lightweight approach remains fast and dependency-free
