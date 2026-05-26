---
title: "atuin: global search"
date: 2026-05-26T10:40:39+02:00
tags:
  - dev
  - pkm
---

[Previously]({{< ref "2025-11-30-atuin" >}}).

**Scenario**:

* machine 1, day 1: run a bunch of commands
* machine 2, day 2: I'd like to run a subset of the commands I ran yesterday. If
  only I could remember them! I do not have access to machine 1 at the moment.

Enter [`atuin`](https://atuin.sh/) global search!

Assuming that you set up `atuin` sync in both machines, all you have to do is
this:

* enter machine 2, run `atuin sync` once, manually[^1]:

```shell
thiago.perrotta ~
% atuin sync
Uploading 102 records to 0198c192{redacted}d30370fad/history
  [00:00:00] [##########################] 102/102 (0.0s)3/0 up/down to record store
Sync complete! 105855 items in history database, force: false
```

* press `Cmd-R` (or `Ctrl-R`), ensure the [filter mode](https://docs.atuin.sh/cli/configuration/config/#filter_mode) is set to `global`:

> global (default): Search from the full history

* grep for the desired commands in the interactive TUI that will follow

* profit!

This is peak PKM! It just works™.

[^1]: Or simply _wait_ until it happens in the background automatically.
