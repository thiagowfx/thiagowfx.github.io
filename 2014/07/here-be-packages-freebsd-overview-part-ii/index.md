---
title: "Here be packages! FreeBSD Overview (Part II)"
url: https://perrotta.dev/2014/07/here-be-packages-freebsd-overview-part-ii/
last_updated: 2026-08-17
---


**TL;DR:** in this post: about getting software and managing packages and ports
on FreeBSD 10. The first post on this series is available [in part I]({{< ref
"2014-07-20-here-be-dragons-freebsd-overview-part-i" >}}).

## Binary package management

`pkgng` seems to be the de-facto standard way to manage and install binary FreeBSD packages. Its interface is pretty traditional; users of Ruby Gems, node's npm and stuff should not have trouble using it. For example, `pkg install bash` was one of the first things I tried. The second one was `pkg install emacs`, but this has failed. Then a simple `pkg search emacs` would reveal that the correct name should be `emacs24`, `emacs23` or `emacs-nox11`. I opted for the last one.

Other simple commands involve `pkg remove`, `pkg info`, `pkg stats` and `pkg
help`. For starters, this is enough. A feature that I love in any package
manager is the reverse query, where you enter a file in your system and then
get the package that installed it. `pkg which` does that. Another one which
helps learning how files are organized within a package is listing all the
files inside a package. `pkg info -l` does that. I like to introspect quickly
what are the commands of a package manager by inspecting the source code of
`pacapt`. A remarkable feature is `pkg audit`, which shows the user any known
vulnerabilities. I've never seen this before – Linux distributions simply
update their packages, that's the way of being safe, so I'm not sure of the
usefulness of audit.

Finally, to locally install a `.txz` package you use `pkg add /path/to/pkg`. All
the commands I listed here should be enough to get your feet wet. What's next?
Let's try to remove a dependent package. For example, `pkg info -d emacs-nox11`
shows me that `emacs` depends on `libxml2`. So, let's try to remove this
dependency? `pkg remove libxml2` gives me an error, telling me that it depends
on emacs. Nice. If I want to forcefully and cleanly remove it, I should enter
`pkg remove -R`. This would remove emacs as well.

As the quantity of binary packages available, I've found out that there are 24k
packages. For comparison, the Debian base has about 40k and the Arch Linux one
7k (if you add the Arch User Repository, this list gets bigger than 50k). So I
could say that the quantity is reasonable. While I don't expect to find
everything, this base should cover standard use cases. What about
out-of-dateness of those packages? You know, Debian, CentOS and these "stable
server family" are slow about updating their packages; I've made quick tests by
searching for `nodejs`, `nginx`, `apache`, `mongodb`. I'm impressed, they were
all up-to-date. Even `calibre` (which is changing faster nowadays) was
up-to-date (in the 1.43 version).

I used this to learn about `pkg`, plus `pkg` itself (it looks well documented).
It is worth noting that this `pkg` utility has been introduced in this tenth
release of FreeBSD. Before it, it looks like there were a collection of programs
responsible for package management, such as `pkg_add`, `portmaster`, something
along these lines.

## Ports (source) system

Using `pkg` is not the only way of getting software installed on FreeBSD. The
user may also opt for using its ports system. It works like the Arch Build
System (ABS) and Gentoo's portage. Run `cd /usr/ports`, then you'll see several
directories with categories. I've made a quick test with `editors/uemacs`. There
were a couple of files inside this directory. Most notably, a **Makefile**; and
additionally, several files with metadata. I expected to see something like a
`PKGBUILD` or a `ebuild`, but I didn't. I believe the equivalent of these on the
FreeBSD world are fetched on-the-fly.

Running `make` built the package; `make package` installed it. Hmmm, I expected
that this last command would create a `.txz` package, then I should install it
with `pkg add`, but this wasn't the case. `make install` and `make clean` both
also work. I'm suspecting that this BSD makefile is just the GNU Makefile of
`uemacs`, but with a few patches applied to it (in fact, there are indeed some
patches lying there).

But how do we update our ports to the newest versions? `portsnap` is the answer.
You can see the in the manual. `portsnap fetch` looks like the most common
command, followed by `portsnap update`. However, the manual recommends doing
`portsnap fetch; portsnap extract` (this takes a while) the first time you issue
this command. Then forget extract and just use update. `portsnap fetch update`
is a one-shot way of doing this. It is also possible to use subversion to update
the ports tree, but I'm okay with the recommended method. (I later discovered
that program source code is installed into `/usr/ports/distfiles`.)

This is a manual about creating new ports. I expect to create some if I decide I
like and stick to FreeBSD, for the same reason that I maintain a collection of
`PKGBUILD`s for Arch Linux.

What about **upgrading** ports? Install **portmaster** (using `pkg` or the
ports system, the way you prefer), then issue `portmaster -a`. It is recommended
to use `portmaster -L` prior to that. It looks like there is another utility to
do this function, called `portupgrade` (suggestive, huh?). Last thing about
    ports: `portsclean` frees up some disk space (see its manual).

## What's next?

I decided to create an org file to track what I'll try next. Here is a snapshot
of it as of this post:

```org
* DONE Binary packages
* DONE Ports
* TODO X Window System (X11)
* TODO nginx hello world
* TODO C/C++ Hello World
* TODO golang Hello World
* TODO create a new port (poudriere?)
* TODO jails, chroot, etc
* TODO services (rc.conf, /etc/rc)
* TODO Linux compatibility?
* TODO what about user contributions? Is there something like AUR? Maybe
  freshports?
```

## And what are my problems for now?

- poor resolution (I believe it is 640x480).
- american keyboard
- no autocompletion and no colors! I'm still using `csh` (the default shell, as
  `echo $SHELL` shows), despite of installing `bash`. I'll probably change my
  default shell to `bash` or `zsh` later on, and install a few plug-ins to them
  (no, not oh-my-zsh stuff, it is much bloated for servers).

**Edit (2014-07-29)**: thank you Alex for correcting me in the comments.

