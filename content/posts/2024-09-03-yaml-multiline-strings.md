---
title: "YAML multiline strings"
date: 2024-09-03T11:55:53+02:00
tags:
  - dev
---

I keep forgetting what the correct syntax is.

This reference is the best: https://yaml-multiline.info/

Summary:

- `>` eats newlines, `|` keeps them.
- Appending a `-` to either of these eats the newline(s) at the end. Omitting it
  keeps one. Appending a `+` preserves all newlines at the end.
