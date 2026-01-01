
We are making a non-trivial change to our cluster monitoring architecture, and I
needed to verify the new rollout is properly working in our infratesting
environment.

A simple way to do so is to create a pod that never leaves the "Pending" state,
because we have an alert (a prometheus rule) that fires whenever a pod is in
that stack for too long (15 minutes is our threshold in most cases).

Use the following manifest:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pending-pod
spec:
  affinity:
    podAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchExpressions:
          - key: "non/existent"
            operator: In
            values:
            - "true"
        topologyKey: "kubernetes.io/hostname"
  containers:
  - name: busybox
    image: busybox
    command: ['sh', '-c', 'echo Hello, Kubernetes! && sleep 3600']
```

...it creates a `pending-pod` in the `default` namespace that should never be
scheduled, due to its strict pod affinity rules.

Save it as `pending-pod.yaml`, deploy it with `kubectl apply -f
pending-pod.yaml`.

```
$ kubectl get pod pending-pod -w
NAME          READY   STATUS    RESTARTS   AGE
pending-pod   0/1     Pending   0          21s
 pending-pod   0/1     Pending   0          65s
pending-pod   0/1     Pending   0          74s
pending-pod   0/1     Pending   0          2m6s
pending-pod   0/1     Pending   0          3m8s
pending-pod   0/1     Pending   0          4m8s
pending-pod   0/1     Pending   0          4m18s
```

At some point the alert fires, as expected.
And now we can roll out these changes to prod!

