---
title: "icdiff: side-by-side diff"
date: 2024-07-09T10:47:51+02:00
tags:
  - dev
---

[`icdiff`](https://www.jefftk.com/icdiff) is a simple diffing tool written in
python that comes with two sensible out-of-the-box defaults:

- colored diff output
- side-by-side diff


The usual `diff` tool in Unix system has some basic color support[^1].
Nonetheless, sometimes the output of `icdiff` is better, with little effort or
memorization.

Given two files (pardon my lack of creativity, but at least you know it's not AI
generated):

```shell
% cat first
gustavo
fring
walter
white
% cat second
walter
white
jesse
pinkman
```

Plain `diff` output (terrible, IMHO):

```shell
% diff first second
1,2d0
< gustavo
< fring
4a3,4
> jesse
> pinkman
```

Better `diff` output:

```shell
% diff --color=auto -uN first second
--- first	2024-07-09 10:50:01
+++ second	2024-07-09 10:50:08
@@ -1,4 +1,4 @@
-gustavo
-fring
 walter
 white
+jesse
+pinkman
```

...which is why I have `alias diff="diff --color=auto -uN"` in my shell config /
dotfiles.

With `icdiff`:

```shell
% icdiff first second
first            second
gustavo
fring
walter           walter
white            white
                 jesse
                 pinkman
```

Two observations:

- in this blog you cannot see the colors, therefore this example is meh
- `icdiff` will happily utilize your full terminal width, positioning the second
  column quite to the right in case, thereby fully utilizing the available space

[^1]: And there's also `colordiff`.
