---
title: "Logseq: linking and backlinking"
date: 2025-01-06T22:49:44-03:00
tags:
  - selfhosted
---

This is the first post about LogSeq / PKM. Run before it's [too
late](https://en.wikipedia.org/wiki/The_Paradox_of_Choice)!

Expect more of these as I find myself slowly migrating from
[Obsidian](https://obsidian.md/) to [Logseq](https://logseq.com/). More on that
later.

When creating pages in logseq, there are **two** basic forms to link to other pages,
and they are essentially equivalent.

The first one is to use a `#hashtag` (or simply 'tag'). For example:

```
Books to read in 2010:

- The Hitchhiker's Guide to the Galaxy by Douglas Adams #book #fiction
- Harry Potter and the Prisoner of Azkaban by J.K. Rowling #book #fiction
- Elite da Tropa by André Batista, Rodrigo Pimentel & Luiz Eduardo Soares #book #nonfiction
```

_^alpha_

Under the hood it creates 3 pages: `Book`, `Fiction` and `Nonfiction`. Clicking
any of these hashtags opens up the corresponding page. In the page it's possible
to find a backlink to the original page / block that links to it.

The second one is to use double brackets. For example:

```
- Elite da Tropa is a Brazilian [[book]] written by the ex-police officers André
  Batista and Rodrigo Pimentel together with Luiz Eduardo Soares. It was first
  published in 2006. The book originated the film Elite Squad.
  - Source: https://en.wikipedia.org/wiki/Elite_da_Tropa
```

_^bravo_

Clicking `[[book]]` goes to the same page as `#book`.

Why are there two forms? I don't know. But here's what I learned: it doesn't
matter which one you choose to use, as they are effectively equivalent. For
example, you could have written instead:

```
- Elite da Tropa is a Brazilian #book written by the ex-police officers André
  Batista and Rodrigo Pimentel together with Luiz Eduardo Soares. It was first
  published in 2006. The book originated the film Elite Squad.
  - Source: https://en.wikipedia.org/wiki/Elite_da_Tropa
```

_^charlie_

...the effect would have been the same.

The idiomatic style seems to favour the use of double brackets when writing
prose (i.e. _bravo_), and the use of hashtags when "tagging" or qualifying
sentences (i.e. _alpha_). That said, intermixing them is harmless.
