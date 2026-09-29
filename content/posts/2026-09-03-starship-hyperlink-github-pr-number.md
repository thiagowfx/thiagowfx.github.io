---
title: "starship: hyperlink github PR number"
date: 2026-09-03T14:02:52+02:00
tags:
  - bloggify
  - dev
  - git
---

[Previously]({{< ref "2026-01-30-starship-github-pr" >}}).

**Problem statement**: the GitHub PR number in my Starship prompt was plain
text.

The custom module already asked `gh` for the PR number and cached it with
[`bkt`]({{< ref "2024-12-29-bkt-cache-command-outputs" >}}):

```toml
[custom.github_pr]
command = "bkt --ttl=10m --scope=\"$(git rev-parse --show-toplevel):$(git branch --show-current)\" -- gh pr view --json number --jq '\"#\" + (.number | tostring)' 2>/dev/null"
when = "git rev-parse --is-inside-work-tree 2>/dev/null"
format = " [$output](magenta)"
ignore_timeout = true
```

An OSC 8 escape sequence can turn `#78` into a terminal hyperlink. I first used
`ESC \` to terminate each sequence. The template produced the expected bytes,
but zsh prompt expansion consumed each backslash and left an incomplete escape
sequence:

```text
missing hyperlink sequence; output=b'...\x1b]8;;https://github.com/thiagowfx/.dotfiles/pull/78\x1b#78\x1b]8;;\x1b...'
```

BEL terminates OSC 8 without passing a backslash through zsh:

```diff
diff --git starship/.config/starship.toml starship/.config/starship.toml
index 87e83794..739ee62f 100644
--- starship/.config/starship.toml
+++ starship/.config/starship.toml
@@ -54,7 +54,7 @@ format = " [⎇ $output]($style)"
 style = "bold yellow"

 [custom.github_pr]
-command = "bkt --ttl=10m --scope=\"$(git rev-parse --show-toplevel):$(git branch --show-current)\" -- gh pr view --json number --jq '\"#\" + (.number | tostring)' 2>/dev/null"
+command = "bkt --ttl=10m --scope=\"$(git rev-parse --show-toplevel):$(git branch --show-current)\" -- gh pr view --json number,url --template '{{printf \"\\033]8;;%s\\007#%v\\033]8;;\\007\" .url .number}}' 2>/dev/null"
 when = "git rev-parse --is-inside-work-tree 2>/dev/null"
 format = " [$output](magenta)"
 ignore_timeout = true
```

I tested the full Starship-to-zsh path against the branch for
[PR #78](https://github.com/thiagowfx/.dotfiles/pull/78):

```shell
% tmp=$(mktemp -d)
% git -C "$tmp" init -q
% git -C "$tmp" remote add origin https://github.com/thiagowfx/.dotfiles.git
% git -C "$tmp" switch -q -c renovate/web-tree-sitter-0.x
% (cd "$tmp" && STARSHIP_SHELL=zsh starship prompt) |
    zsh -c 'prompt=$(cat); print -nP -- "$prompt"' |
    python3 -c 'import sys
out = sys.stdin.buffer.read()
expected = b"\x1b]8;;https://github.com/thiagowfx/.dotfiles/pull/78\x07#78\x1b]8;;\x07"
assert expected in out
print("PASS: zsh-rendered Starship prompt links #78 to PR URL")'
PASS: zsh-rendered Starship prompt links #78 to PR URL
```

`Cmd` + click on the number now opens the PR in Ghostty.

That test covered zsh only. Bash exposed a prompt alignment bug two weeks later.
Text from the command line appeared at the right edge and before the prompt.

Starship did not mark the complete OSC 8 sequence as non-printing for Bash:

```text
\[\x1b]8;;https://github.com\]/[redacted]/[redacted]/pull/7163\x07#7163\[\x1b]8;;\x07
```

Only `ESC ] 8 ;; https://github.com` was inside Readline's `\[` and `\]`
markers. Bash counted the remaining URL as visible prompt text, so its cursor
position was wrong.

I reverted the hyperlink:

```diff
 [custom.github_pr]
-command = "bkt --ttl=10m --scope=\"$(git rev-parse --show-toplevel):$(git branch --show-current)\" -- gh pr view --json number,url --template '{{printf \"\\033]8;;%s\\007#%v\\033]8;;\\007\" .url .number}}' 2>/dev/null"
+command = "bkt --ttl=10m --scope=\"$(git rev-parse --show-toplevel):$(git branch --show-current)\" -- gh pr view --json number --jq '\"#\" + (.number | tostring)' 2>/dev/null"
 when = "git rev-parse --is-inside-work-tree 2>/dev/null"
 format = " [$output](magenta)"
 ignore_timeout = true
```

The PR number is plain text again. The Bash prompt now stays aligned.

- - -

🤖 *Drafted with [`/bloggify`](https://github.com/thiagowfx/skills/blob/master/plugins/thiagowfx/skills/bloggify/SKILL.md).*
