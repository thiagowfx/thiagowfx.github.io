---
title: "New APKBUILD: argocd"
date: 2024-10-09T23:03:32+02:00
tags:
  - dev
---

[ArgoCD](https://argo-cd.readthedocs.io/en/stable/) is a widely used GitOps
software for Kubernetes Continuous Delivery (see
[USERS.md](https://github.com/argoproj/argo-cd/blob/master/USERS.md)).

I am quite surprised no one bothered to create an Alpine Linux package for it.

Until...[now](https://gitlab.alpinelinux.org/alpine/aports/-/merge_requests/73305),
by yours truly.


This `APKBUILD` took a bit longer to create than the usual.
There were a couple of issues with `-buildmode=pie`, addressed with
`export CGO_ENABLED=1` (via `make CGO_FLAG=1`).

Also, not every architecture is compatible with it. The following error message
appears in ARM builds:

```
cannot use math.MaxInt64 (untyped int constant 9223372036854775807) as int value in argument to env.ParseNumFromEnv (overflows)
```

Anyway, once it is merged upstream, enjoy!

```shell
% doas apk add argocd
```
