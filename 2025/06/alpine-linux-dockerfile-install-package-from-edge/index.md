---
title: "Alpine Linux: Dockerfile: install package from edge"
url: https://perrotta.dev/2025/06/alpine-linux-dockerfile-install-package-from-edge/
last_updated: 2026-01-18
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

