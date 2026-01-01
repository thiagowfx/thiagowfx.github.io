
Given `/Users/thiago.perrotta/Corp/gitops/apps/overlays/hoth`.

Assume I am in `/Users/thiago.perrotta/Corp/gitops` (a git repo).

**Problem statement**: Copy the full path of `apps/overlays/hoth`.

**Option #1**: `cd apps/overlays/hoth && pwd`, then [copy]({{< ref
"2025-11-04-new-script-copy" >}}) the output.

This is disruptive though. I would rather not change my working directory.

**Option #2**: `realpath apps/overlays/hoth`.

As per [`realpath(1)`](https://man.archlinux.org/man/realpath.1):

> realpath - print the resolved path

This works perfectly!

Why do this? To retrieve file / directory context for the LLM.

