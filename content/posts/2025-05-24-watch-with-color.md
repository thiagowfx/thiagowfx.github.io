---
title: "watch with --color"
date: 2025-05-24T14:40:07+02:00
tags:
  - dev
  - linux
---

When using `watch(1)` to monitor program output, colors will not be emitted by
default.

Thankfully [`watch(1)`](https://man.archlinux.org/man/watch.1) has a `--color`
(or `-c` flag).

Still, when using it with e.g. [`node` tests](https://nodejs.org/api/test.html),
colors are not emitted:

```
% watch --color -- node mytest.js
Every 2.0s: node ex5.js                       MacBookAir: 14:43:06
                                                     in 0.107s (0)
✔ toWasm (0.865792ms)
ℹ tests 1
ℹ suites 0
ℹ pass 1
ℹ fail 0
ℹ cancelled 0
ℹ skipped 0
ℹ todo 0
ℹ duration_ms 3.8805
```

The command detects that it's not attached to the terminal. :(

How can we **force color output** in this case?

There's no universal answer:

- Set [`CLICOLOR=1`, `CLICOLOR_FORCE=1`](https://bixense.com/clicolors/)
- See whether the program has a `--color` flag. For example:
  [`git`](https://git-scm.com/book/sv/v2/Customizing-Git-Git-Configuration) and
  [`ls`](https://superuser.com/questions/665274/how-to-make-ls-color-its-output-by-default-without-setting-up-an-alias)
  both support `--color=always`.

Another possibility, which is program agnostic, is to use an utility such as
[`unbuffer(1)`](https://man.archlinux.org/man/unbuffer.1) from the [TCL
Expect](https://wiki.tcl-lang.org/page/Expect) package:

```shell
% watch --color -- unbuffer node mytest.js
```

The `unbuffer` solution is my favorite ([previously]({{< ref "2024-12-23-unbuffer" >}})).

**Reference**: [Stack
Overflow](https://stackoverflow.com/questions/3793126/colors-with-unix-command-watch).
