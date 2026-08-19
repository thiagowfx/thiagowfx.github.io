---
title: "kubernetes: force-refresh a cached multi-architecture image"
date: 2026-08-19T11:22:26+02:00
tags:
  - argocd
  - aws
  - bestof
  - bloggify
  - dev
  - docker
  - kubernetes
---

[Previously]({{< ref "2024-12-17-skopeo-operate-container-images-and-registries" >}}).

**Problem statement**: a Kubernetes ARM64 node kept running an AMD64 image after
I replaced the registry tag with a multi-architecture image via `skopeo`, due to
image caching.

I first mirrored only the AMD64 variant into AWS ECR (note: no `--all`):

```shell
% skopeo sync \
  --dest-creds "AWS:$(aws ecr get-login-password --region cn-north-1)" \
  --src docker --dest docker \
  --override-os linux --override-arch amd64 \
  quay.io/argoproj/argocd:v3.5.0 \
  "$REGISTRY/quay.io/argoproj"
```

That image failed on the ARM64 node:

```text
exec /usr/local/bin/argocd: exec format error
```

The source has four platform manifests, so I replaced the ECR tag with the full
manifest list (`-all`[^1]):

[^1]: Why isn't this the default?!

```shell
% skopeo sync \
  --all \
  --dest-creds "AWS:$(aws ecr get-login-password --region cn-north-1)" \
  --src docker --dest docker \
  quay.io/argoproj/argocd:v3.5.0 \
  "$REGISTRY/quay.io/argoproj"
```

```text
linux  amd64    sha256:521d6b62ecd0434c9cc6e9242a74f0e1137bb8fc0026b2c483ea88f3f17e725d
linux  arm64    sha256:8a14921f7e5dc3408111714f05bff68e337d459653c45f0aea738330d156079b
linux  s390x    sha256:28743e713eabeeaacc103d177fc0b651b564d10309839077b0381ca980055c7d
linux  ppc64le  sha256:1f9e154e0eef6df29b75948b0b54dfc8ec490c657100df11a24c34197b9beb3a
```

The sync is complete.

Deleting the failed pod did not help though. Its replacement still used the
cached AMD64 child manifest:

```text
pod: pod/argocd-redis-secret-init-qgnqr
node: ip-10-25-54-66.cn-north-1.compute.internal
arch: arm64
image ID: $REGISTRY/quay.io/argoproj/argocd@sha256:521d6b62ecd0434c9cc6e9242a74f0e1137bb8fc0026b2c483ea88f3f17e725d
pull policy: IfNotPresent
```

The Job pod template is immutable, so changing its pull policy in place (to
`Always`) also failed. Instead, I created a temporary pod on the same node. It
forced a pull and ran a harmless command that proved the selected binary can
be executed:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: argocd-image-refresh
  namespace: argocd
spec:
  nodeName: ip-10-0-0-42.cn-north-1.compute.internal
  restartPolicy: Never
  tolerations:
    - key: arch
      operator: Exists
      effect: NoSchedule
    - key: arch
      operator: Exists
      effect: NoExecute
  containers:
    - name: refresh
      image: $REGISTRY/quay.io/argoproj/argocd:v3.5.0
      imagePullPolicy: Always  # This is the important part!
      command: ["/usr/local/bin/argocd"]
      args: ["version", "--client"]
```

```text
NAME                   READY   STATUS      RESTARTS
argocd-image-refresh   0/1     Completed   0
```

The node cache now pointed at the multi-architecture manifest list:

```text
$REGISTRY/quay.io/argoproj/argocd@sha256:c298cedbaeb31532ba8d4e9904eba9e4987e067293fbd86400c5194e78f743d5
```

I removed the temporary pod and the failed Job pod. The Job controller created
a replacement, and the ARM64 binary started normally.

```shell
% kubectl -n argocd delete pod argocd-image-refresh
% kubectl -n argocd delete pod -l job-name=argocd-redis-secret-init
```

- - -

🤖 *Drafted with [`/bloggify`](https://github.com/thiagowfx/skills/blob/master/plugins/thiagowfx/skills/bloggify/SKILL.md).*
