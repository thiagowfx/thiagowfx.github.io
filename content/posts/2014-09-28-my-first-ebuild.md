---
title: "My first ebuild"
date: 2014-09-28T03:24:00+00:00
tags:
  - dev
  - legacy
---

> Ebuilds are not evil
>
> — _Larry, the Cow_

~~From now on, this will be my overlay repository: https://github.com/thiagowfx/overlay~~

I might change its name in the future, however it will probably remain on GitHub. From my experience with this blog, I realized it would be better to leave a copy of this ebuild here:

```bash
# Copyright 1999-2014 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Header: $
EAPI="5"

inherit font

DESCRIPTION="A font specially designed for comfortably reading on any computer or device"
HOMEPAGE="http://www.huertatipografica.com/fonts/bitter-ht"
SRC_URI="http://www.fontsquirrel.com/fonts/download/${PN}"

LICENSE="OFL"
SLOT="0"
KEYWORDS="amd64 ~arm ~arm64 ~ppc ~ppc64 x86"
IUSE=""
HDEPEND="app-arch/unzip"

FONT_SUFFIX="otf"
S="${WORKDIR}"

src_unpack() {
  mv "${DISTDIR}/${A}" "${DISTDIR}/${A}.zip"
  unpack "${A}.zip"
}

src_install() {
  FONT_S="${WORKDIR}" font_src_install
}
```

My **conclusion**? Writing ebuilds is nice, very nice (yeah, more complex than writing PKGBUILDs, I know, but at least this complexity is justified).

_Edit_: Thanks Buss for pointing me out a small error (`RDEPEND`, instead of `HDEPEND`).
