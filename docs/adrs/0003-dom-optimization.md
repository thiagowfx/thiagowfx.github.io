# ADR-0003: DOM Optimization

## Status

Deprecated

## Date

2026-01-01

## Context

An early Lighthouse audit reported 98 elements on the tested page. The original
plan used DOM element count as a direct optimization target.

Later features added search controls, language and navigation menus, post cards,
copy controls, table-of-contents markup, and post graphs. The repository no
longer uses a fixed DOM element budget.

## Decision

The original phased decision included these changes:

1. Replace hidden previous and next links with a JavaScript object.
2. Reduce wrappers in related posts and the search widget.
3. Lazy-load footer badge images.
4. Later replace social SVGs, hidden microformats, and badge images.

Only lazy loading for footer badges remains unchanged.

## Current State

- `layouts/_default/single.html` renders hidden `data-nav="prev"` and
  `data-nav="next"` anchors for keyboard navigation. It does not define
  `window.navigationLinks`.
- `layouts/partials/related-posts.html` renders full cards for related posts and
  a separate list of previous posts.
- `layouts/_default/baseof.html` keeps the hidden `h-card`.
- Single pages keep hidden `u-url` and author microformat elements.
- Footer badge images use `loading="lazy"`.
- Social SVG replacement and CSS badge backgrounds were not implemented.

DOM structure now follows feature and semantic needs. Element count alone is not
an active acceptance criterion.

## Consequences

- New features can use semantic elements without a fixed count target.
- Lazy footer images still avoid unnecessary image loads.
- DOM performance must be measured through browser behavior, not an old element
  count.
