---
title: "Homebrew conflicts"
date: 2026-05-21T15:32:45+02:00
tags:
  - ai
  - dev
  - macos
---

I wanted to try out [`worktrunk`](https://worktrunk.dev/):

```shell
thiago.perrotta ~
% brew install worktrunk
==> Auto-updating Homebrew...
==> Fetching downloads for: worktrunk
==> Pouring worktrunk--0.52.0.arm64_tahoe.bottle.tar.gz
Error: The `brew link` step did not complete successfully
The formula built, but is not symlinked into /opt/homebrew
Could not symlink bin/wt
Target /opt/homebrew/bin/wt
is a symlink belonging to pancake. You can unlink it:
  brew unlink pancake

To force the link and overwrite all conflicting files:
  brew link --overwrite worktrunk

To list all files that would be deleted:
  brew link --overwrite worktrunk --dry-run

Possible conflicting files are:
/opt/homebrew/bin/wt -> /opt/homebrew/Cellar/pancake/2026.05.07.0/bin/wt
==> Caveats
The following worktrunk executables are shadowed by other commands earlier in your PATH:
  wt (shadowed by /opt/homebrew/bin/wt)
Running these by name will not invoke the version provided by Homebrew.
==> Summary
🍺  /opt/homebrew/Cellar/worktrunk/0.52.0: 12 files, 16.5MB
==> Running `brew cleanup worktrunk`...
==> Caveats
zsh completions have been installed to:
  /opt/homebrew/share/zsh/site-functions
brew install worktrunk  4.12s user 1.21s system 32% cpu 16.417 total
```

...however its `wt` binary conflicts with my
[`wt`](https://github.com/thiagowfx/pancake/tree/master/wt) tool from
[pancake](https://github.com/thiagowfx/pancake/). Booo!

Workaround? A symlink:

```shell
% ln -s /opt/homebrew/Cellar/worktrunk/0.52.0/bin/wt /opt/homebrew/bin/wtr
```

I will refer to it as `mtr` during evaluation.

This is not a proper long-term fix, it's really just a band-aid.

I am more inclined to rename my `wt` for the sake of avoiding conflict should
`worktrunk` stick to daily workflow.

In these moments I miss the flexibility of
[`portage`](https://wiki.gentoo.org/wiki/Portage).
