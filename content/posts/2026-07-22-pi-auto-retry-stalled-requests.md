---
title: "pi: auto-retry stalled requests"
date: 2026-07-22T13:45:41+02:00
tags:
  - ai
  - coding
  - dev
---

[Previously]({{< ref "2026-07-22-pi-cycle-models-backward" >}}).

**Problem statement**: sometimes a prompt in [pi](https://github.com/earendil-works/pi)
just hangs, as if the network dropped. It never recovers on its own — I have to
hit `Esc` and re-prompt.

It's 2026, this symptom should be self-recoverable.

Pi already has agent-level retry on transient errors (`retry.enabled` defaults
to `true`). The catch is _when_ it fires: a stalled connection isn't an error
until the HTTP idle timeout trips, and that defaults to five minutes:

> `httpIdleTimeoutMs` | number | `300000` | HTTP header/body idle timeout in
> milliseconds [...] Set to `0` to disable.

So pi would have _eventually_ recovered. I was just quitting long before the
five-minute clock ran out. Who has patience to wait for **5** minutes?!

:∴ Lower the idle timeout to O(seconds) instead:

```json
{
  "httpIdleTimeoutMs": 30000,
  "retry": {
    "enabled": true,
    "maxRetries": 5,
    "baseDelayMs": 2000
  }
}
```

Dropped into [`~/.pi/agent/settings.json`](https://github.com/thiagowfx/.dotfiles/commit/aae17ba8d7546901820d7474136a628b16d5feee), documented in
[`docs/settings.md`](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/settings.md).
Now a stall errors out after 30s and `pi` retries automatically with exponential
backoff (2s, 4s, 8s…), up to five attempts. There's no need for `Esc` nor
re-prompting.

The idle timer resets on every byte received, so long thinking or a slow stream
won't trip it — only a genuinely dead connection will. Restart `pi` for the
change to take effect.

- - -

🤖 *Drafted with `/bloggify`.*
