---
title: "Linux swap shenanigans"
date: 2022-02-01T17:03:13-05:00
tags:
  - linux
showtoc: true
---

In this post we will cover a few linux swap recipes.

<!--more-->

## Empty swap space

Completely empty (_flush_) swap space:

```shell
% swapoff --all && swapon --all
```

## Decrease swappiness

Emptying is too extreme. Why did you get so much swap in the first place?
A small tweak is to decrease the sensibility of the system to swap:

```shell
$ cat /etc/sysctl.d/90-custom.conf
vm.swappiness=20
vm.vfs_cache_pressure=50
```

The default swappiness of the Linux kernel these days is 60%, which IMHO is
quite aggressive for desktop usage. By decreasing it to 20%, our system will
only start to swap once we use more than 80% of total RAM. In other words, only
when there is 20% or less of free / available RAM.

[`vfs_cache_pressure`](https://www.kernel.org/doc/Documentation/sysctl/vm.txt):

> This percentage value controls the tendency of the kernel to reclaim the
> memory which is used for caching of directory and inode objects.

> At the default value of vfs_cache_pressure=100 the kernel will attempt to
> reclaim dentries and inodes at a "fair" rate with respect to pagecache and
> swapcache reclaim.  Decreasing vfs_cache_pressure causes the kernel to prefer
> to retain dentry and inode caches. When vfs_cache_pressure=0, the kernel will
> never reclaim dentries and inodes due to memory pressure and this can easily
> lead to out-of-memory conditions. Increasing vfs_cache_pressure beyond 100
> causes the kernel to prefer to reclaim dentries and inodes.

However, `/etc/sysctl.d` settings will only be applied after a reboot. To apply
them immediately, use the `sysctl(8)` command:

```shell
% sudo sysctl -p /etc/sysctl.d/90-custom.conf
vm.swappiness = 20
vm.vfs_cache_pressure = 50
```

## Use a swapfile

If you find yourself with a fully partitioned disk without any dedicated swap
partition, there's a trick to adding swap anyway: Use a swap file! [Everything is
a file](https://en.wikipedia.org/wiki/Everything_is_a_file) anyway!

```shell
# https://wiki.archlinux.org/title/Swap#Swap_file

# Create the swap file: 8GiB in this case, to match our total RAM
% dd if=/dev/zero of=/swapfile bs=1M count=8000 status=progress

# Set restricting permissions
% chmod 600 /swapfile

# Format the ~~partition~~ file
% mkswap /swapfile

# Activate the swap file
% swapon /swapfile
```

You can check it's working correctly by inspecting `/proc/swaps`:

```shell
% cat /proc/swaps
Filename				Type		Size		Used		Priority
/swapfile                               file		8388604		0		-2
```

Then finally add it to your `/etc/fstab` so that it is automatically mounted in subsequent boots:

```shell
# swap file
/swapfile none swap defaults 0 0
```

## Add ZRAM swap

Explaining `zram` is out of scope if this post, but check out the
[ArchWiki](https://wiki.archlinux.org/title/Improving_performance#zram_or_zswap)
or [Wikipedia](https://en.wikipedia.org/wiki/Zram).

The recipe I use in Arch Linux is the [`zramswap`](https://aur.archlinux.org/packages/zramswap/) package:

1. Install the package.
2. Set desired zram swap percentage, I picked 20%:

```shell
% cat /etc/zramswap.conf
ZRAM_SIZE_PERCENT=20
```

3. Enable/Start the service:

```shell
% systemctl enable --now zramswap
% systemctl status zramswap
● zramswap.service - Zram-based swap (compressed RAM block devices)
     Loaded: loaded (/usr/lib/systemd/system/zramswap.service; enabled; vendor preset: disabled)
     Active: active (exited) since Tue 2022-02-01 16:13:37 EST; 7h ago
   Main PID: 582 (code=exited, status=0/SUCCESS)
        CPU: 27ms

Feb 01 16:13:37 localhost.localdomain systemd[1]: Starting Zram-based swap (compressed RAM block devices)...
Feb 01 16:13:37 localhost.localdomain zramctrl[627]: Setting up swapspace version 1, size = 1.5 GiB (1654009856 bytes)
Feb 01 16:13:37 localhost.localdomain zramctrl[627]: LABEL=zram0, UUID=a39e0131-f102-4503-a1e7-a3e0ca330126
Feb 01 16:13:37 localhost.localdomain systemd[1]: Finished Zram-based swap (compressed RAM block devices).
```

You can inspect `/proc/swaps` again to check it's working properly[^1]:

```shell
% cat /proc/swaps
Filename				Type		Size		Used		Priority
/swapfile                               file		8388604		0		-2
/dev/zram0                              partition	1615244		0		100
```

[^1]: zswap should have more priority than the swap file.
