---
title: "Compress a .pdf in macOS with Preview.app"
date: 2024-11-30T00:22:38+01:00
tags:
  - dev
---

All hail to [Apple
Documentation](https://support.apple.com/en-ca/guide/preview/prvw1509/mac).

The instructions are very simple:

- open the `.pdf` file in Preview.app
- export it (`File > Export`)
- in "quartz filter", select the "reduce file size" option
- save

I observed a scanned document with ~3.3MiB of file size be compressed to
~350KiB. Not bad! And although not very customizable, it's very user-friendly
and easy to remember.

The alternative would have been to use GhostScript (`gs`). For example, ChatGPT
suggests:

```shell
% gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf
```
