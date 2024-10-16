---
title: "kubectl: list all node pods"
date: 2024-10-16T12:26:24+02:00
tags:
  - dev
  - devops
---

Recipe to list all pods that belong to a given node:

```shell
$ kubectl get pod -o wide --field-selector spec.nodeName={node_name} -A
```

<!--more-->

**Source**: https://stackoverflow.com/questions/39231880/kubernetes-api-get-pods-on-specific-nodes

This _ought to_ be easier to remember...
