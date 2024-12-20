---
title: "pre-commit: try-repo"
date: 2024-11-26T12:26:24+01:00
tags:
  - dev
---

A productivity booster whenever trying out new
[pre-commit.com](https://pre-commit.com/) hooks from the wild:

<!--more-->

**Usage**: `pre-commit try-repo {git-repo} [--all-files]`

**Example**:

```console
% pre-commit try-repo https://github.com/mrtazz/checkmake
[INFO] Initializing environment for https://github.com/mrtazz/checkmake.
===============================================================================
Using config:
===============================================================================
repos:
-   repo: https://github.com/mrtazz/checkmake
    rev: bd26d7905e47713ff0bf3b0e5e7b9c55f0d24e53
    hooks:
    -   id: checkmake
    -   id: checkmake-system
===============================================================================
[WARNING] Unstaged files detected.
[INFO] Stashing unstaged files to /var/folders/yr/6sw3yylx6gjcy5jr38d6j6000000gn/T/tmpakaoxt10/patch1732620344-2186.
[INFO] Installing environment for https://github.com/mrtazz/checkmake.
[INFO] Once installed this environment will be reused.
[INFO] This may take a few minutes...
Makefile linter/analyzer.............................(no files to check)Skipped
Makefile linter/analyzer.............................(no files to check)Skipped
[INFO] Restored changes from /var/folders/yr/6sw3yylx6gjcy5jr38d6j6000000gn/T/tmpakaoxt10/patch1732620344-2186.
```

Previously I would manually add the `repo:` entry with `rev: HEAD` and then run
`pre-commit run --all-files {hook-id}`, one by one, adjusting as needed.

This new workflow is much faster though, and it is a native pre-commit command!

Inspiration to adopt more pre-commit hooks: [all-repos.yaml](https://github.com/pre-commit/pre-commit.com/blob/master/all-repos.yaml)
