---
title: "GNU sed: follow symlinks"
date: 2025-08-14T17:46:27+02:00
tags:
  - dev
---

[Previously]({{< ref "2025-08-08-fd-with-xargs-filenames-with-spaces" >}}).

Today we will upgrade Terraform in the entire codebase:

```shell
fd -e tf | ifne xargs gsed -i -e 's/required_version = "~> 1.6.6/required_version = "~> 1.10.0/g'
```

Easy, right?

During code review, a teammate has pointed out that I replaced many symlinks.
How?! This was completely unintended!

Eventually I figured out the reason. From [`sed(1)`](https://man.archlinux.org/man/sed.1):

> **--follow-symlinks**
>   follow symlinks when processing in place

It turns out it is necessary to pass `--follow-symlinks` to preserve symlinks
when using `-i` with GNU `sed`.
