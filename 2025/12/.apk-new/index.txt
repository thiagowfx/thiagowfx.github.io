
After running an Alpine Linux server for a couple of months (or years), you'll
inevitably find a couple of `.apk-new` files scattered in your filesystem within
`/etc`:

```shell
% doas find / -name "*.apk-new"
/etc/rc.conf.apk-new
/etc/inittab.apk-new
/etc/fstab.apk-new
/etc/ssh/sshd_config.apk-new
/etc/passwd.apk-new
/etc/crontabs/root.apk-new
/etc/group.apk-new
/etc/ufw/ufw.conf.apk-new
/etc/ufw/user6.rules.apk-new
/etc/ufw/user.rules.apk-new
/etc/abuild.conf.apk-new
/etc/default/grub.apk-new
/etc/shadow.apk-new
/etc/network/interfaces.apk-new
/etc/profile.d/locale.sh.apk-new
/etc/doas.conf.apk-new
```

As per the [alpine user
handbook](https://docs.alpinelinux.org/user-handbook/0.1a/Working/apk.html#_installing_packages):

> Installing a package means that the package itself will be downloaded from a
> repository (specified in /etc/apk/repositories) and unpacked to the system.
> Existing files will be overwritten. An exception are configuration files in
> /etc, which will be preserved. The configuration files (which comes from the
> package) will be renamed to *.apk-new.

It's very similar to what happens in Arch Linux with
[`.pacnew`](https://wiki.archlinux.org/title/Pacman/Pacnew_and_Pacsave) files.
Arch Linux has an utility called
[`pacdiff`](https://wiki.archlinux.org/title/Pacman/Pacnew_and_Pacsave#pacdiff):

> It will search for .pacnew, .pacsave and .pacorig files, and will then prompt
> to take action upon them.

...and also in Gentoo Linux with
[`etc-update`](https://wiki.gentoo.org/wiki/Etc-update) or
[`dispatch-conf`](https://wiki.gentoo.org/wiki/Dispatch-conf).

Alpine Linux lacks such an utility, to the best of my knowledge.

As such, I vibe coded one in [`pancake`](https://github.com/thiagowfx/pancake).

I hereby introduce [`apknew`](https://github.com/thiagowfx/pancake/tree/master/apknew):

> Reconcile .apk-new configuration files on Alpine Linux, similar to pacdiff on
> Arch Linux.

By default, it operates on `/etc` only.

A sample run looks like the following, prompting a pair of files at a time:

```
==============================================
File: /etc/crontabs/root.apk-new
Original: /etc/crontabs/root
==============================================

[v]iew diff  [k]eep original  [r]eplace with new  [m]erge  [s]kip
Action:
```

You'll want to hit `v` first to inspect the diff, and then decide whether to:

- keep the original file
- replace it with the newer package file
- interactively merge them (e.g. with `vimdiff`)
- do nothing (skip)

It's much easier than diffing each file manually.

Another example:

```
% apknew/apknew.sh
Searching for .apk-new files in /etc...
Found 14 file(s) to process.

==============================================
File: /etc/passwd.apk-new
Original: /etc/passwd
==============================================

[v]iew diff  [k]eep original  [r]eplace with new  [m]erge  [s]kip
Action: s
Skipping /etc/passwd.apk-new...

==============================================
File: /etc/shells.apk-new
Original: /etc/shells
==============================================

[v]iew diff  [k]eep original  [r]eplace with new  [m]erge  [s]kip
Action: v
--- /etc/shells	2025-12-21 11:07:42.531531775 -0500
+++ /etc/shells.apk-new	2025-12-15 09:00:47.000000000 -0500
@@ -1,5 +1,3 @@
 # valid login shells
 /bin/sh
 /bin/ash
-/bin/zsh
-/bin/bash

[v]iew diff  [k]eep original  [r]eplace with new  [m]erge  [s]kip
Action: k
Removing /etc/shells.apk-new...
Done. Kept original file.
```

