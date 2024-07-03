---
title: "Terraform: perform a global update"
date: 2024-07-02T12:33:37+02:00
tags:
  - dev
  - devops
---

Given a `terraform/modules` directory tree, we would like to globally update the
minimum required terraform version in all modules.

<!--more-->

- Option 1: Use `ack` or `fd` + `sed`.
- Option 2: Use [`tfupdate`](https://github.com/minamijoyo/tfupdate), which can
  be installed via `homebrew` or your favorite package manager (c.f.
  [repology](https://repology.org/project/tfupdate/versions)).

```shell
$ tfupdate terraform -r terraform/modules -v '~> 1.6.6'
```
