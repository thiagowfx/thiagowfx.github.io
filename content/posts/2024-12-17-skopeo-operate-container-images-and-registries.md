---
title: "skopeo: operate container images and registries"
date: 2024-12-17T17:49:31-03:00
tags:
  - bestof
  - dev
  - kubernetes
---

When working with `docker` and private image registries, a common workflow is to copy images from one private registry in the cloud to another. This can be done with [`skopeo`](https://github.com/containers/skopeo/).

This post includes some common recipes for it.

## Usage 1) Default / Root to Staging

From the default / root account registry to the staging registry:

```shell
skopeo sync \
  --src-creds "AWS:$(aws ecr get-login-password --region {region} --profile default)" \
  --dest-creds "AWS:$(aws ecr get-login-password --region {region} --profile staging)" \
  --override-os linux --override-arch amd64 \
  --src docker --dest docker \
  {account_id_root}.dkr.ecr.{region}.amazonaws.com/{org}/{repository}:{tag} \
  {account_id_staging}.dkr.ecr.{region}.amazonaws.com/{org}
```

Example values[^1]:

- repository: `argocd-gitops-tools`
- tag (version): `1.0.1`
- region: `us-east-1`

[^1]: image = registry (includes the org name) + repository + tag

## Usage 2) Public to MFA

From a public registry to a private registry that uses MFA (multi-factor authentication).

First, it's necessary to get MFA credentials. Source the script below
(`china.mfa.sh`):

```shell
#!/usr/bin/env bash
# shellcheck disable=SC2155

export AWS_PROFILE=china

echo -n "Enter the MFA token code for your AWS China account: " && read -r token

mfa_arn="$(aws iam --profile "$AWS_PROFILE" get-user --output text --query User.Arn | sed 's/:user\//:mfa\//')"
credentials="$(aws --profile "$AWS_PROFILE" sts get-session-token --serial-number "$mfa_arn" --token-code "$token" --duration-seconds 86400)"

echo "Got credentials: $credentials"

export AWS_ACCESS_KEY_ID=$(echo "$credentials" | jq -r '.Credentials.AccessKeyId')
export AWS_SECRET_ACCESS_KEY=$(echo "$credentials" | jq -r '.Credentials.SecretAccessKey')
export AWS_SESSION_TOKEN=$(echo "$credentials" | jq -r '.Credentials.SessionToken')

[[ -n "$AWS_SESSION_TOKEN" ] && echo "Success!"
```

**Important**: It is necessary to do `source china-mfa.sh`. Doing `./china-mfa.sh`
will **not** work.

Then we can proceed with the image sync:

```shell
skopeo sync \
  --dest-creds "AWS:$(aws ecr get-login-password --region cn-north-1)" \
  --override-os linux --override-arch amd64 \
  --src docker \
  --dest docker \
  quay.io/argoproj/argocd:v2.12.6 \
  {account_id_mfa}.dkr.ecr.cn-north-1.amazonaws.com.cn/quay.io/argoproj
```

Notes:

- A public registry does not need authentication, hence there's no `--src-creds`.
- `--dest-creds` does not specify a `--profile`. Likewise, no `AWS_PROFILE` env var should be defined.
- In this example, China (`cn-north-1`) is an AWS account with MFA enabled.

## Potpourri

- It's possible to pass `--scoped` to prefix images at destination using the
  full source image path as scope.
- To sync multiple image architectures, pass `-a` or `--all`.
- If syncing from/to Azure (ACR), use `az acr login`. Find the `username` in the
  Azure portal. For example:

  ```shell
  az acr login -n {container registry name} --expose-token | jq -r '.accessToken' | skopeo login {registry} --password-stdin --username {username}
  ```
