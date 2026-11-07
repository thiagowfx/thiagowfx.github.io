---
title: "atuin: resume coding agent sessions"
url: https://perrotta.dev/2026/11/atuin-resume-coding-agent-sessions/
last_updated: 2026-11-07
---


Previously: [`fr`]({{< ref "2026-05-25-fast-resume-search-coding-agent-sessions" >}}),
[`atuin`]({{< ref "2025-11-30-atuin" >}}).

**Today I learned**: `atuin` now searches and resumes coding agent sessions too.

[Session capture and resume](https://blog.atuin.sh/threads-agent-sessions/) arrived in `atuin` 18.24. Installed versions:

```shell
% atuin --version
atuin 18.24.5 (NO_GIT)
% fr --version
fr 2.14.3
```

The entry point is `atuin resume`, short for `atuin threads resume`. It opens a
searchable TUI, much like `fr`. This is not shell history search for the last
`claude` command: it searches the captured conversations themselves.

Capture is opt-in. Enable it, import existing sessions, then open the picker:

```shell
atuin threads enable
atuin threads import
atuin resume
```

Enabling capture turns on the `atuin` daemon and offers an import. The explicit
import brings in old sessions we haven't continued since enabling capture;
repeating it imports only what's new. No sync account is needed for local use.

Both tools search across agents and return us to a session. The difference is
what sits behind the picker:

| Feature | `fr` | `atuin` |
| --- | --- | --- |
| Source | Existing local agent files | Captured/imported sessions in `atuin`'s record store |
| Search | Prompts and replies; typo-tolerant | Conversation text and tool inputs |
| Across machines | No built-in sync | Optional end-to-end encrypted sync |
| Resume | Original agent | Original agent, fork, or continue in another agent |
| Setup | Scan local files on launch | Enable capture and run daemon |
| Agent examples | Pi, Cursor CLI, Kimi Code | Pi, Kiro, Omp |

`fr` remains a local search tool with a disposable index. `atuin` adds a
synced conversation store: it can reconstruct a session on another machine
before resuming it. Hosted sync and self-hosted sync both work.

For JSON search results and repository-scoped browsing:

```shell
fr --json --limit 3 "agent:pi ack"
atuin threads search --harness pi --limit 3 --style json ack
atuin resume --filter-mode workspace
```

The last command opens the picker scoped to the current repository. Given a
session ID, we can bypass the picker, print the resume command, fork the
session, or continue it in another agent:

```shell
atuin resume --print 01a00cb1-6498-7345-850b-3f2e6fa6d346
atuin resume --fork 01a00cb1-6498-7345-850b-3f2e6fa6d346
atuin resume --in codex 01a00cb1-6498-7345-850b-3f2e6fa6d346
```

One distinction from my original `atuin` setup: `enter_accept = false` applies
to shell history, not this picker. Enter proceeds with resuming a session.

The [`atuin` docs](https://docs.atuin.sh/latest/ai/threads/) describe what
survives capture: images are omitted, individual tool inputs/outputs are capped
at 64 KiB, and reasoning text is not retained. Session sync does not sync our
repository's working files either.

For finding a local conversation and reopening its original agent, `fr` is
still the simpler option. For carrying conversations between machines or
agents, `atuin` does something `fr` doesn't.

