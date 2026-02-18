
I struggled a little to get started with Ogre3d graphics, so here are a few
notes. In this post we will be able to run some basic examples from the
framework.

## Installation

Get a distribution with a nice packaging system and install ogre from it. I can
cite two: Arch Linux family (pacman-based) or Gentoo family (portage-based). The
point is: **DON'T** install the ogre package from **deb-based** distros (Debian
and Ubuntu).

They have a few problems:

### 1.1 Packages are usually outdated

In the case of ogre, this isn't a super problem. Its current version is 1.9, and
Ubuntu offers 1.8. You can live with that.

### 1.2 Some files are missing from the packages

I compared the upstream ogre tree (from Bitbucket) with files installed on
Ubuntu (`dpkg-query -L libogre-1.8-dev`), and some files were missing. One
example: SDK Trays.

### 1.3 Some files are installed in non-standard locations

For example, `x86_64-linux-gnu` being used as a directory. This is non-standard.
And what about `/usr/lib/ogre`? This folder doesn't even exist on Ubuntu, but
should!

Worse yet: Ogre documentation assumes the default installation directory is
`/usr/local`. This assumes you don't use a package manager and used `make
install` after compiling, which requires `sudo` rights. This is too restrictive.
Everything that ends up in `/usr/local` (programs installed manually) eventually
becomes a mess.

**Disclaimer**: I'm not trying to convince you not to use Ubuntu for ogre3d
development. I'm just stating I had an awful experience. If you can handle it,
please comment how you did that!

I'm using Arch for ogre3d development now; if forced to use Ubuntu (work, lab),
I'll have to install ogre locally on the system.

## Building with Arch

```bash
pacman -Syu ogre
```

Now see if you can run the most basic pre-example from Ogre. Download it. Files include:

- ogreapp
  - CMakeLists.txt
  - BaseApplication.h
  - BaseApplication.cpp
  - TutorialApplication.h
  - TutorialApplication.cpp
- dist/ folder

There's a `CMakeLists.txt`, so the build should be straightforward. Create your
build directory, `cd` into it, `cmake ..` and `make`. Copy the **OgreApp**
executable into the dist folder manually.

**Note**: The build system could be better. Just do it.

There's a warning: see the plugins.cfg config file. Change `/usr/local/lib/OGRE`
to `/usr/lib/OGRE`.

## Basic Example 1

Get it from Ogre Basic Tutorial 1. Uncompress it, move its files to a 'basic1'
directory, and copy CMakeLists.txt and dist/ from the previous example. Copy and
paste the code from the wiki to `TutorialApplication::createScene` in
TutorialApplication.cpp. Build as usual, and copy the OgreApp executable to the
dist/bin directory. Done!

**PS**: I'll likely write another post about Ogre.

## Footnotes

- The problem isn't cmake (I had experience with it). The problem is the
  documentation. Ogre's wiki is scattered. There should be one entry point for
  "getting started with ogre", but there are several. A typical beginner
  struggles to decide which one to begin with. Documentation outside ogre3d.org
  is poor—forums, Reddit, blogs are either inactive, old, or poor.
- **Bias**: I love both Arch and Gentoo.
- **PPAs?** Please don't use them.

