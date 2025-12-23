---
title: "myrepos: chain configs"
date: 2025-12-22T14:45:45-03:00
tags:
  - dev
---

[myrepos](https://myrepos.branchable.com/):

> You have a lot of version control repositories. Sometimes you want to update
> them all at once. Or push out all your local changes. You use special command
> lines in some repositories to implement specific workflows. Myrepos provides a
> mr command, which is a tool to manage all your version control repositories.

I use `mr` to manage my local git checkouts, see my
[`~/.mrconfig`](https://github.com/thiagowfx/.dotfiles/blob/master/git/.mrconfig).

From `$HOME`, running `mr update` keeps all managed repositories up-to-date
(`git fetch` / `git pull`).

**Problem statement**: Extend (chain) my mrconfig with git repositories from
work.

I keep my git repos from work in `~/Corp`.

Changing directory to it and running `mr update` updates work repos only.

The goal is to have `mr update` in `~` perform updates for personal AND work
repos. We can achieve this with configuration chaining.

This
[commit](https://github.com/thiagowfx/.dotfiles/commit/3f5c5e02dd7cc29bbc30d74f8329ce7bf654bd5e)
addresses it:

```
# chain corp repositories
include = test -f $HOME/Corp/.mrconfig && sed 's|^\[\([^/DEFAULT]\)|[Corp/\1|' $HOME/Corp/.mrconfig || true
```

**Rationale**: If `~/Corp/.mrconfig` exists, include it in the original
`~/.mrconfig`. The `sed` expression is necessary to adjust relative paths when
operating on work repos, so that they all stay within `~/Corp`, otherwise they
would be cloned in `~`.

The `test` and `|| true` is to make this inclusion optional, with graceful
degradation in case the work `.mrconfig` does not exist, thereby simply skipping
it.
