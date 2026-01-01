
Replaced all occurrences of `pipx run` in my projects with `uvx`.

[`uvx docs`](https://docs.astral.sh/uv/guides/tools/):

> The uvx command invokes a tool without installing it.

Perfect for one-off tool executions ("one-shots"). For example:

```shell
% cat ~/.bin/az_switch
#!/bin/sh
# Switch active account in Azure
exec uvx az-account-switcher "$@"
```

