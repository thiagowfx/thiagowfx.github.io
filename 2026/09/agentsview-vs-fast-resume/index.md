---
title: "AgentsView vs fast-resume"
url: https://perrotta.dev/2026/09/agentsview-vs-fast-resume/
last_updated: 2026-09-03
---


[Previously]({{< ref "2026-05-25-fast-resume-search-coding-agent-sessions" >}}).

**Problem statement**: does [AgentsView](https://www.agentsview.io/) replace
[`fast-resume`](https://github.com/angristan/fast-resume), or do they solve
different problems?

I installed both and compared their current releases:

```shell
% agentsview --version
agentsview v0.41.1 (commit a902515a, built 2026-08-18T13:34:56Z)
% fr --version
fr 2.11.2
```

`fr` has one job: search local agent sessions and resume one in its native
agent. Search is typo-tolerant. `Enter` replaces `fr` with the original agent
process and restores its working directory:

```text
Agent stores ──► adapters ──► normalized sessions ──► Tantivy index
                                                        │
Terminal ◄──── resume handoff ◄──── TUI/search ◄────────┘
```

AgentsView is a persistent SQLite archive with a desktop app, local web UI,
CLI, REST API, MCP server, cost reports, and session health signals. Its search
surface is correspondingly larger:

```shell
% agentsview session search --help | grep -E -- '--(fts|hybrid|regex|semantic|in )'
      --fts                      Fast tokenized FTS over messages only
      --hybrid                   Hybrid semantic + full-text search (reciprocal rank fusion)
      --in string                Comma-separated sources: messages,tool_input,tool_result (default all)
      --regex                    Treat pattern as an RE2 regex
      --semantic                 Semantic (vector) search over user/assistant messages
```

AgentsView documents 59 session sources against `fr`'s 12. Resume support is
the opposite: AgentsView maps nine agent types, while `fr` has handoff commands
for all twelve, including Pi:

```text
# fast-resume
Pi → pi --session <id>

# AgentsView resume map
claude, codex, traex, copilot, cursor, gemini, opencode, amp, kiro
```

The local footprint shows the difference in scope:

```shell
% du -sh /opt/homebrew/Cellar/fast-resume/2.11.2 \
    /Applications/AgentsView.app ~/.cache/fast-resume ~/.agentsview
14M     /opt/homebrew/Cellar/fast-resume/2.11.2
116M    /Applications/AgentsView.app
772K    /Users/tperrotta/.cache/fast-resume
28M     /Users/tperrotta/.agentsview
```

`fr` treats its index as a disposable cache. AgentsView keeps sessions until
`agentsview prune` removes them. It also sends an [anonymous daily liveness
ping](https://www.agentsview.io/configuration/#privacy-and-telemetry) and checks
for updates; `fr` 2.11.2 has neither mechanism.

Given the aforementioned trade-offs: I am happier with `fr`. KISS.

- - -

🤖 *Drafted with [`/bloggify`](https://github.com/thiagowfx/skills/blob/master/plugins/thiagowfx/skills/bloggify/SKILL.md).*

