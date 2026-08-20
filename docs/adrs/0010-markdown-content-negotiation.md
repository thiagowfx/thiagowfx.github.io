# ADR-0010: Markdown Content Negotiation for LLMs

## Status

Proposed

## Date

2026-02-16

## Context

The blog generates a Markdown output (`index.md`) for each regular content page
through Hugo's custom output formats (`config/_default/config.yml`). Each matching
HTML page includes a `<link rel="alternate" type="text/markdown">` tag in `<head>`
for discoverability. List pages and the homepage do not have the Markdown output.
A `/llms.txt` file is generated at the site root.

LLMs and AI agents benefit from consuming raw Markdown rather than parsing HTML.
The standard HTTP mechanism for a client to request a specific representation is the
`Accept` header — e.g. `Accept: text/markdown`. Currently, a client must know to
append `/index.md` to any URL; there is no server-side content negotiation.

GitHub Pages does not support custom response headers or URL rewriting, so content
negotiation must be handled by a reverse proxy.

## Current State

The proposal is not implemented. The live site is served directly by GitHub Pages.
A request with `Accept: text/markdown` still returns `Content-Type: text/html`.
Markdown remains available through the alternate link and direct `index.md` URL.

## Decision

### Option A: Cloudflare Transform Rule (recommended)

Place Cloudflare in front of GitHub Pages (free tier) and add a single **URL Rewrite**
transform rule:

- **When**: `http.request.headers["accept"][*] contains "text/markdown"`
- **Then**: Rewrite path to `concat(http.request.uri.path, "index.md")`

This rewrites the origin request so GitHub Pages serves the pre-built Markdown file
for a regular page whose request path ends in `/`. No Workers, repository code, or
build changes are required.

Example:

```
GET /posts/2026-01-01-hello/ HTTP/1.1
Accept: text/markdown

→ Cloudflare rewrites to /posts/2026-01-01-hello/index.md
→ GitHub Pages serves the static Markdown file
```

**Complementary**: Improve `/llms.txt` to list all posts with their Markdown URLs,
following the [llmstxt.org](https://llmstxt.org/) spec more closely.

### Option B: Cloudflare Worker

Write a Worker script that inspects the `Accept` header and fetches the Markdown
variant from the origin.

- **Pros**: Full programmatic control; can set `Content-Type: text/markdown` response
  header precisely
- **Cons**: Code to maintain; Worker invocation limits on the free tier; overkill when
  a declarative rule suffices

### Option C: Static-only discoverability (no proxy)

Rely solely on `<link rel="alternate">` tags and `/llms.txt` for Markdown discovery.
No content negotiation — clients must follow the alternate link or know the `/index.md`
convention.

- **Pros**: Zero infrastructure changes; already implemented
- **Cons**: No `Accept` header support; non-standard discovery; most LLM crawlers
  won't follow `<link>` tags

### Option D: Switch to a host with rewrite support

Move to Netlify or Vercel, which support `_redirects`/`_headers` files or edge
middleware for content negotiation.

- **Pros**: Native rewrite/header support; no external proxy
- **Cons**: Hosting migration is a significant infrastructure change for a single
  feature

## Consequences

### If Option A is adopted

- Clients sending `Accept: text/markdown` receive raw Markdown for regular pages
  that have a Markdown output
- Zero code changes in the repository — the Markdown output already exists
- Requires Cloudflare proxy setup (free tier): DNS pointing to Cloudflare, one
  transform rule
- The same Cloudflare setup unblocks other improvements (custom cache headers per
  ADR-0009, security headers, etc.)
- `<link rel="alternate">` tags and `/llms.txt` continue to work as complementary
  discovery mechanisms
- No impact on regular browser traffic (`Accept: text/html` is unaffected)

### If no change is made

- Markdown output remains available only via direct `/index.md` URLs
- LLM agents must discover Markdown URLs through `<link>` tags or convention
- No infrastructure dependencies beyond GitHub Pages
