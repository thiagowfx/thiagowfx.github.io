---
title: "The Eudyptula Challenge – Part #2"
date: 2015-05-21T15:49:31-03:00
tags:
  - dev
  - legacy
  - linux
---

[Last]({{< ref "2015-01-07-the-eudyptula-challenge" >}}) post.

Hello there. Little is back, and so is me. I'm returning to the eudyptula
challenge, restarting from task #06. By the way, I just sent it to Little a few
minutes before writing this post – I hope it is right...

Okay, so after 3 months I forgot a few things. The Linux Kernel is tricky but it
is very well designed. Let's document a few resources here – they might be
useful in the future:

**Note**: this is not in a tutorial style; it is more in a reference style.

## Coding your module

- [This](https://github.com/vivien/vim-addon-linux-coding-style) vim plug-in by
  Vivien Didelot – the same author of i3blocks – is very nice to force the usage
  of the linux kernel coding style. I added it to my pathogen setup.
- Also, don't forget to double check that your C code is valid in terms of
  formatting and style! Use:

  ```shell
  scripts/checkpatch.pl -f code.c
  ```

- `checkpatch.pl` also contains a `--fix` command. But you should try to
  manually fix errors yourself first. And also note that this `--fix` thing is
  still experimental.
- There is also a `scripts/cleanfile` program to fix any messes about line endings
  (`\r\n` vs `\n` for example) and similars.
- The best source of documentation I'm using right now is `ack` + `find` + `tmux`. I
  tried to quickly set up NetBeans and Qtcreator **just** for documentation
  purposes – not for Linux coding! – but they do not work out of the box. I
  believe it is better to stick to a 'manually search for documentation'
  approach. IDEs don't scale well for this task – at least for kernel and
  systems programming; I wouldn't say the same about Java or other very
  IDE-friendly programming languages.

## Testing your module

- `make`, `make`, `make`!
- `make` will create a `*.ko` module, which you will load with `insmod *.ko`.
- Alternatively, you can `make modules_install` your module, which will be put at
  `/lib/modules//extra`. Then you can load it with `modprobe *.ko`.
- Always remember unloading your module (`rmmod *.ko`) before reloading it. It is
  a good practice: clean before beginning again!
- To check debug messages, use either `dmesg` or `journalctl -xn` – supposing you're
  using a systemd-based daemon for your system (it is the case of Arch right
  now).

## Building your kernel

Use:

- `make localmodconfig`. You don't want to create a `.config` file from scratch!
- `make nconfig` to tweak the settings of your `.config` file.
- `make` to build the kernel
- `make modules` to build the kernel modules
- `sudo make modules_install` will install your modules. Very important to boot
  into it later on!
- `sudo make install`
- It is important to create a boot entry for your kernel. syslinux users will
  probably find this task trivial (it is just a matter of mimicking the
  configuration from your current kernel on `/boot/syslinux/syslinux.cfg`); grub
  users should edit `/etc/grub.d/40_custom` and create a `menuentry` based on an
  already existing entry on `/boot/grub/grub.cfg`. After that, update your config
  file with `sudo grub-mkconfig -o /boot/grub/grub.cfg`
- You should also pay attention if your linux distribution uses an initramdisk.
  Arch does, so I created another config file on `/etc/mkinitcpio.d/` just for the
  eudyptula kernel (and then a `mkinitcpio -p linux-eudyptula`).
- Use `uname -a` to check your new kernel after booting into it.

## Sending non-HTML mail

- [Mutt](http://www.mutt.org/) is still the best option for me for this.
- Use `m` to create a new e-mail.
- Use `a` to add attachments.
- Use `y` to send your e-mail.
- Now, if you need to create a `.muttrc` file from scratch...I'd recommend you to
  (for example) to use
  [mine](https://github.com/thiagowfx/dotfiles/blob/master/.muttrc) as an
  inspiration.

And let's see if this thing will keep going on. See you later :)
