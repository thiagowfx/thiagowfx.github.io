---
title: "Alpine Linux on Raspberry Pi: Diskless Mode with persistent storage"
date: 2022-01-15T23:18:56-05:00
tags:
  - bestof
  - dev
  - selfhosted
---

Use case: Given an Alpine Linux **diskless**[^1] installation meant for
a Raspberry Pi setup, we would like to add a persistent storage component to it
to make it survive across reboots.

## Goal

The [Alpine Linux Wiki][alpine-installation] covers most of the installation process, hence I will only document the bits that were lacking and/or confusing therein.

My use case is the following:

> Given a Raspberry Pi 3B with an old 4GiB SD Card as CF storage[^2], install Alpine Linux in diskless mode. Find a way to preserve modifications in `/etc` and `/var`, as well as any installed packages through its `apk` package manager.

Let's follow the steps outlined in the wiki.

## Copy Alpine to the SD Card

> Grab the SD card and install Alpine Linux in it.

Alpine provides officially supported images designed for the Raspberry Pi.

Most Linux distributions provide an `.iso` or `.img` file to be installed with a tool like [Balena Etcher][balena-etcher], [Rufus][rufus], [**Raspberry Pi Imager**][raspberry-pi-imager] or plain `dd`[^3].

Alpine is not like most Linux distributions: Instead, it provides a `.tar.gz` archive with files that should be copied directly to the SD card. Grab the latest version (3.15 at the time of this post) from https://alpinelinux.org/downloads/. There are 3 options:

- `armhf`: Works with all Pis, but may perform less optimally on recent versions.

- `armv7`: Works with the Pi 3B, 32-bit.

- `aarch64`: Works with the Pi 3B, 64-bit.

I opted for `aarch64` to make it 64-bit, but `armv7` would also have worked well for my setup. In fact, Raspberry Pi OS (Debian) uses `armv7` (32-bit) at the time of this writing.

Before copying files over, format the SD Card. As I was doing this
from a Windows machine because it was the only one I had readily available with
a SD card slot, I just used the native Windows Disk Management tool to do so.
I decided to allocate a 100MB[^4] FAT32 partition. The rest of the SD card would be
blank for now. Alpine is surprisingly small, 100MB was more than enough for the kernel and other needed files.

Once the SD card is formatted, copy the files over to it. It turns out Windows cannot extract tarballs (`.tar.gz`); a tool like [7-zip][7-zip] should do the job. Copy the files over to the root of the newly allocated FAT32 partition, and then safely eject the SD card.

## Boot Alpine from the SD Card

The next step is to insert the SD Card into the Pi and then boot. I had some trouble in this step and eventually figured out I didn't mark the primary FAT32 partition as bootable. Unfortunately it's not straightforward to mark the partition as bootable from Windows. On a Linux machine there's a wide array of tools to do so: `fdisk`, `cfdisk` (TUI), `sfdisk` (scriptable `fdisk`), `parted`, `gparted` (GUI) are some of them. I worked around that by installing Raspberry Pi OS on the SD card with the Raspberry Pi imager, and then overwriting it with the Alpine files. This works because the Raspberry PI OS installation marks the FAT32 partition as bootable.

## Install Alpine

Installing Alpine is well documented in the [wiki][alpine-installation] thus it won't be covered here. It basically comes down to invoking `setup-alpine`, which then invokes other `setup-*` scripts.

Keep in mind we're not really "installing" Alpine as this is a diskless installation. A more accurate term here would be "configuring".

Before invoking the installation script, I created a second primary partition in the SD card, set to `ext4`:

```shell
# Configure networking to get working internet access.
% setup-interfaces

# Install some partitioning tools.
% apk add cfdisk e2fsprogs

# Create a second partition (mmcblk0p2) and write it.
% cfdisk /dev/mmcblk0

# Format the partition as ext4.
% mkfs.ext4 /dev/mmcblk0p2

# Mount the partition under /media.
% mount /dev/mmcblk0p2 /media/mmcblk0p2
```

The installation is straightforward, we just need to pay attention to a few select steps:

- `setup-disk`: Select `none` to ensure a `diskless` installation[^5].
- `setup-apkcache`: Select `/media/mmcblk0p2/cache` to persist downloaded `apk` packages.
- `setup-lbu`: Edit `/etc/lbu/lbu.conf` and set `LBU_MEDIA="mmcblk0p2"`. Note: Do not add `/media` as it is implicit.

Once the installation is complete, run `lbu commit` to persist the changes in the second partition. Once you do so, a `<hostname>.apkovl.tar.gz`[^6] file should materialize on `/media/mmcblk0p2/`.

This is a good moment to reboot. Before we do so, let's cache the packages we had previously downloaded.

```shell
# Cache packages.
% apk cache download

% reboot
```

## After the first reboot

If everything worked as expected, once you reboot all your previously installed packages should have been preserved and automatically restored / reinstalled, as well as your modifications done to `/etc`.

From this point on, whenever you install a new package that you want to be preserved for subsequent reboots, run `lbu commit` afterwards. For example:

```shell
% apk add vim
% lbu commit
```

If you would like to see what is going to be committed, run `lbu status` or `lbu diff` before doing the actual commit. Whenever you commit, `/media/mmcblk0p2/<hostname>.apkovl.tar.gz` gets overwritten with your most recent modifications.

It's possible to keep more than one backup file by changing `BACKUP_LIMIT=` in `/etc/lbu/lbu.conf`. This is specially handy if you decide to revert to an earlier system snapshot / state later on. The stock config looks like this:

```shell
% cat /etc/lbu/lbu.conf
# what cipher to use with -e option
DEFAULT_CIPHER=aes-256-cbc

# Uncomment the row below to encrypt config by default
# ENCRYPTION=$DEFAULT_CIPHER

# Uncomment below to avoid <media> option to 'lbu commit'
# Can also be set to 'floppy'
# LBU_MEDIA=usb

# Set the LBU_BACKUPDIR variable in case you prefer to save the apkovls
# in a normal directory instead of mounting an external media.
# LBU_BACKUPDIR=/root/config-backups

# Uncomment below to let lbu make up to 3 backups
# BACKUP_LIMIT=3
```

**Tip**: You can find the list of all explicitly installed packages in `/etc/apk/world`.

## The last piece: make /var persistent

There are three natural ways that come to mind to make `/var` persistent:

### A) Separate partition (or file)

Instead of two partitions (FAT32 and ext4), create 3 partitions: FAT32, ext4 and ext4. Use the latter one to mount `/var` on, saving this information in `/etc/fstab`. The main disadvantage of this setup is that you'll need to allocate a fixed amount of space of each of the ext4 partitions and it may be difficult to figure out how to split the space between them.

A variant of this approach is to just create the third partition as a file:

```shell
# 500MB file
% dd if=/dev/zero of=/media/mmcblk0p2/var.img bs=1M count=500 status=progress
% mkfs.ext4 /media/mmcblk0p2/var.img
% mount /media/mmcblk0p2/var.img /var
```

This works because the Linux kernel supports mounting files as if they were device blocks, treating them as loop devices (pseudo-devices).

I don't like these approaches because they shadow the preexisting `/var` from the boot media, which in turn messes up with existing services that use it such as `cron`: `% crontab -l` would fail. One workaround would be to mount a `/var` subdirectory instead: for example, `/var/lib/docker` for docker.

### B) Bind mount

This one is straightforward:

```shell
% mount --bind /media/mmcblk0p2/var/lib/docker /var/lib/docker
```

The actual partition lives in the SD card, however we make a bind mount under
`/var`, which is like an _alias_. From [Stack Exchange](https://unix.stackexchange.com/questions/198590/what-is-a-bind-mount):

> A bind mount is an alternate view of a directory tree. Classically, mounting creates a view of a storage device as a directory tree. A bind mount instead takes an existing directory tree and replicates it under a different point. The directories and files in the bind mount are the same as the original. Any modification on one side is immediately reflected on the other side, since the two views show the same data.

### C) Overlay mount

From [ArchWiki](https://wiki.archlinux.org/title/Overlay_filesystem):

> Overlayfs allows one, usually read-write, directory tree to be overlaid onto another, read-only directory tree. All modifications go to the upper, writable layer. This type of mechanism is most often used for live CDs but there is a wide variety of other uses.

It's perfect for our use case, which uses a live bootable SD card for Alpine. It blends the preexisting, ephemeral, in-memory `/var` with the persistent in-disk `/var`.

I wanted to mount `/var` directly but found it to be problematic for the same reasons mentioned earlier, therefore I just went with `/var/lib/docker` instead:

```shell
# Create overlay upper and work directories.
% mkdir -p /media/mmcblk0p2/var/lib/docker /media/mmcblk0p2/var/lib/docker-work

# Add mountpoint entry to fstab. Note: The work dir must be an empty directory in the same filesystem mount as the upper directory.
% echo "overlay /var/lib/docker overlay lowerdir=/var/lib/docker,upperdir=/media/mmcblk0p2/var/lib/docker,workdir=/media/mmcblk0p2/var/lib/docker-work 0 0" >> /etc/fstab

# Mount all fstab entries, including our newly added one.
% mount -a
```

## Conclusion

I opted for the third approach, using an overlay mount, it was the most
seamless one. A bind mount would have been fine as well.

The final setup works surprisingly well:

- Alpine Linux is very lightweight and runs mostly from RAM
- `apk` cache is persistent to the ext4 partition
- `/var/` is persistent to the ext4 partition
- `lbu commit` persists changes in `/etc/` and `/home/` in the ext4 partition
- Every reboot fully resets the system sans persistent components above

## References

- https://vincentserpoul.github.io/post/alpine-linux-rpi0/
- http://dahl-jacobsen.dk/tips/blog/2021-04-08-docker-on-alpine-linux/
- http://dahl-jacobsen.dk/tips/blog/2018-03-15-alpine-on-raspberry-pi/

[7-zip]: https://www.7-zip.org/
[alpine-installation]: https://wiki.alpinelinux.org/wiki/Installation
[balena-etcher]: https://www.balena.io/etcher/
[dd]: https://www.gnu.org/software/coreutils/manual/html_node/dd-invocation.html
[raspberry-pi-imager]: https://www.raspberrypi.com/news/raspberry-pi-imager-imaging-utility/
[rufus]: https://rufus.ie/en/

[^1]: Running (almost) fully from RAM.
[^2]: CF = Compact disk.
[^3]: On Linux I'd usually opt for `dd`, on Windows the Raspberry Pi Imager is a sensible choice.
[^4]: 100MB is overly conservative, but keep in mind I had a very small SD Card, with only 4GiB storage. 250MB or even 500MB should be a more sensible default if you have a bigger SD Card (e.g. 32GiB).
[^5]: An alternative is to select `data` disk mode, but it didn't work for me.
[^6]: _ovl_ is short for _overlay_. Not to be confused with _vol_ for _volume_.
