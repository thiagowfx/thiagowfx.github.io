---
title: "Arch Linux: New PKGBUILD Workflow"
date: 2022-01-18T21:59:07-05:00
tags:
  - dev
  - linux
  - bestof
---

This document describes my workflow to manage `PKGBUILDs` for the [AUR][aur] (Arch User Repository) in [Arch Linux][arch-linux].


## Disclaimer

First of all, this post is not a substitute to the excellent [ArchWiki][arch-wiki] and it will likely get outdated at some point. In particular, refer to the following articles for up-to-date documentation that will outlive this blog:

- https://wiki.archlinux.org/title/Arch_User_Repository
- https://wiki.archlinux.org/title/Arch_package_guidelines
- https://wiki.archlinux.org/title/Creating_packages
- https://wiki.archlinux.org/title/PKGBUILD

This article is not a tutorial, as such it assumes you already know what a `PKGBUILD` is and how to use `makepkg`. In particular, you should have the `base-devel` and `devtools` packages installed in your system.

## Structure

I manage my packages with `git` plus Eli Schwartz's excellent
[aurpublish][aurpublish]. The tree structure is simple, with one `PKGBUILD` per directory:

```shell
$ git clone https://github.com/thiagowfx/PKGBUILDs && tree PKGBUILDs
PKGBUILDs
├── bkt
│   └── PKGBUILD
├── fpp-git
│   └── PKGBUILD
├── git-crecord
│   └── PKGBUILD
├── i3a
│   └── PKGBUILD
├── LICENSE
├── Makefile
├── README.md
├── ttf-camingocode
│   └── PKGBUILD
└── urlwatch.yml
```

`aurpublish` is used _solely_ to automate certain interactions with the AUR, more about it later.

## Bootstrapping

I am going to illustrate with a package I added recently, [`bkt`][bkt]:

- Before you even begin, check if the package already exists, do a quick search in the [AUR](https://aur.archlinux.org/packages/?O=0&K=bkt) and also in the [official repos](https://archlinux.org/packages/?sort=&q=bkt&maintainer=&flagged=)[^3].

- Start by copying over the standard `PKGBUILD` template:

```shell
$ cd PKGBUILDs
$ mkdir bkt && cd bkt
$ cp /usr/share/pacman/PKGBUILD.proto PKGBUILD
$ $EDITOR PKGBUILD
```

- Fill in `PKGBUILD` metadata like `pkgname=`, `url=`, etc. Refer to the ArchWiki for up-to-date best practices.

- The most important step is to refer to https://wiki.archlinux.org/title/Category:Arch_package_guidelines to figure out the package type.

`bkt` is a Rust package. This is my first time packaging for Rust, not a problem though, as I can just refer to https://wiki.archlinux.org/title/Rust_package_guidelines.

The rust package guidelines page contains the blueprint for `prepare()`, `check()`, `build()` and `package()`. Packaging is mostly a matter of gluing everything together. Read the project `README.md` and the wiki, and then combine the needed steps in the `PKGBUILD`.

By doing so, I produced the following `PKGBUILD`:

```bash
pkgname=bkt
pkgver=0.5.0
pkgrel=1
pkgdesc="A subprocess caching utility"
arch=('x86_64')
url="https://www.bkt.rs/"
license=('MIT')
makedepends=('cargo')
source=("$pkgname-$pkgver.tar.gz::https://github.com/dimo414/$pkgname/archive/refs/tags/$pkgver.tar.gz")
sha256sums=()

prepare() {
	cd "$srcdir/$pkgname-$pkgver"

	cargo fetch --locked --target "$CARCH-unknown-linux-gnu"
}

build() {
	cd "$srcdir/$pkgname-$pkgver"

	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	cargo build --frozen --release --all-features
}

check() {
	cd "$srcdir/$pkgname-$pkgver"

	export RUSTUP_TOOLCHAIN=stable
	cargo test --frozen --all-features
}

package() {
	cd "$srcdir/$pkgname-$pkgver"

	install -Dm0755 -t "$pkgdir/usr/bin/" "target/release/$pkgname"
	install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
}
```

**Note**: `$srcdir` refers to the `src/` directory within `bkt`. `$pkgdir` refers to the `pkg/` directory within `bkt`.

## Adjustments

- Generate the checksums with `updpkgsums`. It will automatically update the `PKGBUILD` inplace.

- Download and extract package files with `makepkg -o`.

- `ls src/` and check the directory structure. Update `cd` in your `PKGBUILD` to match it. Usually it will be `cd $srcdir/$pkgname-$pkgver`, but sometimes tiny adjustments are necessary.

- Then run `makepkg -s`. If everything goes well, your package will be successfully built[^1] (`bkt-0.5.0-1-x86_64.pkg.tar.zst`), however that doesn't mean it is a decent package yet.

- Run `namcap PKGBUILD` and `namcap *.pkg.tar.zst` to lint your package and catch common errors. Fix the errors, if any.

- To ensure all dependencies have been correctly declared and none of them are missing, run `makepkg` within a clean [_chroot_][chroot]. I like to use Graysky's excellent [`ccm`][ccm] (Clean Chroot Manager) to do so. Run `ccm s` (="run makepkg in the clean chroot"). If it produces any errors, it likely means you missed some dependencies. Adjust `depends=`, `checkdepends=` and `makedepends=` accordingly.

## Request feedback if needed

If the package is only relevant to you, stop here. `git commit`, `git push`, and then you're done. Install the package with `makepkg -i`.

Otherwise, if the package might be potentially useful to other Arch users, you could consider uploading it to the AUR.

Before you do so, stop for a moment and make an honest judgment whether this is a high quality package and whether you're confident it is clean and polished enough, following the best practices documented in the Wiki. The answer doesn't need to be positive, it's perfectly OK to commit mistakes and everyone is a newbie at some point.

If the answer is negative, or if you're new to this process and would like some help, fear no more! There are at least two decent community resources wherein to ask for help:

1. [AUR Issues, Discussion & PKGBUILD Requests](https://bbs.archlinux.org/viewforum.php?id=38.) BBS / Forums:  Open a new thread, post your `PKGBUILD` (use `[code][/code]` tags if you paste it directly!) or a link to it[^2]. Request folks to critique your work, mention that you're looking for feedback. This kind of thread is generally well received in the official forums if you demonstrate you did diligent research before asking for help.

2. [AUR General Mailing List](https://lists.archlinux.org/pipermail/aur-general/): Send an email to the mailing list asking for help. In general, follow proper mailing list etiquette, good resources for that are https://useplaintext.email/ and https://man.sr.ht/lists.sr.ht/etiquette.md. TL;DR: Use plain-text instead of HTML in your email.

If you're part of any other community (e.g. Reddit, Discord) feel free to ask therein as well. Avoid posting everywhere though, pick one community, draft your post and then patiently wait.

## Publish your package

If all is well, it's time to publish your `PKGBUILD` to the [AUR][aur]. Follow the up-to-date steps at https://wiki.archlinux.org/title/Arch_User_Repository#Submitting_packages.

TL;DR: If you don't use _aurpublish_, do:

```shell
$ makepkg --printsrcinfo > .SRCINFO
```

Then you'll need both the `PKGBUILD` and the `.SRCINFO` file, it's basically a matter of committing your changes and pushing them to the right repository.

If you do use _aurpublish_ this process is much easier, it's mostly a matter of doing `git commit`, `git push` and `aurpublish bkt`. _Aurpublish_ automatically generates the `.SRCINFO` and a commit message by the means of git hooks.

And that's all! Other useful tips:

- Use [repology][repology] to look for preexisting packages in other Linux (or even BSD) distributions, it's very handy as a starting point if you have no idea how to package a given package. In particular, Alpine Linux `APKBUILDs` are very similar to `PKGBUILDs`. Gentoo `EBUILDs` and FreeBSD `Makefiles` are also reasonable approximations.
- Use `makepkg -src` to clean up after building a package.

## Bonus: Track upstream

Use a software like [`urlwatch`][urlwatch] or [`nvchecker`][nvchecker] to track
future upstream changes so that you can update your packages in a timely
fashion[^4]. There's also a web service called [Release
Monitoring][release-monitoring], part of Fedora Infra. I use `urlwatch` the
following way:

```
$ cat PKGBUILDs/urlwatch.yml
# urls for urlwatch(1)
---
name: "bkt"
command: "git ls-remote --tags https://github.com/dimo414/bkt"
---
name: "fpp"
command: "git ls-remote --tags https://github.com/facebook/PathPicker"
---
name: "git-crecord"
command: "git ls-remote --tags https://github.com/andrewshadura/git-crecord"
---
name: "i3a"
command: "git ls-remote --tags https://git.goral.net.pl/mgoral/i3a"
# ---
# name: "ttf-camingocode"
# N/A

# Run this command periodically via cron or systemd timer.
# Set up notifications e.g. via sendmail.
$ urlwatch --urls urlwatch.yml
```

[aur]: https://aur.archlinux.org/
[arch-linux]: https://www.archlinux.org/
[arch-wiki]: https://wiki.archlinux.org/
[aurpublish]: https://github.com/eli-schwartz/aurpublish
[bkt]: https://github.com/dimo414/bkt
[ccm]: https://github.com/graysky2/clean-chroot-manager
[chroot]: https://wiki.archlinux.org/title/Chroo
[nvchecker]: https://github.com/lilydjwg/nvchecker
[release-monitoring]: https://release-monitoring.org/
[repology]: https://repology.org/
[urlwatch]: https://thp.io/2008/urlwatch/

[^1]: Package debugging is out of scope of this post.
[^2]: For example, use https://gist.github.com or http://paste.opensuse.org/ or
  http://ix.io/.
[^3]: If you use https://duckduckgo.com/, query for `!aur bkt` and `!archpkg
  bkt`. Handy!
[^4]: In 99% of the cases this is just a matter of bumping the `pkgver=` and
  updating the checksums. If `pkgver=` is the same but there's a fix to the
  package itself, then bump `pkgrel=` instead.
