---
title: "kubectl: get all logs from all pods"
date: 2024-07-15T13:23:35+02:00
tags:
  - dev
---

Frequently:

```shell
kubectl logs -n argocd argocd-repo-server-5d59975687-dxnh7
```

But how do you know what hash to use after `server-`?


**Option 1)**: TAB auto-completion:

```shell
kubectl logs -n argocd argocd-repo-server-<TAB>
```

**Caveats**:

- tab completion for `kubectl` isn't always properly set up
- if there is more than one pod, you would have to type in the first few letters
  of the hash before hitting TAB again, that's annoying and non-ergonomic

**Option 2)**: subshell

```shell
kubectl logs -n argocd $(kubectl get pod -n argocd | grep argocd-repo-server | cut -f1 -d' ' | head -1)
```

**Caveats**:

- a lot of typing
- `head -1` is necessary in case there are multiple pods[^1]

**Option 3)**: get all logs from all pods that match a given label

```shell
kubectl logs -n argocd -l app=app.kubernetes.io/instance=argocd
[--all-containers] [--ignore-errors]
```

This is much more ergonomic.

You still need to figure out what label to use though:

```shell
$ kubectl describe pod -n argocd argocd-repo-server-5d59975687-dxnh7 | grep -A7 -i labels:
Labels:           app.kubernetes.io/component=repo-server
                  app.kubernetes.io/instance=argocd
                  app.kubernetes.io/managed-by=Helm
                  app.kubernetes.io/name=argocd-repo-server
                  app.kubernetes.io/part-of=argocd
                  app.kubernetes.io/version=v2.11.4
                  helm.sh/chart=argo-cd-7.3.4
                  pod-template-hash=5d59975687
```

**Source**: https://stackoverflow.com/questions/33069736/how-do-i-get-logs-from-all-pods-of-a-kubernetes-replication-controller


Happy logging!


[^1]: Or `tail -1`, for that matter.
