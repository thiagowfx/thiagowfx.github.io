---
title: "New script: SSH mux restart"
date: 2025-10-30T12:59:53+01:00
tags:
  - bestof
  - dev
---

[Previously]({{< ref "2025-10-21-github-the-organization-has-enabled-or-enforced-saml-sso" >}}),
[previously]({{< ref "2025-05-07-1password-ssh-agent-error" >}}).

After experiencing almost daily frustration because of this SSH auth issue, I
decided to script a solution out of it: and now
[`ssh_mux_restart`](https://github.com/thiagowfx/pancake/tree/8707d1792c0d1266180dfa3d49c7d144c71ef23d/ssh_mux_restart)
was born.

A copy of the `README.md` follows below for ease of reference.

The use case is very simple: run the `ssh_mux_restart` script whenever I run
into a git SSH authentication error, typically due to `git pull`, `git fetch` or
`git push`.

## Usage

Basic usage to kill SSH multiplexed connections:

```bash
./ssh_mux_restart.sh
```

To also restart the 1Password SSH agent:

```bash
./ssh_mux_restart.sh --restart-1password
```

## Example Output

```
% ./ssh_mux_restart.sh
Finding SSH multiplexed connections...
Found SSH multiplexed connections:
  88002 ssh: /tmp/ssh-control-FLAPJACK42 [mux]
  88123 ssh: /tmp/ssh-control-WAFFLE55 [mux]
Killing SSH multiplexed connections...
✓ Killed SSH mux process: 88002
✓ Killed SSH mux process: 88123
Killed 2/2 SSH multiplexed connections.

All operations completed successfully!
```

With the `--restart-1password` flag:

```
% ./ssh_mux_restart.sh --restart-1password
Finding SSH multiplexed connections...
Found SSH multiplexed connections:
  88002 ssh: /tmp/ssh-control-PANCAKE99 [mux]
Killing SSH multiplexed connections...
✓ Killed SSH mux process: 88002
Killed 1/1 SSH multiplexed connections.

Restarting 1Password application...
Found 1Password process: 67690
Quitting 1Password...
✓ 1Password quit successfully
Starting 1Password...
✓ 1Password started successfully
1Password SSH agent is now ready for use.

All operations completed successfully!
```

## Why This Matters

SSH multiplexed connections can cache stale authentication credentials, causing issues when:

- GitHub organizations enable or enforce SAML SSO
- 1Password SSH agent credentials need refreshing
- SSH keys have been rotated or updated

Restarting these connections forces SSH to re-authenticate with fresh credentials.

## Prerequisites

- Standard Unix tools (`pgrep`, `pkill`)
- 1Password app (macOS) if using the `--restart-1password` flag
