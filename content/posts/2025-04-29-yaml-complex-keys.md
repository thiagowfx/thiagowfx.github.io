---
title: "YAML: complex keys"
date: 2025-04-29T13:06:16+02:00
tags:
  - dev
---

**Today I learned**: YAML complex keys ([stack
overflow](https://stackoverflow.com/questions/33987316/what-is-a-complex-mapping-key-in-yaml)).

From the [spec](https://yaml.org/spec/1.2.2/), § 2.11:

> A question mark and space (`"? "`) indicate a complex mapping key. Within a
> block collection, key/value pairs can start immediately following the dash,
> colon, or question mark.

```yaml
? - Detroit Tigers
  - Chicago cubs
: - 2001-07-23

? [ New York Yankees,
    Atlanta Braves ]
: [ 2001-07-02, 2001-08-12,
    2001-08-14 ]
```

I noticed it when saving a `values.yaml` file from [helm](https://helm.sh/) in
VSCode, which has auto-formatted it like this:

```diff
diff --git a/helm/argocd/values.yaml b/helm/argocd/values.yaml
index b0884b26d..928c02eb3 100644
--- a/helm/argocd/values.yaml
+++ b/helm/argocd/values.yaml
@@ -471,10 +471,12 @@ argo-cd:
       # Do not trigger a reconciliation when the reported status of a HorizontalPodAutoscaler or ExternalSecret changes.
       # That would mean reconciling every application with a hpa every 5 seconds which is heavy on the cpu.
       #    https://argo-cd.readthedocs.io/en/stable/operator-manual/reconcile/#finding-resources-to-ignore
-      resource.customizations.ignoreResourceUpdates.autoscaling_HorizontalPodAutoscaler: |
+      ? resource.customizations.ignoreResourceUpdates.autoscaling_HorizontalPodAutoscaler
+      : |
         jsonPointers:
           - /status
-      resource.customizations.ignoreResourceUpdates.external-secrets.io_ExternalSecret: |
+      ? resource.customizations.ignoreResourceUpdates.external-secrets.io_ExternalSecret
+      : |
         jsonPointers:
           - /status
```

Initially I thought this was a mistake that would yield a parse error.
Upon running `helm template`, however, I observed it's in fact a no-op.

The LLM says:

> VS Code is reformatting your YAML that way because it's interpreting the
> structure as YAML mapping with complex keys.
>
> This happens when your keys contain special characters (like dots or
> underscores) or are long strings — YAML interpreters sometimes use the `? key
> :` value syntax to denote explicit mapping entries with complex keys.

I surely cannot deny it's a long key. Go blame
[ArgoCD](https://argo-cd.readthedocs.io/en/stable/operator-manual/reconcile/#system-level-configuration)
:P
