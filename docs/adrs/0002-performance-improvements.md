# ADR-0002: Performance Improvements

## Status

Accepted

## Date

2026-01-01

## Context

Google PageSpeed Insights identified critical performance issues:

- Render-blocking CSS requests (150 ms estimated savings)
- Forced reflow issues from DOM operations
- Suboptimal network dependency tree
- Missing cache lifetime headers (15 KiB estimated savings)

## Decision

Implemented four optimizations:

### 1. Eliminate Render-Blocking CSS

- Inlined critical CSS directly in `<style>` tag
- Converted external stylesheet to `rel=preload` with async loading
- Added `<noscript>` fallback

### 2. Prevent Forced Reflows

- Deferred snowflake canvas initialization to after DOMContentLoaded
- Changed multiple style assignments to single `cssText` assignment
- Consolidated dropdown menu event listeners into delegated handler

### 3. Cache Lifetime Configuration

- Static assets (CSS, JS): 1 year
- Images (WebP, PNG, SVG): 1 month
- HTML pages: 1 day
- RSS/Sitemap: No cache (must-revalidate)

### 4. Network Dependency Optimization

- CSS no longer blocks JavaScript execution
- Snowflake animation deferred to after page load

**Files modified:**

- `layouts/_default/baseof.html`
- `layouts/partials/style.html`

## Consequences

**Easier:**

- Faster page loads (~150 ms reduction on first contentful paint)
- Better Lighthouse scores
- Reduced layout shift from animations

**Harder:**

- CSS is now split between inline critical and async-loaded non-critical
- Cache headers require CDN (Cloudflare) for GitHub Pages
