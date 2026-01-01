
To build a docker image completely from scratch, without reusing cache layers on
your system:

```shell
docker build --no-cache -f Dockerfile . -t {image name}:{image tag} --platform
linux/amd64
```

- Pass an explicit platform in case e.g. you're building on a Mac M1 (arm64)
  with the intent of running it on Linux in the cloud (amd64 typically).
- The docker image full specification is: image =
  `{registry}/{repository}:{tag}`. For example, the registry could be an AWS ECR
  URL, whereas the repository is something like "bitnami/sealed-secrets", and
  the tag typically follows semantic versioning.

