# Architecture Decision Records

This directory contains Architecture Decision Records (ADRs) for significant
technical decisions in the blog infrastructure.

## ADRs

<!-- markdownlint-disable MD013 -->

| Number | Title | Status | Date |
| ------ | ----- | ------ | ---- |
| [0001](0001-commentary-category.md) | Commentary Category | Accepted | 2025-01-04 |
| [0002](0002-performance-improvements.md) | Performance Improvements | Accepted | 2026-01-01 |
| [0003](0003-dom-optimization.md) | DOM Optimization | Partially Accepted | 2026-01-01 |
| [0004](0004-microformats-validation.md) | Microformats Validation | Proposed | 2026-01-01 |
| [0005](0005-webmention-support.md) | WebMention Support | Proposed | 2026-01-01 |

<!-- markdownlint-enable MD013 -->

## Adding New ADRs

1. Create a new file: `NNNN-short-title.md` (increment the number)
2. Use this template:

```markdown
# ADR-NNNN: Title

## Status

Proposed | Accepted | Deprecated | Superseded

## Date

YYYY-MM-DD

## Context

What is the issue that we're seeing that is motivating this decision?

## Decision

What is the change that we're proposing and/or doing?
Include its rationale.
Include alternatives considered where applicable.

## Consequences

What becomes easier or more difficult to do because of this change?
```
