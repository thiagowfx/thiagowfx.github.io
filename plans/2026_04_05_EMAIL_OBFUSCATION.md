# ADR: Email Obfuscation via HTML Entity Encoding

## Status

Accepted

## Context

The blog displays the author's email address in several places: the h-card, footer social links, per-post "Reply via email" links, and the `email_link` shortcode. These appear as plaintext `mailto:` links in the HTML source, making them easy targets for email harvesting bots.

## Decision

Obfuscate the email address by converting each character to its hexadecimal HTML entity representation (e.g. `s` becomes `&#x73;`). This is done programmatically via a Hugo partial (`layouts/partials/obfuscated-email.html`) that reads the email from `site.Params.Author.email` and encodes it at build time.

Reference: https://ev-fae.quest/obfuscate-your-email/

### Trade-off: HTML minification

Hugo's production minifier (tdewolff) decodes HTML entities as part of its optimization, which undoes the obfuscation. There is no minifier option to preserve entities. To work around this, HTML minification is disabled in production (`disableHTML: true` in the minify config). CSS, JS, and SVG minification remain active. The size impact is negligible for a static blog.

## Implementation

- `layouts/partials/obfuscated-email.html`: iterates over each character, converts to `&#x{hex};` format, returns the encoded string.
- Callers use `safeHTMLAttr` for `href` attributes and `safeHTML` for display text, to prevent Hugo's template engine from double-escaping the `&` in entities.
- All four email usage sites updated: `baseof.html` (h-card + footer), `single.html` (reply link), `email_link.html` (shortcode).

## Consequences

- Bots scraping the HTML source see `&#x73;&#x65;&#x72;...` instead of the plaintext email.
- Browsers decode the entities automatically, so all mailto links work normally for users.
- No JavaScript required.
- The email remains configured in one place (`config.yml`); the partial reads it dynamically.
- HTML minification is disabled in production, with negligible impact on page size.
