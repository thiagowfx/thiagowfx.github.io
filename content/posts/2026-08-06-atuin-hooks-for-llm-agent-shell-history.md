---
title: "atuin: hooks for LLM agent shell history"
date: 2026-08-06T13:21:31+02:00
tags:
  - ai
  - claude
  - coding
  - dev
  - pi
---

**Today I learned**: [Atuin](https://atuin.sh/) ships
[_hooks_](https://docs.atuin.sh/18.18/guide/agent-hooks/) that capture commands
executed by ~~AI~~ LLM coding agents into the same shell history as mine.

As of today there are hooks for Claude Code, OpenAI Codex and Pi.

```shell
% atuin hook --help
Manage AI-agent shell hooks

Usage: atuin hook
       atuin hook <COMMAND>

Commands:
  install  Install hooks for an AI agent to capture commands in atuin history
  help     Print this message or the help of the given subcommand(s)
```

`install --help` doesn't list which agents are supported, but a bogus one
does (or simply look at their web documentation):

```shell
% atuin hook install invalid-agent
Error: unknown agent: invalid-agent. Supported agents: claude-code, codex, pi
```

Installing the hook for [pi](https://pi.dev/) is straightforward:

```shell
% atuin hook install pi
pi extension: installed atuin extension

Atuin extension installed for pi. Extension: ~/.pi/agent/extensions/atuin.ts
Reload pi with `/reload` or restart pi.
```

It drops a small extension that wraps every `bash` tool call with
`atuin history start --author pi` / `history end`:

```typescript
const historyId = await startHistory(pi, ctx.cwd, command);
if (historyId) pending.set(event.toolCallId, historyId);

// ...

await endHistory(pi, ctx.cwd, historyId, exitCodeFromResult(event.result, event.isError));
```

Commands run by the agent land in the same database as everything typed by
hand (by me!); there's no separate table, just an `--author` tag:

```shell
% atuin search --help | grep -A2 author
      --author <AUTHOR>
          Filter by author. Supports $all-user (non-agents), $all-agent, or literal names.
```

```shell
% atuin search --author pi
% atuin search --author '$all-user'
```

One shared history to rule them all.
