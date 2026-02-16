---
title: "Using keep-sorted to keep your ~/.gitconfig tidy"
date: 2025-03-06T22:53:23+01:00
tags:
  - bestof
  - dev
  - git
  - pre-commit
---

I tend to sort my
[`~/.gitconfig`](https://github.com/thiagowfx/.dotfiles/blob/master/git/.gitconfig)
headings to keep the config tidy.

An example:

```ini
[...]
# https://git-scm.com/docs/git-rerere
[rerere]
	autoUpdate = true
	enabled = true

[status]
	# Show individual files in untracked directories.
	showUntrackedFiles = all
	short = true
	branch = true

[submodule]
	# Clone new submodules in parallel with as many jobs.
	fetchJobs = 0
[...]
```

This was done manually. Until...today.

It has just occurred to me[^1] I could use
[keep-sorted](https://github.com/google/keep-sorted) with the headings.

> Previously:
>
> — [keep-sorted]({{< ref "2024-12-26-keep-sorted" >}})
> — [pre-commit]({{< ref "2024-12-21-pre-commit" >}})

But...how?!

The usage to sort, say, aliases, is quite straightforward[^2]:

```
[alias]
	# keep-sorted begin
	bd = !branch="$(git branch --show-current)" && git default && git branch -D "${branch:-$1}"
	blank = desc -m \"blank commit\"
	cm = commit
	co = checkout
	cp = cherry-pick
	dc = diff --cached
	default = !git checkout main &>/dev/null || git checkout master
	desc = commit --allow-empty -n
	emerge = !git add -A . && git amend -n && git pushm --force-with-lease
	nb = switch --create
        [...]
	# keep-sorted finish
```

How can you apply the same technique to headings?

The out-of-the-box utilization is OK-ish, but not great:

From:

```ini
# keep-sorted begin
[fetch]
	prune = true

[help]
	autocorrect = 10

[format]
	# Automatically sign-off patches when using format-patch.
	signoff = true
# keep-sorted finish
```

To:

```ini
# keep-sorted start

[fetch]
	prune = true
[format]
	# Automatically sign-off patches when using format-patch.
	signoff = true
[help]
	autocorrect = 10
# keep-sorted end
```

(including the blank line at the top)

It turns out all we have to do is a little bit of tweaking:

```ini
# keep-sorted begin block=yes newline_separated=yes
[fetch]
	prune = true

[help]
	autocorrect = 10

[format]
	# Automatically sign-off patches when using format-patch.
	signoff = true
# keep-sorted finish
```

...which then becomes:

```ini
# keep-sorted begin block=yes newline_separated=yes
[fetch]
	prune = true

[format]
	# Automatically sign-off patches when using format-patch.
	signoff = true

[help]
	autocorrect = 10
# keep-sorted finish
```

How nice!

[^1]: Can you even imagine? Having original ideas? In 2025? Without LLMs?! Is
    this even real??

[^2]: I replaced `start -> begin` and `end -> finish` otherwise `keep-sorted`
    would sort this blog post itself. If you copy and paste this example,
    remember to change the words back to the original ones.
