---
title: "Kubernetes: debugging services"
date: 2024-12-16T10:14:11-03:00
tags:
  - dev
---

I am deploying a new helm chart to our staging environments, and needed a way to
ensure its dependencies in `values.yaml` are properly configured.

From the official kubernetes
[documentation](https://kubernetes.io/docs/tasks/debug/debug-application/debug-service/):

> An issue that comes up rather frequently for new installations of Kubernetes
> is that a Service is not working properly. You've run your Pods through a
> Deployment (or other workload controller) and created a Service, but you get
> no response when you try to access it. This document will hopefully help you
> to figure out what's going wrong.

<!--more-->

## Run commands in a brand new pod

```shell
% kubectl run -it --rm --restart=Never busybox --image=gcr.io/google-containers/busybox sh
```

...quite verbose, but it works reliably, spawning a basic pod with
[busybox](https://www.busybox.net/).

I prefer to have a package manager at my fingertips, hence `alpine` is arguably
a better choice:

```shell
% kubectl run -it --rm --restart=Never busybox --image=alpine ash
```

You don't need to remember that alpine uses `ash` by default, `sh` works as
well. In fact:

```shell
/ # ls -al /bin | grep sh
lrwxrwxrwx    1 root     root            12 Dec  5 12:17 ash -> /bin/busybox
lrwxrwxrwx    1 root     root            12 Dec  5 12:17 fdflush -> /bin/busybox
lrwxrwxrwx    1 root     root            12 Dec  5 12:17 sh -> /bin/busybox
```

Then I could do, for example, `apk update` + `apk add mtr nmap`.

Alpine is marvellous for this because `apk` is very lightweight (and, hence,
fast!) and the available packages from upstream are quite comprehensive.

## Run commands in an already existing pod

```shell
% kubectl exec <POD-NAME> -c <CONTAINER-NAME> -- <COMMAND>
```

...however you cannot choose a custom image this way. You're stuck with whatever
the pod is running.

The way around this is with the use of ephemeral debug containers. Newer
versions of kubernetes have the `kubectl debug` command:

```shell
% kubectl debug -it <POD-NAME> --image=alpine [--target=<POD-NAME>]
```

Happy debugging!
