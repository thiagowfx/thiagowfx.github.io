---
title: "Kubernetes: list all ImagePullBackOff container images"
date: 2025-08-21T13:34:27+02:00
tags:
  - dev
  - selfhosted
---

**Problem statement** Upgrade the
[`kube-prometheus-stack`](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack)
helm chart in [Azure China](https://portal.azure.cn/) to the latest version.
**Side effect**: Many container images are now missing from our internal
[ACR](https://azure.microsoft.com/en-us/products/container-registry) (Azure
Container Registry). They need to be synced with [`skopeo`](https://github.com/containers/skopeo).

Which images need to be synced? Use the command below, it is quite readable[^1]:

```shell
kubectl get pods --all-namespaces -o json | jq -r '.items[] | select(any(.status.containerStatuses[]; .state.waiting.reason == "ImagePullBackOff")) | .metadata.namespace + "/" + .metadata.name + "\t" + ( [.status.containerStatuses[] | select(.state.waiting.reason == "ImagePullBackOff").image] | join(", ") )'
```

Sample run:

```
ubuntu@universe:~ $ kubectl get pods --all-namespaces -o json | jq -r '.items[]
      | select(any(.status.containerStatuses[]; .state.waiting.reason == "ImagePullBackOff"))
      | .metadata.namespace + "/" + .metadata.name + "\t" +
        ( [.status.containerStatuses[] | select(.state.waiting.reason == "ImagePullBackOff").image] | join(", ") )'
monitoring/clustermon-kube-prometheus-operator-67c8b6c87c-w72km {my-registry-name}.azurecr.cn/quay.io/prometheus-operator/prometheus-operator:v0.83.0
monitoring/clustermon-prometheus-node-exporter-v7bpt    {my-registry-name}.azurecr.cn/quay.io/prometheus/node-exporter:v1.9.1
```

[^1]: I cannot promise I am able to craft this by hand without looking up man
    pages or getting assistance from an LLM. _C'est la vie_.
