---
title: "The ack + xargs + sed pattern"
date: 2025-04-30T16:20:24+02:00
tags:
  - bestof
  - dev
  - linux
  - macos
---

I employ this pattern almost every day:

- use [`ack`](https://beyondgrep.com/) to search for a given string in a codebase (git repo)
- use [`xargs`](https://man.archlinux.org/man/xargs.1) to iterate through each finding
- use [`sed`](https://www.gnu.org/software/sed/manual/sed.html) to make a text transformation

Example of the day:

```shell
% ack "limit: 2" -l | xargs -n 1 gsed -i -e 's/limit: 2/limit: 5/g'
```

Given multiple [ArgoCD app manifests](https://argo-cd.readthedocs.io/en/stable/) in the form:

```yaml
spec:
  syncPolicy:
    retry:
      limit: 2
      backoff:
        duration: 5s
        factor: 2
        maxDuration: 1m
```

Replace `limit: 2` with `limit: 5` in all files. That's what the command above
does:

- `ack -l` lists all files that match the given pattern
- pipe to `xargs -n 1` iterates on each of them
- `gsed -i` (GNU `sed`) makes a text transformation in-place

It's not bulletproof, but it works most of the time.

Sometimes I use [`fd`](https://github.com/sharkdp/fd) to narrow the search down
to a file pattern. For example:

```shell
% fd -e yaml | xargs ack "limit: 2" -l
```

In this case, though, `ack --yaml` would be even simpler.

When `sed` isn't up for the job, `awk` tends to be a decent alternative.

Regular expression replacements aren't always precise.
False positives can easily take place.
Adding `\b` (word boundaries) sometimes helps.

Other times it's better to use a syntax-aware tool instead of `sed`.

For YAML, there's [`yq`](https://github.com/mikefarah/yq).

For JSON, there's [`jq`](https://jqlang.org/):

> `jq` is like `sed` for JSON data - you can use it to slice and filter and map
> and transform structured data with the same ease that `sed`, `awk`, `grep` and
> friends let you play with text.


