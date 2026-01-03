---
title: "mv: case sensitivity"
date: 2025-09-25T12:22:47+02:00
tags:
  - dev
  - macos
---

From the series: why you should always use a case sensitive file system (like
most of Linux).

By default, to my despair, macOS uses a case-insensitive file system([1], [2]).

We can pretend this is not an issue, and simply brush it under the carpet during
most sunny days.

Nonetheless, at some point the dust must settle.

**Problem statement**: rename `justfile` to `Justfile`.

Too easy? On Linux, yes. On macOS:

```shell
% mv justfile Justfile
mv: 'justfile' and 'Justfile' are the same file
```

Fine. Let's do it the '''hard''' way:

```shell
% mv justfile{,.bkp}
% mv justfile.bkp Justfile
```

And life goes on.

[1]: https://discussions.apple.com/thread/251191099?sortBy=rank
[2]: https://docs.spryker.com/docs/dg/dev/integrate-and-configure/switch-to-a-case-sensitive-file-system-on-mac-os#create-the-disk-image
