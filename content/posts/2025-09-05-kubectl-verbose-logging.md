---
title: "kubectl: verbose logging"
date: 2025-09-05T18:10:33+02:00
tags:
  - dev
  - kubernetes
---

When running `kubectl` commands, to get a glimpse of what is happening under the
hood, pass `-v={N}` to it.

For example:

```shell
% kubectl get pod -n argocd -v=6
I0905 16:10:19.893576 3929356 loader.go:395] Config loaded from file:  /home/ubuntu/.kube/config
I0905 16:10:19.919935 3929356 round_trippers.go:553] GET https://{REDACTED}.us-east-1.elb.amazonaws.com/api/v1/namespaces/argocd/pods?limit=500 200 OK in 17 milliseconds
NAME                                                  READY   STATUS    RESTARTS      AGE
argo-workflows-server-6ffcfbb779-kxdzk                1/1     Running   0             4d18h
argo-workflows-workflow-controller-85c667cf96-rm9dw   1/1     Running   0             2d4h
argocd-application-controller-0                       1/1     Running   0             48m
[...]
```

`-v=10` is super verbose. Fine-tune as needed.

Another example:

```shell
% kubectl get deploy -n argocd -w -v6
I0905 16:12:49.277471 3929550 loader.go:395] Config loaded from file:  /home/ubuntu/.kube/config
I0905 16:12:49.302783 3929550 round_trippers.go:553] GET https://{REDACTED}.us-east-1.elb.amazonaws.com/apis/apps/v1/namespaces/argocd/deployments?limit=500 200 OK in 17 milliseconds
NAME                                 READY   UP-TO-DATE   AVAILABLE   AGE
argo-workflows-server                1/1     1            1           91d
argo-workflows-workflow-controller   1/1     1            1           44d
argocd-applicationset-controller     1/1     1            1           23d
argocd-dex-server                    1/1     1            1           451d
argocd-notifications-controller      1/1     1            1           449d
argocd-redis                         1/1     1            1           451d
argocd-repo-server                   1/1     1            1           451d
argocd-server                        3/3     3            3           428d
I0905 16:12:49.316961 3929550 round_trippers.go:553] GET https://{REDACTED}.us-east-1.elb.amazonaws.com/apis/apps/v1/namespaces/argocd/deployments?resourceVersion=695374153&watch=true 200 OK in 2 milliseconds
```
