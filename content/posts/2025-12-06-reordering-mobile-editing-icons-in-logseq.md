---
title: "Reordering mobile editing icons in logseq"
date: 2025-12-06T00:42:32-03:00
tags:
  - dev
  - serenity
---

[Reordering mobile editing icons in
logseq](https://bate.dev/posts/logseq-mobile/) by Colin Bate:

> I found a way to avoid needing to constantly scroll sideways to access the
> icons I need.

This is why I love the indie web.

I was looking for how to do exactly the same operation, for exactly the same
icon.

Isn't it so amazing when a person documents their solutions publicly online, in
the open? Colin, you are my hero.

Update `custom.css` in LogSeq settings:

```css
/* Move icons 3+ to order 2 */
#mobile-editor-toolbar .toolbar-commands > div:nth-child(n+3) {
  order: 2;
  color: var(--cyan);
}

/* Insert icon 11 (brackets) at order 1 */
#mobile-editor-toolbar .toolbar-commands > div:nth-child(11) {
  order: 1;
  color: var(--orange);
}
```

**Side effect**: The `[]` wikilink button will be moved to be the third one in
the editor bar.
