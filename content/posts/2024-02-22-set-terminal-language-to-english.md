---
title: "Set terminal language to English"
date: 2024-02-22T09:48:34+01:00
tags:
  - dev
---

I changed my macOS system language to German, with the intent of [getting more
exposure to it]({{< ref "2022-04-03-translating-german-to-english" >}}).

One negative side effect is that most binaries I execute with my shell (for
example: `git`) are now outputting German text as well[^1]. In hindsight, this
should have been expected.

<!--more-->

A simple fix is to override the environment locale with English. I made the
following
[addition](https://github.com/thiagowfx/.dotfiles/commit/4b784b1fa89f569623340cf3d58cc22d8504926a)
to my [dotfiles](https://github.com/thiagowfx/.dotfiles):

```shell
# Force the system-wide language to English.
# Both "en_US" and "en_CA" work here.
# We could also optionally set LC_ALL but it is not necessary.
# Verify current locale settings with `locale`.
export LANG="en_US"
```

[^1]: You could argue that it's actually desirable to have terminal applications
    output German. However, nothing beats the standardization, consistency and
    familiarity of English for developer tooling. If I really need to have this
    extreme exposure one day, it's always possible to just `unset LANG`.
