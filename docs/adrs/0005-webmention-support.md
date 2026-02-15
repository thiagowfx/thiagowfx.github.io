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

## Future Enhancements

### Pingback Endpoint

Once webmention.io is set up, add a legacy pingback endpoint to `baseof.html`:

```html
<link rel="pingback" href="https://webmention.io/perrotta.dev/xmlrpc" />
```

This is handled for free by webmention.io and costs nothing to support.

### Brid.gy Integration

[Brid.gy](https://brid.gy/) enables automatic syndication to Mastodon and
Bluesky. When a post is published, Brid.gy can cross-post it and funnel
responses (replies, likes, reposts) back as webmentions.

Setup involves adding hidden `u-syndication` links in post templates pointing to
Brid.gy publish endpoints:

```html
<a href="https://brid.gy/publish/mastodon" class="u-syndication" hidden></a>
<a href="https://brid.gy/publish/bluesky" class="u-syndication" hidden></a>
```

### GitHub Actions Ping

A post-deploy GitHub Actions step can notify Brid.gy for near-instant
syndication rather than waiting for Brid.gy's polling interval:

```yaml
- name: Ping Brid.gy
  run: |
    curl -s -X POST https://brid.gy/publish/webmention \
      -d source=$SITE_URL \
      -d target=https://brid.gy/publish/mastodon
```

### Custom JS Renderer

Instead of using webmention.js directly, a custom vanilla JS renderer with
IntersectionObserver for lazy-loading could be considered. This would allow full
control over the rendering of webmentions (grouping by type, custom avatars,
etc.) while keeping the bundle size minimal. See
[gagor.pro's approach](https://gagor.pro/2026/01/my-indieweb-journey-a-guide-to-posse-on-a-hugo-static-site/)
for an example implementation.
