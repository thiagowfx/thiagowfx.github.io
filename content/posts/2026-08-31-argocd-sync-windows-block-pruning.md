---
title: "argocd: sync windows block pruning"
date: 2026-08-31T13:00:50+02:00
tags:
  - argocd
  - bloggify
  - dev
  - kubernetes
---

**Problem statement**: deleting an ArgoCD `Application` from Git (GitOps) does
not guarantee it will disappear from the cluster.

We removed an app-of-apps child from every garden it lived in and merged the
PR. The parent synced clean:

```text
phase: Succeeded
message: successfully synced (all tasks run)
```

An hour later, six clusters _paged_ 🚨 with `ArgoCdAppSyncUnknown`. The child
was still there:

```text
sync: Unknown
health: Healthy
deletionTimestamp:
finalizers:
```

No `deletionTimestamp`, no finalizer stuck — it was never asked to delete.
The controller logs said why:

```text
level=info msg="Sync prevented by sync window" application=datastore-all
    dest-namespace=infra-services project=garden
```

The app was listed in an `AppProject` sync window:

```json
{
  "kind": "allow",
  "schedule": "0 23 * * *",
  "duration": "1h",
  "timeZone": "America/New_York",
  "applications": ["...", "datastore-all", "..."]
}
```

An `allow` window means auto-sync — including pruning — only runs inside it.
The parent app re-rendered without the child and dropped it from
`status.resources`, but pruning a tracked resource is itself a sync
operation, so ArgoCD deferred it to 23:00–00:00 New York time. Meanwhile the
orphaned `Application` still pointed at a values file that no longer existed
on `HEAD`:

```text
Failed to load target state: failed to generate manifest for source 1 of 2:
    ... open apps/overlays/g28/datastore-all/values.yaml: no such file or directory
```

Manifest generation failure is a sync status of `Unknown`, which is exactly
what fired the alert.

The object had no finalizer, so deleting it directly only removes the
bookkeeping, not the workload it deployed:

```shell
% kubectl -n argocd delete app datastore-all
```

The actual `infra-services` resources it created are still tracked by label
and get pruned once the window opens — or by hand in the meantime.
