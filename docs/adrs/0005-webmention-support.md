# ADR-0005: WebMention Support

## Status

Proposed

## Date

2026-01-01

## Context

The blog has IndieWeb badges but no WebMention implementation. WebMentions
enable cross-site conversations—showing replies, likes, and reposts from other
sites on blog posts.

## Decision

Implement client-side WebMentions using webmention.io:

### Rationale

Chosen over GitHub Actions/server-side approach because:

- Minimal complexity (~30 min setup vs 2-3 hours)
- No additional infrastructure/workflows needed
- Fits "simple is better" philosophy (512kb club member)
- Can migrate to server-side later if needed
- webmention.js is well-maintained and privacy-respecting

### Implementation Steps

1. Sign up at https://webmention.io/ and verify `perrotta.dev`

2. Add endpoint to HTML head:

   ```html
   <link rel="webmention" href="https://webmention.io/perrotta.dev/webmention" />
   ```

3. Download webmention.js to `static/js/webmention.min.js`

4. Add display container to `layouts/_default/single.html`:

   ```html
   <section class="webmentions-section">
     <div id="webmentions"></div>
   </section>
   ```

5. Add CSS styling to `layouts/partials/style.html`

6. Optionally set up Brid.gy for Mastodon/Twitter mentions

### Files to Modify

- `layouts/_default/baseof.html` - endpoint link, script include
- `layouts/_default/single.html` - webmention container
- `layouts/partials/style.html` - webmention styling
- `static/js/webmention.min.js` - new file

## Consequences

**Easier:**

- Receiving and displaying cross-site replies
- Building connections with IndieWeb community
- Showing social media reactions via Brid.gy

**Harder:**

- Moderation may be needed for spam mentions
- Client-side loading adds JS dependency
- Requires external service (webmention.io)
