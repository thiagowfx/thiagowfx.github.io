---
title: "Alpine Linux: Dockerfile: install package from edge"
date: 2025-06-04T12:37:47+02:00
tags:
  - dev
---

**Problem statement**: Given a `Dockerfile` based on a fixed release of Alpine
Linux (e.g. `FROM alpine:3.22`), install a package from `edge` (i.e. a package
that did not yet make it to a fixed release).

The approach is similar to package [pinning]({{< ref
"2025-01-08-alpine-linux-install-pin-old-packages" >}}), by providing a custom
`--repository` to `apk add`:

```dockerfile
RUN apk add --no-cache --repository=https://dl-cdn.alpinelinux.org/alpine/edge/testing gliderlabs-sigil vals
```

Replace "testing" with "community" or "main" as needed.
