---
title: "prometheus: a 117GB WAL that could not truncate"
date: 2026-08-22T23:35:00+02:00
tags:
  - bloggify
  - dev
  - kubernetes
---

[Previously]({{< ref "2026-08-22-azure-disk-resize-needs-the-pvc-patch-too" >}}).

With the volume expanded, the next failure surfaced. The pod came up, served
for 14 minutes, then hit a different wall:

```shell
% kubectl -n monitoring get pod prometheus-...-prometheus-0 -o json | \
    jq '.status.containerStatuses[] | select(.name=="prometheus") | .lastState.terminated'
{
  "reason": "OOMKilled",
  "exitCode": 137,
  "startedAt": "2026-08-22T20:35:12Z",
  "finishedAt": "2026-08-22T20:49:29Z"
}
```

Not disk this time — 129GB was free. The WAL was the problem:

```shell
% du -sh /prometheus/prometheus-db/wal
117.7G	/prometheus/prometheus-db/wal
% ls /prometheus/prometheus-db/wal | wc -l
1062
```

A healthy WAL holds about two hours. This one spanned two days, because WAL
truncation happens at head compaction, and head compaction was OOMKilling
before it could commit. I caught it mid-attempt once:

```shell
% ls -d /prometheus/prometheus-db/wal/checkpoint.*
/prometheus/prometheus-db/wal/checkpoint.00188884
/prometheus/prometheus-db/wal/checkpoint.00189585.tmp
```

That `.tmp` never landed. The next check, it was gone and the old checkpoint
from two days earlier was still the newest one. Each cycle ingested a little
more than it compacted, so the head grew, and the OOM arrived sooner. 205
restarts of no net progress.

The memory limit had no room to grow either:

```yaml {filename="{...}/clustermon/values.yaml"}
      resources:
        limits:
          memory: 14Gi
        requests:
          cpu: 1
          memory: 11Gi
```

14Gi against a `Standard_D4ps_v6` with 15.0Gi allocatable. Raising it makes the
pod unschedulable.

So: delete the WAL. Thanos had already shipped every local block, which is what
made this cheap:

```shell
% cat /prometheus/prometheus-db/thanos.shipper.json
{
	"version": 1,
	"uploaded": [
		"01M0NKKGWJVKD3R84S90WW9R7G",
		"01M0NMBBC2Y31KMSJRA7VSGYXA",
		"01M0NMDM1XRJ0P1MMRBKF5HDV0"
	]
}
```

Scaling the StatefulSet down does not work — prometheus-operator owns it and put
the replica back within two minutes. The `Prometheus` CR is the real lever:

```shell
% kubectl -n monitoring patch prometheus clustermon-kube-prometheus-prometheus \
    --type merge -p '{"spec":{"replicas":0}}'
```

Then a scratch pod on the PVC, where I nearly deleted nothing at all:

```shell
% kubectl -n monitoring exec wal-cleanup -- ls /prometheus
lost+found
prometheus-db
```

The StatefulSet mounts that volume with a `subPath`. Deleting `/prometheus/wal`
would have removed nothing, and the restart would have looked like a fix.
The data is one level down:

```shell
% kubectl -n monitoring exec wal-cleanup -- \
    find /prometheus/prometheus-db/wal /prometheus/prometheus-db/chunks_head -mindepth 1 -delete
% kubectl -n monitoring exec wal-cleanup -- df -h /prometheus | tail -1
/dev/sda                250.9G      3.8G    247.1G   2% /prometheus
```

Replay after that:

```shell
total_replay_duration=280.16µs
```

Down from ten minutes. Cost: five hours of local samples, everything older still
queryable through Thanos.

Two independent limits, hit in sequence: the volume, then the memory ceiling
that kept compaction from ever committing. The remaining one is a limit sized at
93% of the node it runs on, and that needs a bigger node pool.

- - -

🤖 *Drafted with [`/bloggify`](https://github.com/thiagowfx/skills/blob/master/plugins/thiagowfx/skills/bloggify/SKILL.md).*
