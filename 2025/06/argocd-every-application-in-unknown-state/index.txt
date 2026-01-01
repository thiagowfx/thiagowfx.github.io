
**Symptom**: Every single application in the Kubernetes cluster that is managed
by Argo is in `Unknown` sync status. A disaster! 😱

This has only happened in one of our clusters. More specifically, in an
[AKS](https://learn.microsoft.com/en-us/azure/aks/core-aks-concepts) cluster
(from Microsoft Azure).

An observed effect:

```shell
% kubectl get --raw='/openapi/v2' | head -c 200
Error from server (ServiceUnavailable): the server is currently unable to handle the request
```

Aha! The Kubernetes OpenAPI server is not responding properly.
That explains why Argo is having so much trouble to figure out the state of affairs in
the cluster.

It was quite difficult to troubleshoot this issue. There are barely any
resources about it in the open web. We filed an Azure Support ticket, but it was
completely useless. They offered to restart[^1] the OpenAPI server, but that
didn't help (of course it wouldn't!).

Because this is a managed Kubernetes cluster, we have limited access to it,
which includes lack of access to raw logs. The Azure portal doesn't make it easy
but, after digging quite deep into it, eventually we found this error message in
the logs:

```
 {"pod":"kube-apiserver-7785d59f4f-scqmp","stream":"stderr","containerID":"925345f6501626aa6cd40dd187d5cf57837389eec9cb39b2292fb9ae3f66242f","log":"E0512 12:01:36.876768       1 handler.go:160] Error in OpenAPI handler: failed to build merge specs: unable to merge: duplicated path \/apis\/reports.kyverno.io\/v1\/clusterephemeralreports\n"}
```

That was the first clue! Now we know it's related to
[Kyverno](https://kyverno.io/).

That error eventually led us to
[this](https://github.com/kubernetes/kubernetes/issues/122668#issuecomment-2531243040)
issue in Kubernetes:

> We have the same issue here, actually also triggered by installing the kyverno
> reports-server with both apiservices (different groups served by the same
> api-server).

Aha!

Deleting the duplicate CRDs installed by [kyverno reports
server](https://github.com/kyverno/reports-server) has immediately resolved the
OpenAPI server unresponsiveness. It wasn't even necessary to restart it:

```shell
% kubectl delete crd ephemeralreports.reports.kyverno.io clusterephemeralreports.reports.kyverno.io clusterpolicyreports.wgpolicyk8s.io policyreports.wgpolicyk8s.io
customresourcedefinition.apiextensions.k8s.io "ephemeralreports.reports.kyverno.io" deleted
customresourcedefinition.apiextensions.k8s.io "clusterephemeralreports.reports.kyverno.io" deleted
customresourcedefinition.apiextensions.k8s.io "clusterpolicyreports.wgpolicyk8s.io" deleted
customresourcedefinition.apiextensions.k8s.io "policyreports.wgpolicyk8s.io" deleted
```

And now:

```shell
$ kubectl get --raw='/openapi/v2' | head -c 200
{"swagger":"2.0","info":{"title":"Kubernetes","version":"v1.30.11"},"paths":{"/.well-known/openid-configuration/":{"get":{"description":"get service account issuer OpenID configuration, also known as
```

That was a tricky one! Interestingly: it has only occurred in AKS.
[EKS](https://aws.amazon.com/eks/) was fine.

[^1]: [Hello, IT. Have you tried turning it off and on
    again?](https://en.wikiquote.org/wiki/The_IT_Crowd).

