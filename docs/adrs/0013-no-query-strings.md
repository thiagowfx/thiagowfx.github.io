# ADR-0013: Query String Allowlist

## Status

Proposed

## Date

2026-05-24

## Context

[Chris Morgan](https://chrismorgan.info/no-query-strings) rejects query strings
that are not on an explicit allowlist. This prevents tracking parameters from
becoming part of stable URLs.

The blog now has legitimate query-string state:

- Search widgets on post and taxonomy lists use `q`.
- The dedicated search page also uses `tag`, `from`, `to`, and `sort`.
- Fullscreen mode uses `fullscreen` in `assets/js/main.js` on posts and tools
  that render the fullscreen control.

The client reads these values on load and updates them with
`history.replaceState`. A blanket query-string ban would break shared search
URLs and fullscreen state.

GitHub Pages serves static files and cannot inspect or reject query strings. The
live site therefore accepts both known and unknown parameters.

## Decision

Do not implement a blanket query-string ban.

If the site later gains a reverse proxy or a server, use an allowlist:

- Allow `q`, `tag`, `from`, `to`, and `sort` on `/search/`.
- Allow `q` on post, tag, and category list pages that render the search widget.
- Allow `fullscreen` on pages that support fullscreen mode, or globally if the
  simpler rule is preferred.
- Reject unknown parameters or redirect to the same path without them.

No server-side change is possible under the current GitHub Pages deployment.

## Alternatives Considered

- **Client-side removal**: JavaScript could remove unknown parameters after the
  page loads. This would clean the address bar but would not reject the original
  request. It must preserve the search and fullscreen parameters.
- **Cloudflare in front of GitHub Pages**: A Transform Rule or Worker could
  apply the allowlist before the request reaches GitHub Pages. The live site is
  not behind Cloudflare. See [ADR-0012](0012-ai-scraper-poisoning.md).
- **Move off GitHub Pages**: Cloudflare Pages, Netlify, or a managed server could
  enforce the allowlist. This remains too much infrastructure for this feature.

## Consequences

- Search and fullscreen URLs keep their current behavior.
- Unknown tracking parameters remain accepted by GitHub Pages.
- Any future edge rule must preserve the documented application parameters.
- Query parameters can still leak through referrers under the site's current
  `no-referrer-when-downgrade` policy.
