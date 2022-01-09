---
title: 'Linux: Auto Switch to Bluetooth Headset'
date: 2021-12-26T15:27:12-05:00
tags:
  - linux
---

Whenever I connect/disconnect my bluetooth headphones to my Linux workstation, I need to manually switch to/off them.

<!--more-->

Every commercial OS I'm aware of does that automatically, including Chrome OS, macOS and Windows.

To automate this behavior on Linux, it depends whether we're using PulseAudio or Pipewire. It boils down to loading the `module-switch-on-connect` pulseaudio module.

**Note**: Tested on Arch Linux only.

## PulseAudio

```shell
$ sudoedit /etc/pulse/default.pa
...
load-module module-switch-on-connect
...
```

Then restart pulseaudio:

```shell
$ systemctl --user restart pulseaudio
```

## PipeWire

```shell
$ sudo mkdir -p /etc/pipewire
$ sudo cp /usr/share/pipewire/pipewire-pulse.conf /etc/pipewire/pipewire-pulse.conf
$ sudoedit /etc/pipewire/pipewire-pulse.conf
...
# Extra modules can be loaded here. Setup in default.pa can be moved here
context.exec = [
    { path = "pactl"        args = "load-module module-switch-on-connect" }
]
...
```

Alternatively, `~/.config/pipewire/pipewire-pulse.conf` should also work. We
should not edit the file in `/usr` because it will not survive package
upgrades.

Then restart pipewire:

```shell
$ systemctl --user restart pipewire{,-pulse}
```

## References

- https://wiki.archlinux.org/title/PulseAudio#Switch_on_connect
