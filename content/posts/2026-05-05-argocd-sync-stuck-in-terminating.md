---
title: "ArgoCD: sync stuck in terminating"
date: 2026-05-05T13:51:10-02:00
tags:
  - dev
  - kubernetes
---

**Problem statement**: An ArgoCD application's sync operation is stuck in
`Terminating` for hours. The web UI shows _operation is terminating due to
timeout_. A PreSync hook resource keeps appearing as `Running` even though
the underlying `Job` already completed in the cluster.

```shell
% kubectl get application <app> -n argocd -o yaml | yq '.status.operationState.phase'
Terminating
```

The application controller is stuck in a busy loop:

```
"Resuming in-progress operation. phase: Terminating, message: operation is terminating due to timeout"
"No operation updates necessary to '<ns>/<app>'. Skipping patch"
```

In my case this followed a transient `ImagePullBackOff` on a PreSync hook job:
the image was being mirrored to a regional ECR, the first hook attempt failed,
and by the time the image landed and the retry succeeded, the parent operation
had already moved into `Terminating` and never recovered.

The instinct is to clear the operation:

```shell
kubectl patch application <app> -n argocd --type merge -p '{"operation": null}'
```

It's a no-op. The wedge doesn't live in `spec.operation` (the request) — it
lives in `status.operationState` (the controller's bookkeeping). And `status`
is owned by the controller, so a regular `--type merge` patch won't touch it.

We need the `status` subresource:

```shell
kubectl patch application <app> -n argocd --type merge \
  -p '{"operation": null}'
kubectl patch application <app> -n argocd --subresource status --type merge \
  -p '{"status":{"operationState":null}}'
```

Both patches together. Neither touches cluster resources — they only modify
ArgoCD's view of the operation. After that, re-trigger the sync from the UI
and the application reconciles cleanly.

Restarting `argocd-application-controller` does _not_ help: the stuck state
sits in etcd, and the freshly-elected leader picks it up on startup and resumes
the same loop.

One caveat: verify the underlying hook resource has actually finished before
clearing. `kubectl describe job -n argocd <hook-job>` should show
`1 Succeeded`. Otherwise we'll lose in-flight progress.
