---
title: "kargo: cool down upstream releases with a holding stage"
url: https://perrotta.dev/2026/08/kargo-cool-down-upstream-releases-with-a-holding-stage/
last_updated: 2026-08-19
---


**Problem statement**: wait before opening an upstream Helm chart upgrade PR,
without putting a timer in the PR workflow.

In other words: implement [dependency
cooldowns](https://blog.yossarian.net/2025/12/13/cooldowns-redux)[^1] in Kargo.

[^1]: cooldown or cool-off?

A [Kargo](https://kargo.io/) `Warehouse` makes newly discovered `Freight`
immediately available to a Stage that accepts it directly:

```text
Warehouse ──immediate──> open-upgrade-pr ──> PR
```

Kargo already has
[`requiredSoakTime`](https://docs.kargo.io/user-guide/how-to-guides/verification/#soak-times),
but only between Stages. It cannot delay a direct Warehouse-to-Stage promotion.
So add a Stage whose promotion deliberately does nothing:

```yaml
apiVersion: kargo.akuity.io/v1alpha1
kind: Stage
metadata:
  name: hold-upstream-release
spec:
  requestedFreight:
    - origin:
        kind: Warehouse
        name: external-secrets-upstream
      sources:
        direct: true
  promotionTemplate:
    spec:
      steps:
        - uses: compose-output
          config:
            state: holding
```

The PR Stage accepts Freight from that holding Stage and starts only after the
cool-off period:

```yaml
spec:
  requestedFreight:
    - origin:
        kind: Warehouse
        name: external-secrets-upstream
      sources:
        stages:
          - hold-upstream-release
        requiredSoakTime: 72h0m0s
  promotionTemplate:
    # clone, update chart dependency, push, and open PR
```

```text
Warehouse ──> hold-upstream-release ──72h──> open-upgrade-pr ──> PR
```

The holding Stage must auto-promote, as must the PR Stage after its soak. A new
release replaces the current Freight in the holding Stage. If the old release
did not complete 72 hours, it does not advance. This makes the hold a stability
window: only a release that remains current for three days opens a PR.

Explicit Freight approval remains the escape hatch because it bypasses the soak.

- - -

🤖 *Drafted with [`/bloggify`](https://github.com/thiagowfx/skills/blob/master/plugins/thiagowfx/skills/bloggify/SKILL.md).*

