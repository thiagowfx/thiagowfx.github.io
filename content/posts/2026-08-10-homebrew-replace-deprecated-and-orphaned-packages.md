---
title: "homebrew: replace deprecated and orphaned packages"
date: 2026-08-10T15:10:42+02:00
tags:
  - coding
  - dev
  - macos
---

**Problem statement**: `brew doctor` found one deprecated cask and one installed
keg whose formula had disappeared.

## tflint

```text
Warning: Some installed casks are deprecated or disabled.
You should find replacements for the following casks:
flameshot

Warning: Some installed kegs have no formulae!
You should find replacements for the following formulae:
  tflint
```

Homebrew/core [removed TFLint](https://github.com/Homebrew/homebrew-core/commit/6cefefcbba24e4a1093dfd2e189f2cb01170e45f)
after its executable became subject to both MPL 2.0 and BUSL 1.1. Upstream now
maintains [`terraform-linters/tap`](https://github.com/terraform-linters/homebrew-tap)
as a cask, so migrate the old formula instead of merely reinstalling it:

```shell
% brew uninstall tflint
Uninstalling /opt/homebrew/Cellar/tflint/0.61.0... (8 files, 51.8MB)

% brew install terraform-linters/tap/tflint
==> Tapping terraform-linters/tap
Tapped 1 cask (15 files, 14.7KB).
==> Installing Cask tflint
==> Linking Binary 'tflint' to '/opt/homebrew/bin/tflint'
🍺  tflint was successfully installed!

% tflint --version
TFLint version 0.64.0
+ ruleset.terraform (0.15.0-bundled)
```

## Flameshot → Shottr

The [Flameshot cask](https://formulae.brew.sh/cask/flameshot) was deprecated
because it does not pass macOS Gatekeeper checks. I replaced it with
[Shottr](https://shottr.cc/):

```shell
% brew uninstall --cask flameshot
==> Uninstalling Cask flameshot
==> Removing App '/Applications/flameshot.app'
==> Purging files for version 14.0.0,14.0 of Cask flameshot

% brew install --cask shottr
==> Installing Cask shottr
==> Moving App 'Shottr.app' to '/Applications/Shottr.app'
🍺  shottr was successfully installed!
```

The corresponding `Brewfile` [change](https://github.com/thiagowfx/.dotfiles/commit/79cd3dd4eb448d4a3bc5f66a124fd60d3f131d58) keeps the migration reproducible:

```diff
+tap "terraform-linters/tap"

-brew "tflint"

-cask "flameshot"
+cask "shottr"
+cask "tflint"
```

Both offending entries are now gone:

```shell
% brew doctor 2>&1 | grep -E 'flameshot|tflint|deprecated|no formulae'

% brew list --cask | grep -E '^(flameshot|shottr|tflint)$'
shottr
tflint
```

- - -

🤖 *Drafted with [`/bloggify`](https://github.com/thiagowfx/skills/blob/master/plugins/thiagowfx/skills/bloggify/SKILL.md).*
