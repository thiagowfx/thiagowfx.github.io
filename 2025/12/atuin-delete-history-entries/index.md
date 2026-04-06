---
title: "Atuin: delete history entries"
url: https://perrotta.dev/2025/12/atuin-delete-history-entries/
last_updated: 2026-02-07
---


Deleting, scrubbing, redacting old shell history entries is now easier
than ever, thanks to [atuin](https://github.com/atuinsh/atuin).

```shell
% atuin search '^aws_login_headless' --delete
deleting 019ad59e973b7c139c4a1d67fe2155be
deleting 019ad59e973b7c139c4a1d40a0da15f1
```

First do the search without `--delete`, and then re-run the command with
`--delete` if the output is what you expect.

You would want to do so in these two scenarios:

- prevent irrelevant entries from showing up in `C-r` (history search), reducing
  clutter
- delete sensitive entries e.g. passwords (`docker login --password {foo}`)

[Previously]({{< ref "2025-11-30-atuin" >}}).

