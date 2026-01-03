---
title: "git diff interactively"
date: 2025-11-04T11:21:24+01:00
tags:
  - dev
  - git
---

It's possible to do `git patch -p` to review diff hunks interactively, one by
one.

Can we accomplish something similar with `git diff`? If not, is there a tool
that can accomplish that, in the same spirit of `git patch -p`, but with a
read-only-centric workflow?

The naïve approach is to simply run `git patch -p` and then press 'n' (no) for
each diff hunk. It does not feel particularly effective though.

I found another way, which embodies the spirit of `git patch -p` more
effectively: [`tig status`](https://jonas.github.io/tig/).

I already use `tig` every once in a while but wasn't aware that it could do that.

I won't try to illustrate the command output here (it's a TUI); simply give it a
try the next time you run `git diff` or `git add`.

It's also possible to stage per file and per hunk changes in the TUI. This
operation mode somewhats resemble
[`git-crecord`](https://github.com/andrewshadura/git-crecord):

> git subcommand to interactively select changes to commit or stage

...which I packaged to the [Arch User
Repository](https://aur.archlinux.org/packages/git-crecord) a long time ago, but
ended up barely using it. Let's see whether `tig status` will stick.
