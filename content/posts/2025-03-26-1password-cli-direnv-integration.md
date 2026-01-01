---
title: "1Password CLI + direnv integration"
date: 2025-03-26T14:15:15+01:00
tags:
  - bestof
  - dev
  - security
---

Let's stay you're working on a terraform module that has a sensitive variable
named `api_key` in `variables.tf`.

When running `terraform apply`, you'll need to supply its value. Every. Single.
Time.

We can make it persistent by setting `export TF_VAR_api_key={my value}`.
However this is only persistent within the current shell.

To make it persistent across multiple sessions, create a `.envrc` file at the
root module:

```shell
#!/bin/sh
export TF_VAR_api_key={my value}
```

Then source it: `source ~/.envrc`. Now you have to source it every single time
you open a new shell.

We can use [`direnv`](http://direnv.net/) to do so automatically. It has been
[previously covered]({{< ref
"2022-01-04-direnv-automate-your-environment-variables" >}}). But...now we have
a secret stored as plain text in our filesystem.

We could store it in a more secure place, like a password manager, and then have
a mechanism automatically fetch its value.

## First approach

When using 1Password, the [1Password
CLI](https://developer.1password.com/docs/cli/) is such a mechanism.

```shell
#!/bin/sh
export TF_VAR_api_key=$(op run --no-masking -- op read "op://{vault name}/{entry name}/{item name}")
```

You can fetch the secret reference path from 1Password:
[docs](https://developer.1password.com/docs/cli/secret-references/). Click "Copy
Secret Reference" in the corresponding entry item.

## Second approach

The above is one possibility, and it works flawlessly, but there's a second
approach that uses `op run` alone with a secret reference that is dynamically
replaced.

Create an `.env` file:

```shell
TF_VAR_api_key="op://{vault name}/{entry name}/{item name}"
```

Update the `.envrc` file:

```shell
#!/bin/sh
dotenv
```

Now run `terraform apply` via `op run`, as follows:

```shell
op run --env-file=.env -- terraform apply
```

## References

- https://mattedwards.org/2024/01/inject-secrets-into-terraform-environment-using-1password/
- https://nshipster.com/1password-cli/
