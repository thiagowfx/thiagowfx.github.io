
**Problem statement**: Given a pod in Kubernetes, check its memory (RAM) usage.

[Stack
Overflow](https://stackoverflow.com/questions/54531646/checking-kubernetes-pod-cpu-and-memory-utilization):

```shell
kubectl top pod -n {namespace} {pod name} [--containers]
```

```
--containers=false:
    If present, print usage of containers within a pod.
```

This only works if [metrics
server](https://github.com/kubernetes-sigs/metrics-server) is installed (it
should be!).

There's an alternative:

```shell
kubectl describe PodMetrics {pod name}
```

It must be `PodMetrics`. `PodMetric` does not work (ugh![^1]):

```shell
% kubectl get PodMetric
error: the server doesn't have a resource type "PodMetric"
```

If metrics server is not available for some reason, then one needs to dive into
the container:

```shell
kubectl exec -it {pod name} -n {namespace} -- /bin/sh
```

...which won't always work; not every container has `/bin/sh`. Then read the
contents of `/sys/fs/cgroup/memory/memory.usage_in_bytes`.

[^1]: Who designed this? Is it so hard to achieve consistency? Both `kubectl get
    pod` and `kubectl get pods` work. Why can't it be the same with `PodMetric`?
    And, no, `PodMetricses` does not work either.

