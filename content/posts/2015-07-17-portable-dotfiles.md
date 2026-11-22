---
title: "Portable dotfiles"
date: 2015-07-17T15:12:16-03:00
draft: true
tags:
  - dev
  - git
  - legacy
---

[In the past]({{< ref "2015-03-05-documented-dotfiles" >}}), I tried to make my
[dotfiles](https://github.com/thiagowfx/dotfiles) more accessible. I'm not sure
if I achieved this at the time; anyway, yesterday I reorganized them all and
    made them *truly* portable.

I would create my own methods to do that, however I hate reinventing the wheel,
so fortunately I stumbled upon [dotfiles.github.io](http://dotfiles.github.io),
which led me to the awesome Thoughtbot's
[rcm](https://github.com/thoughtbot/rcm). Actually, I already have stumbled upon
`rcm` before, but I didn't care about it at the time.

Anyways, after adopting it, I can say it is really nice and I do recommend it.
Also, it should be portable across several (if not all) *unixes*.

## tl;dr

To clone my dotfiles in a new machine, it is just a matter of:

- `git clone` the right repo (<https://github.com/thiagowfx/dotfiles>)
- have the `rcm` tools in your system – either through a package, or compiled in
  a local directory temporarily (it uses the autotools toolchain)

```shell
% rcup
```

In fact, I could have included the rcm tools in my dotfiles repo too, but I
decided not to do that, at least for now. Also, there is a `Makefile` in there
which automates the process for the lazy ones (-; – except about the part of
getting/compiling `rcm`.
