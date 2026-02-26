---
title: "cco: claude condom (sandbox)"
date: 2026-02-26T13:17:26+01:00
tags:
  - ai
  - bestof
  - dev
  - security
---

**Problem statement**: `claude --dangerously-skip-permissions` ("YOLO mode") is
fast but risky. Introduce a lightweight filesystem-level sandbox. Networking is
explicitly out of scope at this time.

Recently I [aliased]({{< ref "2026-02-18-new-apkbuild-llm-edition" >}}) it to
`claudey` and have been using it daily. It's an effective way to run Claude Code
without being constantly nagged with permission prompts. But going unprotected
has many risks and downsides:

- **Prompt injection**: web search can trick Claude into accessing files or
  running commands outside the project directory
- **No guardrails**: SSH keys and credentials are generally accessible
- [**Approval fatigue**](https://en.wikipedia.org/wiki/Decision_fatigue):
  repeatedly clicking "approve" leads to paying less attention.
- Especially dangerous for **background agents** running unattended.

Effective sandboxing needs both filesystem _and_ network isolation — without
network isolation, a compromised agent can exfiltrate sensitive files. But, as
mentioned in the first paragraph, networking is overruled for now. Baby steps!

[cco](https://github.com/nikvdp/cco) (_Claude Condom_) is a thin wrapper that
runs Claude Code in a sandbox. Originally discovered via [Paras
Chopra](https://invertedpassion.com/my-claude-code-workflow/).

How to use it? First you need to install it. The
[official](https://github.com/nikvdp/cco?tab=readme-ov-file#installation)
installation instructions use `curl | bash` but I [despise]({{< ref
"2025-10-17-distributing-my-own-scripts-via-homebrew" >}}) that.

Hence I created my own `brew`
[formula](https://github.com/thiagowfx/homebrew-taps/blob/master/Formula/cco.rb)
for it. Now it's just one `brew install` command away from usage (and also from
    uninstallation, very important!).

**Usage**: replace `claude` with `cco` and you're done:

```shell
% cco "analyze this codebase"
% cco --resume
```

It will start Claude within the "bypass permissions on" mode, albeit within the
sandbox.

It auto-selects the best available sandbox: native OS
([Seatbelt](https://www.chromium.org/developers/design-documents/sandbox/osx-sandboxing-design/)
on macOS, [bubblewrap](https://github.com/containers/bubblewrap) on Linux) or
Docker fallback. The native macOS sandbox has **near-zero** overhead, which is
remarkable. This kind of low-friction in developer tooling helps to drive its
adoption.

Docker is slow though, especially on macOS. You should avoid it in this context
if you can.

The host filesystem is **read-only by default** (globally). Only the project
directory (git root) is writable. Whitelist additional paths with `--add-dir` as
needed:

```shell
% cco --add-dir ~/.cache \
      --add-dir ~/.aws/cli/cache \
      --add-dir ~/.terraform.d/plugin-cache
```

I had to whitelist the directories above otherwise [`pre-commit`]({{< ref "2024-12-21-pre-commit" >}}) / `prek`, the
`aws` CLI and `terraform` would fail sporadically.

`--safe` hides `$HOME` entirely; only whitelisted paths are visible.

`--deny-path` blocks specific sensitive paths.

All Claude Code flags (`--resume`, `--model`, etc.) pass through transparently.

**Why `cco`?**

- it's zero-config
- its startup has pretty much zero overhead
- it's IDE agnostic
- it just works™

**Why not `cco`?**

It does not handle networking.
[`srt`](https://code.claude.com/docs/en/sandboxing) is more suitable as an
additional step.

I updated my `claudey` alias:

```shell
alias cco="cco --allow-oauth-refresh --add-dir ~/.cache --add-dir ~/.aws/cli/cache --add-dir ~/.terraform.d/plugin-cache"
```

`--allow-oauth-refresh` is necessary, or else:

```
⎿  API Error: 401 {"type":"error","error":{"type":"authentication_error","message":"OAuth token has expired. Please obtain a new token or refresh your
     existing token."},"request_id":"req_{redacted}"} · Please run /login
```

...my login credentials would expire roughly once every day. Re-authenticating
every day is quite annoying.

This is properly [documented](https://github.com/nikvdp/cco/blob/master/SECURITY.md#credential-protection):

> **Credential file access**: The credentials JSON is mounted read-only by default, so Claude cannot update tokens unless `--allow-oauth-refresh` is explicitly enabled.
