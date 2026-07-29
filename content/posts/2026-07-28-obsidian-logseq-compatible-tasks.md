---
title: "obsidian: logseq-compatible tasks"
date: 2026-07-29T14:34:39+02:00
tags:
  - dev
  - pkm
  - security
---

[Previously]({{< ref "2026-07-20-logseq-to-obsidian" >}}).

**Problem statement**: preserve Logseq's task syntax while opening the same markdown
files in Obsidian.

My migration script originally converted every task into Obsidian's checkbox
syntax:

```text
- TODO buy milk     ->  - [ ] buy milk
- DOING ...         ->  - [/] ...
- DONE ...          ->  - [x] ...
```

Obsidian itself does not recognize the left-hand side as tasks. The
[TODOseq](https://github.com/scross01/obsidian-todoseq) community plug-in does:

```markdown
- TODO buy milk
- DOING ...
- DONE ...
```

It keeps the file unchanged, adds clickable task states and a task list to
Obsidian, and remains compatible with Logseq.

Before granting a community plug-in write access to my vault, I inspected the
current release with the LLM™:

```shell
% git clone --depth=1 https://github.com/scross01/obsidian-todoseq.git /tmp/obsidian-todoseq-audit
Cloning into '/tmp/obsidian-todoseq-audit'...
% cd /tmp/obsidian-todoseq-audit
% git rev-parse --short HEAD
4ba5e81
% jq '{id, version, minAppVersion, description}' manifest.json
{
  "id": "todoseq",
  "version": "0.18.1",
  "minAppVersion": "1.11.0",
  "description": "Lightweight keyword-based task tracker using Logseq style keywords."
}
```

A source scan found no network requests, telemetry, process execution, or
dynamic code evaluation[^1].

[^1]: _Hope is not a strategy_.

It does read and modify notes through Obsidian's vault API, as expected:

```shell
% rg -n 'vault\.(read|modify)' src/services/editor-controller.ts | head -4
1130:        const currentContent = await this.plugin.app.vault.read(todayNote);
1135:        await this.plugin.app.vault.modify(todayNote, newContent);
1283:        const todayContent = await this.plugin.app.vault.read(todayNote);
1286:        await this.plugin.app.vault.modify(todayNote, newTodayContent);
```

Low risk, and no task-format conversion needed.

This should make it easier for me to adapt my LogSeq muscle memory to Obsidian,
even if at the cost of enabling community plug-ins.

- - -

🤖 *Drafted with [`/bloggify`](https://github.com/thiagowfx/skills/blob/master/plugins/thiagowfx/skills/bloggify/SKILL.md).*
