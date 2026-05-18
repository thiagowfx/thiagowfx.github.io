---
title: "atuin: delete account"
url: https://perrotta.dev/2026/05/atuin-delete-account/
last_updated: 2026-05-18
---


[Previously]({{< ref "2025-11-30-atuin" >}}).

I've been [self-hosting]({{< ref "2026-01-24-atuin-new-machine-setup" >}})
[`atuin`](https://atuin.sh/) for quite a while now. As such, I no longer need an
account in the official server (created a long time ago).

**Problem statement**: delete that account.

Note that I am currently logged into my self-hosted server.

As such, the first step is to switch back to the official server:

```shell
% $EDITOR ~/.config/atuin/config.toml
```

Then ensure that `sync_address` is either commented out or set to
`https://api.atuin.sh`.

Now log in to it:

```shell
% atuin login --username {username}
>> insert password, insert key
```

And, finally:

```shell
% atuin account delete
```

Afterwards, switch back to the self-hosted server and run `atuin login` again.

