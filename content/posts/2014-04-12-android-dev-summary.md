---
title: "Android dev: summary"
date: 2014-04-12T22:57:34-03:00
tags:
  - dev
  - legacy
---

Esse é um *draft* perdido com algumas anotações sobre Android. Foi criado
enquanto eu estava fazendo um curso no Coursera. Na época, acabei escrevendo
aqui por falta de um lugar melhor para isso. Hoje em dia eu faria diferente,
tenho todo um plano para organizar (e compartilhar!) algumas das minhas
anotações. Por enquanto esse plano ainda não está em prática, mas enfim.

Abaixo está o *draft*, reproduzido na íntegra:

---

Hello there. This is just part of a experiment. Usually I take notes with my
notebooks, but they usually become messed up. Temporarily I'll use this blogging
space as a note taking platform too. I have to find more convenient ways to do
that...any recommendations accepted! I've already thought of github, but it is
not *that* indexable. This public information should (may) be useful for
someone a day.

- Debug @ Console: `xinetd` w/ `systemctl service` > `telnet localhost` > 5554 > 5556 > ... // help FTW

- Use 5554/5556 to refer to the device (e.g. to send text messages or make calls)

- Use LogCat View @ Eclipse to see log messages (filter options FTW) // Code: Log.e [...]

- `C-F12` to rotate the emulator (other hotkeys @ developer.android.com page)

- `command android` to open the Android SDK Manager

- KISS: only the Intel images + the SDK platform are important

- Enable HAXM (Windows or Mac) or KVM (Linux) acceleration if you can

- `.xml` files everywhere...

- `android-udev`: use it to connect your device to your computer on Linux (see the AUR)

- Android API: 10 (2.3.3 - Gingerbread), 16 (4.1.2 - Jelly Bean!), 18 (4.3)

- do not make your `~/workspace` a mess, please

- R.java ==> if any problems, go to Project > Clean...

- `C-S-O` come in handy (Eclipse: organize imports)

- Use the 'Quick Access View'

- `alias emulator-template="emulator -avd "Intel-10-480x800" -qemu -m 512 -enable-kvm -gpu on"` // [https://developer.android.com/tools/devices/emulator.html#acceleration](https://developer.android.com/tools/devices/emulator.html#acceleration)

- host is acessible from the emulator via 10.0.2.2 (QEMU feature)

- `C-I` auto indent @ Eclipse
