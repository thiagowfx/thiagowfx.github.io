---
title: "ArgoCD: git index.lock issue"
date: 2025-08-23T12:39:14+02:00
tags:
  - dev
  - selfhosted
---

**Problem statement**: Every ArgoCD application is stuck in _Unknown_ state,
with the following error:

```
Failed to load target state: failed to generate manifest for source 1 of 2:
rpc error: code = Unknown desc = failed to initialize repository resources: rpc
error: code = Internal desc = Failed to checkout FETCH_HEAD: failed to checkout
FETCH_HEAD: `git checkout --force FETCH_HEAD` failed exit status 128: fatal:
Unable to create '<path to cached source>/.git/index.lock': File exists. Another
git process seems to be running in this repository, e.g. an editor opened by
'git commit'. Please make sure all processes are terminated then try again. If
it still fails, a git process may have crashed in this repository earlier:
remove the file manually to continue.
```

It is a lock contention race condition issue within the ArgoCD repo server
component, with the git `index.lock`.

The easiest way to address it is to restart the repo server:

```shell
kubectl rollout restart deploy -n argocd argocd-repo-server
```

Afterwards, refresh all applications in the cluster via the web UI:

- click Applications on the left-side nav bar
- click Refresh apps at the top
- select ALL applications, set refresh type to NORMAL
- click refresh
