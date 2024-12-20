---
title: "Kubernetes: tail logs from pods with stern"
date: 2024-12-17T16:37:16-03:00
tags:
  - dev
---

You can always use `kubectl logs -n {namespace} {pod} [-c {container}] -f` to
inspect logs from a specific pod[^1].

[^1]: `-c` to specify a container within it, and `-f` to stream logs à la `tail
    -f`.

Nonetheless that doesn't scale when you don't know which pod you want in the
first place.

<!--more-->

You could start with deployments, dive into replica sets, and then into
individual pods, one by one, but... that is tedious and slow.

We can do better with [stern](https://github.com/stern/stern):

> ⎈ Multi pod and container log tailing for Kubernetes

Usage:

```
stern pod-query [flags]
```

> The pod-query is a regular expression or a Kubernetes resource in the form
> `<resource>/<name>`.

Example:

```shell
% stern -n argocd argocd
```

We can also `grep` for specific strings in log lines with `--include`:

```shell
% stern -n argocd argocd --include level=error
```

Or `grep -v` with `--exclude`.

It's better to use `--include` / `--exclude` than to `| grep`, because it
preserves color attributes (each pod has a different color in the aggregated
log output).

The logs stream by default (like `tail -f`, or `kubectl logs -f`).
