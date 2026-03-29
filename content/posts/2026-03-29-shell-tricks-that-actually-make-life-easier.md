---
title: "Reply to: Shell tricks that actually make life easier (and save your sanity) | larvitz blog"
date: 2026-03-29T16:21:49+02:00
categories:
  - commentary
tags:
  - dev
external_link: "https://blog.hofstede.it/shell-tricks-that-actually-make-life-easier-and-save-your-sanity/"
---

> There is a distinct, visceral kind of pain in watching an otherwise brilliant
> engineer hold down the Backspace key for six continuous seconds to fix a typo
> at the beginning of a line.

I would be lying if I said I don't cringe upon observing this action.

What an amazing collection of tips & tricks!

I use most of these 'tricks' all the time, pretty much every week. They are
compatible with `bash` and `zsh`.

There are two constructs I don't use much that would be useful for me to learn:

> **The Everything-Logger**
>
> `command |& tee file.log`: Standard pipes (`|`) only catch standard output
> (`stdout`). If a script throws an error (`stderr`), it skips the pipe and
> bleeds directly onto your screen, missing the log file. |& pipes both stdout
> and stderr (it's a helpful shorthand for `2>&1 |`).

and

> **Backgrounding and Disowning**
>
> You started a massive, hour-long database import task, but you forgot to run
> it in `tmux` or `screen`. It's tying up your terminal, and if your SSH
> connection drops, the process dies. Panic sets in.
>
> [...]
>
> `CTRL + Z`, then `bg`, then `disown`

The author ends with:

> The shell is a toolbox, not an obstacle course. You don't need to memorize all
> of these today. Pick just one trick, force it into your daily habits for a
> week, and then pick another. Stop letting the terminal push you around, and
> start rearranging the furniture. It's your house now.

...which I vehemently agree with.
