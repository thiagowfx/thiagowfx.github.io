---
title: "claude: srt: sandbox runtime"
date: 2026-03-04T20:00:00+01:00
tags:
  - ai
  - dev
  - security
---

[Previously: `cco`]({{< ref "2026-02-26-cco-claude-condom-sandbox" >}}).

**`cco` handles filesystem isolation but not networking — `srt` adds network
isolation.**

**Disclaimer**: This post was adapted from a slides presentation I recently
created for an AI hackathon. Its prose resembles a quick-reference manual.

## `srt`: sandbox-runtime

[`srt`](https://github.com/anthropic-experimental/sandbox-runtime) is
Anthropic's open-source sandbox runtime. It is process agnostic and it uses
OS-native primitives —
[Seatbelt](https://www.chromium.org/developers/design-documents/sandbox/osx-sandboxing-design/)
on macOS, [bubblewrap](https://github.com/containers/bubblewrap) on Linux — no
container overhead, just like `cco`.

Run a command inside the sandbox ("hello world"):

```shell
% npx @anthropic-ai/sandbox-runtime <command>
```

Or you might as well install it so that it is easily invokable as `srt`[^1]:

[^1]: `srt` reminds me of the popular subtitles extension format for videos.
    Also, I constantly makee typos by typing `str` instead.

```shell
% npm install -g @anthropic-ai/sandbox-runtime
```

`-g` is for global (=not local).

Network restrictions in action:

```shell
% srt "curl anthropic.com"
<html>...</html>                  # allowed

% srt "curl example.com"
Connection blocked by network allowlist  # blocked
```

Filesystem restrictions in action:

```shell
% srt "cat README.md"
# Anthropic Sandb...               # current dir allowed

% srt "cat ~/.ssh/id_rsa"
cat: Operation not permitted        # blocked
```

The sandbox configuration lives globally in `~/.srt-settings.json`:

```json
{
  "network": {
    "allowedDomains": ["github.com", "registry.npmjs.org"],
    "deniedDomains": []
  },
  "filesystem": {
    "denyRead": ["~/.ssh", "~/.aws/credentials"],
    "allowWrite": ["."],
    "denyWrite": [".env", "config/production.json"]
  }
}
```

It is secure by default — everything is blocked unless explicitly allowed.
Separate controls for filesystem reads, writes, and network domains.

## native `/sandbox`

Since [v1.0.29](https://code.claude.com/docs/en/sandboxing), Claude Code ships
with native sandboxing — powered by `srt` under the hood. Enable it with the
`/sandbox` command. Zero setup on macOS.

Two modes:

- **Auto-allow**: sandboxed commands run without prompts; unsandboxable commands
  fall back to the regular permission flow.
- **Regular**: all commands still require approval, but sandbox boundaries are
  enforced. The most **strict**.

In the first mode, you will see the following pattern quite often:

```
⏺ Bash(gh api user --jq .login)
  ⎿  Error: Exit code 71
     sandbox-exec: sandbox_apply: Operation not permitted

     sandbox-exec: sandbox_apply: Operation not permitted

⏺ Sandbox restriction on gh. Let me retry outside the sandbox.

⏺ Bash(gh api user --jq .login)
  ⎿  thiagowfx
```

Anthropic reports ~84% fewer permission prompts with auto-allow mode.

`~/.claude/settings.json`:

```json
{
  "sandbox": {
    "enabled": true,
    "autoAllowBashIfSandboxed": true,
    "allowUnsandboxedCommands": true,
    "allowedDomains": ["registry.npmjs.org", "api.github.com"],
    "excludedCommands": ["docker"],
    "filesystem": {
      "allowWrite": ["~/.kube", "/tmp/build", "~/.cache"]
    }
  }
}
```

- `autoAllowBashIfSandboxed` — sandboxed commands run without prompts
- `excludedCommands` — tools that always run outside the sandbox (e.g. Docker)
- `allowUnsandboxedCommands` — escape hatch for commands that fail inside the
  sandbox (still requires approval)
- `filesystem.allowWrite` — grant subprocess write access to paths outside the
  working directory

**When to use what?**

- **`cco`**: quick filesystem-only sandbox, zero config, IDE agnostic
- **`srt`**: standalone sandbox for any process (not only Claude Code) with
  network isolation
- **`/sandbox`**: native Claude Code integration, fewest prompts, recommended
  for daily use

I've been daily driving `cco` + the native `/sandbox`. It encompasses the best
of all worlds.
