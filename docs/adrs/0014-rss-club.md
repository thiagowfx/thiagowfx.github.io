# ADR-0014: RSS Club (RSS-only posts)

## Status

Accepted

## Date

2026-05-25

## Context

Some posts should reach only RSS subscribers — small notes, half-baked thoughts, replies, "between-post" content. The pattern was popularized by Terence Eden's "RSS Club" post (<https://shkspr.mobi/blog/2026/04/welcome-to-rss-club/>): the post is in the feed, but is not linked from anywhere on the website. The only way to find it is to subscribe.

Hugo does not provide this out of the box. The existing `rss.xml` template supports the inverse — `rss: false` excludes a post from the feed while it remains on the site. There is no symmetric mechanism for the reverse.

## Decision

Introduce a `rss_only: true` front matter flag. Posts with this flag are:

- **Included** in the RSS feed (`layouts/_default/rss.xml`, unchanged — it only filters out `rss: false`).
- **Hidden** from every other enumeration of posts on the site.
- **Marked `noindex`** on their own single page, so search engines do not surface them even if a URL leaks.

The post is still rendered at its permalink. Anyone with the URL (e.g. an RSS subscriber clicking through, or someone sharing the link) can read it. This is RSS Club, not access control.

### Surfaces that must hide `rss_only` posts

- `layouts/_default/list.html` — year-grouped post list, plus taxonomy term pages.
- `layouts/_default/single.html` — prev/next neighbor computation (keyboard shortcuts j/k).
- `layouts/index.html` — featured (`bestof`) grid on the homepage.
- `layouts/404.html` — recent posts fallback.
- `layouts/_default/random.html` — random-post redirect.
- `layouts/_default/search.search.json` — client-side search index.
- `layouts/_default/home.llms.txt` — LLM-facing index.
- `layouts/_default/home.sitemapmd.md` — markdown sitemap.
- `layouts/sitemap.xml` — XML sitemap (the standard `sitemap: disable: true` front matter already works here; `rss_only` should imply it).
- `layouts/_default/graph.graphdata.json` — interactive graph nodes.
- `layouts/partials/related-posts.html` and `layouts/partials/backlinks.html` —
  filter resolved pre-computed page IDs by `.Params.rss_only`.
- `layouts/partials/mini-graph.html` — must apply the same filter when it resolves
  incoming and outgoing page IDs.

### Surfaces that should keep `rss_only` posts

- `layouts/_default/rss.xml` — the whole point.
- The post's own permalink — readers reach it from the feed.

### Alternatives considered

- **Draft + future date**: hides from the site but also hides from RSS. Wrong direction.
- **`_build.list: never`**: removes the page from collections entirely, which also removes it from RSS. Wrong direction.
- **Headless bundle**: same problem — not enumerated, so not in RSS either.
- **Separate content section** (e.g. `content/rss/`): would need its own RSS template merged with the main one, and breaks URL conventions. More machinery than a single front matter flag.

### Why `noindex` and not just hiding

A determined search engine can still discover the URL (RSS aggregators expose feeds, `Permalink` is in the feed XML, robots can follow). `noindex` is the polite way to say "please don't surface this in search results."

## Implementation

1. **List filter** — in `list.html`, filter `$pages` by `Params.rss_only != true` at the top, so both the main posts list and taxonomy term pages skip them. The taxonomy header count uses the filtered slice too.
2. **Per-post template filters** — in `single.html`, filter `$posts` before computing prev/next. In `index.html`, filter the `bestof` slice. In `404.html`, filter `RegularPages`. In `random.html`, skip `rss_only`. In `search.search.json`, `home.llms.txt`, `home.sitemapmd.md`, `sitemap.xml`, `graph.graphdata.json`, add the same filter.
3. **Related/backlinks partials** — after resolving pre-computed IDs to pages, filter out pages with `.Params.rss_only`.
4. **`noindex`** — in `seo_tags.html`, emit
   `<meta name="robots" content="noindex, nofollow">` when `.Params.rss_only` is
   true.

The archetype (`archetypes/blog.md`) deliberately does NOT include `rss_only: false` — it would clutter every new post's front matter. Authors add `rss_only: true` only when needed.

## Current State

As of 2026-08-20, one post uses `rss_only: true`. The original surfaces apply the
filter. Two later additions have gaps:

- `layouts/partials/mini-graph.html` resolves backlinks and outlinks without an
  `rss_only` check. A linked RSS-only post can appear in a public post's mini
  graph.
- Category and tag cloud counts in `layouts/_default/list.html` use taxonomy
  `.Pages` directly. They can include RSS-only posts in aggregate counts, but do
  not show their titles or URLs.

The full graph output filters RSS-only nodes and edges. The pre-computed
`data/links.json` still includes all posts.

## Consequences

- Authors get a one-line flag (`rss_only: true`) to publish to RSS subscribers only.
- Cost: every template that enumerates posts needs the filter. New enumeration
  templates must add it explicitly. The mini-graph gap above shows this maintenance
  cost.
- Pre-computed `data/links.json` (built by `ci/precompute_links.py`) still contains references to/from `rss_only` posts. Filtering happens at the template layer when resolving IDs to pages. If `rss_only` posts ever need to be excluded from the *computation* of related/backlinks (so they don't show up as "related" to public posts), the script would need to learn the flag — out of scope here.
- `rss_only` posts are not in the sitemap, so search engines learn about them only via the RSS feed or external links. Combined with `noindex`, the practical result is that they stay out of search results.
- `rss: false` and `rss_only: true` are independent flags. Setting both is meaningless (post would be in neither place) but harmless.
