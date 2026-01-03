---
title: "git: update master to main"
date: 2025-01-03T12:16:44-03:00
tags:
  - dev
  - git
---

In your Forge (most likely Github or Gitlab), update the default branch from
`master` to `main`. Normally this has the effect of renaming `master` to `main`
automatically.

In your clients, run:

```shell
git branch -m master main
git fetch origin
git branch -u origin/main main
git remote set-head origin -a
```

Done!

How to refer to the default branch in scripts and aliases?

Set the following `git` alias:

```shell
% cat ~/.gitconfig
[...]
[alias]
	default = !git symbolic-ref refs/remotes/origin/HEAD | sed 's@^refs/remotes/origin/@@'
[...]
```

It outputs `master` or `main` – there's no `origin/` prefix.

The `default` alias only works if you have a `origin` remote set up.
It will fail if the repository is fully local:

```shell
% cdtmp
/tmp/thiago.perrotta-2025-01-03-pk0GPp
% git init
Initialized empty Git repository in /private/tmp/thiago.perrotta-2025-01-03-pk0GPp/.git/
% git default
fatal: ref refs/remotes/origin/HEAD is not a symbolic ref
```
