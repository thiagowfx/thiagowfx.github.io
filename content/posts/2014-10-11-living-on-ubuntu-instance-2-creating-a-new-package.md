---
title: "Living on Ubuntu - Instance #2 - Creating a new package"
date: 2014-10-11T14:14:52-03:00
tags:
  - dev
  - legacy
---

These are **notes** from a few weeks ago when I created a sample package for
Ubuntu. This article is written both as a guide and a timeline. There is no
explicit tutorial here, so get your feet wet by yourself, and make sure to
follow the references. **Edit**: enumeration became a mess here. Sorry for that.

## Initial setup

1. Introduction; Packaging new software for Ubuntu; Debian Packaging Tutorial
2. Get a couple of packages for packaging (duh):

```shell
sudo aptitude install gnupg pbuilder ubuntu-dev-tools bzr-builddeb apt-file packaging-dev
```

3. Make sure you have a PGP key.
4. Send your PGP key to Ubuntu servers.

```shell
gpg --send-keys --keyserver keyserver.ubuntu.com <KEY ID>
```

5. Make sure you have a SSH key.

## Building environment

6. Create a clean build environment:

```shell
pbuilder-dist <release> create
```

At the time of this post, I used 'trusty' as the release name.

7. Make sure you have a Launchpad account.
8. Update your Launchpad information **and** upload both your SSH and your GPG key into there.
9. Identify yourself with bzr.

```shell
bzr whoami "Bob Dobbs [subgenius@example.com](mailto:subgenius%40example.com)"
bzr launchpad-login subgenius
```

## Creating the package

10. Start a new package, and choose its type to create a new template.

```shell
bzr dh-make hello 2.7 hello-2.7.tar.gz
```

11. Explore and edit the files of your new template. In particular, see the
    `debian` directory.
12. `bzr add` and `commit` your changes. This is a DVCS such as `git`, so this
    should feel familiar.

## Building and testing

13. Building the package:

```shell
bzr builddeb -- -us -uc
```

The previous flags tell the system not to use GPG. `-nc` might also be useful:
it tells the system not to start from scratch.

14. To view the contents of a package:

```shell
lesspipe *.deb
```

15. To install / remove your new built package:

```shell
sudo dpkg -i *.deb # attention to the architecture of your package!
sudo dpkg -r <name-of-your-package>
```

An alternative is to invoke `sudo debi`.

16. Check for errors.

```shell
lintian *.dsc *.deb
```

## Optional testing with chroot

17. Next (optional; just to test the package in the chroot you have set up before, with `pbuilder`)

```shell
bzr builddeb -S
cd ../build-area
pbuilder-dist trusty build *ubuntu*.dsc
```

## Upload

18. Upload your package to Launchpad:

```shell
dput ppa:<your-launchpad-username>/<your-ppa-name> *.changes
```

If you wanted to create a pull request instead:

```shell
bzr push lp:~<launchpad-username>/+junk/hello-package
```

And that's it! Then just share your PPA with your friends and clients. I hope
this guide could serve to you as a quick reference of creating a new Ubuntu (or
even Debian) package.
