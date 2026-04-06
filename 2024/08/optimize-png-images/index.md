---
title: "Optimize PNG images"
url: https://perrotta.dev/2024/08/optimize-png-images/
last_updated: 2025-09-05
---


Before checking `.png` images into git repositories, you should optimize them –
mostly for their file size.

The Chromium project provides [this
script](https://chromium.googlesource.com/chromium/src/+/refs/heads/main/tools/resources/optimize-png-files.sh)
to do so. It boils down to installing and running the following executables:

- `optipng`: https://optipng.sourceforge.net/
- `pngcrush`: https://pmt.sourceforge.io/pngcrush/
- `pngout`: https://www.jonof.id.au/kenutils.html

The first two are available via homebrew.

