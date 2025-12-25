---
title: "Alpine Linux: install / pin old packages"
date: 2025-01-08T15:54:44-03:00
tags:
  - dev
---

Let's say you want to install an older version of `jq` in Alpine Linux.

For example:

- Alpine v3.18 has `jq` 1.6
- Alpine v3.19 has `jq` 1.7

You're probably using Alpine v3.21 or edge today, which has an even newer
version of `jq`. Hence `doas apk add jq` will not do.

Let's assume you do not want to edit your `/etc/apk/repositories`, as this is an
one-off, for a single package. What can you do then?

Use the `--repository` flag from `apk`!

```shell
% doas apk add --no-cache --repository=http://dl-cdn.alpinelinux.org/alpine/v3.18/main jq=~1.6
```

It's also important to pin the package version (`~1.6`), otherwise the latest
one available gets installed.

Replace "main" with "community" or "testing" as needed.
