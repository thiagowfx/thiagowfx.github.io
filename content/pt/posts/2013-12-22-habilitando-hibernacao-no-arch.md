---
title: Habilitando hibernação no Arch
date: 2013-12-22T19:49:31-03:00
tags:
  - dev
  - legacy
---

Incrível como eu não tinha feito isso até hoje...se você *não* usa btrfs e quer agilizar um pouco a sua vida,

a) **(The hard way)** Leia essas duas páginas:

- [https://wiki.archlinux.org/index.php/Suspend_and_Hibernate](https://wiki.archlinux.org/index.php/Suspend_and_Hibernate)

- [https://wiki.archlinux.org/index.php/Mkinitcpio](https://wiki.archlinux.org/index.php/Mkinitcpio)

e/ou

b) **(The easy way)** Faça as seguintes modificações:

- Edite `/etc/mkinitcpio.conf` e adicione a hook de `resume`.

```shell
sudo emacs -nw /etc/mkinitcpio.conf
```

Mais especificamente, procure a linha `HOOKS="(...)"` e acrescente a hook **resume** entre **block** e **filesystems**. Isso serve para a initramfs suportar o resumo a partir de uma partição (ou de um arquivo).

- Depois edite `/etc/default/grub` e acrescente **resume=** em `GRUB_CMDLINE_LINUX`. Tem que ficar mais ou menos assim:

```
GRUB_CMDLINE_LINUX="resume=/dev/sdb2"
```

Naturalmente, se não se lembrar da sua partição de swap, use o gparted, o cfdisk ou o /proc/swaps para refrescar a memória.

- Gere novamente o arquivo de boot do grub:

```shell
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

Se você por acaso notar o erro

```
error: out of memory
error: syntax error
error: Incorrect command
Syntax error in line 164
```

na saída desse comando, veja [este tópico](https://bbs.archlinux.org/viewtopic.php?pid=1357793). Em resumo, basta adicionar no `/etc/default/grub` as seguintes linhas:

```
# fix broken grub.cfg gen
GRUB_DISABLE_SUBMENU=y
```

Você deverá hibernar com o comando **systemctl hibernate** (existem outros! Exemplo: ver o pacote pm-utils), ou através do diálogo de saída de algum DE (por exemplo, no Cinnamon funciona perfeitamente).
