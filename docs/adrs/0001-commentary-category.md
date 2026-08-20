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
   `categories: [commentary]` and the `external_link` field
2. **Justfile recipe**: `just commentary <url> ["optional title"]` (alias:
   `just comment`). The recipe fetches the page title when no title is given.
3. **Initial migration**: Added the commentary category and `external_link` to
   11 existing posts

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
