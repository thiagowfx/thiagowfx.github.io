---
title: "kargo: notify when a soak completes"
url: https://perrotta.dev/2026/08/kargo-notify-when-a-soak-completes/
last_updated: 2026-09-03
---


[Previously]({{< ref "2026-08-19-kargo-cool-down-releases-with-a-holding-stage" >}}).

**Problem statement**: notify a Slack channel whenever Freight finishes soaking in
an upstream Kargo Stage, without promoting it to the next environment.

A soak does not finish a process. Once `requiredSoakTime` elapses, Kargo simply
makes the Freight available downstream. There is no soak-complete event in the
[Kargo event list](https://docs.kargo.io/user-guide/reference-docs/events/event-reference).

**Worakround**: I made availability start a notification-only promotion. Relevant excerpt,
with variable values omitted:

```yaml {filename="apps/base/kargo-pipelines/manifests/argocd/stage-notify-remaining-gardens-ready.yaml"}
metadata:
  name: notify-remaining-gardens-ready
spec:
  requestedFreight:
    - origin:
        kind: Warehouse
        name: argocd
      sources:
        stages:
          - staging-gardens
        requiredSoakTime: 48h0m0s
  promotionTemplate:
    spec:
      steps:
        - uses: http
          config:
            method: POST
            url: https://slack.com/api/chat.postMessage
            responseContentType: application/json
            successExpression: response.status == 200 && response.body.ok == true
            failureExpression: response.status != 200 || response.body.ok != true
            body: |-
              ${{ quote({
                "channel": vars.slackChannel,
                "username": "Kargo",
                "icon_emoji": ":kargo:",
                "unfurl_links": false,
                "text": ":white_check_mark: *argocd*: chart " + chartFrom(vars.chartRepo, "argocd").Version
                  + " completed 48h of soak in staging-gardens and is ready for promotion to remaining-gardens."
                  + "\nFreight: `" + ctx.targetFreight.name + "`"
              })
              }}
```

...wherein remaining-gardens = prod.

Only the notification Stage auto-promotes:

```yaml {filename="apps/base/kargo-pipelines/manifests/argocd/project-config.yaml"}
promotionPolicies:
  - stageSelector:
      name: notify-remaining-gardens-ready
    autoPromotionEnabled: true
```

Once the HTTP step succeeds, the Freight occupies this Stage and does not send
again. The real downstream Stage remains human-gated. A Slack API error fails
only the notification Promotion, which can be retried.

```shell
% prek run kargo-promotion-tasks --all-files
Check Kargo PromotionTask references.....................................Passed
```

This uses Kargo's generic [`http`
step](https://docs.kargo.io/user-guide/reference-docs/promotion-steps/http) as
the notification transport and Kargo itself as the timer.

There's no need to enroll into Akuity Platform ($$) just for the sake of
[`send-message`](https://docs.kargo.io/user-guide/reference-docs/promotion-steps/send-message).

