---
title: "ArgoCD: persistent PDB selector diff"
url: https://perrotta.dev/2026/05/argocd-persistent-pdb-selector-diff/
last_updated: 2026-05-22
---


[Previously]({{< ref "2026-05-13-argocd-stale-vault-secret-after-population" >}}).

**Problem statement**: An ArgoCD application shows a persistent diff on a
`PodDisruptionBudget` — `spec.selector.matchExpressions` is in the rendered
manifest but missing from the live object. Sync doesn't clear it. Hard refresh
doesn't clear it. Syncing with replace or with server-side apply or with force
doesn't clear it. Ugh!

`policy/PodDisruptionBudget/default/my-super-cool-app`:

```yaml
selector:
  matchExpressions:
    - key: job-name
      operator: DoesNotExist
  matchLabels:
    release: my-super-cool-app
```

The chart was updated to add `matchExpressions` to the PDB selector. The diff
shows up. Sync runs. Diff stays.

First idea: _Kubernetes mutates PDB selectors server-side_ — no.
The PDB registry strategy in
[`pkg/registry/policy/poddisruptionbudget/strategy.go`](https://github.com/kubernetes/kubernetes/blob/master/pkg/registry/policy/poddisruptionbudget/strategy.go)
only touches `Status` and `Generation`. No selector mutation, no admission
plugin in tree that injects this. Patterns like
`matchExpressions: [{key: job-name, operator: DoesNotExist}]` come from chart
authors, not from K8s. This is all according to the LLM.

Second idea: _PDB selectors are immutable on older K8s_ — is also wrong
here. Selector mutability landed in 1.27. The cluster is on 1.33+.

The actual culprit is **client-side `kubectl apply` 3-way merge**, which is
what ArgoCD uses by default. The merge needs three inputs:

1. The previous applied state, read from
   `metadata.annotations.kubectl.kubernetes.io/last-applied-configuration`.
2. The live object.
3. The new desired manifest.

Check the annotation on the live PDB:

```shell
% kubectl get pdb my-super-cool-app -n default -o yaml | yq '.metadata.annotations."kubectl.kubernetes.io/last-applied-configuration"'
{"apiVersion":"policy/v1","kind":"PodDisruptionBudget","metadata":{...},"spec":{"maxUnavailable":1,"selector":{"matchLabels":{"release":"my-super-cool-app"}}}}
```

No `matchExpressions`. So the 3-way merge sees: _the previous apply didn't have
the field, the live object doesn't have the field, the new manifest has the
field_. It treats this as an addition — but the existing implementation in this
path doesn't reliably propagate the new key into the live selector when the
parent (`spec.selector`) is owned as an opaque value. The `managedFields` confirm
it:

```yaml
- manager: argocd-controller
  operation: Update
  fieldsV1:
    f:spec:
      f:maxUnavailable: {}
      f:selector: {}   # opaque — no sub-field ownership
```

`f:selector: {}` means argocd-controller owns the whole selector blob with no
sub-field tracking. New fields under `spec.selector` get lost in the merge.

The fix is to delete the live PDB and let ArgoCD recreate it on the next sync:

```shell
% kubectl delete pdb my-super-cool-app -n default
```

This can alternatively be done via the ArgoCD Web UI.

It is a safe operation: a PDB only gates voluntary disruptions (drains,
evictions). A brief gap doesn't affect running pods. The recreated object gets a
fresh `last-applied-configuration` containing `matchExpressions`, and the diff
clears.

The longer-term fix is to switch the application to server-side apply, which
tracks ownership at the field level and handles this correctly:

```yaml
syncPolicy:
  syncOptions:
    - ServerSideApply=true
```

It's always a dilemma whether or not to use server-side apply.

