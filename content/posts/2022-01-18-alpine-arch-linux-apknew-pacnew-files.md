---
title: "Alpine / Arch Linux: .apk-new and .pacnew files"
date: 2022-01-18T14:25:20-05:00
tags:
  - linux
showtoc: true
---

As packages are upgraded over time, updated configs files under `/etc` may
arise. Different package managers treat this issue differently.

<!--more-->

## Alpine Linux

`apk` creates `.apk-new` files, which can be located and merged by running
`doas update-conf`. Here is a recent example:

```shell
% doas update-conf
--- //etc/securetty
+++ //etc/securetty.apk-new
@@ -12,3 +12,6 @@
 tty11
 hvc0
 ttyS0
+ttyS1
+ttyAMA0
+ttyAMA1
New //etc/securetty available:
Quit, Next, Show diff, Edit new, Zap new, Use new (q/n/s/e/z/u) [s] u
```

## Arch Linux

`pacman` creates `.pacnew` files, which can be located and merged by running `sudo pacdiff`.

**Tip**: The [`pacdiff-pacman-hook-git`][pacdiff-pacman-hook-git] package helpfully adds
a pacman hook that automatically checks whether there are any due `.pacnew`
files upon upgrading the system (`pacman -Syu`), being a simple and effective
way to automate this maintenance task.

[pacdiff-pacman-hook-git]: https://aur.archlinux.org/packages/pacdiff-pacman-hook-git/
