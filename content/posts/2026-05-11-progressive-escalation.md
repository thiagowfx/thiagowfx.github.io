---
title: "Progressive escalation"
date: 2026-05-11T17:56:02+02:00
tags:
  - dev
  - serenity
---

A pattern I keep stumbling upon: start with the gentlest (softest?) action, then
**escalate** _only when_ it didn't properly go through:

- **Killing processes.** Start with `SIGINT`. Then `SIGTERM`. Finally `SIGKILL`.
  [`murder(1)`](https://github.com/thiagowfx/pancake/tree/master/murder)
  encapsulates that.

- **ArgoCD syncing.** Start with a normal sync. Then sync with server-side
  apply. Next, sync with `--force`. Finally, sync with `--replace`.

- **Business negotiations.** Start with a reasonable offer. Then converge, little by
  little. If that fails, walk away.

- **Connectivity issues.** Turn the Wi-Fi off and on again. Next, connect to
  another Wi-Fi hotspot and then back to the desired one. Finally, completely
  reboot your device. No luck yet? Then reboot the router.

Different domains, same shape: cheap and _reversible_ first, slowly converting
to (more) expensive and "more" irreversible last.
