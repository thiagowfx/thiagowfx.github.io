---
title: "mise: prune old installations"
url: https://perrotta.dev/2026/09/mise-prune-old-installations/
last_updated: 2026-09-03
---


**Today I learned**: [mise](https://mise.jdx.dev/) can remove tool versions no
longer referenced by its tracked configuration files.

List versions eligible for cleanup (dry-run):

```shell
% mise ls --prunable
% mise prune --tools --dry-run
```

Run the cleanup (without `--dry-run`):

```shell
% mise prune --tools
```

`mise prune` also handles stale tracked configuration links:

```shell
% mise prune --dry-run
mise pruned configuration links [dryrun]
```

For an one-off cleanup, `mise uninstall` removes selected versions instead:

```shell
% mise uninstall node@18.0.0
% mise uninstall --all node
```

The first command removes one version. The second removes every installed
version of one tool.

