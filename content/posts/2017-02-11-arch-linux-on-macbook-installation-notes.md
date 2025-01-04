---
title: "Arch Linux on macbook installation notes"
date: 2025-01-04T18:36:02-03:00
tags:
  - dev
  - linux
---

Imported from [thiagowfx](https://gist.github.com/thiagowfx/)@'s gist.

Arch Linux Installation Notes (Macbook, UEFI, LVM ON LUKS, swap, btrfs root and home):

## References

* Create an installation disk (USB Flash Drive):
  http://zanshin.net/2015/02/05/arch-linux-on-a-macbook-pro-part-1-creating-a-usb-installer/
* Partitioning (EFI boot partition + LVM on LUKS partition):
  https://gist.github.com/jasonwryan/4618490
  * Naming conventions:
    http://www.pavelkogan.com/2014/05/23/luks-full-disk-encryption/
  * Support docs:
    https://wiki.archlinux.org/index.php/Dm-crypt/Encrypting_an_entire_system#LVM_on_LUKS
* Bootloader: https://wiki.archlinux.org/index.php/systemd-boot
* Official Installation Guide:
  https://wiki.archlinux.org/index.php/Installation_guide

## Post-installation

* https://wiki.archlinux.org/index.php/Mac#Arch_Linux_only
* https://github.com/yantis/instant-archlinux-on-mac%
