---
title: "Kubernetes: one-off env exec"
url: https://perrotta.dev/2026/03/kubernetes-one-off-env-exec/
last_updated: 2026-03-23
---


**Problem statement**: run an one-off script and/or binary within a kubernetes
pod. It needs a certain environment variable (`VAULT_TOKEN`) to be set.

**Wrong**:

```shell
ubuntu@my-deploy-server:~ $  kubectl exec -n vault vault-1 -- VAULT_TOKEN=hvs.mysupersecrettoken vault read auth/kubernetes/role/vault-init
error: Internal error occurred: Internal error occurred: error executing command in container: failed to exec in container: failed to start exec "7455bd5880fe41c177a47702e3dfacbe4240207d53a19ac13edf74b62c626e61": OCI runtime exec failed: exec failed: unable to start container process: exec: "VAULT_TOKEN=hvs.mysupersecrettoken": executable file not found in $PATH
```

It is trying to look for a file named `VAULT_TOKEN=hvs.mysupersecrettoken` in
the `$PATH`. Surely that's not we want here!

**Right**:

```shell
ubuntu@my-deploy-server:~ $  kubectl exec -n vault vault-1 -- env VAULT_TOKEN=hvs.mysupersecrettoken vault read auth/kubernetes/role/vault-init
Key                                         Value
---                                         -----
alias_name_source                           serviceaccount_uid
bound_service_account_names                 [vault-init]
bound_service_account_namespace_selector    n/a
bound_service_account_namespaces            [vault]
policies                                    [vault-init]
token_bound_cidrs                           []
token_explicit_max_ttl                      0s
token_max_ttl                               0s
token_no_default_policy                     false
token_num_uses                              0
token_period                                168h
token_policies                              [vault-init]
token_ttl                                   0s
token_type                                  default
```

...just pass it via [`env(1)`](https://man.archlinux.org/man/env.1):

> env — run a program in a modified environment
>
> `env [OPTION]... [-] [NAME=VALUE]... [COMMAND [ARG]...]`

Also, if you pay attention, you'll notice there are two spaces between `$` and
`kubectl`. This is intentional. See [Why is bash not storing commands that start
with
spaces?](https://unix.stackexchange.com/questions/115917/why-is-bash-not-storing-commands-that-start-with-spaces)
for context. `bash` won't record the command in the shell history if it starts
    with spaces — though that behavior depends on the `HISTCONTROL` setting. We
    do not want to store our `VAULT_TOKEN` in plain text in the shell history
        (`~/.bash_history`).

