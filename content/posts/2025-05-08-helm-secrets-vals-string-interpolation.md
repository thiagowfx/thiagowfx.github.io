---
title: "helm-secrets + vals: string interpolation"
date: 2025-05-08T15:25:14+02:00
tags:
  - dev
  - security
---

[helm-secrets](https://github.com/jkroepke/helm-secrets) is:

> a helm plugin that helps to manage secrets with Git workflow and store them
> anywhere.

It uses [vals](https://github.com/helmfile/vals) underneath, which is a:

> Helm-like configuration values loader with support for various sources

...including, in particular, [HashiCorp Vault](https://www.hashicorp.com/en/products/vault).

The `vals` syntax is documented
[in the vals documentation](https://github.com/helmfile/vals?tab=readme-ov-file#expression-syntax).

**Problem statement**: construct a string composed of the following two vault
entries:

- `vault://kv-v2/services/common/postgres/#url`
- `vault://kv-v2/services/common/postgres/#params`

...to yield `{url}?{params}`.

How do we concatenate two vault entries?
The secret is in the `+`:

 > Finally, the optional trailing `+` is the explicit "end" of the expression.
 > You usually don't need it, as if omitted, it treats anything after `ref+` and
 > before the new-line or the end-of-line as an expression to be evaluated. An
 > explicit `+` is handy when you want to do a simple string interpolation. That
 > is, `foo ref+SECRET1+ ref+SECRET2+ bar` evaluates to `foo SECRET1_VALUE
 > SECRET2_VALUE bar`.

The final result:

```
secrets+literal://ref+vault://kv-v2/services/common/postgres/#url+?ref+vault://kv-v2/services/common/postgres/#params
```

...wherein `secrets+literal://` comes from `helm-secrets`. It needs to appear only
once. `ref+vault://` comes from `vals`, it appears once for each vault entry.
