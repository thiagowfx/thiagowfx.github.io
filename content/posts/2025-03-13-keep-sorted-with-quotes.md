---
title: "keep-sorted, with quotes"
date: 2025-03-13T13:00:06+01:00
tags:
  - dev
---

[keep-sorted]({{< ref "2024-12-26-keep-sorted" >}}) has been previously covered.

**Problem statement**: how to automatically sort the following YAML list?

```yaml
- azure-workload-identity
- clustermon
- flatfile
- kube2iam
- mongo
- node-local-dns
- "pgbouncer*"
- "rabbitmq*"
- "redis*"
- traefik
- vault
```

I would naturally add `keep-sorted` to it, but the result is not what I expected.

```yaml
# keep-sorted start
- "pgbouncer*"
- "rabbitmq*"
- "redis*"
- azure-workload-identity
- clustermon
- flatfile
- kube2iam
- mongo
- node-local-dns
- traefik
- vault
# keep-sorted end
```

Quotes are coming first!

Which does indeed make sense. They are ASCII characters
([`ascii(7)`](https://man.archlinux.org/man/ascii.7)), value 34, which comes
before `a-z`. Oh well.

I tried `ignore_prefixes="` to no avail. I also tried `by_regex=[\w-]+` to no
avail.

Only the following form worked:

```yaml
# keep-sorted start by_regex=['\w+[\w ]*']
- azure-workload-identity
- clustermon
- flatfile
- kube2iam
- mongo
- node-local-dns
- "pgbouncer*"
- "rabbitmq*"
- "redis*"
- traefik
- vault
# keep-sorted end
```

...but it's a mouthful. I filed an upstream bug:
https://github.com/google/keep-sorted/issues/76.
