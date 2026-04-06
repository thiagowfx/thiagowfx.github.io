---
title: "ArgoCD: all applications stuck on refresh"
url: https://perrotta.dev/2025/08/argocd-all-applications-stuck-on-refresh/
last_updated: 2026-01-03
---


The problem is very likely the Application Controller.

You can restart it:

```shell
kubectl rollout restart sts -n argocd argocd-application-controller
```

Or inspect its logs:

```shell
kubectl logs -n argocd argocd-application-controller-0 --tail=100 | less
```

While we're here, make sure there is at least one replica running:

```
% kubectl get sts -n argocd argocd-application-controller
NAME                            READY   AGE
argocd-application-controller   1/1     415d
```

[Upstream issue](https://github.com/argoproj/argo-cd/issues/11831).

