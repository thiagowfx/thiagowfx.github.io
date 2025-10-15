---
title: "git: partially cherry-pick a commit"
date: 2025-10-15T11:08:27+02:00
tags:
  - dev
---

**OR**: "cherry-pick a cherry-pick".

[Adam Johnson](https://adamj.eu/tech/2025/09/08/git-partial-cherry-pick/):

> git cherry-pick allows you to copy a commit another branch to your current
> one.
>
> [...]
>
> One limitation with a straight-up git cherry-pick, as above, is that it always
> copies the entire commit. If a commit contains multiple changes, but you only
> want one of them, you'll need to undo the undesired cherry-picked changes.
> This can be tedious and error-prone.

The trick is to use the [`-n`
(`--no-commit`)](https://git-scm.com/docs/git-cherry-pick) argument to prevent changes from
being committed right away.

```shell
% git cherry-pick -n {branch or SHA}
```

This happens to be the default in
[mercurial](https://mercurial-scm.org/help/commands/graft) with `hg graft`.

As such, another possibility is to create an alias:

```gitconfig
[alias]
  graft = cherry-pick -n
```

```shell
% git graft {branch or SHA}
```
