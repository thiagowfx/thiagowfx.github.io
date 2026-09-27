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

### External CSS

`layouts/partials/style.html` concatenates `assets/css/theme.css` and
`assets/css/style.css`, then minifies and fingerprints the result with Hugo
Pipes. Pages load the generated file through one blocking stylesheet link.
The fingerprint changes when either source file changes.

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

- Browsers reuse CSS across page visits.
- HTML responses do not repeat shared CSS.
- Fingerprinted CSS and JavaScript can change without stale asset URLs.
- Image dimensions reduce layout movement.

**Harder:**

- First visits need one blocking CSS request.
- GitHub Pages keeps control of cache lifetime.
- CSS and JavaScript processing depend on Hugo Pipes.
