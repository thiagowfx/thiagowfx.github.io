---
title: "kubectl: atomic upsert"
date: 2026-06-09T16:16:12+02:00
tags:
  - dev
  - kubernetes
---

**Problem statement**: A cronjob refreshes an image-pull secret in every
namespace so nodes can authenticate to a private registry. It does the obvious™
thing: delete the old secret, then create the new one right away:

```shell
kubectl delete secret --ignore-not-found aws-ecr-token -n "$namespace"
kubectl create secret docker-registry aws-ecr-token -n "$namespace" \
    --docker-server="https://$AWS_ACCOUNT.dkr.ecr.$AWS_REGION.amazonaws.com" \
    --docker-username="AWS" \
    --docker-password="$(aws ecr get-login-password --region "$AWS_REGION")"
```

Every couple of hours, for a fraction of a second, that secret **does not
exist** in the cluster (booo!). Most of the time nobody notices. Occasionally a
deploy step that copies the secret into a tenant namespace runs into exactly
that gap, its `kubectl get` returns non-zero, and the whole deployment fails
with `ImagePullError`. Occasional flakiness, our favorite kind.

The idiomatic fix is to **never delete**.

The solution is to employ `kubectl create` with a client-side dry-run that
renders the object to YAML without touching the cluster; pipe that into `kubectl
apply` and we get an upsert:

```shell
kubectl create secret docker-registry aws-ecr-token -n "$namespace" \
    --docker-server="https://$AWS_ACCOUNT.dkr.ecr.$AWS_REGION.amazonaws.com" \
    --docker-username="AWS" \
    --docker-password="$(aws ecr get-login-password --region "$AWS_REGION")" \
    --dry-run=client -o yaml | kubectl apply -f -
```

The first run creates the secret; every run afterwards updates it in place.
There is no moment wherein it's absent.

The thing I wanted to be sure of before trusting it: does `apply` over a secret
that was originally `create`d actually *rotate* the password, or does it merge
in some way that leaves stale data behind? `kubectl apply` does a [3-way
merge]({{< ref "2026-05-22-argocd-pdb-selector-drift" >}}) against the
`last-applied-configuration` annotation, and that merge has bitten me before. A
secret with no prior annotation falls back to a 2-way merge — so this is worth
checking, just in case.

So I checked. Two consecutive upserts on a throwaway namespace, rotating the
password between them:

```shell
% kubectl get secret aws-ecr-token -n "$ns" -o jsonpath='{.metadata.uid}'
38d4c676-7169-4d1d-9911-9de068bba29a   # run 1
# [...]
38d4c676-7169-4d1d-9911-9de068bba29a   # run 2 — same uid: never deleted

% kubectl get secret aws-ecr-token -n "$ns" \
    -o jsonpath='{.data.\.dockerconfigjson}' | base64 -d
{"auths":{"...":{"username":"AWS","password":"PASSWORD_V2_ROTATED",...}}}
```

The `uid` is stable across runs — proof the object was never deleted and
recreated, only updated. `resourceVersion` bumped, the password rotated to the
new value, and no trace of the old one lingered. The 2-way-merge worry didn't
materialize: for a flat field like `.data.\.dockerconfigjson`, apply replaces
the value outright.

A `uid` that survives a refresh is the whole proof. Delete-then-create mints a
new `uid` every cycle; an in-place update keeps it. If we ever want to know
whether something *replaced* an object or *mutated* it, the `uid` is the way to
go.

Two more things worth highlighting:

- It's atomic from a *consumer's* point of view — the secret is never missing.
  It is not a transaction. `apply` is still a single API write; we're trading a
  delete-then-create pair (two writes, with a gap) for one write (no gap).
- `--dry-run=client` is the spelling since k8s 1.18. Older clusters used a bare
  `--dry-run` or `--dry-run=true`.

The same pattern works for configmaps, or anything else `kubectl create` knows
how to build. `create ... --dry-run=client -o yaml | apply -f -` is the way to
do whenever we'd otherwise reach for delete-then-create.
