---
title: "cmux: search all windows"
date: 2026-08-12T11:41:09+02:00
tags:
  - ai
  - bestof
  - dev
---

**Problem statement**: given a `cmux` session with a dozen[^1] workspaces, how can you
quickly find the one you're looking for?

Keyboard shortcut (macOS): `Cmd + ⌥ + F`.
[Source](https://cmux.com/docs/keyboard-shortcuts).

There's also a system tray icon for `cmux` with a `Search All Windows...` menu
item.

How did I look this up? Via [Kagi Search](https://kagi.com/search?q=cmux+search+shorcut%3F&r=no_region&sh=LJvrhfVS1VIXBrbO4rOJrw).
My query was `cmux search shorcut?`.

The question mark (`?`)[^2] at the end triggers the [quick
answer](https://help.kagi.com/kagi/ai/quick-answer.html) feature, including
links to sources:

> Kagi's Quick Answer quickly produces a summary of the results across the pages
> returned and provides references to the pages that are used. This
> functionality allows you to quickly consume the desired information from the
> search while giving you the pointers to dive deeper into the information if
> desired.

Whenever I know exactly the shape of the problem that I want to look up and
solve, and whenever it is byte-sized enough, I often resort to this approach; it
is very efficient.

In the ~~old~~ pre-LLM days, I would instead scour [Stack
Overflow](https://stackoverflow.com/) or the upstream documentations.

In the early LLM days, I would ask [ChatGPT](https://chatgpt.com/) or
[Duck](https://duck.ai/), but I'd be limited to the training cut-off of the
underlying model.


[^1]: _"""This should not happen"""_. We're poor humans with poor attention
    spans. Managing more than 4-7 workspaces at once is counter-productive due
    to context switching tax. One _should not_ end up in this situation in the
    first place.

[^2]: The friction of adding the question mark is important and deliberate, it
    is what enables the decision to get a digest of ~~slop~~ LLM results. I
    quite dislike the approach of [other search engines](http://google.com/),
    unconditionally shoving questionable AI results on everyone's face.

