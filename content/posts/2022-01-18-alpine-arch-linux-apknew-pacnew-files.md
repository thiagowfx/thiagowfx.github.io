---
title: "Alpine / Arch Linux: .apk-new and .pacnew files"
date: 2022-01-18T14:25:20-05:00
tags:
  - dev
  - linux
---

As packages are upgraded over time, updated configs files under `/etc` may
arise. Different package managers treat this issue differently.


## Alpine Linux

`apk` creates `.apk-new` files, which can be located and merged by running
`doas update-conf`. Here is a recent example:

```shell
% doas update-conf
--- //etc/securetty
+++ //etc/securetty.apk-new
@@ -12,3 +12,6 @@
 tty11
 hvc0
 ttyS0
+ttyS1
+ttyAMA0
+ttyAMA1
New //etc/securetty available:
Quit, Next, Show diff, Edit new, Zap new, Use new (q/n/s/e/z/u) [s] u
```

## Arch Linux

`pacman` creates `.pacnew` files, which can be located and merged by running
`sudo pacdiff`. Here is a recent example:

```shell
% sudo pacdiff
==> pacnew file found for /etc/sudoers
:: (V)iew, (S)kip, (R)emove pacnew, (O)verwrite with pacnew, (Q)uit: [v/s/r/o/q]
```

**Tip**: The [`pacdiff-pacman-hook-git`][pacdiff-pacman-hook-git] package helpfully adds
a pacman hook that automatically checks whether there are any due `.pacnew`
files upon upgrading the system (`pacman -Syu`), being a simple and effective
way to automate this maintenance task. It looks like this:

```shell
: Running post-transaction hooks...
(1/5) Reloading system manager configuration...
(2/5) Creating temporary files...
(3/5) Arming ConditionNeedsUpdate...
(4/5) Registering Haskell modules...
(5/5) Reviewing .pacnew files...

/etc/sudoers.pacnew ⟶   /etc/sudoers
────────────────────────────────────────────────────────────────────────────────

────┐
76: │
────┘
 ##
 ## User privilege specification
 ##
-root ALL=(ALL:ALL) ALL
+root ALL=(ALL) ALL

 ## Uncomment to allow members of group wheel to execute any command
-# %wheel ALL=(ALL:ALL) ALL
+# %wheel ALL=(ALL) ALL

 ## Same thing without a password
-# %wheel ALL=(ALL:ALL) NOPASSWD: ALL
+# %wheel ALL=(ALL) NOPASSWD: ALL

 ## Uncomment to allow members of group sudo to execute any command
-# %sudo    ALL=(ALL:ALL) ALL
+# %sudo    ALL=(ALL) ALL

 ## Uncomment to allow any user to run sudo if they know the password
 ## of the user they are running the command as (root by default).
 # Defaults targetpw  # Ask for the password of the target user
-# ALL ALL=(ALL:ALL) ALL  # WARNING: only use this together with 'Defaults targetpw'
+# ALL ALL=(ALL) ALL  # WARNING: only use this together with 'Defaults targetpw'

 ## Read drop-in files from /etc/sudoers.d
 @includedir /etc/sudoers.d
 :: Searching databases for updates...
 :: Searching AUR for updates...
  there is nothing to do
```

[pacdiff-pacman-hook-git]: https://aur.archlinux.org/packages/pacdiff-pacman-hook-git/
