---
title: "migrating from pre-commit to prek"
date: 2026-04-20T10:00:00+02:00
tags:
  - dev
  - pre-commit
---

[Previously]({{< ref "2024-12-21-pre-commit" >}}).

**Today I learned**: [prek](https://prek.j178.dev/) is a drop-in replacement
for `pre-commit`, rewritten in Rust. Same `.pre-commit-config.yaml`, same hook
ecosystem, much faster.

> A single binary with zero dependencies, much faster than the original
> pre-commit, drop-in compatible.

Install:

```shell
% brew install prek
# or
% cargo install prek
```

Then swap the command. Nothing else changes:

```diff
-pre-commit run --all-files
+prek run --all-files
```

Or skip the swap entirely: `prek install -f` drops in a shim that replaces the
`pre-commit` binary, so existing scripts and git hooks keep working unchanged.

The CI workflow on this blog ([`prek.yml`](https://github.com/thiagowfx/thiagowfx.github.io/blob/master/.github/workflows/prek.yml))
now uses [`j178/prek-action`](https://github.com/j178/prek-action) instead of
`pre-commit/action`, and the monthly autoupdate job
([`prek-autoupdate.yml`](https://github.com/thiagowfx/thiagowfx.github.io/blob/master/.github/workflows/prek-autoupdate.yml))
runs `prek auto-update --freeze` — the [`--freeze`]({{< ref "2025-03-20-pre-commit-pin-dependencies-with-freeze" >}})
flag works the same.

The [benchmark](https://prek.j178.dev/benchmark/) is what sold me. On cold
caches, `prek` is around 10x faster at resolving and installing hooks; on warm
runs, the difference is smaller but still noticeable.

Two other niceties `pre-commit` does not have:

- **Split configs across multiple files**. `prek` supports
  [multi-file configs](https://prek.j178.dev/config/#multiple-configs), so
  hooks can live next to the subproject they belong to in a monorepo instead
  of piling up in a single top-level YAML.
- **Run against a commit or a range**. `prek run --from-ref A --to-ref B`
  restricts the run to files changed between two refs — handy for checking a
  PR locally without touching unrelated files. A plain `prek run HEAD~3..HEAD`
  also works.

The `.pre-commit-config.yaml` file stays put, and `pre-commit.ci` still reads
it. No lock-in.
