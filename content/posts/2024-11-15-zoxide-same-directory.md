---
title: "zoxide: cd within the same directory"
date: 2024-11-15T16:03:29+01:00
tags:
  - dev
  - devops
---

I am a big fan of [`zoxide`](https://github.com/ajeetdsouza/zoxide):

> A smarter cd command. Supports all major shells.

The idea is simple: as you keep `cd`ing during the day, it builds up a local
database of your most frequently accessed directories.

<!--more-->

Perhaps you `cd` often to `~/projects/company/major/area/foo`.

Next time, run `z foo`, and it will magically `cd` into it.

What if you have `~/Downloads/foo` as well? Then it will `cd` to the one you
access more frequently.

It does so transparently and dynamically, out-of-the-box, without any extra
intervention.

Sometimes though it `cd`s to a directory you didn't intend.

To instruct it to `cd` to a subdirectory within `$PWD` (the current working
directory), just pass a slash (`/`) as its second argument:

```shell
~/projects/company$ z foo /
```

In the previous example, it would _not_ `cd` to `~/Downloads`.

There are many similar projects to `zoxide`. In the past, I used
[`autojump`](https://github.com/wting/autojump).
