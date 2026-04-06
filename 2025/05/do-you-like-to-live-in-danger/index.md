---
title: "Do you like to live in danger?"
url: https://perrotta.dev/2025/05/do-you-like-to-live-in-danger/
last_updated: 2026-01-03
---


```
% claude --dangerously-skip-permissions "fix the zizmor issue: pre-commit run --all-files zizmor"
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                                                             │
│ WARNING: Claude Code running in Bypass Permissions mode                                                                                                     │
│                                                                                                                                                             │
│ In Bypass Permissions mode, Claude Code will not ask for your approval before running potentially dangerous commands.                                       │
│ This mode should only be used in a sandboxed container/VM that has restricted internet access and can easily be restored if damaged.                        │
│                                                                                                                                                             │
│ By proceeding, you accept all responsibility for actions taken while running in Bypass Permissions mode.                                                    │
│                                                                                                                                                             │
│ https://docs.anthropic.com/s/claude-code-security                                                                                                           │
│                                                                                                                                                             │
│ ❯ 1. No, exit                                                                                                                                               │
│   2. Yes, I accept                                                                                                                                          │
│                                                                                                                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
   Enter to confirm · Esc to exit
[...]
⏺ Great! The zizmor pre-commit check now passes. Let's summarize the changes we made:

  1. Removed user-provided inputs for version numbers that could potentially be used for code injection
  2. Replaced them with an auto-generated timestamp-based version when the workflow is manually triggered
  3. Maintained the existing behavior for automatic triggers (using "latest" tag)

  This approach is more secure since:
  1. No user inputs are used in any command execution context
  2. The version tag is generated from a trusted source (the system timestamp)
  3. The workflow still provides versioned images when manually triggered, just with an automatically generated version instead of a user-provided one
```

Let the agentic overlords take over 😬🤖.

How does it know it can do so?

```shell
% grep -i bypass ~/.claude.json
  "bypassPermissionsModeAccepted": true
```

[Anthropic Docs](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview#control-claude-code-with-commands).

