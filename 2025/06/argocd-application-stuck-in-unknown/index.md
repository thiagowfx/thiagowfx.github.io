---
title: "ArgoCD: application stuck in unknown"
url: https://perrotta.dev/2025/06/argocd-application-stuck-in-unknown/
last_updated: 2026-01-03
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
% kubectl rollout restart deployment argocd-server -n argocd
% kubectl rollout restart deployment argocd-repo-server -n argocd
```

