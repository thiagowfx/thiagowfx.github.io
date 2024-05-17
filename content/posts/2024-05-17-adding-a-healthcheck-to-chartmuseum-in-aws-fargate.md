---
title: "Adding a healthcheck to chartmuseum in AWS Fargate"
date: 2024-05-17T11:15:09+02:00
tags:
  - devops
  - linux
---

Assume that you have a [Chartmuseum](https://chartmuseum.com/) container running
in [AWS Fargate](https://aws.amazon.com/fargate/).

Chartmuseum is a repository for helm charts. AWS Fargate is an Amazon service to
run containers ("serverless"), being part of ECS (Elastic Container Service).

Problem statement: Add a container _healthcheck_ to the chartmuseum task
definition associated with the container.

<!--more-->

The [official
docs](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_HealthCheck.html)
suggest using `curl`:

```
["CMD-SHELL", "curl -f http://localhost/ || exit 1"]
```

For Chartmuseum specifically we're interested in its `/health` endpoint, as per
[this reference](https://github.com/helm/chartmuseum/issues/28):

```
["CMD-SHELL", "curl -f http://localhost/health || exit 1"]
```

But we're using port 8080:

```
["CMD-SHELL", "curl -f http://localhost:8080/health || exit 1"]
```

If you use this healthcheck for the official chartmuseum image
(`ghcr.io/helm/chartmuseum`) it will fail, because the Alpine Linux environment
it uses does not contain `curl`.

A straightforward fix is to use `wget` instead:

```
["CMD-SHELL", "wget -q --spider http://localhost:8080/health || exit 1"]
```

`--spider` is needed because we do not want to download anything, `-q` is
optional and short for "quiet".

The `/health` endpoint merely returns a simple JSON:

```json
{"healthy":true}
```
