---
title: "Folderify: Generate macOS folder icons natively"
date: 2024-12-28T06:15:58-03:00
tags:
  - dev
  - macos
---

[via Mike Rockwell](https://initialcharge.net/2024/06/folderify/):

> You install it using Homebrew, point Folderify at an image file using a simple
> Terminal command, and it spits out a macOS-style folder icon with that image
> on it.
>
> I can't believe I didn't know this existed.

Project github: https://github.com/lgarron/folderify

Usage:

```shell
% brew install folderify
% folderify ~/Downloads/company_logo.webp ~/Company
```

I got our company logo lazily with Google Images + filtering for transparent
images. `.webp` worked just fine, `.png` would have worked as well.

The end result is really nice. It's a small modification that [sparks
joy](https://www.netflix.com/title/81231940).
