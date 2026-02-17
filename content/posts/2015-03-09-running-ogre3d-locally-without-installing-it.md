---
title: "Running Ogre3d locally (without installing it)"
date: 2015-03-09T03:05:25-03:00
tags:
  - dev
  - legacy
---

[![simple build systems, huh?](https://thiagoperrotta.files.wordpress.com/2015/03/11056835_726102464175254_2082355176_n.jpg?w=300)](<https://thiagoperrotta.files.wordpress.com/2015/03/11056835_726102464175254_2082355176_n.jpg>) simple build systems, huh? Hello there. In this post we will run the "Basic 1" example from the [Ogre3d wiki](<http://www.ogre3d.org/tikiwiki/tiki-index.php>) without installing [ogre](<http://www.ogre3d.org/>) in the system. For that, I'll assume you're using a *nix system. First things first: grab the latest ogre version. At the time of this post, it is the 1.9 release, and you can find its repository [on Bitbucket](<https://bitbucket.org/sinbad/ogre/downloads>). **Note:** you want to download the 1.9 version using the tag download feature from Bitbucket; **do not** simply download the master branch. After that, extract it, create a build directory inside its directory, cd into it, and do a

    cmake .. -DCMAKE_INSTALL_PREFIX=$HOME/.lib -DOGRE_INSTALL_SAMPLES=TRUE -DOGRE_INSTALL_DOCS=TRUE -DOGRE_INSTALL_SAMPLES_SOURCE=TRUE -DCMAKE_BUILD_TYPE=Release

This is a pretty much standard cmake build. If your system is missing some of its dependencies, you will be warned and you should install them. Then:

    make OgreDoc install

Now it is a good moment to read [xkcd](<https://xkcd.com/303/>). The usual difference here is that we don't do a normal **make install**. Why? Because we don't want our stuff ending up on **/usr/local.** Instead, we want it somewhere where we have full access as a normal (non-root) user -- in this example, **$HOME/.lib/ogre**.

## Basic 1

Now, head to the [basic 1](<http://www.ogre3d.org/tikiwiki/tiki-index.php?page=Basic+Tutorial+1>) page of the ogre wiki and download its example. You should try to build it, but take care to change all ogre3d references from /usr/local to your new install directory ($HOME/.lib/ogre). Yeah, that's it. **Note:** if the _basic 1_ download doesn't come with a CMakeLists.txt file, you can download it from [the Ogre CMake wiki page](<http://www.ogre3d.org/tikiwiki/tiki-index.php?page=Building+Your+Projects+With+CMake>) (clean ogre cmake project). You can use it verbatim; just put it in the same directory as the basic 1 files **and** \-- again -- change any references to _/usr/local_ to your new install directory. Also, copy the **dist/** directory too (if it is missing from the Basic 1 project), I'll add a small observation: in the case cmake complains about pkg-config, try adding this line to the top of your CMakeLists.txt (but after the project version):

    set(ENV{PKG_CONFIG_PATH} "$ENV{HOME}/.lib/ogre/lib/pkgconfig:$ENV{PKG_CONFIG_PATH}")

**Credits:** the build style I adopted here was derived from the [Ogre Arch Linux package.](<https://projects.archlinux.org/svntogit/community.git/tree/trunk/PKGBUILD?h=packages/ogre>) Thanks Sven for your excellent packaging skills! :) **Update:** in your _plugins.cfg_ , **do not** use "$HOME" as your PluginFolder. This seems to cause issues when you run your ogre app. Instead, expand $HOME manually (in my case, to '/home/thiago'). This is not much portable, I know, but there must be some workaround for this I haven't discovered yet.

## Footnotes

* Image credit: a screenshot from the "Clean Code" software engineering book by Robert C. Martin (a good one, by the way).
