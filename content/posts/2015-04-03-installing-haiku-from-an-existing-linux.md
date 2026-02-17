---
title: 'Installing Haiku from an existing linux'
date: 2015-04-03T17:20:19-03:00
tags:
  - dev
  - legacy
---

## What&#8217;s Haiku in the first place?

It is an operating system, period. What might cause a small surprise is that it is not based either on Linux or on BSD &#8212; and yet it is (probably) runnable in your modern computer/laptop!

What I most like on it is that the system is integrated with the GUI, so the end user gets a nice experience. This is not so common as it sounds: most Linux distributions are simply a collection of programs and utilities put together in one place, but they are not necessarily integrated &#8212; however, **you** can integrate them. This makes all the difference between user-friendly and user-centered paradigms[^1].

Anyway, Haiku is simple, so for me this post is more a hobby than something useful that I will use in the future; however, I find that knowing about more and more about different operating systems has its own advantages.

For more, see https://www.haiku-os.org/about.

## Installing Haiku

**Note:** most of those instructions come from [the Haiku installation guide](https://www.haiku-os.org/guides/installing_haiku_image_disk_partition). Also, thanks David Couzelis for kindly giving me some advice and pointing me out to them.

1. Get Haiku. You can do it either from [the official download page](https://www.haiku-os.org/get-haiku), or get nightly releases from [the nightly builds page](http://download.haiku-os.org/nightly-images/x86_gcc2_hybrid/). I personally recommend the nightly releases; I first installed the latest non-nightly one, but later on I discovered that is was very old (circa 2012): it didn&#8217;t even have a package manager.
2. Which image should you download? In this post, I am assuming we&#8217;ll install Haiku directly to a (real) disk, so I&#8217;m downloading the **raw** image. Actually, the **anyboot** image can also be downloaded &#8212; and this is the one you will get if you opted for a non-nightly version; however, the anyboot image will be converted to a raw one in step 3 before we proceed. So, skip the next step if you downloaded the raw image.
3. Got your anyboot image? Now, convert it to raw (run this from a bash compatible shell):

```shell
$ dd if=haiku-anyboot.image of=haiku.raw bs=1M skip=$(expr $(od -j 454 -N4 -i -A n haiku-anyboot.image) / 2048)
$ dd if=/dev/zero of=haiku.raw bs=1 seek=506 count=4 conv=notrunc
```

**Update (2022)**: These days `dd` supports `status=progress` to display the image writing progress.

4. Now that we got a raw image, we are writing it directly to a disk partition. First things first: find 3GB or more of free space in your disk. Then create room for a partition in there (for example, with _fdisk_ or _gparted)_. Got it? Now create a partition in there. I&#8217;ll assume the partition is `/dev/sda42`. Please change 42 for the appropriate number in your case.
5. Copy the raw image to the partition (this should be done as ROOT); **WARNING**: double check the partition and the disk number, otherwise you might lose data.

```shell
$ dd if=haiku.raw of=/dev/sda42 bs=1M conv=notrunc
```

6. Make the installation _bootable_: you&#8217;ll need to compile and run the _makebootabletiny_ program, which can be downloaded from [the Haiku installation guide](https://www.haiku-os.org/guides/installing_haiku_image_disk_partition). It is a simple C program, so:

```shell
$ gcc makebootabletiny.c -o makebootabletiny
% ./makebootabletiny /dev/sda42  # this one: as ROOT
```

7. Make your bootloader know about Haiku. If you&#8217;re using `grub2`z, you can add something such as the following lines to `/etc/grub.d/40_custom`:

```shell
menuentry "Haiku OS" {
    set root(hd0,42)
    chainloader +1
}
```

8. Then run as root: _grub-mkconfig -o /boot/grub/grub.cfg_

**Done!** Now you should be able to boot into Haiku.

## Now what?

This post is not a review of Haiku, so I&#8217;m stopping here. However, if I write a review about Haiku, I&#8217;ll do that from Haiku 🙂.

I&#8217;m just leaving this here: https://www.haiku-os.org/slideshows/haiku-1

[^1]: By the way, Arch Linux is user-centered, which means that you&#8217;re supposed to integrate the system as you wish. If you don&#8217;t wish that then you&#8217;re screwed anyway, so go away 🙂
