# 0013 — No Query Strings

## Status

Proposed (tracked for future hosting changes)

## Context

[Chris Morgan](https://chrismorgan.info/no-query-strings) blocks any
unauthorized query string on his website to prevent tracking parameters
(`ref=`, UTM, etc.) and protect URL integrity. He implements this server-side
via a `Caddyfile` rule that rejects requests carrying query strings not on an
explicit allowlist.

The blog has no legitimate query-string-driven pages, so the same blanket-ban
would be safe here in principle.

## Decision

Defer server-side query-string rejection until hosting permits it. The blog
is hosted on GitHub Pages (`.github/workflows/gh-pages.yml`), which serves
static files with no support for Caddy/nginx-style rules, conditional
redirects, or query-string inspection. Morgan's approach depends on running
his own server and is incompatible with this hosting setup.

Tracking this as a future improvement: if hosting ever moves behind
Cloudflare or to a server we control, implement the rule then.

## Alternatives Considered

- **Client-side strip (JS in base layout)**: A `<script>` in
  `layouts/partials/` could call `history.replaceState` on load to drop
  unknown query params. Doesn't reject the request — the page still renders —
  but cleans the URL bar, reduces referrer leakage of the params, and breaks
  analytics that read `location.search`. Weakest form but cheapest; doesn't
  require leaving GH Pages.
- **Cloudflare in front of GitHub Pages**: Proxy `perrotta.dev` through
  Cloudflare and add a Transform Rule or Worker that returns 404 (or
  308-to-clean-URL) when `http.request.uri.query` is non-empty or not in an
  allowlist. Closest real equivalent to the Caddyfile rule. Same option
  flagged in [[0012-ai-scraper-poisoning]] for bot management.
- **Move off GitHub Pages**: Cloudflare Pages, Netlify, or a Caddy VPS would
  let this be done natively. Overkill for this alone.

## Notes

- Impact is mostly cosmetic: the blog doesn't run analytics that key off
  query strings, so tracking parameters added by external sites don't change
  what's served — they just clutter the URL bar and may leak via referer.
- If a Cloudflare proxy is ever set up (for bot mitigation per
  [[0012-ai-scraper-poisoning]] or otherwise), revisit and add a
  query-string Transform Rule at the same time.
