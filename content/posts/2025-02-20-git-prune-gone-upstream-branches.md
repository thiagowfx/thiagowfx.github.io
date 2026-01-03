---
title: "git: prune gone upstream branches"
date: 2025-02-20T11:43:04+01:00
tags:
  - dev
  - git
---

**Problem statement**: Delete all local git branches whose upstream counterparts
have already been merged ("gone" in git lingo).

Augment your `~/.gitconfig`:

```ini
[alias]
	prune-gone = !git fetch -p && git branch -vv | awk '/: gone]/{print $1}' | xargs -r git branch -D
```

Run `git prune-gone`. That's it.

It lists all branches that are "gone" and deletes them.

I have another git alias (`'world'`) to do all this sort of _clean-up_ tasks at
once:

```ini
[alias]
    world = !git fetch --all && git remote prune origin && git prune-gone
```
