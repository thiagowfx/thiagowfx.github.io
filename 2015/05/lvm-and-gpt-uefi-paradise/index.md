---
title: "LVM and GPT/UEFI paradise"
url: https://perrotta.dev/2015/05/lvm-and-gpt-uefi-paradise/
last_updated: 2026-11-22
---


I'm now using [LVM](https://wiki.archlinux.org/index.php/LVM) on my linux
installations and there is no looking back. I also migrated to
[GPT](https://wiki.archlinux.org/index.php/GUID_Partition_Table)/[UEFI](https://wiki.archlinux.org/index.php/Unified_Extensible_Firmware_Interface)
– instead of MBR, and I have to say it is not that hard. Pretty easy, actually,
unless your system has some problem with secure boot.

The ESP (EFI system partition), formatted as FAT-32, should have something
between 250 and 500MB of allocated space; this is enough in most cases. GRUB and
syslinux are well-known to boot (U)EFI systems. I'm using GRUB2 right now, but
later on I'll try syslinux too (I used it before, but for MBR).

