---
title: "Remove the executable bit from all files with a given extension"
date: 2024-11-25T11:43:20+01:00
tags:
  - dev
  - devops
---

To illustrate, consider TypeScript files (`*.ts`).

Run:

```shell
% fd -e .ts -x chmod -x
```

References:

- `fd`: `find` on steroids: https://github.com/sharkdp/fd
- `-x`: execute the given command on all matched files

You could also use classic `find`:

```shell
% find . -type f -name '*.ts' -exec chmod -x {} \;
```

Or:

```shell
% find . -type f -name '*.ts' | xargs chmod -x
```

Or, with more ~~style~~ safety:

```shell
% find . -type f -name '*.ts' -print0 | xargs -0 -n 1 chmod -x
```
