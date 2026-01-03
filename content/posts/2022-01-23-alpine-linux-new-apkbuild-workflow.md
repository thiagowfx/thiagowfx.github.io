---
title: "Alpine Linux: New APKBUILD Workflow"
date: 2022-01-23T19:15:02-05:00
tags:
  - alpine-linux
  - bestof
  - dev
---

This document describes my workflow to manage `APKBUILDs` for the
[aports][aports] repository in [Alpine Linux][alpine-linux].

## Disclaimer

First of all, this post is not a substitute to the [AlpineWiki][alpine-wiki]
and it will likely get outdated at some point. In particular, refer to the
following articles for up-to-date documentation that will outlive this blog:

- https://wiki.alpinelinux.org/wiki/APKBUILD_Reference
- https://wiki.alpinelinux.org/wiki/Abuild_and_Helpers
- https://wiki.alpinelinux.org/wiki/Aports_tree
- https://wiki.alpinelinux.org/wiki/Creating_an_Alpine_package

This article is not a tutorial, as such it assumes you already know what an
`APKBUILD` is and how to use `abuild`. In particular, you should have the
`alpine-sdk`, `atools` and `spdx-licenses-list` packages installed in your
system.

## Structure

I manage my packages with `git`. Create a GitLab account on
https://gitlab.alpinelinux.org/, fork the [`aports`][aports] tree, and `git
clone` your fork.

The structure follows Alpine Linux repositories:

```
$ git clone https://gitlab.alpinelinux.org/alpine/aports.git && tree -L 1 aports
aports
├── CODINGSTYLE.md
├── COMMITSTYLE.md
├── README.md
├── community
├── main
├── non-free
├── scripts
├── testing
└── unmaintained
```

## Bootstrapping

I am going to illustrate with a package I added recently, [`sensible-utils`][sensible-utils]:

- Before you even begin, check if the package already exists, do a quick search in the [Alpine Repositories](https://pkgs.alpinelinux.org/packages?name=sensible%2Dutils)[^1].

- Start by scaffolding a new `APKBUILD` from the base template:

```shell
$ cd aports/testing  # Always add new packages in testing/ first.
$ newapkbuild sensible-utils
$ cd sensible-utils
$ $EDITOR APKBUILD
```

**Note**: If you have a language-specific package (e.g. perl, python, rust),
use the language-specific template instead of the base one. Run `newapkbuild
-h` to list available templates. There are also some `apkbuild-*` helpers such
as `apkbuild-pypi` and `apkbuild-cpan`.

- Fill in `APKBUILD` metadata like `pkgname=`, `url=`, etc. Refer to the AlpineWiki for up-to-date best practices.

- By doing so, I produced the following `APKBUILD`:

```bash
pkgname=sensible-utils
pkgver=0.0.14
pkgrel=0
pkgdesc="Utilities for sensible alternative selection"
url="https://packages.debian.org/source/sensible-utils"
arch="all"
license="GPL-2.0-or-later"
makedepends="po4a"
subpackages="$pkgname-doc"
source="http://ftp.debian.org/debian/pool/main/s/$pkgname/${pkgname}_$pkgver.tar.xz"
builddir="$srcdir/$pkgname.git"

build() {
	./configure --prefix=/usr
	make
}

check() {
	make -k check
}

package() {
	make DESTDIR="$pkgdir/" install

	# only works with update-alternatives, specific to debian
	rm "$pkgdir/usr/bin/select-editor"
}

sha512sums="
15ba996f811ab3a9c1f5726f35766d74aafdf925c5c2392b33c6643d6c439796a742f9d0f4625c79de640e6b5e4a6a032b768eb1bc4ac31b448f9767b0ceed44  sensible-utils_0.0.14.tar.xz
"
```

**Note**: `$srcdir` refers to the `src/` directory within `sensible-utils`. `$pkgdir`
refers to the `pkg/` directory within `sensible-utils`.

If you're used to Arch Linux `PKGBUILDs` you'll notice a striking similarity to
`APKBUILDs`. I highlighted a few notable differences in a previous post, [`My
First APKBUILD`]({{< ref "2022-01-07-my-first-apkbuild#build-comparison" >}}).

## Adjustments

- Generate the checksums with `abuild checksum`. It will automatically update the `APKBUILD` inplace.

- Download and extract package files with `abuild unpack`.

- `ls src/` and check the directory structure. Update `$builddir` in your
  `APKBUILD` to match it. Usually it will be `$srcdir/$pkgname-$pkgver`, but
  sometimes tiny adjustments are necessary. In this case, it was
  `$srcdir/$pkgname.git`.

- Then run `abuild -r`. If everything goes well, your package (and subpackages,
  if any) will be successfully built[^2] in an isolated environment and placed
  in `~/packages` (`sensible-utils-0.0.14-r0.apk` and
  `sensible-utils-doc-0.0.14-r0.apk`), however that doesn't mean it is a decent
  package yet.

- Run `apkbuild-lint APKBUILD` and `abuild validate`[^4] to lint your package
  and catch common errors. Fix the errors, if any.

## Request feedback if needed

If the package is only relevant to you, stop here. `git commit`, `git push`, and then you're done. Install the package with `doas apk add <pkg>`.

Otherwise, if the package might be potentially useful to other Alpine users, you could consider uploading it to the [aports][aports] repository.

Before you do so, stop for a moment and make an honest judgment whether this is a high quality package and whether you're confident it is clean and polished enough, following the best practices documented in the Wiki. The answer doesn't need to be positive, it's perfectly OK to commit mistakes and everyone is a newbie at some point.

If the answer is negative, or if you're new to this process and would like some help, fear no more! There are at least two decent community resources wherein to ask for help:

1. [`#alpine-devel` on OFTC IRC](https://wiki.alpinelinux.org/wiki/Alpine_Linux:IRC) Drew DeVault wrote a good [post](https://drewdevault.com/2021/11/24/A-philosophy-for-instant-messaging.html) about IRC etiquette.

2. [`alpine-devel` mailing list](https://wiki.alpinelinux.org/wiki/Alpine_Linux:Mailing_lists).

If you're part of any other community (e.g. Reddit, Discord) feel free to ask therein as well. Avoid posting everywhere though, pick one community, draft your post and then patiently wait.

## Publish your package

If all is well, it's time to publish your `APKBUILD`. Follow the up-to-date
steps at
https://wiki.alpinelinux.org/wiki/Creating_an_Alpine_package#Code_review. There are basically two options:

1. Send a gitlab merge request (MR). This follows the standard git forge workflow
   (GitHub / BitBucket / GitLab) wherein you fork the main repository, create
   a branch in your own clone, push it and then initiate a pull request[^3].

2. Alternatively, send an email with your patch to the `aports` mailing list
   with [`git send-email`][git-send-email]:

```shell
$ git config sendemail.to "alpine-aports@lists.alpinelinux.org"
$ git send-email -1  # Implicitly uses --to=alpine-linux@lists.alpinelinux.org as set above
```

**Tip**: The second approach has a steep learning curve, however once you
figure it out it's actually faster, simpler and more streamlined. Whenever
a new email is sent to the aports mailing list, a MR is automatically created
on GitLab.

**Note**: If you adopt the email workflow and need to send a follow-up to your
initial patch, do not use `--in-reply-to`. Instead, create a new email thread.
This is needed because as of this post new GitLab MRs are only created when new
email threads are created. Replies to existing email threads do not update the
MR patch.

And that's all! Other useful tips:

- Use [repology][repology] to look for preexisting packages in other Linux (or even BSD) distributions, it's very handy as a starting point if you have no idea how to package a given package. In particular, Arch Linux `PKGBUILDs` are very similar to `APKBUILDs`. Gentoo `EBUILDs` and FreeBSD `Makefiles` are also reasonable approximations.
- Use `abump` to bump pkgver in `APKBUILD` files if the package gets an update to a newer upstream release.
- Use `apkgrel` to bump or reset the `pkgrel` value of your `APKBUILD`.
- Use [`urlwatch`]({{< ref "2022-01-18-arch-linux-new-pkgbuild-workflow#bonus-track-upstream" >}}) to track upstream updates.

[alpine-linux]: https://alpinelinux.org/
[alpine-wiki]: https://wiki.alpinelinux.org/wiki/Main_Page
[aports]: https://gitlab.alpinelinux.org/alpine/aports
[git-send-email]: https://git-send-email.io/
[repology]: https://repology.org/
[sensible-utils]: https://packages.debian.org/source/sensible-utils

[^1]: If you use https://duckduckgo.com/, query for `!alpine sensible-utils`.
[^2]: Package debugging is out of scope of this post.
[^3]: In GitLab it's called Merge Request (MR). The list of all aports MRs is [available on GitLab](https://gitlab.alpinelinux.org/alpine/aports/-/merge_requests).
[^4]: **Update(2025-05-10)**: Previously: `abuild sanitycheck`.
