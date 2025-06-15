---
title: "Rename files in bulk"
date: 2024-06-19T13:39:04+02:00
tags:
  - dev
---

Whenever the files are in the same directory, `vidir` from [moreutils]({{< ref
"2022-05-01-tools-you-should-know-about-moreutils" >}}) is the best
interactive tool.

If files are scattered across multiple directories, consider using the
[`rename`](https://man.archlinux.org/man/rename.1.en) utility from `util-linux`.


A simple example to rename all `readme.md` files to `README.md` for consistency:

```shell
rename 's/readme\.md/README.md/' **/*
```

A more recent example (2024-07-25):

```shell
rename 's/promtail-global-testing/promtail-global/g' **/*
```

If there are nested directories that match the expression, you'll need to run
`rename` multiple times.
