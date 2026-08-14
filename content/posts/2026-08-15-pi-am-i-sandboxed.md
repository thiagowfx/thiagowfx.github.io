---
title: "pi: am I sandboxed?"
date: 2026-08-15T00:56:29+02:00
tags:
  - ai
  - coding
  - dev
  - pi
  - security
---

**Problem statement**: asking a coding agent whether it runs in a sandbox
returns a confident answer derived from its system prompt, not from the machine
it is actually running on.

I asked [Pi](https://github.com/earendil-works/pi-mono) exactly that. The reply
was assured:

> No — pi itself doesn't sandbox tool execution. When I run `bash`, `edit`, or
> `write`, they execute directly on your machine with your user's permissions,
> in the current working directory (`/Users/thiago.perrotta/.pi`). [...] But
> there's no OS-level sandbox (no container, no seccomp, no filesystem jail).

It's plausible, well-formatted, and...**wrong**!. One typo-ridden command was
enough to break the illusion:

```shell
% ls ~/worksppace
ls: cannot access '/home/hostuser/worksppace': No such file or directory
```

`~` is not `/Users/thiago.perrotta`. The follow-up probe:

```shell
% pwd; uname -a; whoami; cat /etc/os-release
/Users/thiago.perrotta/.pi
Linux lima-rancher-desktop 6.18.37-0-virt #1-Alpine SMP PREEMPT_DYNAMIC 2026-06-29 10:52:25 aarch64 GNU/Linux
hostuser
PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"
```

A macOS-shaped `pwd` inside an aarch64 Debian container, on an Alpine
[Lima](https://lima-vm.io/) VM, under Rancher Desktop. _Containerception_.

And the giveaway at the filesystem root:

```shell
% ls -la / | head -5
total 68
drwxr-xr-x   1 root root 4096 Aug 15 00:54 .
drwxr-xr-x   1 root root 4096 Aug 15 00:54 ..
-rwxr-xr-x   1 root root    0 Aug 15 00:54 .dockerenv
drwxr-xr-x   3 root root 4096 Aug 15 00:54 Users
```

`/.dockerenv`, plus a `/Users` bind mount recreating just enough of the host
path for the system prompt's `cwd` to resolve.

The model was not lying; it had no way to know. Its self-description comes from
tokens someone else wrote, while the ground truth sits one `uname` away. The
useful lesson is that agent introspection is a documentation lookup, not a
measurement — for anything security-relevant, make it run the command.

The sandbox was [cco]({{< ref "2026-02-26-cco-claude-condom-sandbox" >}}).

- - -

🤖 *Drafted with [`/bloggify`](https://github.com/thiagowfx/skills/blob/master/plugins/thiagowfx/skills/bloggify/SKILL.md).*
