# Commentary Category Setup

## Overview
Created a new blog category "commentary" for a link blog format, inspired by Simon Willison's approach (https://simonwillison.net/2024/Dec/22/link-blog/).

## What is a Commentary Post?
- Links to external content with personal commentary
- Short, focused posts that add context or perspective
- Often replies to or reactions to other blog posts/articles
- Includes quotations, screenshots, or key takeaways from linked content

## Implementation

### Archetype
Created `archetypes/commentary.md` with frontmatter for:
- title (auto-generated from filename)
- date (auto-set)
- category: commentary
- tags: (empty, to be filled per post)
- external_link: (optional URL for the main link being discussed)

### Justfile Recipe
Added `just commentary` (alias: `just comment`) recipe:
```bash
just commentary "post title"
```

Creates a new commentary post at `content/posts/YYYY-MM-DD-post-title.md`

## Posts to Migrate to Commentary

All "Reply to:" posts are excellent candidates for commentary:
1. 2024-12-28-reply-to-douglas-adams-on-reactions-to-technology-by-age.md
2. 2024-12-21-reply-to-i-hate-the-news.md
3. 2024-12-23-reply-to-introduce-yourself-to-your-remote-team.md
4. 2024-12-30-reply-to-co-pilot-having-a-normal-one.md
5. 2025-01-05-reply-to-my-approach-to-running-a-link-blog.md
6. 2025-01-05-reply-to-mistakes-engineers-make-in-large-established-codebases.md
7. 2025-01-20-reply-to-smash-that-subscribe-button.md
8. 2025-03-06-reply-to-growth-at-big-tech.md

Other commentary candidates:
- 2024-12-22-link-blogs.md
- 2024-12-31-independence.md
- 2025-01-03-100-days-to-offload.md

These are posts that link to external content with personal commentary, matching the link blog format.

## Migration Complete ✓
All 11 posts have been migrated to the commentary category with `external_link` field populated:
1. 2024-12-21-reply-to-i-hate-the-news.md
2. 2024-12-22-link-blogs.md
3. 2024-12-23-reply-to-introduce-yourself-to-your-remote-team.md
4. 2024-12-28-reply-to-douglas-adams-on-reactions-to-technology-by-age.md
5. 2024-12-30-reply-to-co-pilot-having-a-normal-one.md
6. 2024-12-31-independence.md
7. 2025-01-03-100-days-to-offload.md
8. 2025-01-05-reply-to-my-approach-to-running-a-link-blog.md
9. 2025-01-05-reply-to-mistakes-engineers-make-in-large-established-codebases.md
10. 2025-01-20-reply-to-smash-that-subscribe-button.md
11. 2025-03-06-reply-to-growth-at-big-tech.md

Build verification: ✓ Passed (1918 pages in 2121ms)
