---
title: "ArgoCD: cache: key is missing"
date: 2025-01-09T20:20:03-03:00
tags:
  - dev
  - selfhosted
---

If you experience the title error message in ArgoCD (e.g. via its web UI and/or
in pod logs), it's related to
[argo-cd#5068](https://github.com/argoproj/argo-cd/issues/5068). The full error
message is:

```
Unable to load data: cache: key is missing
```

As I
[commented](https://github.com/argoproj/argo-cd/issues/5068#issuecomment-2580878251)
in the bug, here's how to fix it:

> The following workaround sufficed for me: `kubectl delete pod -n argocd
> argocd-application-controller-0`.
>
> Initially I ran `kubectl rollout restart deployment -n argocd
argocd-application-controller` but it didn't work.

In my experience, this error only happens once, ephemerally, during ArgoCD
bootstrapping. Once fixed it does not reoccur.

**Update(2025-06-06)**: This error reoccurs intermittently 🤷.

Another potential workaround is to disable redis / caching altogether, as ArgoCD
can fully operate without it, but I wouldn't recommend that.

See also: [#18503](https://github.com/argoproj/argo-cd/issues/18503).
