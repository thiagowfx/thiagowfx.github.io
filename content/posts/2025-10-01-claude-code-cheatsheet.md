---
title: "Claude Code: cheatsheet"
date: 2025-10-01T20:03:54+02:00
tags:
  - bestof
  - dev
---

A brain dump as of Oct 1st, 2025 of my head, all things [Claude Code](https://www.claude.com/product/claude-code).

## Keyboard shortcuts

- `Shift+Tab` to cycle through: "default" -> "⏵⏵ accept edits on" -> "⏸ plan mode on"
  - "⏵⏵ Accept edits on" is a comfortable mode to be on by default, especially
    when paired with git commits as checkpoints.
  - A well-curated tool whitelist (c.f. `~/.claude/settings.json`) can further
    enhance this mode.
  - "⏵⏵ Accept edits on" is not the same as `--dangerously-skip-permissions`:

> Bypass all permission checks. Recommended only for sandboxes with no internet access.

- `Tab` to toggle "Thinking on" / "Thinking off"
  - This is a brand new feature in [Claude Code 2.0](https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously), just released this week.
    Hence I haven't used it so far. Toggling the plan mode is typically enough
    for my needs.
- `Esc Esc` to clear input / `/rewind` to a previous checkpoint
  - I prefer to "manually steer / tune" the LLM. Learn from past mistakes!
- `Ctrl-r` to search previous prompts – similarly to `bash` / `zsh` shell
  history
- `!` for shell mode e.g. `! ls` or `! git commit -a -m "msg"`. Good for
  one-offs.
  - Alternatively, simply open a new shell tab / split / window.
  - Alternatively, suspend Claude with `Ctrl-z`:

```
Claude Code has been suspended. Run `fg` to bring Claude Code back.
Note: ctrl + z now suspends Claude Code, ctrl + _ undoes input.
[1]  + 78756 suspended (signal)  claude
```

- `/` for commands – TAB completion is available.
- `@` for file paths e.g. `@README.md` or `@.env` – TAB completion is supported
  - Use `@` to provide targeted context in prompts, for example: `Upgrade
    @main.go to incorporate logging. Follow a pattern similar to
    @vendor/main.go. Update @README.md afterwards`
- `#` to memorize (a.k.a. "add to memory")
  - I don't use this shortcut much. Instead, prefer editing `CLAUDE.md` directly
    for pristine, per-repo settings. This is comparable to having a local, per
      git repo `.gitignore` versus a `~/.gitignore_global` that affects all
      repositories.
  - Project memory lives in `CLAUDE.md`, user memory lives in
    `~/.claude/CLAUDE.md`.
- `Ctrl-o` for verbose output
- `Ctrl-t` to show TODOs
- `Shift+Enter` for newline (`\n`); pre-requisite: `/terminal-setup`
- Emacs / readline keybindings generally work for text navigation: `C-a`, `C-e`,
  `C-b`, `C-f`, `C-u`, `C-p`, `C-n`, `C-w`. There's also a vim mode that can be
  toggled with `/vim`.
- **Gripe**: `Ctrl-l` does not clear the screen. And neither does `Esc Esc`.
  Surely someone has already filed a feature request for this? There's a
  `/clear` command, but it is meant to clear history and free up context, which
  is totally different.
- `Ctrl-_` to undo. I prefer `C-w`.
- **Gripe**: It hard-codes mentioning "bash" in various places, instead of
  "shell". `bash` is not the only POSIX shell out there. Heck, there's even a
  `/bashes` command to list and manage background tasks.
- `Esc` to interrupt (think of `C-g` on Emacs).

Most of the above reference can be pulled up with:

- `?` for help

A few handy comments not previously mentioned:

- `/cost`: show total cost + duration of the current session
  - See also: [ccusage]({{< ref "2025-09-04-claude-ccusage" >}})
- `/export`: copy the current conversation to the clipboard, or export it to a
  file
- `/init`: to bootstrap and scaffold / populate `CLAUDE.md`
- `/mcp` to manage MCP servers
- `/resume`: resume a (previous) conversation.
  - Alternatively, launch `claude` with [`--resume`]({{< ref "2025-09-02-claude-resume" >}}) in the desired CWD.

## Settings

My `~/.claude/settings.json` at the time of this post:

```json
{
  "env": {
    "CLAUDE_CODE_ENABLE_TELEMETRY": "0"
  },
  "permissions": {
    "allow": [
      "Bash(ansible-doc:*)",
      "Bash(command -v:*)",
      "Bash(fd:*)",
      "Bash(find:*)",
      "Bash(gh pr diff:*)",
      "Bash(gh pr list:*)",
      "Bash(gh pr review-comment list:*)",
      "Bash(gh pr view:*)",
      "Bash(grep:*)",
      "Bash(hadolint:*)",
      "Bash(helm template:*)",
      "Bash(ls:*)",
      "Bash(rg:*)",
      "Bash(yamllint:*)"
    ]
  },
  "statusLine": {
    "type": "command",
    "command": "bash ~/.claude/statusline.sh"
  },
  "alwaysThinkingEnabled": false
}%
```

- no telemetry (privacy!)
- allow a couple of often used tools (utilities), especially read-only ones
- add a simple status line; originally scaffolded with `/statusline`
- do not always think (it's slow & expensive!)

`settings.json` and `statusline.sh` are both in my
[dotfiles](https://github.com/thiagowfx/.dotfiles).
