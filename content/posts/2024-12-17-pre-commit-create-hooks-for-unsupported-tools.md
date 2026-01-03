---
title: "pre-commit: create hooks for unsupported tools"
date: 2024-12-17T22:46:41-03:00
tags:
  - bestof
  - dev
  - pre-commit
---

When using [pre-commit.com](https://pre-commit.com/), in an ideal world, every
formatter / linter / code analyzer would have a `.pre-commit-config.yaml` file
in its repository root.

In the real world, that's not always the case.

A recent example: [cloudflare/pint](https://github.com/cloudflare/pint):

> Prometheus rule linter/validator

It is a golang binary that lints [prometheus](https://prometheus.io/) rules.

Can we bridge the gap?

The end goal is the ability to run `pre-commit run --all-files pint` in our git
repository.

For that, we'll need to define a local / custom hook in our
`~/.pre-commit-config.yaml`:

```yaml
repos:
  - repo: local
    hooks:
      - id: pint
        name: Validate prometheus rules with pint
        language: golang
        additional_dependencies:
          - github.com/cloudflare/pint/cmd/pint@v0.69.1
        entry: pint --offline lint
        types:
          - yaml
        files: ^helm/clustermon-alerts/rules/
```

That simply works™. How did I get there? Starting with the references:

1. https://adamj.eu/tech/2023/02/09/pre-commit-hooks-unsupported-tools/
2. https://perrotta.dev/2024/11/pre-commit-additional-dependencies-in-golang/
3. https://stackoverflow.com/questions/62974985/go-module-latest-found-but-does-not-contain-package
4. https://pkg.go.dev/github.com/cloudflare/pint@v0.69.1/cmd/pint

The key part is `language: golang` + `additional_dependencies`.

Specifying `additional_dependencies` is a bit tricky. Initially, I did:

```
github.com/cloudflare/pint@v0.69.1
```

...but that yields nothing. In fact:

```shell
% go run github.com/cloudflare/pint@v0.69.1
go: github.com/cloudflare/pint@v0.69.1: module github.com/cloudflare/pint@v0.69.1 found, but does not contain package github.com/cloudflare/pint
```

We must always specify the module that contains the `main` function with `go
run`, and that is `cmd/pint`.
