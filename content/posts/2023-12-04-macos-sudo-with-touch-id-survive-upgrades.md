---
title: "macOS: sudo with touch ID: survive upgrades"
date: 2023-12-04T22:40:21+01:00
tags:
  - macos
showtoc: true
---

Recent macbooks have a fingerprint reader, which is typically used to unlock the computer and log in.

It is also possible to use it for `sudo` authentication via [PAM](https://en.wikipedia.org/wiki/Pluggable_authentication_module).

This was previously covered [here]({{< ref "2022-03-21-macos-sudo-with-touch-id.md" >}}).

Now, with macOS Sonoma, it's also possible to make this setting survive OS upgrades.

<!--more-->

```shell
% sudo cp /etc/pam.d/sudo_local{.template,}
% sudo $EDITOR /etc/pam.d/sudo_local
```

Then uncomment (or add, if not existing) the following line:

```
auth       sufficient     pam_tid.so
```

You can test it out by opening a new terminal and executing `sudo echo`.

Credits: https://sixcolors.com/post/2023/08/in-macos-sonoma-touch-id-for-sudo-can-survive-updates/
