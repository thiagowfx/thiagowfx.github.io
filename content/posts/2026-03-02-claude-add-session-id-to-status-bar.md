---
title: "claude: add session ID to status bar"
date: 2026-03-02T11:18:19+01:00
tags:
  - ai
  - bestof
  - dev
---

Desired outcome:

```
❯ claude

 ▐▛███▜▌   Claude Code v2.1.63
▝▜█████▛▘  Opus 4.6 · Claude Team
  ▘▘ ▝▝    ~/.dotfiles

──────────────────────────────────────────────────────────
❯
──────────────────────────────────────────────────────────
  .dotfiles (git:master*) [Opus 4.6] $0.00 sid:9afc33ee-610d-47cc-8bde-1a52d1b22832
```

The status bar displays the current:

- git repository we're on
- git branch
- model name
- session cost (in USD)
- session ID

I recently added the last two items, and the post title reflects that.

The session cost is helpful as a pat on the shoulder to remind you of how
expensive Anthropic models are. If you want to put a cap on the session,
`--max-budget-usd` could be helpful:

```
--max-budget-usd <amount>		Maximum dollar amount to spend on API calls (only works with --print)
```

The session ID is, by itself, useless. It is just a boring UUID, auto-generated
whenever a new session is started.

That said, the session ID can become powerful when you start to treat sessions
as first-class citizens (e.g. like how [Amp Code](https://ampcode.com/) does to
threads).

## Use cases

**Use case #1**: resume a previous session.

```shell
claude [-r | --resume] <uuid>
```

```
-r, --resume [value]		Resume a conversation by session ID, or open interactive picker with optional search term
```

This is useful whenever you know in advance you'll need to close your terminal
(e.g. to restart your computer for system upgrades).

**Use case #2**: multiple divergent explorations.

```shell
claude --fork-session [-r | --resume | -c | --continue] <uuid>
```

```
--fork-session				 When resuming, create a new session ID instead of reusing the original (use with --resume or --continue)
```

Whenever you reach a point of ambiguity when vibe coding, you may want to
explore multiple paths. `--fork-session` creates new sessions from an existing
context window (session ID), allowing you to preserve your original session
context.

**Use case #3**: refer to other sessions.

Sample prompt:

```
let's continue work from sid:484b8360-b5ee-4a47-9137-f45c00ff2dc0

this foo path is too slow, make it faster by activating the infinite
improbability module
```

## The config

The resulting diff:

```diff
thiago.perrotta ~/.dotfiles git:master
❯ git --no-pager show 0f94082
commit 0f9408223c60dcda980c18787d3d0c1519428c30
Author: Thiago Perrotta <{redacted}>
Date:   Fri Feb 27 16:56:57 2026 +0100

    claude: status bar: add session ID, add cost

diff --git claude/.claude/statusline.sh claude/.claude/statusline.sh
old mode 100644
new mode 100755
index 785b5f3..f43527a
--- claude/.claude/statusline.sh
+++ claude/.claude/statusline.sh
@@ -5,8 +5,10 @@ input=$(cat)

 # Extract information from JSON
 model_name=$(echo "$input" | jq -r '.model.display_name')
+session_id=$(echo "$input" | jq -r '.session_id')
 current_dir=$(echo "$input" | jq -r '.workspace.current_dir')
 output_style=$(echo "$input" | jq -r '.output_style.name')
+cost=$(echo "$input" | jq -r '.cost.total_cost_usd')

 # Get current working directory basename
 dir_name=$(basename "$current_dir")
@@ -87,5 +89,15 @@ if [[ -n "$context_info" ]]; then
     status_parts+=("$context_info")
 fi

+# Add cost
+if [[ -n "$cost" && "$cost" != "null" ]]; then
+    status_parts+=("$(printf '$%.2f' "$cost")")
+fi
+
+# Add session ID
+if [[ -n "$session_id" && "$session_id" != "null" ]]; then
+    status_parts+=("sid:$session_id")
+fi
+
 # Join parts with spaces and print
 printf "%s" "$(IFS=' '; echo "${status_parts[*]}")"
```

The full [status line
config](https://github.com/thiagowfx/.dotfiles/blob/b44959f6d0b916d983d2970528c6aa67288b9f45/claude/.claude/statusline.sh).
I'll inline it here for completeness:

```shell
#!/bin/bash

# Read JSON input from stdin
input=$(cat)

# Extract information from JSON
model_name=$(echo "$input" | jq -r '.model.display_name')
session_id=$(echo "$input" | jq -r '.session_id')
current_dir=$(echo "$input" | jq -r '.workspace.current_dir')
output_style=$(echo "$input" | jq -r '.output_style.name')
cost=$(echo "$input" | jq -r '.cost.total_cost_usd')

# Get current working directory basename
dir_name=$(basename "$current_dir")

# Get git information if in a git repository
git_info=""
if git rev-parse --git-dir > /dev/null 2>&1; then
    branch=$(git branch --show-current 2>/dev/null)
    if [[ -n "$branch" ]]; then
        # Check for uncommitted changes
        if ! git diff --quiet 2>/dev/null || ! git diff --cached --quiet 2>/dev/null; then
            dirty="*"
        else
            dirty=""
        fi

        # Check if in a linked worktree (not the main worktree)
        worktree_info=""
        git_dir=$(cd "$(git rev-parse --git-dir 2>/dev/null)" && pwd)
        git_common_dir=$(cd "$(git rev-parse --git-common-dir 2>/dev/null)" && pwd)
        if [[ "$git_dir" != "$git_common_dir" ]]; then
            # We're in a linked worktree - show its name
            worktree_path=$(git rev-parse --show-toplevel 2>/dev/null)
            worktree_name=$(basename "$worktree_path")
            worktree_info=" ⎇ $worktree_name"
        fi

        git_info="(git:$branch$worktree_info$dirty)"
    fi
fi

# Calculate context window usage (relative to auto-compact threshold ~80%)
context_info=""
usage=$(echo "$input" | jq '.context_window.current_usage')
if [ "$usage" != "null" ]; then
    # Include output_tokens for accurate context measurement
    current=$(echo "$usage" | jq '.input_tokens + .output_tokens + .cache_creation_input_tokens + .cache_read_input_tokens')
    size=$(echo "$input" | jq '.context_window.context_window_size')

    # Auto-compact triggers at ~80% of context window
    compact_threshold=$((size * 80 / 100))

    # Calculate percentage toward auto-compact (capped at 100%)
    pct=$((current * 100 / compact_threshold))
    if [ "$pct" -gt 100 ]; then pct=100; fi

    # Create progress bar (5 characters wide)
    filled=$((pct / 20))
    empty=$((5 - filled))
    bar=""
    for ((i=0; i<filled; i++)); do bar+="█"; done
    for ((i=0; i<empty; i++)); do bar+="░"; done

    context_info="[${bar}]"
fi

# Build status line
status_parts=()

# Add current directory
status_parts+=("$dir_name")

# Add git info if available
if [[ -n "$git_info" ]]; then
    status_parts+=("$git_info")
fi

# Add model name
status_parts+=("[$model_name]")

# Add output style if not default
if [[ "$output_style" != "default" && "$output_style" != "null" ]]; then
    status_parts+=("{$output_style}")
fi

# Add context usage if available
if [[ -n "$context_info" ]]; then
    status_parts+=("$context_info")
fi

# Add cost
if [[ -n "$cost" && "$cost" != "null" ]]; then
    status_parts+=("$(printf '$%.2f' "$cost")")
fi

# Add session ID
if [[ -n "$session_id" && "$session_id" != "null" ]]; then
    status_parts+=("sid:$session_id")
fi

# Join parts with spaces and print
printf "%s" "$(IFS=' '; echo "${status_parts[*]}")"
```
