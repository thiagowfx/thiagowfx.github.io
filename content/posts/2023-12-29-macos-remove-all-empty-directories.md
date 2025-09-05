---
title: "macOS: remove all empty directories"
date: 2023-12-29T02:02:19+01:00
tags:
  - dev
---

For some odd reason my [Calibre](https://calibre-ebook.com) backup to cloud
storage had a bunch of empty directories. I've been meaning to remove them, but
it's cumbersome to do so from the web client.

Instead, let's do it from a local client.

Upon installing the cloud storage software, a local directory is exposed under
`/Users/$USER/Library/CloudStorage` (macOS).

My first instinct is to use [`find(1)`](https://man.archlinux.org/man/find.1.en):

```shell
$ find -empty -type d -delete
```

However that does not work on macOS:

```
find: illegal option -- e
usage: find [-H | -L | -P] [-EXdsx] [-f path] path ... [expression]
       find [-H | -L | -P] [-EXdsx] -f path [path ...] [expression]
```

My second go to choice is [`fd(1)`](https://man.archlinux.org/man/fd.1.en):

```shell
$ fd -t e -x rmdir
```

...this lists all empty directories and invokes `rmdir` on each of them.
