---
title: ".gitignore .claude/settings.local.json"
date: 2025-06-12T22:17:43+02:00
tags:
  - dev
---

The initial attempt:

```shell
% cat ~/.gitignore
.claude/settings.local.json
```

However, it doesn't work when you run [claude
code](https://www.anthropic.com/claude-code) in a subdirectory of your git
repository root. `git diff` still surfaces it.

The correct form is:

```diff
-.claude/settings.local.json
+**/.claude/settings.local.json
```

Add `**` to include subdirectories as well.
