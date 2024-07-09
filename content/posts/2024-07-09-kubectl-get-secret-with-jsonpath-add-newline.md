---
title: "kubectl: get secret with jsonpath and add a newline"
date: 2024-07-09T11:36:34+02:00
tags:
  - dev
  - devops
---

When retrieving opaque secrets with `kubectl`, one will often invoke this
typical command:

```shell
ubuntu@ubuntu:~ $ kubectl get secret -n argocd argocd-github-webhook-secret -o jsonpath='{.data.value}'
eW91IGFyZSBjdXJpb3VzIGFyZW50IHlvdQ==ubuntu@ubuntu:~ $
```

But isn't this ugly? The prompt is concatenated with the output.

<!--more-->

It turns out `jsonpath` can emit a newline for improved readability:

```shell
ubuntu@ubuntu:~ $ kubectl get secret -n argocd argocd-github-webhook-secret -o jsonpath='{.data.value}{"\n"}'
eW91IGFyZSBjdXJpb3VzIGFyZW50IHlvdQ==
ubuntu@ubuntu:~ $
```

Note that the `{"\n"}` **must** be quoted.

And then you could pipe it to `base64 -d` afterwards, as usual, and it's a no-op:

```shell
$ kubectl get secret -n argocd argocd-github-webhook-secret -o jsonpath='{.data.value}{"\n"}' | base64 -d
you are curious arent youubuntu@ubuntu:~ $
```

However, the `base64` output also swallows the newline. This can be resolved
with a simple `echo`:

```shell
$ kubectl get secret -n argocd argocd-github-webhook-secret -o jsonpath='{.data.value}{"\n"}' | base64 -d && echo
you are curious arent you
ubuntu@ubuntu:~ $
```

Newlines are hard, eh?
