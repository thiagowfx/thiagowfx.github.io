---
title: "macOS: sudo with touch ID"
date: 2022-03-21T02:13:27-03:00
tags:
  - dev
---

Recent macbooks have a fingerprint reader, which is typically used to unlock the computer and log in.

It is also possible to use it for `sudo` authentication via [PAM](https://en.wikipedia.org/wiki/Pluggable_authentication_module):


```shell
% $EDITOR /etc/pam.d/sudo
# sudo: auth account password session
auth       sufficient     pam_tid.so             # <== add this line
auth       sufficient     pam_smartcard.so
auth       required       pam_opendirectory.so
account    required       pam_permit.so
password   required       pam_deny.so
session    required       pam_permit.so
```

Once the file is saved with the added line, a command with `sudo` will spawn the touch ID prompt. I confirmed it works on both Terminal.app and Kitty.

This solution [does not](https://apple.stackexchange.com/a/392407) work within `tmux` (confirmed), and apparently within iTerm2 as well (not confirmed). A separate PAM module is needed to do so ([`pam_reattach.so`](https://github.com/fabianishere/pam_reattach)). I'd rather keep my core dependencies surface small though and not include a third party, so for now I am satisfied with the native touch ID module.

## References

- https://sixcolors.com/post/2020/11/quick-tip-enable-touch-id-for-sudo/
- https://apple.stackexchange.com/a/306324
