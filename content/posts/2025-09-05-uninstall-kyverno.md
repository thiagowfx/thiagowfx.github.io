---
title: "Uninstall Kyverno"
date: 2025-09-05T17:03:04+02:00
tags:
  - dev
---

It's always a bit frustrating to do it.

Despite the excellent [upstream
documentation](https://kyverno.io/docs/installation/uninstallation/), our
Kubernetes clusters often leave cruft behind when doing so.

```shell
% kubectl rollout restart sts -n argocd argocd-redis-ha-server
E0905 12:29:24.284879 3908207 memcache.go:287] couldn't get resource list for wgpolicyk8s.io/v1alpha2: the server is currently unable to handle the request
E0905 12:29:24.287856 3908207 memcache.go:287] couldn't get resource list for reports.kyverno.io/v1: the server is currently unable to handle the request
E0905 12:29:24.290250 3908207 memcache.go:121] couldn't get resource list for reports.kyverno.io/v1: the server is currently unable to handle the request
E0905 12:29:24.292666 3908207 memcache.go:121] couldn't get resource list for wgpolicyk8s.io/v1alpha2: the server is currently unable to handle the request
E0905 12:29:24.295959 3908207 memcache.go:121] couldn't get resource list for reports.kyverno.io/v1: the server is currently unable to handle the request
E0905 12:29:24.298226 3908207 memcache.go:121] couldn't get resource list for wgpolicyk8s.io/v1alpha2: the server is currently unable to handle the request
E0905 12:29:24.302703 3908207 memcache.go:121] couldn't get resource list for reports.kyverno.io/v1: the server is currently unable to handle the request
E0905 12:29:24.305009 3908207 memcache.go:121] couldn't get resource list for wgpolicyk8s.io/v1alpha2: the server is currently unable to handle the request
[...]
```

That output junk is emitted on every `kubectl` command.

This time the culprit was:

```shell
% kubectl get apiservice | egrep -i "(kyverno|wgpolicy)"
v1.reports.kyverno.io                           reports-server/kyverno-reports-server   False (MissingEndpoints)   76d
v1alpha2.wgpolicyk8s.io                         reports-server/kyverno-reports-server   False (MissingEndpoints)   76d
```

Deleting these two entries resolves the issue:

```shell
% kubectl delete apiservice v1.reports.kyverno.io v1alpha2.wgpolicyk8s.io -n reports-server
```
