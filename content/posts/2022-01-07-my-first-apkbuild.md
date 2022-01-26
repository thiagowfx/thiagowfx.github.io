---
title: "My First APKBUILD"
date: 2022-01-07T20:03:07-05:00
tags:
  - linux
---

In the same spirit of my first [`PKGBUILD`]({{< ref "2014-02-13-meu-primeiro-pkgbuild.md" >}}) and [`Ebuild`]({{< ref "2014-09-28-my-first-ebuild.md" >}}), herein I will describe my first `APKBUILD`.

<!--more-->

## At a glance

Alpine Linux package management is very similar to Arch Linux, with tiny differences:

- `PKGBUILD` → `APKBUILD`: The filename is obviously different. Their format are very similar though, both of them are bash scripts with variables and functions. In particular, there's `check`, `patch`, `build` and `package`.
- `cp /usr/share/pacman/PKGBUILD.proto` → `newapkbuild`: Template versus scaffolding.
- `pacman` → `apk`: The package manager is different.
- `makepkg -s` → `abuild -r`: `makepkg` drives all things package building for `pacman`. `abuild` drives package building for `apk`.
- `makepkg -i` → `apk add <pkg>`: `makepkg` can also drive package installations whereas `abuild` cannot, `apk` must be used.
- `namcap` → `apkbuild-lint` (from `atools`) + `abuild sanitycheck`[^lint]: Linters are different.
- `updpkgsums` → `abuild checksum`: Generate hashes for package sources.

{{< figure align="center" src="https://imgs.xkcd.com/comics/standards.png" link="https://xkcd.com/927/" alt="Fortunately, the charging one has been solved now that we've all standardized on mini-USB. Or is it micro-USB? Shit." attr="XKCD Courtesy of Randall Munroe" >}}

Other than that, the process of writing an `APKBUILD` is very similar to writing a `PKGBUILD`. In fact, the Arch repositories (especially the [AUR][aur]) tend to be much more comprehensive than Alpine's in terms of number of packages, so chances are if you want to write a new package for Alpine, check in Arch's repos first, it's a good starting point.

## My first package: `fpp`

`fpp` stands for 'Facebook Path Picker'.

As of the time of this post, I maintain [`fpp-git`][fpp-git] in the AUR. It looks like this:

```bash
pkgname=fpp-git
pkgver=0.9.2.r130.ge0d5cfc
pkgrel=1
pkgdesc='TUI that lets you pick paths out of its stdin and run arbitrary commands on them'
url='https://facebook.github.io/PathPicker'
license=('MIT')
source=("${pkgname%-git}::git+https://github.com/facebook/PathPicker.git")
sha256sums=('SKIP')
arch=('any')
makedepends=('git')
depends=('python')
conflicts=("${pkgname%-git}")
provides=("${pkgname%-git}")

prepare() {
  cd "$srcdir/${pkgname%-git}"
  rm -r "src/tests"
}

pkgver() {
  cd "$srcdir/${pkgname%-git}"
  git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

package() {
  cd "$srcdir/${pkgname%-git}"

  # library
  install -Dm755 "fpp" -t "$pkgdir/usr/share/fpp"
  cp -a src "$pkgdir/usr/share/fpp"

  # entrypoint
  install -dm755 "$pkgdir/usr/bin"
  ln -s "/usr/share/fpp/fpp" "$pkgdir/usr/bin"

  # documentation
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 "debian/usr/share/man/man1/fpp.1" -t "$pkgdir/usr/share/man/man1"
}
```

`PKGBUILD` guidelines and instructions:

- https://wiki.archlinux.org/title/PKGBUILD
- https://wiki.archlinux.org/title/Arch_package_guidelines

The equivalent `APKBUILD` I wrote looks like this:

```bash
pkgname=fpp
pkgver=0.9.2
pkgrel=0
pkgdesc="TUI that lets you pick paths out of its stdin and run arbitrary commands on them"
url="https://facebook.github.io/PathPicker"
arch="noarch"
license="MIT"
depends="bash python3"
subpackages="$pkgname-doc"
source="$pkgname-$pkgver.tar.gz::https://github.com/facebook/PathPicker/archive/$pkgver.tar.gz"
builddir="$srcdir/PathPicker-$pkgver"

check() {
	fpp --version
}

prepare() {
	default_prepare

	rm -r "src/__tests__"
}

package() {
	# library
	install -Dm755 "fpp" -t "$pkgdir/usr/share/fpp"
	cp -a src "$pkgdir/usr/share/fpp"

	# entrypoint
	install -dm755 "$pkgdir/usr/bin"
	ln -s "/usr/share/fpp/fpp" "$pkgdir/usr/bin"

	# documentation
	install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
	install -Dm644 "debian/usr/share/man/man1/fpp.1" -t "$pkgdir/usr/share/man/man1"
}

sha512sums="
65b6b077f437bd642ebf94c55be901aabc73f7b9c89e4522c4f51970c4d63d744ad8fa29cac06816851f63bcb81d0480e61d405231c582e9aca0f4e650949a97  fpp-0.9.2.tar.gz
"
```

`APKBUILD` guidelines and instructions:

- https://wiki.alpinelinux.org/wiki/Creating_an_Alpine_package
- https://wiki.alpinelinux.org/wiki/APKBUILD_Reference

## Build Comparison

Let's highlight a few similarities and differences in them, excluding the fact that one is fetched from git and the other one fetches a point release directly[^release]:

- package metadata, by the means of bash variables, are almost equivalent
  one-to-one
  - A notable difference is the architecture, Arch primarily supports
    _x86_64_ whereas Alpine has support for multiple architectures. When
    a package is architecture agnostic, Arch denotes it with `any` whereas
    alpine has both `noarch` and `all`, the latter is like `any` (=all
    architectures), the `former` means it's agnostic (=e.g. a pure bash script
    or python package).
  - `APKBUILDs` use flat strings, whereas `PKGBUILDs` use bash arrays
  - Alpine encourages splitting larger packages into subpackages, as such
    `APKBUILD` has first-class support and syntactic sugar for that. `-dev` and
    `-doc` subpackages are very common. On the other hand, Arch tends to have
    monolithic packages in order to keep it simple, although it also supports
    subpackages.
  - Alpine supports setting `$builddir` whereas Arch doesn't. As a consequence, it's often unneeded to `cd` in `build()` and `package()` in Alpine, whereas in Arch one does need to manually change directories to `$srcdir/$pkgname` before building.
  - Alpine lacks optional dependencies, whereas Arch has `optdepends`.
- Alpine enforces the use of `check` in test packages, otherwise it needs to be explicitly disabled and documented with `!check` in `options=`. That's not the case in Arch.
- `check()`, `build()` and `package()` are pretty much similar in both formats. `$srcdir` and `$pkgdir` are provided in both.
- The [ArchWiki][archwiki] is way more documented in terms of packaging guidelines and examples than Alpine's. If you use DuckDuckGo, you can query for `!aw <foo>` as a bang shortcut to search directly in the ArchWiki.

Last but not least, in Arch one can install package tarballs[^tarball] with `makepkg -i` or `pacman -U`. In Alpine that approach doesn't seem to be directly supported. The workflow is to add a local repository diretory in `/etc/apk/repositories` (notice the last two lines):

```shell
$ cat /etc/apk/repositories
# http://dl-cdn.alpinelinux.org/alpine/v3.15/main
# http://dl-cdn.alpinelinux.org/alpine/v3.15/community
# http://dl-cdn.alpinelinux.org/alpine/latest-stable/main
# http://dl-cdn.alpinelinux.org/alpine/latest-stable/community
http://dl-cdn.alpinelinux.org/alpine/edge/main
http://dl-cdn.alpinelinux.org/alpine/edge/community
http://dl-cdn.alpinelinux.org/alpine/edge/testing
/home/$USER/packages/community
/home/$USER/packages/testing
```

`abuild` will place the resulting package tarball in `~/packages`, in this case:

```shell
$ ls ~/packages/testing/x86_64/fpp*
/home/$USER/packages/testing/x86_64/fpp-0.9.2-r0.apk
/home/$USER/packages/testing/x86_64/fpp-doc-0.9.2-r0.apk
```

...and then `apk add fpp` will automagically recognize it's in there and install it. The advantage of this approach is that it keeps a local package repository around and it's well integrated with `apk`, way differently from `pacman` that has no integration with the AUR at all. One could also possibly set up a local repository in Arch, for example, with [`ccm`][ccm], but it takes extra steps and it's not officially supported.

## Upstream Contributions

On Arch, to contribute a `PKGBUILD` upstream one just needs to create an account in the [AUR][aur]. Armed with a git + ssh infrastructure, all you need to do is `git push`. There are no ACLs involved, anyone can do that[^acl].

On Alpine there's a bit more of politics involved[^politics]: Anyone can send a `patch(1)`, either via [mailing list][aports-list] or via a [Gitlab MR][aports-gitlab] (merge request). Patch works well with `git send-email -1`, being automatically cross-posted to a Gitlab MR. On the other hand the MR workflow is easier to be followed up on feedback from developers and other contributors (`git push --force`), and it's also cross-posted, to the mailing list. An Alpine developer with the appropriate permissions must approve your patch/MR before it becomes available to other Alpine users.

Sadly at the time of this writing [my patch][my-patch] hasn't yet been approved (2 weeks later), however we're in holiday season. This wouldn't have been a problem in the AUR, where I could have just pushed it immediately, without any review. On the other hand the Alpine approach at least gives me some hope that the submitted packages have slightly higher quality than the average ones in the AUR, since they need to be manually reviewed/approved/vetted by at least one Alpine developer.


[archwiki]: https://wiki.archlinux.org/title/Main_page
[aur]: https://aur.archlinux.org/
[aports-list]: mailto:alpine-aports@lists.alpinelinux.org
[aports-gitlab]: https://gitlab.alpinelinux.org/alpine/aports
[ccm]: https://github.com/graysky2/clean-chroot-manager
[fpp-git]: https://aur.archlinux.org/packages/fpp-git/
[my-patch]: https://lists.alpinelinux.org/~alpine/aports/patches/3799

[^release]: The AUR tends to have both non-vcs and vcs versions of a software, whereas Alpine is focused a bit more on stability and tends to have non-vcs only. This is not a hard rule though, exceptions may exist.
[^lint]: Install `spdx-licenses-list` to lint the licenses, it's used by `abuild sanitycheck` as an optional dependency.
[^tarball]: `.tar.xz` or, more recently, `.tar.zstd`.
[^acl]: And this is one of the reasons why you should always inspect every `PKGBUILD` you install from the Arch User Repository, as it could have been tampered with and/or contain malicious code.
[^politics]: I'll leave it open-ended whether that's a bug or a feature. Depending on the lens you see through, it could be considered either gatekeeping (bureaucracy, control) or sanity (quality, stability). It has pros and cons, and even those are arguable.
