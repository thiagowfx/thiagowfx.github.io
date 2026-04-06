---
title: "bkt: bypass cache"
url: https://perrotta.dev/2025/05/bkt-bypass-cache/
last_updated: 2025-05-05
---


[Previously]({{< ref "2024-12-29-bkt-cache-command-outputs" >}}).

Whenever using [`bkt`](https://www.bkt.rs/), sometimes you may need to evict the
cache to get fresh data.

Use the `--force` option to do so. Usage:

Replace:

```shell
% bkt --ttl 30d -- {my cool command}
```

with:

```shell
% bkt --force --ttl 30d -- {my cool command}
```

