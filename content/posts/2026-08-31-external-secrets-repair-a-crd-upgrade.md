---
title: "external secrets: repair a CRD upgrade"
date: 2026-08-31T16:29:01+02:00
tags:
  - argocd
  - bloggify
  - dev
  - kubernetes
---

**Problem statement**: an External Secrets Operator upgrade left different
clusters in different states, and a normal ArgoCD retry could not repair them.

The upgrade moved from ESO 0.9.20 to 2.9.0. Two CRDs rendered at about 707 KB.
Client-side apply tried to store each complete manifest in an annotation capped
at 262144 bytes:

```text
metadata.annotations: Too long: may not be more than 262144 bytes
```

Server-side apply avoids
`kubectl.kubernetes.io/last-applied-configuration`:

```shell
% kubectl apply --server-side --force-conflicts -f crd-secretstores.yaml
```

That fixed only half of the problem. The old chart configured CRD conversion
through the ESO webhook. The new chart omitted the conversion block, but
server-side apply does not remove a field that the desired manifest never
mentions. Reads still went to a `/convert` endpoint that ESO 2.9.0 no longer
served:

```text
conversion webhook for external-secrets.io/v1beta1, Kind=SecretStore failed
```

The conversion field had to be removed before the new schema was applied:

```shell
% kubectl patch crd/secretstores.external-secrets.io --type=merge \
    -p '{"spec":{"conversion":{"strategy":"None","webhook":null}}}'
% kubectl apply --server-side --force-conflicts -f crd-secretstores.yaml
```

Order matters. Applying the schema first creates a window where every
`SecretStore` read reaches the dead webhook.

One fixed sequence was still not enough. A cluster with the old controller and
old CRDs was healthy. Applying the v1 CRDs before ArgoCD deployed ESO 2.9.0
would instead produce this controller error:

```text
no matches for kind
```

I made the upgrade script classify live state before changing it:

```bash
case "$IMG_TAG:$V1_COUNT:$WEBHOOK_COUNT" in
  v2.9.*:3:0|2.9.*:3:0)  CLASS=DONE ;;
  v2.9.*:*|2.9.*:*)      CLASS=NEEDS-CRD-FIX ;;
  v0.9.*:0:*|0.9.*:0:*)  CLASS=NOT-STARTED ;;
  v0.9.*:*|0.9.*:*)      CLASS=MIXED ;;
  *)                      CLASS=UNKNOWN ;;
esac
```

`DONE` is a no-op. `NEEDS-CRD-FIX` patches conversion, renders all three CRDs
from the pinned Helm chart, applies them server-side, and restarts the
controller. `MIXED` and `UNKNOWN` stop instead of guessing.

`NOT-STARTED` also stops by default. Its separate opt-in path enables ArgoCD
auto-sync, waits for the new controller to land, then asks for a second run:

```bash
$ALLOW_NOT_STARTED || die "refusing without --allow-not-started"
run kc patch app external-secrets -n argocd --type=merge \
  -p '{"spec":{"syncPolicy":{"automated":{
    "enabled":true,"prune":true,"selfHeal":true
  }}}}'
info "Then: $0 $GARDEN"
```

The final checks compare custom resource counts, read all three resource kinds,
check every `ExternalSecret`, scan controller logs, and require ArgoCD to
converge:

```bash
for k in clustersecretstores secretstores externalsecrets; do
  kc_ok get "$k.external-secrets.io" -A || FAIL=true
done

if (( CSS_AFTER < CSS_BEFORE || SS_AFTER < SS_BEFORE || \
      ES_AFTER < ES_BEFORE )); then
  FAIL=true
fi

APP="$(kc get app external-secrets -n argocd \
  -o "jsonpath={.status.sync.status}/{.status.health.status}")"
[[ "$APP" == "Synced/Healthy" ]] || FAIL=true
```

The repair became an idempotent state transition instead of a command sequence.

- - -

🤖 *Drafted with [`/bloggify`](https://github.com/thiagowfx/skills/blob/master/plugins/thiagowfx/skills/bloggify/SKILL.md).*
