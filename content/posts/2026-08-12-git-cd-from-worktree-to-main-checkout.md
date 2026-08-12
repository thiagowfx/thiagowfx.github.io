---
title: "git: cd from worktree to main checkout"
date: 2026-08-12T17:22:01+02:00
tags:
  - coding
  - dev
  - git
---

[Previously]({{< ref "2024-10-11-cdg" >}}).

**Problem statement**: make my `cdg` shortcut jump from a linked Git worktree
back to the main checkout when already at the worktree root.

The shortcut originally stopped at the current checkout's root:

```shell
alias cdg='cd "$(git root)"'
```

I wanted two consecutive calls from a worktree subdirectory to behave like
the following:

```text
worktree/subdirectory
        ↓ cdg
worktree (at the root)
        ↓ cdg
main checkout (at the root)
```

An alias cannot succinctly express the necessary conditional behavior, whereas
an external script cannot change its parent shell's working directory. A shell
function can:

```shell
cdg() {
	# This file is sourced by bash and zsh, both of which support local.
	# shellcheck disable=SC3043
	local line main_is_bare main_worktree root worktrees

	root=$(git rev-parse --path-format=absolute --show-toplevel) || return

	if [ "$(pwd -P)" != "$root" ]; then
		cd "$root" || return
		return
	fi

	worktrees=$(git worktree list --porcelain) || return
	main_worktree=
	main_is_bare=false
	while IFS= read -r line; do
		case "$line" in
			worktree\ *) main_worktree=${line#worktree } ;;
			bare) main_is_bare=true ;;
			'') break ;;
		esac
	done <<-EOF
	$worktrees
	EOF

	if [ "$main_is_bare" = false ] && [ -n "$main_worktree" ] && [ "$main_worktree" != "$root" ]; then
		cd "$main_worktree" || return
	fi
}
```

The first entry from `git worktree list --porcelain` is the main checkout. At
its root, `cdg` remains a no-op. If that entry is a bare repository, it also
stays put instead of entering the Git directory.
