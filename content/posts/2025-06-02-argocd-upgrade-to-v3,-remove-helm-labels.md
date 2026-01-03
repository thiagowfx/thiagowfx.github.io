---
title: "ArgoCD: upgrade to v3, remove helm labels"
date: 2025-06-02T13:03:24+02:00
tags:
  - dev
  - kubernetes
---

I am leading the effort to upgrade ArgoCD to its [newest major version
(v3)](https://blog.argoproj.io/announcing-argo-cd-v3-small-but-mighty-df05c0b39ad6)
across our fleet.

One of its [breaking
changes](https://argo-cd.readthedocs.io/en/stable/operator-manual/upgrading/2.14-3.0/)
is the removal of helm labels from argo applications, like such:

```yaml
metadata:
# [...]
  labels:
    app.kubernetes.io/managed-by: Helm
```

Applying a normal sync does not get rid of the label.

I found out that doing an one-off [server-side apply
sync](https://argo-cd.readthedocs.io/en/latest/user-guide/sync-options/#server-side-apply)
addresses the label removal, and it is safe to do (incurs no downtime):

> However, there are some cases where you want to use `kubectl apply
> --server-side` over `kubectl apply`:
>
> [...]
>
> Patching of existing resources on the cluster that are not fully managed by
> Argo CD.

There's no need to make the server-side apply a permanent config, i.e.:

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
spec:
  syncPolicy:
    syncOptions:
    - ServerSideApply=true
```

...though there's no harm either in doing so.
