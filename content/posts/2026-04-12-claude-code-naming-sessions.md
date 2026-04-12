---
title: "claude code: naming sessions"
date: 2026-04-12T10:06:51+02:00
tags:
  - ai
  - bestof
  - dev
---

[Previously]({{< ref "2026-03-02-claude-add-session-id-to-status-bar" >}}).

**Problem statement**: `claude --resume` accepts a session ID (UUID), but UUIDs
are not human-friendly.

```shell
% claude --resume 92884e7a-422a-4e2a-9fbc-dc0a2e85380b
```

I can't remember that at all, and even copy-and-paste is error-prone in this
context (e.g. missing the first or last character in the UUID).

There are a few ways to turn this into a nicer developer experience.

**Start a session with a name**:

```shell
% claude --name "golden-ami-deploy-servers"
```

Realistically, though, that's hard to remember. Also, oftentimes you'll start a
session without knowing upfront what you'll work on.

**Rename mid-session** with `/rename`:

```
/rename golden-ami-deploy-servers
```

Better! The name can be adjusted on-the-fly. It resembles `tmux` in this aspect.

Or: just `/rename` with no argument will auto-generate a name from the
conversation history. Fancy. That will burn a few more tokens though.

And now, back to the original problem:

**Resume by name**:

```shell
% claude --resume "golden-ami-deploy-servers"
```

The interactive picker (`claude --resume` with no argument) also displays
session names, making it easy to find what you're looking for.

You can also invoke `/resume` mid-session.
