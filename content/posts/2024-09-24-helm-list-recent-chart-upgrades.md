---
title: "helm: list recent chart upgrades"
date: 2024-09-24T14:21:20+02:00
tags:
  - dev
---

**Problem statement**: Given a kubernetes cluster with many helm charts in
different namespaces, how to use `helm` to query the list of the last recently
"touched" charts?

By "touched" we mean either installed (via `helm install`) or upgraded (via
`helm upgrade`).

Something like: `helm ls --all --sort-by updated`. Using `kubectl` directly
would also be OK.

## Solution

The brute force way:

```shell
helm ls --max 99999 -A -o json | jq -r '.[] | "\(.updated)\t\(.name)"' | sort | tail | column -t
```

- `-A` for all namespaces
- `--max 99999` to "disable" [paging](https://github.com/helm/helm/issues/3322) (there's no better way as of 2024-09-24)
- `jq` to filter out on the "updated" field

Note that a sample json entry looks like the following:

```json
{
  "name": "hoth-cb7f8a327",
  "namespace": "default",
  "revision": "2",
  "updated": "2024-06-14 15:02:16.775174131 +0000 UTC",
  "status": "deployed",
  "chart": "hoth-0.1.0",
  "app_version": "1.0.0"
}
```

Sample output of the aforementioned command:

```
2024-09-24  10:56:15.655674586  +0000  UTC  geonosis
2024-09-24  10:56:15.731630075  +0000  UTC  coruscant
2024-09-24  11:01:35.156973247  +0000  UTC  endor
2024-09-24  11:02:30.314014351  +0000  UTC  hoth
```
