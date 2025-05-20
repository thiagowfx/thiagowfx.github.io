---
title: "kubernetes: list pending pods in daemonset"
date: 2025-05-20T16:41:00+02:00
tags:
  - dev
  - linux
  - selfhosted
---

**Problem statement**: Given a DaemonSet with a couple of pods stuck in
"Pending" state during their rollout, find out which nodes did not yet complete
the pod initialization.

```shell
% kubectl get nodes -o name | grep -vFf <(kubectl get pods -n {namespace} -l {ds-label-selector} -o wide --no-headers | awk '{print "node/" $7}')
node/aks-database-12345678-vmss000000
node/aks-database-12345678-vmss000002
node/aks-systempool-87654321-vmss000000
node/aks-systempool-87654321-vmss000001
```

Notes:

- `kubectl get nodes -o name`: list all node names in the `node/<name>` form
- `kubectl get pods [...] -o wide`: get the node name for each running DaemonSet pod
- `awk '{print "node/" $7}'`: get the node name matching the output of `get nodes`
- `grep [...]`: find the nodes we are looking for

Surely there must be an easier way to accomplish this?
