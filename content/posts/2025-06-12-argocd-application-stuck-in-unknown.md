---
title: "ArgoCD: application stuck in unknown"
date: 2025-06-12T11:51:32+02:00
tags:
  - dev
  - selfhosted
---

**Problem statement**: An application in ArgoCD that was previously running
smoothly has suddenly started to fail. Its status has changed to "Unknown".
The "Refresh" button is grayed out in the Argo web UI.

I found the following works in this scenario, which is typically a transient
issue:

- restart the argo server
- restart the argo repo server

In terms of commands:

```shell
kubectl rollout restart deployment argocd-server -n argocd
kubectl rollout restart deployment argocd-repo-server -n argocd
```
