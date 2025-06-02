---
title: "PDB: minAvailable and maxUnavailable cannot be both set"
date: 2025-06-02T12:00:05+02:00
tags:
  - dev
  - selfhosted
---

In Kubernetes it's not possible to have a [`PodDisruptionBudget`
(PDB)](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) with
both `minAvailable` and `maxUnavailable` set simultaneously:

```
one or more objects failed to apply, reason: PodDisruptionBudget.policy "pgbouncer-pgbouncer" is invalid: spec: Invalid value: policy.PodDisruptionBudgetSpec{MinAvailable:(*intstr.IntOrString)(0xc02c03dd20), Selector:(*v1.LabelSelector)(0xc02c03dd40), MaxUnavailable:(*intstr.IntOrString)(0xc02c03dd60), UnhealthyPodEvictionPolicy:(*policy.UnhealthyPodEvictionPolicyType)(nil)}: minAvailable and maxUnavailable cannot be both set (retried 5 times).
```

Our manifests did not violate this rule though. Then where did the error message
come from?

It turns out [ArgoCD](https://argo-cd.readthedocs.io/en/stable/) was creating an
intermediate state containing both properties:

```yaml
# [...]
spec:
  minAvailable: 1
  maxUnavailable: 1
# [...]
```

One solution is to sync the underlying application PDB manifest with
[replace](https://argo-cd.readthedocs.io/en/latest/user-guide/sync-options/#replace-resource-instead-of-applying-changes).

**Warning**: It's better to "sync with replace" **only** the PDB. Do not do it
with the entire application.
