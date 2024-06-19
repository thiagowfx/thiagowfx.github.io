---
title: "Rename files in bulk"
date: 2024-06-19T13:39:04+02:00
tags:
  - dev
  - linux
---

Whenever the files are in the same directory, `vidir` from [moreutils]({{< ref
"2022-05-01-tools-you-should-know-about-moreutils.md" >}}) is the best
interactive tool.

If files are scattered across multiple directories, consider using the
[`rename`](https://man.archlinux.org/man/rename.1.en) utility from `util-linux`.

<!--more-->

A simple example to rename all `readme.md` files to `README.md` for consistency:

```shell
rename 's/readme\.md/README.md/' **/*
```
