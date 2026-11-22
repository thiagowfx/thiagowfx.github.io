---
title: "jo: create JSON from shell arguments"
date: 2026-11-22T11:37:05Z
tags:
  - bloggify
  - dev
---

**Today I learned**: [`jo`](https://github.com/jpmens/jo) creates JSON from
shell arguments. [`jq`](https://jqlang.org/) queries and transforms JSON.
They work well together, complementing each other.

Both can create objects. `jo`:

```shell
% repo=$(basename "$PWD")
% branch=$(git branch --show-current)
% jo repo="$repo" branch="$branch"
{"repo":"perrotta.dev","branch":"master"}
```

The equivalent with `jq` needs `-n` (no input) and `--arg` for each
string. `-c` keeps the output compact:

```shell
% jq -cn --arg repo "$repo" --arg branch "$branch" '{repo: $repo, branch: $branch}'
{"repo":"perrotta.dev","branch":"master"}
```

My take: `jo` is more ergonomic to create JSON than `jq`.

`jo -a` creates an array. Command substitution lets us nest it in an object:

```shell
% jo -a bloggify dev
["bloggify","dev"]
% jo repo="$repo" tags="$(jo -a bloggify dev)"
{"repo":"perrotta.dev","tags":["bloggify","dev"]}
```

My take: not sure whether this is super useful.

Shell quotes prevent word splitting. They do **not** force JSON strings:

```shell
% version=$(jo -v | cut -d ' ' -f 2)
% jo version="$version"
{"version":1.9}
% jo -- -s version="$version"
{"version":"1.9"}
```

`jo` detects numbers and booleans. Use `-- -s` to force the next value to a
string. By contrast, `jq --arg` always creates a string.

For querying or changing the result, pass it to `jq`:

```shell
% jo repo="$repo" branch="$branch" | jq -r '.branch'
master
```

`jo` for short JSON creation commands; `jq` for filters and transformations.
