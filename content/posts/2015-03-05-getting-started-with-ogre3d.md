---
title: Getting started with Ogre3d
date: 2015-03-05T16:46:49+00:00
tags:
  - classics
  - programming
showtoc: true
---

I struggled a little[^1] to get started with Ogre3d graphics, so here are a few notes. In this post we will be able to run some basic examples from the Ogre3d framework.

<!--more-->

1. Get a distribution with a nice packaging system[^2] and install ogre from it. I can cite two of them: Arch Linux family (pacman-based) or Gentoo family (portage-based). The point is: **DON&#8217;T **install the ogre package from **deb-based** distros (those include Debian and Ubuntu). They have a few problems:

    1.1 Packages are usually outdated[^3]. In the case of ogre, this is not a super problem. Its current version is 1.9, and the available one in Ubuntu is 1.8. Even if you can live with that, don&#8217;t install Ogre3d on Ubuntu. Keep reading.

    1.2 Some files are missing from the packages. Yeah, and I&#8217;m pretty sure of that. I compared the upstream ogree tree (from mercurial/BitBucket) with the files that are installed on Ubuntu (`dpkg-query -L libogre-1.8-dev`), and some files were missing, period. One example I recall? `SdkTrays`.

    1.3 Some files are installed in non-standard locations. I can&#8217;t list them because I&#8217;m not using an Ubuntu distro right now, but I remember, for example, `x86_64-linux-gnu` (or something along these lines) being used as a directory. Really? This is non-standard. And what about `/usr/lib/ogre`? This folder doesn&#8217;t even exist on Ubuntu. And it should!

Worse yet? Ogre documentation assumes the default installation directory is **/usr/local**. In other words, it assumes you don&#8217;t use a package manager at all, **plus** you used `make install` after compiling it, which implies you must have `sudo` rights on the system. This is simply too restrictive. Also, we all know everything that ends up on `/usr/local` (=programs installed manually by the user, without a package manager) sooner or later turns into a mess.

Okay, that said, please notice I&#8217;m not trying to convince yourself not to use Ubuntu for ogre3d development. I&#8217;m just stating I had an awful experience with it. You do whatever you want, okay? Also, if you can handle ogre3d on Ubuntu, please leave a comment telling me how you did that.

I&#8217;m using Arch to do ogre3d development from now on; and, if I&#8217;m ever forced to use Ubuntu (for example, at work or at my lab at college), I&#8217;ll have to struggle to install ogre locally on the system. More on that later.

## `pacman -Syu ogre`

Now, see if you can run the most basic **pre-example** from Ogre. It is [here](http://www.ogre3d.org/tikiwiki/tiki-download_wiki_attachment.php?attId=186&download=y) This link will probably be broken in the future, so I&#8217;ll say those are the files from this example:

```
* ogreapp/ 
    * CMakeLists.txt (see below)
    * BaseApplication.h
    * BaseApplication.cpp
    * TutorialApplication.h
    * TutorialApplication.cpp
```

There is also a `dist` folder.

You see, it contains a `CMakeLists.txt`, so the build is (should be!) pretty straightforward. Well, not on Ubuntu&#8230;but I&#8217;m assuming we&#8217;re not using Ubuntu from this point, so, just create your build directory, `cd` into it, `cmake ..` and `make`.

Now, you&#8217;ll have to copy (manually) the **OgreApp** executable into the `dist` folder. This build system could be better, but&#8230;okay. Just do it. And it should work. Unless you&#8217;re using a virtual machine: this can cause problems if you forget to enable 3D acceleration. You have been warned.

Oh, just a little warning. See the `plugins.cfg` config file. You should probably change `/usr/local/lib/OGRE` to `/usr/lib/OGRE`.

## Basic Example 1

You should get it from [here](http://www.ogre3d.org/tikiwiki/Basic+Tutorial+1). Now what? Manual work: uncompress it, move its files to a `basic1` directory, and copy `CMakeLists.txt` and `dist/` from the previous example to `basic1`.

Then you will have do copy and paste the code from the wiki to `TutorialApplication::CreateScene` on `TutorialApplication.cpp`. Done? Now build as usual, and copy the `OgreApp` executable to the `dist/bin` directory. And we&#8217;re done.

**PS.** It is likely I&#8217;ll write another post about Ogre.

[^1]: Not really&#8230;a little? This must be a joke. **Note**: `cmake` wasn&#8217;t the problem, since I had experience with it. I think the problem is the documentation. Ogre&#8217;s wiki is way too scattered. There should be a single entry point on &#8220;getting started with ogre&#8221;, but there are several ones. A typical beginner (=me) will struggle to decide which one to begin with. Worse yet: documentation outside the ogre3d website is way too poor. Discussion forums, reddit, blog posts&#8230;no, all the ones that I&#8217;ve found are either inactive, old or poor. But now you know that: please don&#8217;t make the same mistakes I did.

[^2]: **Bias**: I like (correction, **love**) both Arch and Gentoo.

[^3]: PPAs? Please just don&#8217;t use them.