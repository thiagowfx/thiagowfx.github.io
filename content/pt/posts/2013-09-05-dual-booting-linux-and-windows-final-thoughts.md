---
title: "Dual Booting Linux and Windows – Final thoughts"
date: 2013-09-05T17:58:49-03:00
tags:
  - dev
  - legacy
---

Vou escrever o post completamente em inglês para treinar um pouco. Se você
quiser me ajudar, não hesite em me apontar erros de gramática, ortografia ou
eventuais stack overflows! Da série "só se aprende errando" e "é melhor escrever
um pouco em vez de só ficar lendo".

Nota 1: eu não perdi tempo utilizando google translate.

Nota 2: eu só vou corrigir meus próprios erros daqui a algum tempo, para ter
noção do quanto eu evoluí daqui até lá. Então é provável que você encontre
vários erros aqui, anyway. Sorry por isso.

In this post I'll try to explain a particular way of setting up a Windows +
Linux environment on a single PC.

First things first. You should firstly have in mind which version of Windows and
which Linux distro you intend to install. Probably the windows question won't be
much difficult to answer, since there aren't really that *many* versions of it,
but the Linux and open source world is a world of choice: there are hundreds of
distros to choose from! So, I'll assume that you have already defined these. And
I'll assume that you only want to install a single distro.

Now, you should transfer your Linux ISO to a installation medium. From here,
I'll tell you a secret. This post is not intended to be a full tutorial. In
these modern web days, you can find all the stuff you need *just* by yourself
([DIY](http://en.wikipedia.org/wiki/Do_it_yourself)) and with a help of doctor
[Google](www.google.com.br). What google doesn't really have, at least now – of
course –, is the **know-how** of the things. That you can find here – at least a
bit. So, use google and don't complain at me. You'll get smarter if you do so (I
didn't said more intelligent, I said smarter).

Now, let's go back to our point. You need your ISO in a medium. What about using
the `dd` command, Mr. expert? I'll remember you how to do that:

```shell
sudo dd if=/path/to/your/iso.img of=/dev/sdb bs=4M && echo Wait && sync && echo OK
```

If you don't know what I am talking about, please consider searching more
information about **dd**. The GUI way of doing the same thing is to use programs
like **Lili USB Creator** if you are in Windows, or **Unetbootin** if you are in
GNU/Linux (this program is also available for Windows).

OK, now let's boot into our distro. Configure your BIOS settings to do that. The
option that you are searching for is something like "boot order" or "boot
options" or "boot priority". By the way, you should press some key in your
keyboard while your system is booting up to have access to your BIOS.

Now, are you in the live environment of your distro? Good! But maybe you picked
one like Arch Linux or Gentoo Linux so you don't have a live environment at
all...that doesn't *really* matter. Let's work.

You should begin partitioning your HDD. You can do it by several ways. This is
the partitioning scheme that I recommend, supposing that you have a 500GB HDD
(pretty common these days). You'll use MBR (oh, don't bother me with GPT).
Create the following partitions:

- `/dev/sda1` 50GB NTFS (for our future windows)
- `/dev/sda5` ext4 (logical) 50GB (for `/`)
- `/dev/sda6` swap (logical) 3GB (for swap. This one is **optional**)
- The rest: `/dev/sda2` NTFS (for `/home` and Windows Program Files and Documents)

Create these partitions either with **gparted** or with **cfdisk**.

Now go to the installation process of the distro that you picked and be alert to
mount `/`, swap and `/home` on the places that you chosed.

You should install **grub** or **grub2**!

Now reboot your system and boot into the Windows installation medium. Follow the
instructions from the wizard and install windows in the correct partition.

Now boot into Windows. You should notice that our **grub** was replaced by the
default Windows bootloader, so we can't boot into Linux again (at least now).
This is why some people recommend to install Windows first. But I find the
converse better. In Windows, you should create the "Program Files" folder in the
big partition (`/home`) and make windows recognize it. Go to the registry editor
(Win + R ==> regedit). Edit the key:

`HKEY_LOCAL_MACHINE\SOFTWARE\MicrosoftWindows\CurrentVersion\ProgramFilesDir` to
your newly created Program Files. Now: create some libraries.

(...)

**Update(2026-08-21)**: Apparently some text is missing at the end 🤷.
