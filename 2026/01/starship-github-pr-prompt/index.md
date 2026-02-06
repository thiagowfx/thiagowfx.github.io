
[Previously]({{< ref "2025-12-27-starship" >}}).

**Problem statement**: add to [starship](https://starship.rs/) the GitHub PR
associated with the current git branch.

The following starship custom module does the trick:

```
[custom.github_pr]
command = "bkt --ttl=10m --scope=\"$(git rev-parse --show-toplevel):$(git branch --show-current)\" -- gh pr view --json number --jq '\"#\" + (.number | tostring)' 2>/dev/null"
when = "git rev-parse --is-inside-work-tree 2>/dev/null"
format = " [$output](magenta)"
ignore_timeout = true
```

The module is activated only within git repositories (see the `when` variable).

The `command` consists of the `gh` CLI, as you would expect. There's one major
problem: it makes a network call on every prompt. This is super inefficient.
Can't do.

That's why we use [`bkt`]({{< ref "2024-12-29-bkt-cache-command-outputs" >}}):
it caches the PR info for a certain amount of time (10 minutes in the
aforementioned example), which makes this a feasible prompt.

The full prompt (without colors) looks roughly like this:

```
thiago.perrotta ~/.dotfiles git:master! ⎇ #466
❯
```

The full git commit that implements and uses it:

```shell
% git --no-pager show
commit d2a80f6b8edfa6a07204a1d97b278abacba57813 (HEAD -> master)
Author: Thiago Perrotta <{redacted}>
Date:   Fri Jan 30 00:55:02 2026 +0100

    starship: add github pr

diff --git starship/.config/starship.toml starship/.config/starship.toml
index 2c5e78e..9fbf19b 100644
--- starship/.config/starship.toml
+++ starship/.config/starship.toml
@@ -1,5 +1,5 @@
 # Minimal starship config matching grml prompt
-format = "$status$sudo$username$hostname$directory$git_branch$git_state$git_status${custom.git_worktree}$line_break$character"
+format = "$status$sudo$username$hostname$directory$git_branch$git_state$git_status${custom.git_worktree}${custom.github_pr}$line_break$character"
 right_format = "$cmd_duration$jobs"
 add_newline = true

@@ -52,3 +52,9 @@ command = "printf '⎇'"
 when = "[ -f .git ]"
 format = " [$output]($style)"
 style = "bold yellow"
+
+[custom.github_pr]
+command = "bkt --ttl=10m --scope=\"$(git rev-parse --show-toplevel):$(git branch --show-current)\" -- gh pr view --json number --jq '\"#\" + (.number | tostring)' 2>/dev/null"
+when = "git rev-parse --is-inside-work-tree 2>/dev/null"
+format = " [$output](magenta)"
+ignore_timeout = true
```

