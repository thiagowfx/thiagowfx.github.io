
Recipe to list all pods that belong to a given node:

```shell
$ kubectl get pod -o wide --field-selector spec.nodeName={node_name} -A
```

**Source**: https://stackoverflow.com/questions/39231880/kubernetes-api-get-pods-on-specific-nodes

This _ought to_ be easier to remember...

