---
title: "typst: color-coded choir parts"
date: 2026-09-03T16:54:39+02:00
tags:
  - bloggify
  - dev
---

[Previously]({{< ref "2026-02-07-making-a-slides-presentation-in-2026" >}}).

**Problem statement**: a plain lyrics sheet does not say who sings what. In a
choir rehearsal one has to annotate every line by hand: sopranos here, everybody
on the refrain.

Two files, one helper, no music engraving:

```shell
% ls
AGENTS.md  main.pdf  main.typ  template.typ
```

`template.typ` holds the styling only — page, font, headings:

```typst
#let template(doc) = {
  set page(paper: "a4", margin: (left: 2cm, right: 2cm, top: 2cm, bottom: 2cm))
  set text(font: "Libertinus Serif", size: 11pt, lang: "en")
  set heading(numbering: none)

  show heading.where(level: 1): it => {
    set text(size: 24pt, weight: "bold")
    set align(center)
    it
    v(0.5em)
  }

  doc
}
```

`main.typ` holds the content, plus a `parts_line()` that draws one colored
square per voice above the lyrics:

```typst
#let parts_line(parts_colors, lyrics) = {
  let squares = parts_colors.map(((part, color)) => {
    box(width: 1em, height: 1em, fill: color, stroke: rgb("#000"), inset: 0pt)
  }).join(h(0.2em))

  set align(left)
  [#squares \ #lyrics]
}

#let soprano = rgb("#ffc0cb")
#let alto = rgb("#90ee90")
#let tenor = rgb("#ffffff")
#let bass = rgb("#87ceeb")
#let all = rgb("#f0f0f0")
```

The verse then reads almost like the score:

```typst
== Verse 1

#parts_line((("S", soprano), ("B", bass)), "Oh the weather outside is frightful,")
#parts_line((("all", all),), "And since we've no place to go.")
#parts_line((("S", soprano), ("A", alto), ("T", tenor), ("B", bass)), "Let It Snow! Let It Snow! Let It Snow!")
```

Two pages, a sixth of a second:

```shell
% typst --version
typst 0.15.1 (unknown commit)

% time typst compile main.typ
typst compile main.typ  0.04s user 0.07s system 63% cpu 0.169 total
```

Tenor is white and only visible because of the black stroke, which is a happy
accident: on a photocopy it still reads as a distinct part. The `"S"` and `"B"`
strings are ignored by the helper — they are there so the source stays readable
without counting colors.
