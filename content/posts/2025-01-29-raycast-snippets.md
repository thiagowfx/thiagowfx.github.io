---
title: "Raycast snippets"
date: 2025-01-29T13:52:23+01:00
tags:
  - bestof
  - dev
---

[Raycast](https://www.raycast.com/):

> Your shortcut to everything.
>
> A collection of powerful productivity tools all within an extendable launcher.
Fast, ergonomic and reliable.

It's for macOS only.
I originally heard of it via [DHH](https://world.hey.com/dhh).

One of its features I like is [snippets](https://manual.raycast.com/snippets):

> Write faster by using snippets to store and insert frequently used text.
> Expand them automatically with a keyword.
>
> Use the Create Snippet command to store a new snippet. If you specify a
> keyword, you can simply type it in any application to have it auto-expand
> in-place.
>
> Snippets are handy for frequently used text such as canned email responses,
> code or emojis.

For example, I can assign a `@@fzf` shortcut so that it expands to

```shell
[[ -f /usr/share/doc/fzf/examples/key-bindings.bash ]] && source /usr/share/doc/fzf/examples/key-bindings.bash
```

...which is quicker than (i) typing it out, (ii) retrieving it from a wiki
and/or second brain app.

Having text macros like these is handy whenever you do not have full control
over the environment.
If you happen to have control, you could always create a shell alias
and/or a `Makefile` target for ergonomics and discoverability.

These expansions can happen anywhere: terminal emulator, web browser, email
client, LLM prompt.

A follow-up feature I am interested in exploring is the ability to export
snippets from Raycast to a location within version control, such as
[dotfiles](https://github.com/thiagowfx/.dotfiles). It would be perfect if I
could manage them all via text in an easy to edit format such as YAML.

Another snippet example: `@@gca` expands to:

```
EDITOR=vim git commit --author="Thiago Perrotta <{my-corp-email}>"
```

I chose `@@` because that's a chord I am unlikely to type.
