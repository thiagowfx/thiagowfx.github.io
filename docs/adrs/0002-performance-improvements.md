# ADR-0002: Performance Improvements

## Status

Partially Accepted

## Date

2026-01-01

## Context

Google PageSpeed Insights identified these performance issues:

- Render-blocking CSS requests
- Forced reflow from DOM operations
- A long network dependency chain
- Short cache lifetimes for static assets

The implementation changed after the original audit. This ADR now records the
parts that remain in the repository.

## Decision

### Inline CSS

`layouts/partials/style.html` reads `static/theme.css`, minifies it with Hugo
Pipes, and emits it with the rest of the site CSS in one `<style>` element.
There is no asynchronous stylesheet or `<noscript>` fallback.

### Defer JavaScript

`assets/js/main.js` is minified and fingerprinted with Hugo Pipes. The base
layout loads the generated file with `defer`. Event handlers initialize after
the document has been parsed.

### Load images according to priority

The header avatar has fixed dimensions and `fetchpriority="high"`. Footer badge
images have fixed dimensions and `loading="lazy"`.

### Accept GitHub Pages cache policy

The repository does not define cache headers. GitHub Pages serves HTML and
static assets with `Cache-Control: max-age=600`. ADR-0009 evaluates inlining
small assets or adding a proxy to change this behavior.

The snowflake animation and its canvas initialization no longer exist.

## Consequences

**Easier:**

- CSS needs no separate request.
- Fingerprinted JavaScript can change without stale asset URLs.
- Image dimensions reduce layout movement.

**Harder:**

- Inlined CSS is repeated in each HTML response.
- GitHub Pages keeps control of cache lifetime.
- CSS and JavaScript processing depend on Hugo Pipes.
