---
title: "ArgoCD: deployment spec.selector: field is immutable"
date: 2025-06-30T13:04:51+02:00
tags:
  - dev
  - kubernetes
---

When using [ArgoCD](https://argo-cd.readthedocs.io/en/stable/) to manage an app,
the Deployment manifest needs to undergo significant changes, updating its
selector labels. When trying to sync the argocd app, we get the following error:

```
one or more objects failed to apply, reason: error when patching "/dev/shm/3469418025": Deployment.apps "myapp" is invalid: spec.selector: Invalid value: v1.LabelSelector{MatchLabels:v1.LabelSelectorRequirement(nil)}: field is immutable. Retrying attempt #2 at 11:02AM.
```

This error doesn't come directly from Argo, it is from `kubectl apply`.

There are two ways to address it:

1. Sync the argo app with the
   ["force"](https://argo-cd.readthedocs.io/en/latest/user-guide/sync-options/#force-sync)
   option enabled

2. Run `kubectl apply` with `--force` (which is ultimately what the
   aforementioned option maps to).

In action (`-w` is short for `--watch`):

```
% kubectl get endpoints -w
NAME         ENDPOINTS         AGE
myapp        <none>            5y44d
myapp                          5y44d
myapp        10.1.13.40:8080   5y44d
```
