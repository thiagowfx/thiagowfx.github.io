---
title: "docker: dive into images"
date: 2025-08-11T13:20:08+02:00
tags:
  - dev
---

Recently bitnami has [pulled the
plug](https://github.com/bitnami/charts/issues/35164) off their public docker
images offering[^1].

We are relying on their
[`bitnami/kubectl`](https://hub.docker.com/r/bitnami/kubectl) image. Now what?

We could build our own, or use another upstream image. Looking at the [Docker
Hub](https://hub.docker.com/search?q=kubectl) catalog, I was pleased to find
[`rancher/kubectl`](https://hub.docker.com/r/rancher/kubectl) (backed by SUSE)
there.

This is enough for our needs.

It would have been trivial to build our own image otherwise if needed:

```Dockerfile
FROM alpine:3.22
RUN apk add --no-cache kubectl
```

How can we ensure these images are equivalent, for practical purposes?

One way is to use [`dive`](https://github.com/wagoodman/dive) to introspect
each of them:

> A tool for exploring each layer in a docker image

```shell
% dive bitnami/kubectl:latest
% dive rancher/kubectl:v1.30.14
```

The rancher image has 50MB in size and contains _only_ the `kubectl` binary.
There's no shell, not even `/bin/sh`.

The bitnami image has 326MB and contains a bunch of other stuff.

It turns out we will get some (unexpected) efficiency gains out of this
migration!

[^1]: ["""Recession"""](https://en.wikipedia.org/wiki/Enshittification).
