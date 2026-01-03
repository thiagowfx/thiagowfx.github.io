---
title: "Claude: new slash commands"
date: 2025-11-23T17:43:04-03:00
tags:
  - ai
  - bestof
  - dev
  - serenity
---

[Previously]({{< ref "2025-10-06-claude-code-custom-commands" >}}).

Instead of creating custom slash commands myself, now I am turning to Claude to
do so for me.

**Prompt**:

> @agent-claude-code-guide create a slash command for...

This is a built-in agent.

Let the ~~experts~~ agents handle the cruft.

For example, `/commit`:

```
% cat ~/.claude/commands/commit.md
---
allowed_tools: ["Bash(git add:*)", "Bash(git commit:*)", "Bash(git status:*)", "Bash(git rev-parse:*)"]
argument-hint: [message]
description: Make a concise git commit on the current branch
---

Create a concise git commit with the provided message.

Steps:
1. Show current git status to confirm changes
2. Commit with the provided message
3. Ask the user if they want to push the changes

If the user provides a message as argument, use it directly. Otherwise, ask them for a commit message.
```
