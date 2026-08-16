---
title: "Hello World! FreeBSD Overview (Part III)"
date: 2013-04-20T01:29:20-03:00
tags:
  - dev
  - legacy
---

[Previous post]({{< ref "2014-07-21-here-be-packages-freebsd-overview-part-ii" >}}).

**TL;DR:** In this post: setup of gcc/g++, golang, nginx and Xorg/X11. Let's
begin with a simple C/C++ hello world. For that, I'll test both `gcc` and
`g++`.

## gcc

Run `pkg install gcc` and create a new `hello.c` file:

```c
#include <stdio.h>

int main() {
  printf("Hello World!\n");
  return 0;
}
```

The `gcc` command doesn't exist, but it is easy to find the correct executable
name: `gcc47`. Then run `gcc47 hello.c -o hello -Wall` and test it: `./hello`.
Everything was nice here. For C++, the `gcc` package already contains it. You
can also test the previous file, with the `g++47` executable.

Newer versions are also available: its packages are named `gcc48` and `gcc49`
as of this post. It is not hard to see that all these versions can coexist.
For comparison, Gentoo also (elegantly) allows multiple versions of packages;
and Arch, **by design**, sticks only to the latest version (gcc 4.9 in this
case), although it is not hard to obtain previous versions, as they are
usually available in the AUR.

## golang

I just wanted to pick some less traditional language (no Python, Ruby or Java
here) to test, so I chose Go, since I'm learning it now. Also, since the Go
library compiles fast (by design), I chose to install it using ports. Run `cd
/usr/share/ports/lang/go` and `make install`. The whole process took under 90
seconds, using only one processor (also, remember I'm running FreeBSD under
VirtualBox). Now edit `hello.go`:

```go
package main

import "fmt"

func main() {
  fmt.Printf("Hello, 世界\n")
}
```

Then run `go run hello.go`. Nice!

## node.js

Just one more quick example, shall we? Run `pkg install node`. This time I'm
testing interactively, just running `node` then `console.log("Hello
world!\n");`

## nginx

Now, let's get our feet wet. Run `pkg install nginx`. I also need a text
browser, since I'm not running X yet. Run `pkg install w3m`. Now: how to start
nginx? With a little serendipity (yes, no Googling!), we can use `pkg info -l
nginx` to find the archives we need. They are all within `/usr/local`. And,
with a little luck, we also find that the `service` command exists. If I were
on a Linux machine, I would do a `service nginx start`. But this doesn't work
here.

Reading the man page of `service`, and with some additional tries, I discover
that we should do a `service nginx onestart`. This works, because I can see
the success message; additionally, I can confirm it with `pgrep nginx` or with
`ps aux | grep nginx`. Without further reading, it looks like if I wanted to
enable nginx permanently, I should add an entry to `/etc/rc.conf`; and every
time I want to start it manually, I should use `one*`, like `onestatus`,
`onestop`, etc.

For comparison with the systemd world, the `onestart` equivalent to it would
be a `systemctl start nginx` and the 'permanently start' equivalency is
`systemctl enable nginx`. I guess it is just different here, but since it is
easy to use this 'one' thing, I don't have reasons to complain for now. A
simple `w3m localhost` shows that it really worked. An additional step would
be to enable PHP and FastCGI in our little server, but I won't do that here,
since I'm not focusing specifically in the server side of FreeBSD.

## X11

This is the last tool that will give hello to you today, I promise. Run `pkg
install xorg`. Next, I've created a `$HOME/.xinitrc` file as another user (not
root):

```shell
xterm &
exec twm
```

Then run `startx`. Well, X started. But I couldn't use the mouse – actually,
I'm running this VM in a ultrabook, so I couldn't use the touchpad. I also
couldn't see the `xterm` window (although it looked like it was minimized, but
I'm not really sure about that – no familiarity with `twm`). Also,
`Ctrl+Alt+BackSpace` didn't work out-of-the-box, so I had to forcefully
shutdown the VM, then restart it.

OK, debug time. I installed the `sudo` package, then added my non-root user to
the sudoers file (by running `visudo` and changing the appropriate line). Now
I can log in again with my non-root user and install programs properly with
`sudo`. I'm going to test with tools I'm familiar with: `pkg install i3
rxvt-unicode`. Now, an updated version of my `$HOME/.xinitrc` file:

```shell
urxvt &
exec i3
```

This time I couldn't even start Xorg, because it was complaining about some
missing `libxcb-cursor` library (missing dependency, huh?). Despite of me
installing everything I could find about `xcb`, the problem persisted. So I
had to read section 6.4 of the manual. It recommended me to add `hald` and
`dbus` to `rc.conf`, to enable those services, and to regenerate a `xorg.conf`
file, with `Xorg -configure`, then moving it to `/etc/X11`.

After another reboot, I got a kernel panic. And another. And another. Oh no,
it became a boot loop with successive kernel panics. What is worst? I have no
idea why. I haven't touched anything critical. A screenshot of the kernel
panic is a screenshot of the kernel panic. I'm not in the mood of reinstalling
everything just to continue this series; however, I'm still going to try to
recover it. If you have any idea or tips about that strange (and unexpected!)
error, please leave a comment. It looks like a disk error, maybe the virtual
hard disk has been damaged, maybe because of my forced shutdown? I don't know.

## What's next?

Not sure. I'll only continue this if I recover the system. Here is the org
list, anyways:

```org
* DONE Binary packages
* DONE Ports
* TROUBLE X Window System (X11)
* DONE nginx hello world
* DONE C/C++ Hello World
* DONE golang Hello World
* TODO create a new port (poudriere?)
* TODO jails, chroot, etc
* PROGRESS services (rc.conf, /etc/rc)
* TODO Linux compatibility?
* TODO what about user contributions? Is there something like AUR? Maybe freshports?
```

I'm still going to write at least another post.

**Update (2014-07-25)**: Thanks to Vinicius I'm going to continue this series,
now on QEMU with KVM instead of VirtualBox. I'll take a little while to write
the next post, but now you know it will exist :)
