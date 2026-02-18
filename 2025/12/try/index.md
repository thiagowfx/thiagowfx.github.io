
Inspired by [`tobi/try`](https://github.com/tobi/try)
([via](https://world.hey.com/dhh/six-billion-reasons-to-cheer-for-shopify-55720846)),
I created my own `try` in [pancake](https://github.com/thiagowfx/pancake/tree/master/try):

> Interactive ephemeral workspace manager.
>
> Create and navigate to temporary project directories with fuzzy finding,
> automatic date-prefixing, and recency scoring. Automatically spawns a new
> shell in the selected workspace.

Usage:

```
% try +feature
thiago@thiagoperrotta-MacBook-Pro ~/workspace/tries/2025-12-02-feature
```

This creates a dated throwaway directory wherein to make experiments. I need not
worry about deleting it later.

If, in the future, I need to recall that experiment, I can simply run
`try feature`. It will open `fzf` with fuzzy finding, prompting me to select a
workspace.

Normally I delete these directories. This workflow encourages me to keep them
around, should I need to recall something from them.

For _truly_ throwaway directories, use [`cdtmp`]({{< ref "2024-10-07-cdtmp" >}})
instead.

