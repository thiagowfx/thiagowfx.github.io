---
title: "ArgoCD: vertical-pod-autoscaler sync loop"
date: 2025-02-13T13:17:36+01:00
tags:
  - dev
  - selfhosted
---

We've had a long time issue wherein our
[vertical-pod-autoscaler](https://artifacthub.io/packages/helm/cowboysysop/vertical-pod-autoscaler)
(VPA) ArgoCD application, deployed via its helm chart, got stuck in a sync loop.

More specifically: the helm chart automatically generates a self-signed
certificate via the
[GenCA](https://helm.sh/docs/chart_template_guide/function_list/#genca) helm
function upon every change to our gitops repository. It turns out
[this](https://github.com/cowboysysop/charts/blob/9527602f8f2ea59f51cd3a7d3380810ba60c39fc/charts/vertical-pod-autoscaler/README.md?plain=1#L236)
is documented and we can see its corresponding manifest
[here](https://github.com/cowboysysop/charts/blob/9527602f8f2ea59f51cd3a7d3380810ba60c39fc/charts/vertical-pod-autoscaler/templates/admission-controller/tls-secret.yaml#L3C1-L3C91).

So that's where the sync loop was coming from! ArgoCD was constantly reporting
(and resolving) a diff in the admission controller secret.

The manifest:

```yaml
apiVersion: v1
data:
  ca.crt: ++++++++
  tls.crt: ++++++++
  tls.key: ++++++++
kind: Secret
metadata:
[...]
  name: vertical-pod-autoscaler-admission-controller-tls
  namespace: kube-system
[...]
```

The problematic are all the ones under `data:`.

I confirmed that was indeed the case in the [CNCF
Slack](https://cloud-native.slack.com/archives/C01TSERG0KZ/p1739442822542539)
`#argo-cd`. Thanks Tim!

How to address it?

We leverage
[`ignoreDifferences`](https://argo-cd.readthedocs.io/en/stable/user-guide/diffing/)
(c.f. [Stack
Overflow](https://stackoverflow.com/questions/77510338/argocd-show-as-out-of-sync-on-every-push-for-auto-generate-certs-password))
in the ArgoCD app manifest:

```
% git diff HEAD~2..HEAD
diff --git apps/base/vertical-pod-autoscaler/vertical-pod-autoscaler.yaml apps/base/vertical-pod-autoscaler/vertical-pod-autoscaler.yaml
index 92bfbcc..90d8435 100644
--- apps/base/vertical-pod-autoscaler/vertical-pod-autoscaler.yaml
+++ apps/base/vertical-pod-autoscaler/vertical-pod-autoscaler.yaml
@@ -34,3 +34,15 @@ spec:
         maxDuration: 1m
     syncOptions:
       - CreateNamespace=true
+      - RespectIgnoreDifferences=true
+  ignoreDifferences:
+    - group: ""
+      kind: Secret
+      name: vertical-pod-autoscaler-admission-controller-tls
+      jsonPointers:
+        - /data
+    - group: apps
+      kind: Deployment
+      name: vertical-pod-autoscaler-admission-controller
+      jsonPointers:
+        - /spec/template/metadata/annotations/checksum~1tls-secret
```

In [JSON Pointers](https://www.rfc-editor.org/rfc/rfc6901) (RFC 6901), one
escapes the slash character with a `~1` (c.f. section 3 in the spec):

>  ```
>  Because the characters '~' (%x7E) and '/' (%x2F) have special meanings in
>  JSON Pointer, '~' needs to be encoded as '~0' and '/' needs to be encoded as
>  '~1' when these characters appear in a reference token.
>  ```

Problem resolved!

In general all helm charts that generate self-signed certificates (with `genCA`)
may experience this sync loop when used with a CD framework such as Argo.
