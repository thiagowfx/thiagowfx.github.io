---
title: "fd: match full path"
url: https://perrotta.dev/2024/10/fd-match-full-path/
last_updated: 2026-08-26
---


When using [`fd(1)`](https://github.com/sharkdp/fd), only the filename is
matched by default.

To match the full path, use `-p`. It is often useful to combine it with `--type
file`.

```shell
% fd -p prometheus --type file
apps/base/prometheus/prometheus.yaml
apps/base/prometheus/kustomization.yaml
apps/overlays/g02/prometheus/patches.yaml
apps/overlays/g02/prometheus/values.yaml
```

A natural extension is to pipe it to `| ifne xargs -n 1 gsed -i -e
'{expression}'`. Changes in the entire codebase at your fingertips!

**Update(2025-11-30)**: We can use `xargs -r` instead of `ifne`.

