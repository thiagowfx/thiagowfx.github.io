---
title: "git stash -m"
date: 2025-11-23T13:14:09-03:00
tags:
  - dev
  - git
---

When running `git stash`, it's possible to pass a "stash message" to it with
`-m`, just like how you give a "commit message" to `git commit`.

```shell
git stash -m "first draft, approach #1 from design doc"
```

You can view past stashes with `git stash list`:

```shell
% git stash list
stash@{0}: On master: first draft, approach #1 from design doc
[...]
```

Now your ~~junk~~ stashes can be properly organized!
