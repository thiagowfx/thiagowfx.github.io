---
title: "git: shell prompt: worktrees"
date: 2026-01-10T15:15:21-03:00
tags:
  - ai
  - dev
  - git
---

My shell prompt displays the git branch my repository has
currently checked out:

```
thiago.perrotta perrotta.dev git:master?
❯
```

**Problem statement**: augment that prompt to signal whether we're inside a
checked out [git worktree](https://git-scm.com/docs/git-worktree).

This is helpful because lately multiple repository worktrees have been
popularized thanks to LLM coding agents.

The following change to [starship]({{< ref "2025-12-27-starship" >}}) does the
trick:

```diff
commit b7de6881c0fb57c840def52189502985442842e1
Author: Thiago Perrotta <{redacted}>
Date:   Fri Jan 9 21:18:09 2026 -0300

    starship: add worktree symbol

diff --git starship/.config/starship.toml starship/.config/starship.toml
index 87df9ff..ea7acc8 100644
--- starship/.config/starship.toml
+++ starship/.config/starship.toml
@@ -1,5 +1,5 @@
 # Minimal starship config matching grml prompt
-format = "$status$sudo$username$hostname$directory$git_branch$git_state$git_status$line_break$character"
+format = "$status$sudo$username$hostname$directory$git_branch$git_state$git_status${custom.git_worktree}$line_break$character"
 right_format = "$cmd_duration$jobs"
 add_newline = true

@@ -24,13 +24,13 @@ format = " [$path](bold) "

 [git_branch]
 symbol = "git:"
-format = "[$symbol$branch](bold cyan) "
+format = "[$symbol$branch](bold cyan)"

 [git_state]
 format = "|[$state]()"

 [git_status]
-format = "[$conflicted$deleted$renamed$modified$staged$untracked$ahead_behind](red) "
+format = "[$conflicted$deleted$renamed$modified$staged$untracked$ahead_behind](red)"

 [cmd_duration]
 min_time = 2000
@@ -46,3 +46,9 @@ format = "[🧙](red) "
 [character]
 success_symbol = "[❯](green)"
 error_symbol = "[x](red)"
+
+[custom.git_worktree]
+command = "printf '⎇'"  # or 🌲, but I find the emoji too distracting in this context
+when = "git rev-parse --is-inside-work-tree 2>/dev/null && [ -f $(git rev-parse --git-dir)/commondir ]"
+format = " [$output]($style)"
+style = "bold yellow"
```

You don't need to use starship to adopt it. The core logic is:

```shell
git rev-parse --is-inside-work-tree &>/dev/null && [ -f "$(git rev-parse --git-dir)/commondir" ] && printf '⎇'
```

The result:

```
thiago.perrotta perrotta.dev git:thiagowfx/my-custom-branch ⎇
❯
```

It is subtle yet informative.
