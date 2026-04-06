---
title: "YAML multiline strings"
url: https://perrotta.dev/2024/09/yaml-multiline-strings/
last_updated: 2025-09-05
---


I keep forgetting what the correct syntax is.

This reference is the best: https://yaml-multiline.info/

Summary:

- `>` eats newlines, `|` keeps them.
- Appending a `-` to either of these eats the newline(s) at the end. Omitting it
  keeps one. Appending a `+` preserves all newlines at the end.

