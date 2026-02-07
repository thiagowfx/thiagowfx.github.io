# ADR-0008: Bear Blog Discover Cross-posting

## Status

Proposed

## Date

2026-02-07

## Context

This blog uses a custom fork of the [Bear Blog](https://bearblog.dev/) Hugo theme
but is **not** hosted on the Bear Blog platform — it is a self-hosted Hugo site
deployed independently.

Bear Blog's [`/discover`](https://bearblog.dev/discover/) feed is a
community-curated trending page where posts from Bear Blog users surface based on
upvote-based ranking. It provides organic reach to a readership that values
minimalist, content-focused blogs — a natural audience for this site.

Because the blog is not on the Bear Blog platform, posts do not appear in
`/discover` automatically. Cross-posting would require maintaining content on both
platforms.

## Decision

Evaluate three approaches:

### Option A — Manual Cross-posting

Create a Bear Blog account and selectively copy posts to Bear Blog's web editor
with the `make_discoverable: true` frontmatter flag. Each cross-posted entry would
include a canonical URL (`<link rel="canonical">`) pointing back to the Hugo site to
avoid SEO penalties from duplicate content.

- **Workflow**: After publishing on Hugo, manually paste the Markdown into Bear
  Blog's editor, set `make_discoverable: true`, and add a canonical link.
- **Selectivity**: Only cross-post content likely to resonate with the Bear Blog
  community (e.g., blogging meta-posts, minimalism, web dev), not every post.

### Option B — Automated Sync (Future)

Bear Blog does not expose a public API today. If an API becomes available in the
future, automate publishing from Hugo build output — e.g., a post-build script that
pushes new/updated posts to Bear Blog with canonical URLs set automatically.

### Option C — Do Nothing

Continue with the current Hugo-only setup. Rely on RSS, search engines, Hacker News,
and organic sharing for discovery. No additional maintenance burden.

### Comparison

| Criteria              | Option A (Manual)         | Option B (Automated)             | Option C (Do Nothing) |
| --------------------- | ------------------------- | -------------------------------- | --------------------- |
| Effort                | Low–moderate per post     | High upfront, low ongoing        | None                  |
| Discoverability       | Bear Blog community reach | Same as A, but hands-free        | Status quo            |
| Content freshness     | May lag behind Hugo site  | Near-real-time                   | N/A                   |
| Canonical URL control | Manual, error-prone       | Automated, reliable              | N/A                   |
| Platform dependency   | Soft (optional channel)   | Harder (build pipeline coupling) | None                  |
| Feasibility today     | Yes                       | No (no public API)               | Yes                   |

### Recommendation

Option A is the only viable approach today. It is low-commitment — a Bear Blog
account is free, and cross-posting can be done selectively. The main cost is the
manual effort of copying and formatting each post, plus ensuring canonical URLs are
set correctly.

Option B is worth revisiting if Bear Blog introduces an API.

No change has been made yet — this ADR captures the analysis for future reference.

## Consequences

### If Option A is adopted

- Content exists in two places; canonical URLs must be set on every cross-posted
  entry to avoid duplicate-content SEO penalties
- Manual copy-paste introduces a maintenance burden and risk of staleness if the
  Hugo version is updated after cross-posting
- Provides access to Bear Blog's `/discover` audience with minimal infrastructure
  changes
- Soft dependency on Bear Blog platform — if the platform changes or disappears,
  only the cross-posted copies are affected

### If Option B becomes feasible

- Build pipeline gains a new external dependency (Bear Blog API)
- Canonical URLs and content sync are automated, reducing human error
- Tighter coupling to Bear Blog as a distribution channel

### If no change is made

- No additional maintenance burden
- Discovery remains limited to existing channels (RSS, search engines, social sharing)
- No risk of duplicate content or platform dependency
