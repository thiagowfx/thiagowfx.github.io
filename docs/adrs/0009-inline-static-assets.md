# ADR-0009: Inline Static Assets for Cache Efficiency

## Status

Proposed

## Date

2026-02-07

## Context

Lighthouse flags 10 first-party assets with short cache lifetimes (~15 KiB total,
estimated savings). GitHub Pages enforces `Cache-Control: max-age=600` (10 minutes)
on all static assets with no override mechanism — there is no `_headers` file,
`.htaccess`, or server configuration available.

Flagged assets:

| Asset | Cache TTL | Transfer Size |
| ----- | --------- | ------------- |
| `/vendor/html5-validator-badge.webp` | 10m | 4 KiB |
| `/vendor/cc-by-nc-sa-4.0-88x31.webp` | 10m | 2 KiB |
| `/thiagowfx.webp` | 10m | 2 KiB |
| `/vendor/valid-rss-rogers.webp` | 10m | 2 KiB |
| `/vendor/cookiezero.webp` | 10m | 2 KiB |
| `/vendor/vim.webp` | 10m | 1 KiB |
| `/vendor/green-team.webp` | 10m | 1 KiB |
| `/js/main.min.b095a83….js` | 10m | 1 KiB |
| `/vendor/indieweb88x31-flat.webp` | 10m | 1 KiB |
| `/vendor/powrss-88-31.webp` | 10m | 1 KiB |

The blog already inlines CSS via Hugo Pipes (`commit eef4d55370`), establishing a
precedent for eliminating external asset requests.

## Decision

### Option A: Inline assets as data URIs (recommended)

Eliminate the HTTP requests entirely by inlining assets into the HTML, following the
CSS inlining precedent.

**Images**: Move 8 vendor badge WebP files from `static/vendor/` to `assets/vendor/`
and use Hugo Pipes to generate data URIs:

```go-html-template
{{- with resources.Get "vendor/foo.webp" -}}
{{- $src := printf "data:%s;base64,%s" .MediaType.Type (.Content | base64Encode) -}}
<img {{ printf "src=%q" $src | safeHTMLAttr }} width="88" height="31" alt="..." loading="lazy" />
{{- end -}}
```

The `safeHTMLAttr` pattern is required because Hugo's `html/template` escapes `+` as
`&#43;` inside HTML attributes, corrupting base64 strings
([Hugo #12443](https://github.com/gohugoio/hugo/issues/12443)).

**Avatar** (`thiagowfx.webp`): Copy to `assets/` for inlining, keep original in
`static/` because `static/rss.xsl` references `/thiagowfx.webp` directly (XSL
cannot use Hugo Pipes).

**JavaScript**: Inline the script content directly (already in `assets/`):

```go-html-template
{{- $js := resources.Get "js/main.js" | minify }}
<script>{{ $js.Content | safeJS }}</script>
```

**Trade-offs**: HTML size increases by ~22 KiB raw (~17 KiB base64 images + ~3 KiB
JS + overhead), but gzips well. Eliminates 10 HTTP round-trips. After 10 minutes,
repeat visitors make 1 revalidation request (HTML) instead of 11 (HTML + 10 assets).

### Option B: Add a CDN (Cloudflare)

Place Cloudflare in front of GitHub Pages to override cache headers with longer TTLs
for static assets.

- **Pros**: Addresses the root cause; no HTML size increase; benefits all assets
- **Cons**: Adds infrastructure dependency; DNS configuration changes; overkill for
  ~15 KiB of badge images

### Option C: Switch hosting platform

Move to Netlify or Vercel, which support `_headers` files for custom cache control.

- **Pros**: Full control over HTTP headers; `_headers` file is simple to maintain
- **Cons**: Hosting migration is a significant infrastructure change

### Option D: Accept the limitation

The flagged assets are small (15 KiB total), all lazy-loaded in the footer (except
the avatar), and the 10-minute cache still provides benefit for short browsing
sessions.

- **Pros**: No code changes; no maintenance burden
- **Cons**: Lighthouse warning persists

## Consequences

### If Option A is adopted

- All 10 cache lifetime warnings are eliminated from Lighthouse
- HTML size increases by ~22 KiB raw per page (compresses well with gzip/brotli)
- Fewer HTTP requests on first visit (1 vs 11)
- Fewer revalidation requests on repeat visits after cache expiry (1 vs 11)
- Badge images are no longer independently cacheable — changes require a new HTML
  download, but this is negligible for 1-4 KiB images
- The `defer` attribute is lost on the inlined JS, but the script is already at the
  end of `<body>`, so behavior is equivalent
- `static/thiagowfx.webp` must be kept for RSS XSL backward compatibility

### If no change is made

- Lighthouse continues to flag 10 assets with 10-minute cache TTL
- No impact on actual user experience (assets are small, lazy-loaded)
