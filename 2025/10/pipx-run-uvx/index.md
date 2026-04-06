---
title: "pipx run → uvx"
url: https://perrotta.dev/2025/10/pipx-run-uvx/
last_updated: 2026-03-26
---


Replaced all occurrences of `pipx run` in my projects with `uvx`.

[`uvx docs`](https://docs.astral.sh/uv/guides/tools/):

> The uvx command invokes a tool without installing it.

Perfect for one-off tool executions ("one-shots"). For example:

```bash {filename="~/.bin/az_switch"}
#!/bin/sh
# Switch active account in Azure
exec uvx az-account-switcher "$@"
```

