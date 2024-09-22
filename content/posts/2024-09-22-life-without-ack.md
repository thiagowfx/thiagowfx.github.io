---
title: "Life without ack"
date: 2024-09-22T14:30:29+02:00
tags:
  - dev
  - devops
---

Every macOS upgrade comes with disappointment and sorrow in the form of some
tool, dependency / library or system-wide configuration breaking[^1].

This time: the upgrade to macOS Sequoia (15.0) broke `ack` (Perl).

<!--more-->

```
% ack
zsh: /opt/homebrew/bin/ack: bad interpreter: /usr/bin/perl5.30: no such file or directory
```

I desperately needed to use `ack`, however there was no internet connection. And
I didn't have any of its alternatives installed (e.g. `ag`, `ripgrep` / `rg`).

Then the best way is to fall back to good ol' `grep`[^2]:

```
% grep [-l] '\bref\b' **/*
```

Alternatively, within a git repository, there is `git grep`:

```
% git grep [-l] '\bref\b'
```

With `git grep` there is no need to specify which files to `grep`, as it entails
all files that belong to the repository...which happens to be a caveat for newly
created files that were not yet `git add`-ed.

[^1]: Homebrew (`brew`) being _almost always_ one of them.
[^2]: If `grep` ever breaks, we are screwed.
