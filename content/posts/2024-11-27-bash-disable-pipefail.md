---
title: "bash: disable pipefail"
date: 2024-11-27T11:50:58+01:00
tags:
  - dev
---

We often do `set -euo pipefail` in shell scripts[^1].
It's an overall good habit in defensive programming.

Nonetheless, sometimes the default behavior for `pipefail` is desired.

Recently we had an example involving [pre-commit.com](https://pre-commit.com/)
and [`mdsh`](https://github.com/zimbatm/mdsh), consider this `README.md` file:

```md
`> files=$(grep -rl '/spec/sources/0/targetRevision' --include="*.yaml" apps/overlays | sort -d -u) && if [ -z "$files" ]; then echo "None"; else echo "$files" | sed -e 's/^/- /'; fi`
```

The intention is to find all `.yaml` files that match the given string within
the `apps/overlays` directory.

The result is added to the `README.md` file with a git pre-commit hook, which
runs `mdsh` underneath, proudly showcasing a glimpse of literate programming.

What happens when there are no matches, and `grep` returns with exit code 1?

```
`> files=$(grep -rl '/spec/sources/0/targetRevision' --include="*.yaml" apps/overlays | sort -d -u) && if [ -z "$files" ]; then echo "None"; else echo "$files" | sed -e 's/^/- /'; fi`

ERROR: some commands failed:

`> files=$(grep -rl '/spec/syncPolicy/automated' --include="*.yaml" apps/overlays | sort -d -u) && if [ -z "$files" ]; then echo "None"; else echo "$files" | sed -e 's/^/- /'; fi`
failed with exit status: 1.
```

Of course it fails, because `mdsh` sets [`-o
pipefail`](https://github.com/zimbatm/mdsh/pull/63/files).

The desired behavior is to disable it: `set +o pipefail`. Then it works
properly:

```
> set +o pipefail && files=$(grep -rl '/spec/syncPolicy/automated' --include="*.yaml" apps/overlays | sort -d -u) && if [ -z "$files" ]; then echo "None"; else echo "$files" | sed -e 's/^/- /'; fi
```

[^1]: A
    [gist](https://gist.github.com/mohanpedala/1e2ff5661761d3abd0385e8223e16425)
    with an explanation.
