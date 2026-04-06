---
title: ".gitignore .claude/settings.local.json"
url: https://perrotta.dev/2025/06/.gitignore-.claude/settings.local.json/
last_updated: 2026-03-26
---


The initial attempt:

``` {filename="~/.gitignore"}
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

