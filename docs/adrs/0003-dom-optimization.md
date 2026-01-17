# ADR-0003: DOM Optimization

## Status

Partially Accepted

## Date

2026-01-01

## Context

Lighthouse audit identified DOM bloat (98 total elements). Large DOM increases
style calculation time, layout reflows, and memory usage.

## Decision

Phased approach to reduce DOM element count:

### Phase 1 (Accepted, Implemented)

1. **Hidden navigation links → JavaScript object**: Removed 2 hidden anchor
   elements, replaced with `window.navigationLinks` object
2. **Related posts restructure**: Simplified from 5+ wrapper elements to
   semantic `<aside>` with direct anchor links (-2-4 elements)
3. **Lazy-load badge images**: Added `loading="lazy"` to 8 badge images
4. **Search widget consolidation**: Merged wrapper divs (-1 element)

**Result**: 98 → ~91-93 elements (~5-7% reduction)

### Phase 2 (Proposed, Not Yet Implemented)

1. **Social link SVGs → Unicode/icon font**: Replace 8 SVG icons with Unicode
   characters (-17-20 elements)
2. **h-card → JSON-LD**: Convert hidden microformat div to structured data
   script (-6 elements)
3. **Remove aria-hidden anchors**: Remove redundant microformat anchors
   (-2 elements)

**Target**: ~65-68 elements (-33-35% total reduction)

### Phase 3 (Proposed, Lower Priority)

Badge images as CSS backgrounds instead of `<img>` tags (-8 elements).

## Consequences

**Easier:**

- Faster style calculations and layout
- Lower memory usage
- Better Lighthouse DOM scores

**Harder:**

- Phase 2 SVG→Unicode may reduce icon clarity on some devices
- h-card→JSON-LD requires validating IndieWeb compatibility
