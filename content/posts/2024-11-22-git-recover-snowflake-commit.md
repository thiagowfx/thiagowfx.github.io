---
title: "git: recover a snowflake commit"
date: 2024-11-22T11:51:26+01:00
tags:
  - dev
  - devops
---

When working with `git`, sometimes we make
[PEBKAC](https://en.wikipedia.org/wiki/User_error) mistakes and end up losing a
given checkout or commit or worktree.

<!--more-->

`git reflog` can often help recover from these mistakes. It is a bit difficult
to understand, but quite straightforward to use:

```shell
% git reflog | grep {branch_name}
```

For example:

```shell
% git reflog | grep -i 'thiagowfx/global-services'
```

Enjoy a real example:

```shell
% git reflog | grep -i 'thiagowfx/global-services'
7ca9ac6de77 HEAD@{0}: checkout: moving from 8882c1a128dd2cf35aa2188def3d176c7c15d2f1 to thiagowfx/global-services-docker
8882c1a128d HEAD@{1}: checkout: moving from thiagowfx/global-services-docker to 8882c1a12
7fcc128d2ea HEAD@{15}: rebase (finish): returning to refs/heads/thiagowfx/global-services-docker
16fcb83d888 HEAD@{20}: rebase (finish): returning to refs/heads/thiagowfx/global-services-docker
431509d9d0a HEAD@{24}: rebase (abort): returning to refs/heads/thiagowfx/global-services-docker
ee408b6e38c HEAD@{30}: checkout: moving from master to thiagowfx/global-services-docker
3babf6588f3 HEAD@{55}: checkout: moving from thiagowfx/global-services-docker to thiagowfx/base-global-services-image-tag
ee408b6e38c HEAD@{57}: rebase (abort): returning to refs/heads/thiagowfx/global-services-docker
ee408b6e38c HEAD@{60}: checkout: moving from master to thiagowfx/global-services-docker
3ef5b7c3844 HEAD@{77}: checkout: moving from thiagowfx/global-services-docker to thiagowfx/check-executables-have-shebangs
ee408b6e38c HEAD@{78}: checkout: moving from master to thiagowfx/global-services-docker
87f6bb2d95d HEAD@{86}: checkout: moving from thiagowfx/global-services-docker to thiagowfx/actionlint
8d07b53fd47 HEAD@{89}: rebase (finish): returning to refs/heads/thiagowfx/global-services-docker
c21089ab78c HEAD@{95}: rebase (finish): returning to refs/heads/thiagowfx/global-services-docker
70941a98ad0 HEAD@{104}: checkout: moving from master to thiagowfx/global-services-docker
2dd03ecdd09 HEAD@{149}: checkout: moving from thiagowfx/global-services-docker to lts13.1
1d62e88a8e2 HEAD@{151}: rebase (finish): returning to refs/heads/thiagowfx/global-services-docker
c9c2b36b058 HEAD@{166}: checkout: moving from master to thiagowfx/global-services-docker
0faa6f637b6 HEAD@{281}: checkout: moving from thiagowfx/global-services-docker to thiagowfx/pre-commit-trailing-4
c9c2b36b058 HEAD@{282}: checkout: moving from master to thiagowfx/global-services-docker
b0521a1a0f7 HEAD@{284}: checkout: moving from thiagowfx/global-services-docker to master
72b137aa4c7 HEAD@{286}: checkout: moving from master to thiagowfx/global-services-docker
81ac79b0c90 HEAD@{316}: checkout: moving from thiagowfx/global-services-docker to master
baef8a5eda1 HEAD@{319}: rebase (finish): returning to refs/heads/thiagowfx/global-services-docker
81ac79b0c90 HEAD@{343}: checkout: moving from master to thiagowfx/global-services-docker
```

How to find the correct checkout?

The easiest (albeit tedious) way is by brute-forcing your search in the output:

```shell
% git show 7ca9ac6de77
% git show 8882c1a128d
[...]
```

...until you find the diff you are looking for[^1].

From there, either `git checkout` (perhaps with the aid of `git worktree`) or
copy-and-paste (maybe with `git apply`).

[^1]: I am using the term "snowflake commit" in the title but it's not really
    idiomatic. The meaning is roughly _a sand grain in the beach_, or _a
    snowflake in the snow_.
