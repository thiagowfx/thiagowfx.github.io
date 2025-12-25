---
title: "git: configure identities for work"
date: 2025-01-01T17:22:05-03:00
tags:
  - bestof
  - dev
---

**Problem statement**: Given two sets of git configurations, one for personal
projects and one for work, how can you effectively separate them?

## Workflow

I like the following workflow.

First, create your usual `~/.gitconfig`. It will be used for your personal
project:

```ini
[user]
        name = Thiago Perrotta
        email = {personal-email}

[...]

# Import corp configs if any.
[include]
        path = .gitconfig_corp
```

This config should live in your personal laptop and in your work laptop.

Normally I include it via my [.dotfiles](https://github.com/thiagowfx/.dotfiles)
(git repo) i.e. with a simple `stow git` away.

And we are done with our personal laptop.

Now, for the work laptop, create `~/.gitconfig_corp`:

```ini
[includeIf "gitdir:~/Orgname/**"]
  path = .gitconfig_orgname

[includeIf "hasconfig:remote.*.url:git@github.com:orgname/**"]
  path = .gitconfig_orgname

# vim: ft=gitconfig
```

The corp config is conditionally included / used in the following scenarios:

1. whenever I am working on a git repository that lives within `~/Orgname`
1. whenever the git remote of the repository I am working on is a git repository
   under the organization `orgname`

This config is usually included via my corp dotfiles (named `.dotfiles_corp` in
`git`), which is a separate git repository. There's no fiddling with git
submodules: both git repositories are cloned and managed independently.

And now, last but not least, is the actual git config for work:

```ini
% cat ~/.gitconfig_orgname
[user]
        name = Thiago Perrotta
        email = {work-email}

# vim: ft=gitconfig
```

Inspired by [benji.dog](https://www.benji.dog/articles/git-config/).
