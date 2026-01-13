---
title: "git aicommit"
date: 2026-01-13T15:58:48-03:00
tags:
  - ai
  - dev
  - git
---

**Problem statement**: auto-generate a commit message for `git` from the
command-line. The solution should be vendor agnostic.

Given a `git-foo.sh` in `$PATH`, it can be invoked as `git foo`, as if it
were a built-in `git` command.

This is helpful to enable seamless integration with `git`. I chose to call the
subcommand `aicommit`. I suppose `commit-ai` would also be sensible.

The goal is to create `git-aicommit.sh` in `~/.bin` (which is in my `$PATH` via
my `[.dotfiles](https://github.com/thiagowfx/.dotfiles/blob/018c50ebd86b70b30578d4a1393054fd04bd4553/profile/.profilerc#L42)`)

This initial draft worked well:

```shell
#!/bin/bash
#
# git-aicommit - Create a commit with an AI-generated title based on staged changes

set -e

# Check if we're inside a git repository
if [ "$(git rev-parse --is-inside-work-tree 2>/dev/null)" != "true" ]; then
  echo "Error: Not in a git repository"
  exit 1
fi

# Check if there are staged changes
if git diff --cached --quiet; then
  echo "Error: No staged changes to commit"
  exit 1
fi

# Select AI agent (default: claude)
agent="${GIT_AI_AGENT:-claude}"
case "$agent" in
  # keep-sorted start
  amp|ampcode)
    ai_prompt() { amp -x "$1"; }
    ;;
  claude)
    ai_prompt() { claude -p "$1"; }
    ;;
  # keep-sorted end
  *)
    echo "Error: Unknown AI agent: $agent"
    exit 1
    ;;
esac

prompt="Look at the staged git changes and create a summarizing git commit title. Only respond with the title and no affirmation."

# Generate commit message and commit
echo "Generating commit message with $agent..."
git commit -m "$(ai_prompt "$prompt")" "$@"

echo "AI commit created successfully"
```

Refer to [this
source](https://github.com/thiagowfx/.dotfiles/blob/master/git/.bin/git-aicommit-quick)
for an up-to-date version as it evolves.

Let's break it down:

* [Previously]({{< ref "2026-01-03-oneshot-prompting" >}}): we employ an
  oneshot command to call an LLM agent, so that there's no need to do it
  interactively. Initially I added only Claude Code and Amp because they are the
  agents I use the most; perhaps this list will be expanded later on but it is
  not intended to be exhaustive[^1].
* The command is intended to run in O(seconds). If it takes too long, then it
  should be simplified (via a better prompt).
* By default it uses Claude. To use another agent, call it like:

```shell
GIT_AI_AGENT="amp" git aicommit
```

This preference could be trivially made persistent on a per-repo basis by using
[direnv]({{< ref "2022-01-04-direnv-automate-your-environment-variables" >}}).
For example, use Claude at work and Amp in personal git repositories[^2].

Later on I split the command into two: `git aicommit` and `git aicommit-quick`.
"Quick" populates the commit message title only (think `git commit -m "foo"`),
whereas the non-quick version populates the body as well, accounting for [GitHub
PR
templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository)
when they exist. Time will tell whether I need this distinction.

[^1]: This gives me the idea to create a separate script for "oneshotting" LLMs
    in [pancake](https://github.com/thiagowfx/pancake).

[^2]: [It's all Claude anyway](https://ampcode.com/news/opus-4.5), this
    distinction is mostly for the sake of discretionary billing.
