---
title: "Amp Code: queue/unqueue messages"
date: 2026-01-01T17:03:12-03:00
tags:
  - dev
---

When using [Amp Code](https://ampcode.com/) (a CLI coding agent), sending two
messages in a row results in the second message interrupting the first.

Most other agents (e.g. Claude Code, OpenAI Codex, Google Gemini) support
message queueing by default, wherein the second message "waits" until the first
prompt is complete.

To achieve the same behavior in `amp`, use `/queue`. There's also `/dequeue` to
undo it.
