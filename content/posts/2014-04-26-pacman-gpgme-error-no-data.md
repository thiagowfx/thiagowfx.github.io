---
title: "Pacman GPGME error: No data"
date: 2014-04-26T21:08:00-03:00
tags:
- dev
- legacy
---

If you ever come across this error when using pacman, just do the following:

```shell
sudo pacman-key --init
sudo pacman-key --populate archlinux
sudo pacman -Syy
```

This **should** solve your problems. If not, please consult the ArchWiki or the
forums.
