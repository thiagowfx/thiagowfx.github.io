---
title: "Diffoscope: recursive diffs"
date: 2024-08-24T01:09:42+02:00
tags:
  - dev
---

There are many ways to `diff` two individual files:

- `diff`
- [`colordiff`](https://www.colordiff.org/)
- [`icdiff`](https://github.com/jeffkaufman/icdiff)
- [`delta`](https://github.com/dandavison/delta)

But how can you `diff` two individual directories?

Enter [`diffoscope`](https://diffoscope.org/).

Install it with your favorite package manager. Usage is as simple as:

```shell
diffoscope /path/to/dir1 /path/to/dir2
```

There's also a webapp: https://try.diffoscope.org/

It is particularly handy in the context of [Reproducible
Builds](https://reproducible-builds.org/).
