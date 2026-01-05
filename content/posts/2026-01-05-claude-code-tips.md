---
title: "Claude Code tips"
date: 2026-01-05T15:18:13-03:00
tags:
  - ai
  - dev
---

These are great collections:

- https://github.com/ykdojo/claude-code-tips
- https://adocomplete.com/advent-of-claude-2025/

New tips to me:

`/rename` to set a session name, like you would with a tmux window. Later
on, resume the session with `/resume {name}` or `claude --resume {name}`.

Since
[v2.0.74](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2074)
LSP became a first-class citizen, comparable to OpenCode:

> Added LSP (Language Server Protocol) tool for code intelligence features like
> go-to-definition, find references, and hover documentation
