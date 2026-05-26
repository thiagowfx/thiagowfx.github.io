---
title: "fast-resume: search coding agent sessions"
url: https://perrotta.dev/2026/05/fast-resume-search-coding-agent-sessions/
last_updated: 2026-05-26
---


[`fast-resume`](https://github.com/angristan/fast-resume) (`fr`), via
[Stanislas](https://stanislas.blog/2026/01/tui-index-search-coding-agent-sessions/):

> I use many coding agents these days: Claude Code, Codex, OpenCode, Copilot,
> and more. Sometimes I remember that I, or the agent, mentioned something
> specific in a previous session, and I want to go back to it.
>
> Most coding agents have a /resume feature now, which allows a session to be
> reopened with all the state back. While the resume feature works great,
> finding which session to resume is harder.
>
> [...]
>
> Let's say I have a few sessions about building a TUI program. I remember that
> in one of the sessions, the agent mentioned textual. I can't search for
> textual in the resume view! Also, if I don't remember the folder and which
> agent I used, I'm screwed. And some agents don't have that feature at all.

I've been longing for a solution to this problem. `fast-resume` nails it! It
reminds me of [`fpp`](https://facebook.github.io/PathPicker/), but for agent
sessions instead of disk files. In other words, it's like a `ripgrep` on
steroids designed specifically for coding agent sessions.

It supports various agents (including Claude Code, OpenAI Codex and Open Code),
among others.

## Installation

```shell
brew tap angristan/tap
brew install fast-resume
% brew ls fast-resume
/opt/homebrew/Cellar/fast-resume/1.16.2/bin/fast-resume
/opt/homebrew/Cellar/fast-resume/1.16.2/bin/fr
/opt/homebrew/Cellar/fast-resume/1.16.2/libexec/_internal/ (140 files)
/opt/homebrew/Cellar/fast-resume/1.16.2/libexec/fr
/opt/homebrew/Cellar/fast-resume/1.16.2/sbom.spdx.json
```

## Usage

`fr` is all you need to remember.

The program is a TUI, and it is very intuitive to use. Here are a few handy
terms for the search bar:

- `dir:foo`
- `agent:claude`
- `date:today`, `date:yesterday`

Upon selecting an entry you drop into its corresponding coding agent session.

"YOLO" mode is transparently supported, respecting the original session
settings.

The TUI mode is optional:

```shell
fr "agent:claude date:<7d api bug"
```

A local search index is created at `~/.cache/fast-resume` by default. If you
need to re-create it for whatever reason, run `fr --rebuild`.

In case you're wondering (not that it should matter), it's implemented in
Python.

See also:

- `fr --list`
- `fr --stats`

