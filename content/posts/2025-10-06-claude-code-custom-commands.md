---
title: "claude code: custom commands"
date: 2025-10-06T17:31:30+02:00
tags:
  - ai
  - bestof
  - dev
---

[Claude Code](https://www.claude.com/product/claude-code) supports [custom commands](https://docs.claude.com/en/docs/claude-code/slash-commands#custom-slash-commands).

The precise term is "custom slash commands":

> Custom slash commands allow you to define frequently-used prompts as Markdown
> files that Claude Code can execute. Commands are organized by scope
> (project-specific or personal) and support namespacing through directory
> structures.

I created my first custom slash command:

```shell
% cat ~/.claude/commands/send-pr.md
You are a world-class software developer who can write concise and descriptive
pull requests (PRs).

Sources of inspiration include:

- Daniel Stenberg (curl)
- Junio Hamano (git)
- Linus Torvalds (linux)

Send out a PR[1] corresponding to the current branch.
If there's a .github/PULL_REQUEST_TEMPLATE.md file, use it as template.

If the current branch is 'main' or 'master', create a local branch first.
The branch name should be prefixed by my github username[2] and a slash.

[1]: 'gh pr create'
[2]: 'gh api user --jq .login'
```

It can be "executed" with `/send-pr`.

"Execution" is merely "sending the prompt".

It's akin to a snippet expander. Arguably one could do the same by setting a
`:send-pr` snippet on e.g. [Espanso](https://espanso.org/).

Perhaps it is even better, as it would work with all CLI agents – not only
Claude Code. Well, we keep on experimenting.

Reusable custom slash commands will be shared in my [.dotfiles](https://github.com/thiagowfx/.dotfiles/tree/master/claude/.claude/commands).
