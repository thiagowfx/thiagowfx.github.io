---
title: "espanso: reload config after editing"
url: https://perrotta.dev/2026/06/espanso-reload-config-after-editing/
last_updated: 2026-06-24
---


[Previously]({{< ref "2025-05-16-espanso-hello-world" >}}).

**Problem statement**: `espanso edit corp` opens a config file, but saving it
doesn't take _immediate_ effect.

At $DAILYJOB I keep a separate match file for work-specific snippets ("corp").
Espanso supports multiple match files under `match/`:

```shell
% espanso edit corp
Editing file: /Users/thiago.perrotta/Library/Application Support/espanso/match/corp.yml
```

After saving, the new trigger doesn't expand. Espanso doesn't auto-reload on
file change.

The intended fix:

```shell
% espanso restart
```

Except that it has timed out:

```
unable to start service: timed out
Hint: sometimes this happens because another Espanso process is left running for some reason.
      Please try running 'espanso restart' or manually killing all Espanso processes, then try again.
```

A stale process was holding the IPC socket lock, so `espanso restart`,
`espanso start`, and even `espanso service start` all timed out — while
`espanso status` cheerfully reported `espanso is not running`. The hint is right,
but its suggested remedy (run `espanso restart` again) doesn't break the cycle.

On macOS, `espanso` runs as a `launchd` service. The reliable escape hatch is to
bounce it through `launchd`, which owns the process:

```shell
% launchctl kickstart -k "gui/$(id -u)/com.federicoterzi.espanso"
```

`-k` kills the existing instance before restarting it. After that, `corp.yml`
expands again.

**Meta**: should I create a trigger for this command? :P

- - -

🤖 *Drafted with `/bloggify`.*

