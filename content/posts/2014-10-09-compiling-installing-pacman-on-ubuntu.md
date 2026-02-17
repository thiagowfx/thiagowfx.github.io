---
title: "Compiling / Installing pacman on Ubuntu"
date: 2014-10-09T23:20:52+00:00
tags:
  - dev
  - legacy
---

No, this is not the classic game. Here are logs.

```bash
git clone git://projects.archlinux.org/pacman.git
cd pacman/
./autogen.sh
./configure LIBS="-lpthread -larchive"
```

Attention here! `./configure` without this parameter didn't work on my machine.
The error was: `DSO missing from command line`.

```bash
make
sudo checkinstall
```

Attention here! You could simply (and näively) do a `sudo make install`,
however, this wouldn't create a `.deb` package. Since we have good tools, we
should use them!

Now, you can remove pacman anytime you want with `dpkg -r pacman`. No need for
`make uninstall`.

Why this post? Because of [this forum
thread](https://bbs.archlinux.org/viewtopic.php?id=187942).
