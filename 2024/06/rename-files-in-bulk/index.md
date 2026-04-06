---
title: "Rename files in bulk"
url: https://perrotta.dev/2024/06/rename-files-in-bulk/
last_updated: 2025-09-05
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

