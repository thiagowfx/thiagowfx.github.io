---
title: "Remove large files from your computer"
date: 2024-01-21T10:40:13-03:00
tags:
  - dev
---

Whenever disk space gets almost full, I like to use the following software to
clean up (unnecessary) big files from my computers:


## Windows

[WinDirStat](https://windirstat.net/):

> WinDirStat is a disk usage statistics viewer and cleanup tool for various
> versions of Microsoft Windows.

It's user-friendly and open source.

## Linux / macOS

[ncdu](https://dev.yorhel.nl/ncdu):

> Ncdu is a disk usage analyzer with an ncurses interface. It is designed to
> find space hogs on a remote server where you don't have an entire graphical
> setup available, but it is a useful tool even on regular desktop systems.
> Ncdu aims to be fast, simple and easy to use, and should be able to run in
> any minimal POSIX-like environment with ncurses installed.

Naturally, the command line way™ prevails on Unix systems. It's one
installation command away from your favorite package manager. Usage:

```shell
% ncdu /
```

**Update(2025-09-02):** [diskonaut](https://github.com/imsnif/diskonaut):

> Terminal disk space navigator 🔭

```
% diskonaut /
```

Wherein `ncdu` uses a tree, ranger-style representation and `diskonaut` uses a
visual block representation.
