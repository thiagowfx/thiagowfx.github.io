---
title: "homebrew: cask receipt drift after an in-app update"
date: 2026-08-16T14:11:17+02:00
tags:
  - bloggify
  - coding
  - dev
  - macos
---

[Previously]({{< ref "2026-08-10-homebrew-replace-deprecated-and-orphaned-packages" >}}).

**Problem statement**: every `brew upgrade` died on a cask whose app had
upgraded itself years ago.

```shell
% brew upgrade
==> Upgrading 1 outdated package:
1password 7.9.2 -> 8.12.33
==> Upgrading 1password
  7.9.2 -> 8.12.33
Error: 1password: It seems the App source '/Applications/1Password 7.app' is not there.
==> Purging files for version 8.12.33 of Cask 1password
```

That path stopped existing when 1Password 8 renamed its bundle from
`1Password 7.app` to `1Password.app`. The app had updated itself in place,
behind Homebrew's back:

```shell
% defaults read /Applications/1Password.app/Contents/Info.plist CFBundleShortVersionString
8.12.30
% brew list --cask --versions 1password
1password 7.9.2
```

Two disagreeing sources of truth. `--adopt` looked like the obvious cure, and
wasn't — the stale receipt still routes into the upgrade code path, which still
looks for the v7 bundle:

```shell
% brew install --cask --adopt 1password
==> Upgrading 1password
  7.9.2 -> 8.12.33
Error: 1password: It seems the App source '/Applications/1Password 7.app' is not there.
```

The receipt is the whole problem, so look at what it actually holds:

```shell
% find /opt/homebrew/Caskroom/1password -maxdepth 2
/opt/homebrew/Caskroom/1password
/opt/homebrew/Caskroom/1password/.metadata
/opt/homebrew/Caskroom/1password/.metadata/config.json
/opt/homebrew/Caskroom/1password/.metadata/7.9.2
/opt/homebrew/Caskroom/1password/7.9.2
% ls -A /opt/homebrew/Caskroom/1password/7.9.2/
% du -sh /opt/homebrew/Caskroom/1password
8.0K	/opt/homebrew/Caskroom/1password
```

Eight kilobytes of bookkeeping and an empty version directory. Nothing in there
is the application. Delete it, then reinstall over the app that is really on
disk:

```shell
% rm -rf /opt/homebrew/Caskroom/1password
% brew install --cask --force 1password
==> Fetching downloads for: 1password
✔︎ Cask 1password (8.12.33)
Warning: It seems there is already an App at '/Applications/1Password.app'; overwriting.
==> Installing Cask 1password
==> Removing App '/Applications/1Password.app'
==> Moving App '1Password.app' to '/Applications/1Password.app'
🍺  1password was successfully installed!
```

Both sides agree again:

```shell
% defaults read /Applications/1Password.app/Contents/Info.plist CFBundleShortVersionString
8.12.33
% brew list --cask --versions 1password
1password 8.12.33
% brew outdated --cask | grep 1password
```

Quitting the app first is mandatory, and this one ignored two polite
`osascript` requests before a plain `kill` took:

```shell
% osascript -e 'quit app "1Password"'
% pgrep -x 1Password
740
% kill 740
```

The general shape: a cask whose app ships its own updater will drift, and
Homebrew only notices when the vendor also renames the bundle. `--adopt` is for
an app Homebrew never tracked; for an app it tracked *wrongly*, the receipt has
to go first.

- - -

🤖 *Drafted with [`/bloggify`](https://github.com/thiagowfx/skills/blob/master/plugins/thiagowfx/skills/bloggify/SKILL.md).*
