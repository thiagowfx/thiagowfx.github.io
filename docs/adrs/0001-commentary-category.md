# ADR-0001: Commentary Category

## Status

Accepted

## Date

2025-01-04

## Context

The blog lacked a dedicated format for link blog posts—short posts that link to
external content with personal commentary. This pattern is common in the
IndieWeb community, inspired by Simon Willison's approach.

Posts like "Reply to: ..." were scattered without a unifying category.

## Decision

Created a new "commentary" category for link blog format posts:

1. **Archetype**: `archetypes/commentary.md` with frontmatter including
   `category: commentary` and `external_link` field
2. **Justfile recipe**: `just commentary "title"` (alias: `just comment`)
3. **Migrated 11 existing posts** to commentary category with `external_link`
   populated

Posts in this category:

- Link to external content with personal commentary
- Are short, focused posts adding context or perspective
- Often replies to or reactions to other blog posts/articles
- Include quotations or key takeaways from linked content

## Consequences

**Easier:**

- Creating new link blog posts with consistent structure
- Filtering/browsing commentary posts via `/categories/commentary/`
- Distinguishing original content from reactions/replies

**Harder:**

- Nothing significant
