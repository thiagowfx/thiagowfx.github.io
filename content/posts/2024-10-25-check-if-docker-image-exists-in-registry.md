---
title: "Check if docker image exists in registry"
date: 2024-10-25T14:11:14+02:00
tags:
  - dev
---

Given a docker registry, image and tag, run the following command:


```shell
% docker manifest inspect 9876543210.foo.ecr.us-east-1.amazonaws.com/org/image:123456789
```

If it does not exist, you'll see:

```
no such manifest: 9876543210.foo.ecr.us-east-1.amazonaws.com/org/image:123456789
```

Ensure you are authenticated and/or connected to the VPN in case of a private registry.

When using ECR (AWS's registry), you can authenticate this way:

```shell
% which docker_login
docker_login () {
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 9876543210.foo.ecr.us-east-1.amazonaws.com
}
```
