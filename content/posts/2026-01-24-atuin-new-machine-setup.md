---
title: "atuin: new machine setup"
date: 2026-01-24T18:46:02+01:00
tags:
  - dev
  - selfhosted
---

[Previously]({{< ref "2025-11-30-atuin" >}}).

**Problem statement**: you're already using `atuin`, and have sync configured.
You just got a new machine. Now, configure `atuin` in it.

If you self-host, configure your sync server first:

```shell
$EDITOR ~/.config/atuin/config.toml
# ---
## address of the sync server
# sync_address = "https://api.atuin.sh"
sync_address = "https://{your-server-here}"
```

Then log in to your server:

```shell
atuin login --username {username}
<type in password>
```

You can also provide the password with the `--password` switch, but keep in mind
it will be logged to your shell history unless you take precautions.

The next step is to import your current history into atuin. If this is a
fresh new machine then there's no need to do so.

If you had been using it for a while but didn't set up `atuin` from the
beginning, go on:

```shell
atuin import auto
```

Finally, sync it once:

```shell
atuin sync
```

Syncing happens automatically, but it's sensible to manually kick-off the
initial sync upfront.

_Fin_.
