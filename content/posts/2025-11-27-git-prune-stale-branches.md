---
title: "git: prune stale branches"
date: 2025-11-27T18:04:45-03:00
tags:
  - bestof
  - dev
---

**Problem statement**: Delete all local git branches whose counterpart remote
branches have already been merged upstream.

Update `~/.gitconfig`:

```gitconfig
[alias]
    prune-gone = !git fetch -p && git branch -vv | awk '/: gone]/{print $1}' | xargs -r git branch -D
    world = !git fetch --all && git remote prune origin && git prune && git prune-gone
```

Now simply run `git prune-gone` – or, even better, `git world` for a more
complete cleanup.

This is much more ergonomic than hunting down individual branches and doing `git
push origin :{my branch}`.
