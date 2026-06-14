---
title: "git: switch-to-default with wt"
date: 2026-06-14T20:03:03+02:00
tags:
  - dev
  - git
---

My `switch-to-default` git alias had been trying branch names in order:

```gitconfig
switch-to-default = !git switch --force main 2>/dev/null \
    || git switch --force master 2>/dev/null \
    || git switch --force $(git symbolic-ref refs/remotes/origin/HEAD \
        | sed 's@^refs/remotes/origin/@@')
```

It works, but it's trial-and-error. Different people and different projects
cannot decide whether to use `main` or `master`. It's a mess.

[Worktrunk](https://worktrunk.dev/tips-patterns/#reuse-default-branch)
tracks the default branch as part of its worktree state:

```shell
% wt config state default-branch
master
```

No need to guess!

New alias:

```gitconfig
switch-to-default = !git switch --force \
    $(wt config state default-branch 2>/dev/null \
        || git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null \
            | sed 's@^refs/remotes/origin/@@' \
        || echo master)
```

`wt` first, then fall back to `origin/HEAD` if `wt` is not installed, then
`master` as a last resort.

- - -

🤖 *Drafted with `/bloggify`.*
