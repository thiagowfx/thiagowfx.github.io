---
title: "Making a slides presentation in 2026"
date: 2026-02-07T18:40:50+01:00
tags:
  - ai
  - bestof
  - dev
  - serenity
---

**Problem statement**: make a _slides_ presentation for a certain business or
academic use case.

## Part I: What?

**Classic approach**: pick one of: LibreOffice, Microsoft PowerPoint, Google
Slides.

**Hipster approach**: pick one of: Notion, [Reveal.JS](https://revealjs.com/)
(or similar), [Golang present](https://pkg.go.dev/golang.org/x/tools/present),
[Prezi](https://prezi.com/).

**Academic approach**: [LaTeX
beamer](https://www.overleaf.com/learn/latex/Beamer),
[LyX](https://www.lyx.org/).

**Minimalist approach**: [Emacs Org
mode](https://orgmode.org/worg/org-tutorials/non-beamer-presentations.html),
[Terminal](https://github.com/sotte/presenting.vim).

Of course, I am pioneering – by choosing none of the above!

We'll settle with [Typst](https://typst.app/) +
[Polylux](https://polylux.dev/book/), because we want best-in-class™
presentations:

> Polylux is a package for the typesetting system Typst to create presentation
> slides, just like you would use the beamer package in LaTeX. (So far, it is
> much less advanced than beamer, obviously.)
>
> If you haven't heard of things like LaTeX's beamer before, here is how this
> works: As a rule of thumb, one slide becomes one PDF page, and most PDF
> viewers can display PDFs in the form of a slide show (usually by hitting the
> F5-key).

But first, a bit of trivia:

> Why the name?
>
> A polylux is a brand of overhead projectors very common in Eastern German
> schools (where the main author of this package grew up). It fulfils a similar
> function to a projector, namely projecting visuals to a wall to aid a
> presentation. The German term for projector is beamer, and now you might
> understand how it all comes together. (The original author of the
> aforementioned LaTeX package is German as well.)

_Germans, Germans everywhere_ {picture the Buzz Lightyear meme here}

## Part II: You are pretty and you know it

I am not using the default theme. Sorry, that's just not gonna happen.

Built-in
[beamer](https://deic.uab.cat/~iblanes/beamer_gallery/index_by_theme.html)
[themes](https://www.overleaf.com/learn/latex/Beamer) inspire me. I choose
[metropolis](https://typst.app/universe/package/metropolis-polylux/), with a few
bits of [beamer
frankfurt](https://deic.uab.cat/~iblanes/beamer_gallery/large/Frankfurt-default-default-12.png)
sprinkled in (mainly the top navigation guides).

Such a short section, so cute! ✨

## Part III: How?

It's 2026. Agentic LLMs are all the rage.

Obviously, we're going to use [Claude
Code](https://code.claude.com/docs/en/overview). It's the obvious choice.
[Nothing else comes close](https://acecombat.fandom.com/wiki/Loading_quotes).

OK, I'll also give you a break if you use OpenAI, it comes in a close second. No
other choice is possible. Not if you want to become state-of-the-art. Sorry.

[Checklist](https://www.goodreads.com/book/show/6667514-the-checklist-manifesto):

- have claude code installed? Check
- have enough, readily available tokens to burn? Check
- have a [workspace]({{< ref "2025-12-02-try" >}}) ready? Check
- have `git init` run in the workspace? Check
- have two claude code sessions open, one for content and one for form? Check
- have a `Justfile` ready? Check

```make {filename="Justfile"}
watch:
        typst watch slides.typ
```

## Part IV: [The Future Starts With You](https://www.youtube.com/watch?v=XJIgHWnkcnA)

Good luck out there!

Iterate.
Tell the LLM what you want.
Be verbose in your prompting.
Course-correct as needed.

There's no right or wrong from here.

[**Just do it**](https://www.youtube.com/watch?v=ZXsQAXx_ao0)!
