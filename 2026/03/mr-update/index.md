---
title: "mr update"
url: https://perrotta.dev/2026/03/mr-update/
last_updated: 2026-03-26
---


Every day at the office, I start my day with `mr update`:

```shell
% mr update
[...]
mr update: /Users/thiago.perrotta/workspace/adventofcode
Already up to date.

mr update: /Users/thiago.perrotta/workspace/check-json-schema-meta
Already up to date.

mr update: /Users/thiago.perrotta/workspace/homebrew-taps
Already up to date.

mr update: /Users/thiago.perrotta/workspace/pre-commit-hooks
Already up to date.

mr update: /Users/thiago.perrotta/workspace/pancake
Already up to date.
[...]
```

`mr` is short for [myrepos](https://myrepos.branchable.com/):

> You have a lot of version control repositories. Sometimes you want to update
> them all at once. Or push out all your local changes. You use special command
> lines in some repositories to implement specific workflows. Myrepos provides a
> mr command, which is a tool to manage all your version control repositories.

`mr` is a single tool to control multiple DVCSes at once — typically `git`, but
others are also supported:

> All you need to get started is some already checked out repos. These could be
> using git, or bzr, mercurial or darcs, or many other version control systems.
> Doesn't matter, they're all supported!

The example output above was lame because nothing changed — they're my personal
repositories. In the git repositories of my workplace there are typically
various changes to be absorbed every day.

How do we achieve this?

Refer to its [man page](https://man.archlinux.org/man/mr.1) for the config
format. [My config](https://github.com/thiagowfx/.dotfiles/blob/3252e552a8a33c001ea32f82b1f73e59f3a3fabf/mr/.mrconfig):

```conf {filename="~/.mrconfig"}
# vim: ft=conf

include = cat ~/.mrconfig.defaults

[.dotfiles]
checkout = git clone 'git@github.com:thiagowfx/.dotfiles.git' '.dotfiles'

[.dotfiles_corp]
checkout = git clone 'git@github.com:thiagowfx/.dotfiles_corp.git' '.dotfiles_corp'
skip = lazy

[workspace/adventofcode]
checkout = git clone 'git@github.com:thiagowfx/adventofcode' 'adventofcode'
skip = lazy

[workspace/check-json-schema-meta]
checkout = git clone 'git@github.com:thiagowfx/check-json-schema-meta' 'check-json-schema-meta'
skip = lazy

[workspace/aports]
checkout = git clone 'git@gitlab.alpinelinux.org:thiagowfx/aports.git' 'aports'
skip = lazy
update = git pull upstream master

[workspace/homebrew-taps]
checkout = git clone 'git@github.com:thiagowfx/homebrew-taps' 'homebrew-taps'
skip = lazy

[workspace/pancake]
checkout = git clone 'git@github.com:thiagowfx/pancake' 'pancake'
skip = lazy

[workspace/perrotta.dev]
checkout = git clone 'git@github.com:thiagowfx/thiagowfx.github.io.git' 'perrotta.dev'
skip = lazy

[workspace/pre-commit-hooks]
checkout = git clone 'git@github.com:thiagowfx/pre-commit-hooks' 'pre-commit-hooks'
skip = lazy
```

```conf {filename="~/.mrconfig.defaults"}
# vim: ft=conf

[ALIAS]
pull = update

[DEFAULT]
git_xl = git xl "$@"
jobs = 6
```

