---
title: "Helm: migrate chart dependencies from HTTPS to OCI"
date: 2025-01-08T18:45:57-03:00
tags:
  - dev
---

I got aware of this due to
[Bitnami](https://blog.bitnami.com/2024/10/bitnami-helm-charts-moving-to-oci.html)'s
blog post.

In `Chart.yaml`, instead of depending on:

```
- https://charts.bitnami.com/bitnami/airflow-18.3.2.tgz
```

Instead, depend on:

```
- oci://registry-1.docker.io/bitnamicharts/airflow:18.3.2
```

The switch is transparent, it works out-of-the-box.

However there's one caveat: You cannot `helm repo add
oci://registry-1.docker.io/bitnamicharts`. That only works for `https://`
registries.

The workaround is to `helm pull oci://[...] --version {version}` and/or to
browse available tags/versions via docker hub.
