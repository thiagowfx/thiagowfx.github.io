---
title: "ack with context"
date: 2025-05-19T14:12:35+02:00
tags:
  - dev
  - linux
  - macos
---

I often use [`ack(1)`](https://beyondgrep.com/) to `grep` for text patterns in git
repositories[^1].

Today I learned about its [`-C`](https://linux.die.net/man/1/ack) flag:

```
-C [ NUM ], --context[= NUM ]
  Print NUM lines (default 2) of context around matching lines.
```

It's a handy shortcut, better than fiddling with `-A` and `-B` (after and
before, respectively).

**Bonus**: the same flag exists in `grep` and in `rg` (`ripgrep`).


[^1]: I should probably fully migrate to
    [`ripgrep`](https://github.com/BurntSushi/ripgrep) one day. Heck, it's not
    even in the [Arch core repositories](https://aur.archlinux.org/packages/ack)
    anymore.

