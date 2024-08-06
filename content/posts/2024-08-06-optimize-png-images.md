---
title: "Optimize PNG images"
date: 2024-08-06T14:39:31+02:00
tags:
  - dev
  - devops
---

Before checking `.png` images into git repositories, you should optimize them –
mostly for their file size.

<!--more-->

The Chromium project provides [this
script](https://chromium.googlesource.com/chromium/src/+/refs/heads/main/tools/resources/optimize-png-files.sh)
to do so. It boils down to installing and running the following executables:

- `optipng`: https://optipng.sourceforge.net/
- `pngcrush`: https://pmt.sourceforge.io/pngcrush/
- `pngout`: https://www.jonof.id.au/kenutils.html

The first two are available via homebrew.
