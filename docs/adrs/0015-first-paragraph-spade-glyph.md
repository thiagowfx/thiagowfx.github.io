# ADR-0015: Spade glyph on the first paragraph

## Status

Accepted

## Date

2026-07-18

## Context

Two separate mechanisms prepend a spade glyph (`♠`) to the start of each post:

- **HTML page** (`assets/theme.css`, added in `0a3e8cb7`): a CSS rule
  `.e-content > p:first-child::before { content: "♠"; … }` renders the glyph
  before the post body on the site.
- **RSS feed** (`layouts/_default/rss.xml`, added in `29a4aede`): a
  `replaceRE` on the rendered `.Content` prepends `♠` to the first `<p>` in
  the feed item HTML.

Both were written assuming every post opens with a paragraph. That assumption
does not hold.

### Problem 1 — HTML: `p:first-child` misses list/heading-first posts

`p:first-child` matches a `<p>` only when it is literally the first child of
`.e-content`. Posts that open with a list, blockquote, or heading (e.g.
`content/posts/2026-07-18-the-lifecycle-of-physical-books.md`, whose body
starts with a `<ul>`) have a non-`<p>` first child, so the rule never fires and
no spade appears.

`p:first-of-type` would match the first `<p>` regardless of what precedes it,
but as a direct-child selector (`.e-content > p:first-of-type`) it targets the
first *top-level* paragraph. On a list-first post the first top-level `<p>`
can be well into the body (paragraphs inside `<li>` are not direct children of
`.e-content`), so the spade would land on a mid-post paragraph rather than the
visual opening — arguably worse than nothing.

### Problem 2 — RSS: regex hits the first `<p>` anywhere

The feed's `replaceRE \`(<p>)\` \`${1}♠ \` $content 1` replaces the first
literal `<p>` in the serialized HTML. On a list-first post that first `<p>` is
the one nested inside the opening `<li>`, so the RSS spade and the (absent)
HTML spade disagree about where "the start of the post" is.

### Related fix

The RSS `replaceRE` originally used a piped form
(`$content | replaceRE \`(<p>)\` \`${1}♠ \` 1`). Hugo's pipe appends the piped
value as the *last* argument, so `1` was read as the INPUT and `$content` as
the LIMIT, failing to cast the HTML string to an int and breaking
`hugo`/`just build` for the `recipes` category feed. Fixed in `a0c53a72` by
passing arguments explicitly:
`replaceRE \`(<p>)\` \`${1}♠ \` $content 1`. That fix is orthogonal to the
placement question above — it made the feed build again, not the glyph land
correctly on list-first posts.

## Decision

Keep `.e-content > p:first-child` for HTML and only add the RSS glyph when the
rendered content begins with a paragraph. Anchor the RSS replacement regex to
the start of `.Content`: `^(<p>)`.

Posts beginning with a list, blockquote, heading, or other block receive no
spade on either surface. The glyph is decorative, so omission is preferable to
placing it inside a nested paragraph or midway through the post.

Alternatives rejected:

1. **`.e-content > p:first-of-type`** — places the glyph on the first top-level
   paragraph, which may be midway through a list-first post.
2. **`.e-content > :first-child`** — prefixes blocks such as lists and headings,
   where the glyph reads oddly.

## Consequences

- HTML and RSS agree: paragraph-first posts receive a spade; other posts do not.
- The RSS regex no longer inserts the glyph into nested paragraphs.
- The glyph remains purely decorative and degrades gracefully when omitted.
- Authors who want the glyph can begin a post with a paragraph.
