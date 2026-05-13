---
title: "ArgoCD: stale Vault secret after population"
url: https://perrotta.dev/2026/05/argocd-stale-vault-secret-after-population/
last_updated: 2026-05-13
---


**Problem statement**: An ArgoCD application references a Vault secret via
`helm-secrets` / `vals` (e.g. `vault://kv-v2/services/foo#/apiKey`). The
application is created _before_ the secret exists in Vault, or while the
corresponding key is blank. The key is populated later on. The application keeps
behaving as if the value is still missing — usually a `404` from Vault, or a
`permission denied` on the cached lookup:

```
Failed to load target state: failed to generate manifest for source 1 of 2:
rpc error: code = Unknown desc = Manifest generation error (cached): failed to
execute helm template command: [...] vals error: expand
vault://kv-v2/services/foo#/apiKey: Error making API request. URL: GET
http://vault.infra-services:8200/v1/sys/internal/ui/mounts/kv-v2/services/foo
Code: 404.
```

Note the `(cached)` part of the error. The `argocd-repo-server` caches the
result of manifest generation, _including_ failed `vals` / `helm-secrets`
lookups. A normal sync or refresh happily reuses the cached (stale) failure and
never re-resolves the Vault reference. So the freshly-populated secret goes
unnoticed. A blank to non-blank update counts as well, besides outright
token rotations.

The fix is to perform a **Hard Refresh** on the application — that's what busts
the manifest cache and forces a fresh Vault lookup:

```shell
argocd app get <app> --hard-refresh
```

Or, in the web UI: open the application → `REFRESH ▾` dropdown → `HARD
REFRESH`.

If a hard refresh alone doesn't pick up the new value, restart the argocd repo
server:

```shell
kubectl rollout restart deployment -n argocd argocd-repo-server
```

A regular refresh won't do. The cache key for the failed lookup outlives the
refresh.

By default, the application cache lasts for **24h** (though it can be changed
via helm values); hence, another way to resolve the issue is to simply sit out
on it and wait.

