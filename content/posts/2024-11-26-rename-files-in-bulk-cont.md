---
title: "Rename files in bulk (cont)"
date: 2024-11-26T11:50:06+01:00
tags:
  - dev
---

Deeper into the [rabbit hole]({{< ref "2024-06-19-rename-files-in-bulk" >}}):

```shell
% fd Dockerfile.dockerignore | xargs -n 1 rename 's/Dockerfile\.dockerignore/.dockerignore/'
```

The pre-commit [identify](https://github.com/pre-commit/identify) library
currently mistags these files as Dockerfiles, even though they are not[^1],
which creates all sorts of issues.

<!--more-->

[^1]: They are akin to `.gitignore` files in terms of structure.
