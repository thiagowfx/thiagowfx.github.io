# ADR-0015: Spade glyph on the first paragraph

## Status

Proposed

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

Not yet decided. Options considered:

1. **`.e-content > p:first-of-type`** — spade on the first top-level paragraph,
   even after a leading list/heading. CSS-only, but on list-first posts the
   glyph lands mid-body, not at the visual opening.
2. **`.e-content > :first-child`** — spade on the very first block whatever its
   type. Guarantees a glyph at the opening, but prefixes a `<li>` bullet or a
   heading, which reads oddly.
3. **Leave `p:first-child`** — accept that list/heading-first posts get no
   spade. Simplest; the glyph is decorative, not load-bearing.

Whatever is chosen for the HTML page, the RSS regex should be reconciled so the
two surfaces agree on where "the start" is (or the divergence accepted
explicitly).

## Consequences

- Until decided, list-first posts show the spade in the feed (on a nested
  `<p>`) but not on the HTML page — an inconsistency between surfaces.
- The glyph is purely decorative; absence degrades gracefully. This is low
  urgency.
- Any chosen selector interacts with post-authoring conventions: if most posts
  open with a paragraph, `p:first-child` already covers them and only the
  list/heading-first minority is affected.
