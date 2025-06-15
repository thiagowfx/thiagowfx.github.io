---
title: "Ventoy: Automate your Distro hopping"
date: 2022-01-05T18:28:20-05:00
tags:
  - dev
---

Alternative title:

> Ventoy: A keychain for all your live operating systems

From the project website, [**ventoy**][ventoy] is an:

> open source tool to create bootable USB drive for ISO/WIM/IMG/VHD(x)/EFI files.
>
> With ventoy, you don't need to format the disk over and over, you just need to copy the ISO/WIM/IMG/VHD(x)/EFI files to the USB drive and boot them directly.


## Before

The typical linux desktop user workflow to try out new distros[^vm] is to:

1. Download an `.iso` or `.img` file.
1. Grab a USB stick[^cd] and format/erase it.
1. Run an application[^app] to write the image to the block device.
1. Boot your workstation, press some key to change your BIOS/UEFI setup to boot via USB.
1. Profit.

This works well if you only need to do it once or twice, but carries a few caveats:

1. The USB flash drive contents are completely erased. Extra measures need to be taken in order to use it the rest of its storage persistently.
1. You'll have to redo this whole process whenever there's a new release of your OS. Even for rolling release OSes like Arch Linux, Gentoo or Alpine Linux, you'll typically want to have a more up-to-date image anyway, otherwise the installation process will eventually become problematic[^problematic], as the system gets more and more out-of-date.
1. You can only keep one bootable image at a time in your USB stick. Unless you have multiple USB sticks, suddenly you will find that your 32 GB (or even 128 GB) storage is useless to hold multiple operating systems.

## Afterwards

Compare that with Ventoy's workflow:

1. Download Ventoy, and install it to your USB flash drive. This needs to be done only once[^ventoyreimg].
1. Download an `.iso` or `.img` file.
1. Copy it to the USB storage, using your file manager. You could use `cp` from the command line, you could also drag and drop using your file manager, whether it's from Windows, Linux or macOS, doesn't really matter. The destination is just an ordinary directory, nothing fancy.
1. Boot your workstation, press some key to change your BIOS/UEFI setup to boot via USB.
1. Profit.

The number of steps is the same, but Ventoy really shines in the following aspects:

1. There's no need to use any special software to write your images to the USB stick. You just copy and paste a file. Really! And you can do that from any OS.
1. You can add as many images as you want. For example, you could keep your favorite desktop OS therein, alongside your favorite ARM OS (for your raspberry pi), alongside your favorite system rescue utility. They will all co-exist, and once you boot with the USB you'll be able to choose which image you want to boot to, with a nice bootloader menu, à la GRUB or systemd-boot.
1. Upgrading an OS is just a matter of deleting the old one and copying the new one over, exactly like you would do with a simple document file.
1. Your USB flash drive is formatted in such a way that it's possible to use its unused storage as persistent storage. So for example you could boot into your desktop OS, save your work, then reboot into your system rescue utility[^sysrescue] and pick up the leftover files therein.

Ventoy is **magic**. It allows you to carry a single USB stick with all of your favorite operating systems - and they don't even have to be Linux, most operating systems are supported:

> Most type of OS supported (Windows/WinPE/Linux/ChromeOS/Unix/VMware/Xen...)

The full list of supported systems is [here](https://www.ventoy.net/en/isolist.html).

If you need some inspiration to fill in your Ventoy USB stick, head over to [distrowatch](https://distrowatch.com/).


[ventoy]: https://www.ventoy.net/en/index.html

[^app]: In 2020s, [Balena Etcher](https://www.balena.io/etcher/) is a pretty popular application to do so. Linux users often just resort to the command-line instead: `% dd if=mydisk.img of=/dev/sdb status=progress; sync`.
[^cd]: No one _burns_ CDs anymore, right? Right?
[^problematic]: Try installing Arch from a 2010 `.iso` in 2020 and let me know how it goes.
[^vm]: Obviously excluding virtualized solutions like containers (like `docker` or `lxc`) and virtual machines. I am also excluding chroots like `systemd-boot`.
[^sysrescue]: My favorite one is [GRML](https://grml.org/), which is debian-based.
[^ventoyreimg]: You may want to occasionally re-image Ventoy, say, in 5, 10 years? It will probably keep working even if you don't, though, at least with the operating systems supported at the time you installed it.
