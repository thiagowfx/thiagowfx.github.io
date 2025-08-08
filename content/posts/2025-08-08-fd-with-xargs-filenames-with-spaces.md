---
title: "fd with xargs: filenames with spaces"
date: 2025-08-08T14:33:27+02:00
tags:
  - dev
---

**Problem statement**: find all `base/mongo` occurrences in `kustomization.yaml`
files in the codebase.

[My favorite approach]({{< ref "2025-04-30-the-ack-xargs-sed-pattern" >}}):

```shell
% fd kustomization.yaml | ifne xargs -n 1 ack "base/mongo" -l
[...]
ack: scaffolding/cookiecutter/base/{{: No such file or directory
ack: cookiecutter.app_name: No such file or directory
ack: }}/kustomization.yaml: No such file or directory
```

But it looks horrible!

The problem is that there is a file named as follows:

```
scaffolding/cookiecutter/base/{{ cookiecutter.app_name }}/kustomization.yaml
```

...more specifically, the spaces are the problem. It's easy to fix it though:

```
% fd -0 kustomization.yaml | ifne xargs -0 -n 1 ack "base/mongo" -l
```

...adding `-0` to `fd` instructs it to print the results null-separated (`\0`)
instead of newline (`\n`) separated. And the corresponding switch in `xargs`
instructs it to expect null-separated input.

I especially like this approach because it's easy to memorize.
