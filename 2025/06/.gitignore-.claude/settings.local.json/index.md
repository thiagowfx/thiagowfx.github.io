
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

