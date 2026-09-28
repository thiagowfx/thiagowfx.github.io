---
title: "typst: reusable polylux slides with section navigation"
url: https://perrotta.dev/2026/09/typst-reusable-polylux-slides-with-section-navigation/
last_updated: 2026-09-29
---


[Previously]({{< ref "2026-02-07-making-a-slides-presentation-in-2026" >}}).

**Problem statement**: how can I reuse a Typst slide layout without rebuilding its
section navigation every time?

Here is the complete [Polylux](https://polylux.dev/book/) template. Put these
three files in one directory. `theme.typ` owns the Metropolis-inspired layout
and Frankfurt-style navigation: section names above one dot per content slide.
Its state records the section counts and active slide. `new-section` creates a
divider without a dot; `slide` adds a dot; `untracked-slide` is for title or
closing pages.

```typst {filename="theme.typ"}
// =============================================================================
// Metropolis theme + Frankfurt-style navigation bar with mini-frame dots
// =============================================================================
// Visual style: Metropolis (navy blue, light blue accent, clean typography)
// Navigation:   Frankfurt (section names + circle dots for slide progress)
// =============================================================================

#import "@preview/polylux:0.4.0": *
#let _polylux-slide = slide

// ---------------------------------------------------------------------------
// Colors — Navy blue palette
// ---------------------------------------------------------------------------
#let dark-teal = rgb("#1a2744")    // navy blue (primary dark)
#let bright = rgb("#4a90d9")       // accent / emphasis (medium blue)
#let brighter = rgb("#a8c4e0")     // muted light blue
#let bg = white.darken(2%)
#let fg = dark-teal

// ---------------------------------------------------------------------------
// Navigation state — tracks slides per section for mini-frame dots
// ---------------------------------------------------------------------------
#let _nav-sections = state("nav-sections", ())       // [{name, count}, ...]
#let _nav-current-sec = state("nav-current-sec", -1)  // index into sections
#let _nav-current-frame = state("nav-current-frame", 0)

#let _begin-section(name) = {
  _nav-sections.update(secs => {
    secs.push((name: name, count: 0))
    secs
  })
  _nav-current-sec.update(i => i + 1)
  _nav-current-frame.update(_ => 0)
}

#let _count-frame() = {
  context {
    let sec-idx = _nav-current-sec.get()
    if sec-idx >= 0 {
      _nav-current-frame.update(f => f + 1)
      _nav-sections.update(secs => {
        if sec-idx < secs.len() {
          secs.at(sec-idx).count += 1
        }
        secs
      })
    }
  }
}

// ---------------------------------------------------------------------------
// Navigation header — section names + mini-frame circles
// ---------------------------------------------------------------------------
#let _nav-header() = context {
  let all-secs = _nav-sections.final()
  let curr-sec = _nav-current-sec.get()
  let curr-frame = _nav-current-frame.get()

  if all-secs.len() == 0 { return }

  set text(fill: white, size: 0.5em, weight: "bold")

  let n = all-secs.len()

  // Row 1: Section names
  let names-row = all-secs.enumerate().map(((i, sec)) => {
    let is-current = i == curr-sec
    let is-past = i < curr-sec
    let name-color = if is-current { white } else if is-past { white.darken(10%) } else { white.darken(35%) }
    align(center, text(fill: name-color, sec.name))
  })

  // Row 2: Mini-frame dots (aligned under each section name)
  let dots-row = all-secs.enumerate().map(((i, sec)) => {
    let is-current = i == curr-sec
    let is-past = i < curr-sec

    let dots = range(sec.count).map(j => {
      let frame-num = j + 1
      let dot-fill = if is-past {
        white.darken(10%)
      } else if is-current and frame-num < curr-frame {
        white.darken(5%)
      } else if is-current and frame-num == curr-frame {
        bright
      } else {
        none
      }
      let dot-stroke = if dot-fill == none { 0.6pt + white.darken(30%) } else { none }
      let fill = if dot-fill == none { dark-teal } else { dot-fill }
      box(circle(radius: 2.5pt, fill: fill, stroke: dot-stroke))
    })
    align(center, dots.join(h(2.5pt)))
  })

  // Combine into a two-row grid
  block(width: 100%, fill: dark-teal, inset: (x: 0.6em, y: 0.3em),
    grid(
      columns: (1fr,) * n,
      row-gutter: 0.25em,
      ..names-row,
      ..dots-row,
    )
  )
}

// ---------------------------------------------------------------------------
// Slide title header (Metropolis style — below nav bar)
// ---------------------------------------------------------------------------
#let _title-header = toolbox.next-heading(h => {
  show: toolbox.full-width-block.with(fill: dark-teal, inset: (x: 1em, y: 0.6em))
  set align(horizon)
  set text(fill: bg, size: 1em)
  strong(h)
})

// ---------------------------------------------------------------------------
// Footer — Metropolis style
// ---------------------------------------------------------------------------
#let _the-footer(content) = {
  set text(size: 0.7em)
  show: pad.with(0.5em)
  set align(bottom)
  context text(fill: fg.lighten(40%), content)
  h(1fr)
  toolbox.slide-number
}

// ---------------------------------------------------------------------------
// Progress bar — Metropolis style (blue)
// ---------------------------------------------------------------------------
#let progress-bar = toolbox.progress-ratio(ratio => {
  set grid.cell(inset: (y: 0.03em))
  grid(
    columns: (ratio * 100%, 1fr),
    grid.cell(fill: bright)[],
    grid.cell(fill: brighter)[],
  )
})

// ---------------------------------------------------------------------------
// Public API: slide (tracked), new-section, focus, alert, note, divider
// ---------------------------------------------------------------------------

/// Content slide — automatically tracked in the navigation bar.
/// Use `= Title` as the first line for the slide title.
#let slide(body) = {
  _count-frame()
  _polylux-slide(body)
}

/// Section divider slide — registers a new section and shows a title card.
/// Not counted in mini-frame dots.
#let new-section(name) = {
  _begin-section(name)
  _polylux-slide({
    set page(header: none, footer: none)
    toolbox.register-section(name)
    show: pad.with(20%)
    set text(size: 1.5em, fill: fg)
    name
    progress-bar
  })
}

/// Focus slide — inverted colors for key messages.
#let focus(body) = context {
  set page(header: none, footer: none, fill: dark-teal, margin: 2em)
  set text(fill: bg, size: 1.5em)
  set align(center + horizon)
  body
}

/// Untracked slide — for title, closing, etc. No navigation counting.
#let untracked-slide(body) = _polylux-slide(body)

/// Blue divider line
#let divider = line(length: 100%, stroke: 0.1em + bright)

/// Alert text (blue bold)
#let alert(body) = text(fill: bright, weight: "bold", body)

/// Two-column layout helper — e.g. diagram left, bullets right
#let side-by-side(left, right, ratio: 1fr) = {
  grid(
    columns: (ratio, 1fr),
    gutter: 1em,
    left, right,
  )
}

/// Captioned image from assets directory
#let fig(path, caption: none, width: 80%) = {
  align(center,
    figure(
      image("assets/" + path, width: width),
      caption: if caption != none { text(size: 0.75em, caption) },
    )
  )
}

/// Speaker notes — pass `--input notes=false` to hide
#let note(body) = {
  let hidden = sys.inputs.at("notes", default: "true") == "false"
  if not hidden {
    place(bottom + left, dx: 0pt, dy: 0.8em)[
      #block(
        width: 100%,
        inset: 6pt,
        fill: rgb("#fef9c3").transparentize(20%),
        radius: 4pt,
        text(size: 10pt, style: "italic", fill: fg, body),
      )
    ]
  }
}

// ---------------------------------------------------------------------------
// Theme setup — call as:  #show: theme.setup.with(...)
// ---------------------------------------------------------------------------
#let setup(
  footer: none,
  navbar: true,
  text-font: "Avenir Next",
  math-font: "Avenir Next",
  code-font: "IBM Plex Mono",
  text-size: 22pt,
  body,
) = {
  set page(
    paper: "presentation-16-9",
    fill: bg,
    margin: (top: if navbar { 4.5em } else { 3em }, left: 1.2em, right: 1.2em, bottom: 1.8em),
    header: {
      set align(top)
      if navbar { toolbox.full-width-block[#_nav-header()] }
      _title-header
    },
    footer: _the-footer(footer),
  )

  set text(
    font: text-font,
    size: text-size,
    fill: fg,
  )
  set strong(delta: 100)
  show math.equation: set text(font: math-font)
  show raw: set text(font: code-font)
  show raw.where(block: true): it => block(
    width: 100%,
    fill: luma(240),
    inset: 10pt,
    radius: 3pt,
    stroke: 0.5pt + luma(200),
    it,
  )
  set align(horizon)
  set list(spacing: 1.4em)
  set enum(spacing: 1.4em)
  show emph: it => text(fill: bright, it.body)
  show heading.where(level: 1): _ => none

  body
}
```

```typst {filename="slides.typ"}
#import "theme.typ"
#import theme: slide, untracked-slide, new-section, alert, note

#show: theme.setup.with(
  footer: [Slide template],
  text-font: "Libertinus Serif",
  code-font: "DejaVu Sans Mono",
  text-size: 22pt,
)

#untracked-slide[
  #set page(header: none, footer: none)
  #set align(center + horizon)
  #text(size: 1.5em, weight: "bold")[Slide template]
]

#new-section[First section]

#slide[
  = First slide

  A #alert[highlight] and a speaker note.

  #note[This note is absent from the audience PDF.]
]

#slide[
  = Second slide

  The navigation bar counts this slide within the first section.
]

#new-section[Second section]

#slide[
  = Third slide

  The section changes, and the dot count starts again.
]
```

```just {filename="Justfile"}
watch:
    typst watch --input notes=true slides.typ

all: build audience

build:
    typst compile --input notes=true slides.typ

alias speaker := build

audience:
    typst compile --input notes=false slides.typ slides-audience.pdf
```

`slides.typ` is a minimal deck with two sections, three tracked slides, an
untracked title, and a speaker note. Change its content and fonts for a new
presentation; keep the theme and build recipes.

`Justfile` produces two PDFs from the same source. `notes=false` hides speaker
notes from the audience copy:

```text
% just all
typst compile --input notes=true slides.typ
typst compile --input notes=false slides.typ slides-audience.pdf
```

