---
title: "fd: match full path"
date: 2024-10-02T13:30:29+02:00
tags:
  - dev
  - devops
---

When using [`fd(1)`](https://github.com/sharkdp/fd), only the filename is
matched by default.

To match the full path, use `-p`. It is often useful to combine it with `--type
file`.

<!--more-->

```shell
% fd -p clustermon --type file
apps/base/clustermon/clustermon.yaml
apps/base/clustermon/kustomization.yaml
apps/overlays/g02/clustermon/patches.yaml
apps/overlays/g02/clustermon/values.yaml
```

A natural extension is to pipe it to `| ifne xargs -n 1 gsed -i -e
'{expression}'`. Changes in the entire codebase at your fingertips!
