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

```ini
[alias]
    prune-gone = !git fetch -p && git branch -vv | awk '/: gone]/{print $1}' | xargs -r git branch -D
    world = !git fetch --all && git remote prune origin && git prune && git prune-gone
```

Now simply run `git prune-gone` – or, even better, `git world` for a more
complete cleanup.

This is much more ergonomic than hunting down individual branches and doing `git
push origin :{my branch}`.

Example usage:

```shell
% ~/Workspace/pancake (git)-[master]
% git world
From github.com:thiagowfx/pancake
 - [deleted]         (none)     -> origin/thiagowfx/apkbuild-sync
 - [deleted]         (none)     -> origin/thiagowfx/wt-no-origin-graceful
remote: Enumerating objects: 13, done.
remote: Counting objects: 100% (13/13), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 8 (delta 5), reused 3 (delta 3), pack-reused 0 (from 0)
Unpacking objects: 100% (8/8), 2.61 KiB | 668.00 KiB/s, done.
   f727bd7..51f81ee  master     -> origin/master
Deleted branch thiagowfx/wt-cd-dash (was 6403261).
```
