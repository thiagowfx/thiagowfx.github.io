---
title: "git pull: authentication issues"
date: 2025-06-03T14:35:04+02:00
tags:
  - dev
---

`git pull` authentication issues is _really_ a disguise for `ssh` auth issues.

Today a teammate could not `git pull` one of our internal repos:

```
% git pull
Enter passphrase for key '/Users/user/.ssh/id_ed25519':
git@github.com: Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

The first thing we verified was that his public key was
[added](https://github.com/settings/keys) to his github profile, and that the
private key was present in `~/.ssh/id_ed25519`.

Next, verify `~/.ssh/config`:

```
Host github.com
AddKeysToAgent yes
UseKeychain yes
IdentityFile ~/.ssh/id_ed25519
```

Looks fine. Then:

```shell
% export GIT_SSH_COMMAND="ssh -vvv"
% git pull
[...]
debug3: Search for item with query: {
    acct = "/Users/user/.ssh/id_ed25519";
    agrp = "com.apple.ssh.passphrases";
    class = genp;
    labl = "SSH: /Users/user/.ssh/id_ed25519";
    nleg = 1;
    "r_Data" = 1;
    svce = OpenSSH;
    "u_AuthUI" = "u_AuthUIF";
}
debug2: Unexpected keychain error while searching for an item: User interaction is not allowed.
```

Herein lies the error! The interaction with the system keychain in macOS was not
successful.

I suggested him to remove `AddKeysToAgent` and `UseKeychain` from this config
file, but that did not work either:

```shell
% git pull
[...]
Enter passphrase for key '/Users/user/.ssh/id_ed25519':
debug2: no passphrase given, try next key
debug2: we did not send a packet, disable method
debug1: No more authentication methods to try.
git@github.com: Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

The ssh key is protected with a passphrase.

In this case, it's better to fix the keychain issue. We readd the two deleted
lines.

Restart the `ssh-agent` and readd the key there:

```shell
% eval "$(ssh-agent -s)"
% ssh-add -K ~/.ssh/id_ed25519
```

Problem resolved! `git pull` works now.
