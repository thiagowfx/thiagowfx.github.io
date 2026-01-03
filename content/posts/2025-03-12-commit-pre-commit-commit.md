---
title: "commit, pre-commit, commit"
date: 2025-03-12T16:41:53+01:00
tags:
  - dev
  - pre-commit
---

[Premature optimization is the root of all
evil](https://en.wikipedia.org/wiki/Program_optimization) but I run into this
almost every single day, it's time to finally address it.

**Problem statement**: When using [pre-commit](https://pre-commit.com/) with a
hook that will automatically fix an issue, the commit will fail the first time
it runs. This means I need to issue two `git commit -a` commands in order to
effectively create a commit: the first one will trigger `pre-commit run`, the
second one will add the changes / fixes done by it. The question is: how can I
merge these two steps into a single command?

There are several ways to tackle this issue:

- create a custom shell script that does a double commit invocation
- create a `git` alias that does a double commit invocation
- use a native shell solution

I am hesitant to pollute my dotfiles with more scripts, hence I'd rather find a
native shell solution.

I came up with this very simple idea: since I use `zsh`, leverage the [`repeat`
built-in](https://zsh.sourceforge.io/Doc/Release/Shell-Grammar.html):

> repeat word do list done
>
> word is expanded and treated as an arithmetic expression, which must evaluate to a number n. list is then executed n times.

```shell
% repeat 2 git commit -a -m "feat: bootstrap time travel"
```

This only works iff I _really_ want to commit everything that is in the staging
area (the git index).
