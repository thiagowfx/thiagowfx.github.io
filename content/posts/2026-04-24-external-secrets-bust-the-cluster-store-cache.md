---
title: "external-secrets: bust the ClusterSecretStore cache"
date: 2026-04-24T01:22:06+02:00
tags:
  - dev
  - kubernetes
---

This post is hyper-specific but I am quite sure I'll forget how to do it the
next time it happens again, so I'm better off documenting it.

[External Secrets](https://external-secrets.io/):

> External Secrets Operator is a Kubernetes operator that integrates external
> secret management systems like AWS Secrets Manager, HashiCorp Vault, Google
> Secrets Manager, Azure Key Vault, IBM Cloud Secrets Manager, CyberArk Secrets
> Manager, Pulumi ESC and many more. The operator reads information from
> external APIs and automatically injects the values into a Kubernetes Secret.

**Problem statement**: a `ClusterSecretStore` is stuck on a past
authentication failure long after the Vault-side config was fixed, and every
`ExternalSecret` that references it reports `SecretSyncedError: the desired
SecretStore is not ready`.

Verify the store really is healthy now:

```shell
% kubectl describe clustersecretstore external-secrets-vault-backend
...
Status:
  Conditions:
    Last Transition Time:  2026-04-21T23:16:45Z   # <- stale
    Message:               unable to create client
    Reason:                InvalidProviderConfig
    Status:                False
    Type:                  Ready
```

`Last Transition Time` is from before I fixed the auth role. The operator
hasn't re-evaluated since. Poke it with an annotation to force a reconcile:

```shell
% kubectl annotate clustersecretstore external-secrets-vault-backend \
    force-reconcile=$(date +%s) --overwrite
```

Now it validates:

```shell
% kubectl describe clustersecretstore external-secrets-vault-backend | grep -A3 Status:
Status:
  Capabilities:  ReadWrite
  Conditions:
    Last Transition Time:  2026-04-23T23:11:30Z
    Message:               store validated
```

But the `ExternalSecret`s are *still* stuck — the operator caches store
readiness per-ES, not just per-CSS. Same trick:

```shell
% kubectl annotate externalsecret -n argocd --all \
    force-reconcile=$(date +%s) --overwrite
externalsecret.external-secrets.io/argocd-external-secret annotated
externalsecret.external-secrets.io/argocd-external-secret-github-webhook annotated
...

% kubectl get externalsecret -n argocd
NAME                       STORE                            STATUS         READY
argocd-external-secret     external-secrets-vault-backend   SecretSynced   True
...
```

No controller restart is necessary.

The annotation value doesn't matter — any change to the object metadata
re-queues it.
