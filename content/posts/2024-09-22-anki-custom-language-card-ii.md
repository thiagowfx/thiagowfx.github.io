---
title: "Anki: custom language card (cont.)"
date: 2024-09-22T13:02:39+02:00
toc: true
tags:
  - bestof
  - dev
---

This post builds upon the previous [Anki: custom language card]({{< ref
"2024-02-03-anki-custom-language-card" >}}).

## Searching word boundaries

When searching for a word such as _Mann_, results such as _Mannschaft_ come up.

To search accounting for the word boundary, like a typical `\bMann\b` regex, use
`w:`. In this example: `w:Mann`.

## Searching ignoring accents

When searching for a word with Umlauts such as _Über_, you should type it
exactly as is.

If you are lazy or do not recall where the umlaut falls, perhaps you would think
of searching for _uber_, however that does not work.

To make it work, prepend `nc:` to the word. In this case: `nc:uber` will
properly match _über_. NC stands for non-combining.

## Searching word boundaries **whilst** ignoring accents

Is it possible to combine the two aforementioned operators? For example, to
match _für_. Unfortunately, [it is
not](https://stackoverflow.com/questions/79011851/anki-how-to-match-while-using-both-w-and-nc-simultaneously).
Anki does not support `w:nc:fur` nor `nc:w:fur`, which is unfortunate. _Schade_!

In this case the best compromise would be to search for `w:für`.

## Adding images to flashcards

It is pretty straightforward: Right click the image in your favorite web
browser, copy it, and then paste it (Ctrl/Cmd + V) into Anki. The image is
automatically imported.

No-brainer image sources:

- [dict.cc](https://dict.cc/)
- [Google Images](https://images.google.com/)

Nowadays it would also be natural[^1] to use "AI" to generate images.

## Providing examples: style

To illustrate with a concrete example:

**1**: <u>Ja</u>, genau.

**2**: Das ist <u>ja</u> komisch.

_Affirmative_

The structure:

- **Bold** numbers to disambiguate
- <u>Underscore</u> the word in question to emphasize it
- _Italicize_ everything that is meta or an explanation about the word

To highlight substrings, e.g. _Mann_ in _Mannschaft_, use underscores[^2].

## Tags

I seldom tag notes because there is no need for categorization, all cards are
treated the same way. Tagging is only useful in two scenarios:

- for grouping / retrieval: for example, if you want to make custom study
  sessions for a specific domain / area (e.g. animals, programming, trips)

- for provenance annotations: to make it easier to remember where a given note
  came from (e.g. "textbook", "my german teacher", "blog", "podcast", "work")

Adding tags creates the burden of managing and standardizing them. You do not
want to spend valuable mental effort derailing from your main task.

## Sources

- https://docs.ankiweb.net/searching.html

[^1]: Albeit deeply unnecessary and wasteful (energy-wise).
[^2]: This principle is not strict. I often interchange bold and underscore.
    Choose whichever feels more natural in the appropriate context.
