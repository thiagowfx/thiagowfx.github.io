---
title: "myrepos: a wip action to find unfinished work"
url: https://perrotta.dev/2026/07/myrepos-a-wip-action-to-find-unfinished-work/
last_updated: 2026-07-17
---


[Previously]({{< ref "2026-03-26-mr-update" >}}).

**Problem statement**: I manage a few dozen repos via
[myrepos](https://myrepos.branchable.com/) (`mr`), and I wanted a single command
to show which ones have work in progress ("WIP") — uncommitted changes, dirty
staging area, stray branches and alike.

I want essentially a filtered version of `mr ls`.

So I defined my own command. A repo is *not* WIP when all three hold:

- the default branch is checked out;
- no other local branches exist;
- and the working tree is fully clean.

Anything else gets flagged with a reason.

[The definition](https://github.com/thiagowfx/.dotfiles/blob/28376040a292a9898cca59f8ce27de81482d1a26/mr/.mrconfig.defaults#L14-L23):

```ini
# List repos with work in progress: not on default branch, extra local branches, or dirty tree.
# Run as `mr -m wip`: the -m (minimal) flag drops mr's per-repo "mr wip:" header and blank
# lines, leaving only the flagged repos. This cannot be defaulted per-action (mr only honors
# -m/-q as CLI flags, not via config).
wip =
 reasons=""
 cur=$(git symbolic-ref --quiet --short HEAD 2>/dev/null || echo "(detached)")
 def=$(git symbolic-ref --quiet --short refs/remotes/origin/HEAD 2>/dev/null | sed 's|^origin/||')
 if [ -z "$def" ]; then if git show-ref --verify --quiet refs/heads/main; then def=main; elif git show-ref --verify --quiet refs/heads/master; then def=master; fi; fi
 if [ -n "$def" ] && [ "$cur" != "$def" ]; then reasons="$reasons branch:$cur"; fi
 n=$(git for-each-ref --format='%(refname)' refs/heads | wc -l | tr -d ' ')
 if [ "$n" -gt 1 ]; then reasons="$reasons +$((n-1))_branches"; fi
 if [ -n "$(git status --porcelain)" ]; then reasons="$reasons dirty"; fi
 if [ -n "$reasons" ]; then printf '%s [%s]\n' "$MR_REPO" "${reasons# }"; fi
```

Naturally, the snippet above is art from the LLM, but it accomplishes exactly
what I want:

```shell
thiago.perrotta ~
% mr -m wip
mr wip: /Users/thiago.perrotta/Corp/gitops
/Users/thiago.perrotta/Corp/gitops [branch:thiagowfx/acme +1_branches]

mr wip: /Users/thiago.perrotta/Corp/terraform
/Users/thiago.perrotta/Corp/terraform [+1_branches]

mr wip: /Users/thiago.perrotta/workspace/perrotta.dev
/Users/thiago.perrotta/workspace/perrotta.dev [+3_branches dirty]
```

Clean repos stay silent. I get to see all repos with unfinished work, and I can
see exactly why each one is dirty.

`mr wip` works too but it's noisier. I need to add `mr -m wip` to my muscle
memory[^1]. Without the `-m` flag, `mr` prepends a `mr wip:` header and a blank
line for *every* repo, WIP or not.

`-m` can't be baked into the action definition — `mr` only honors it as a CLI
flag — so the comment above the action documents it.

[^1]: Should I rely on this workflow more often, I could leverage [Espanso]({{< ref "2025-05-16-espanso-hello-world" >}}) or a
    shell alias/function to easen its recall.

Previously I'd run `mr xl` (an alias for `git branch -vv` across every repo) and
eyeball the result — but that's dozens of lines of branch tips for tens of
repos, and I still have to scan for the ones that are actually behind or dirty.
`wip` does the scanning: it only prints the repos that need attention, with the
reason attached. Much more ergonomic than visually diffing a wall of green.

Runs read-only, so it's safe to run twice.

- - -

🤖 *Drafted with `/bloggify`.*

