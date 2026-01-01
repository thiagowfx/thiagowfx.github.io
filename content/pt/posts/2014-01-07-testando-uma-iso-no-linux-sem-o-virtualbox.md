---
title: Testando uma ISO no Linux sem o VirtualBox
date: 2014-01-07T16:22:01+00:00
tags:
  - dev
---

Não imagino que seja incomum o seguinte cenário:

* News: uma nova versão da distro _Debisuse_ está disponível.
* Usuário: vou baixar a ISO,
* criar uma máquina virtual no _VirtualBox_ (ou no _VMWare_, vai que),
* Bootar a ISO a partir dela.

Isso tudo é muito mais prático do que gravar a ISO num Flash (Pen) Drive e então testá-la com um novo _boot_. No entanto, podemos ser mais práticos ainda se utilizarmos, para isso, **um único comando**, com o `qemu`! O comando típico é:

```shell
qemu-system-x86_64 --enable-kvm -m 512M -cdrom ~/Downloads/debisuse-latest.iso
```

Se sua arquitetura for de 32 bits, você vai querer _qemu-system-i386_. O parâmetro _m_ regula a quantidade de memória a ser alocada para a máquina virtual.

Para utilizar o QEMU, você vai precisar encontrar o pacote adequado na sua distro.

* No Debian/Ubuntu e openSUSE: `qemu` e `kvm` (não testei, mas tudo indica que são esses)
* No Arch: `qemu` (veja https://wiki.archlinux.org/index.php/Kvm e https://wiki.archlinux.org/index.php/QEMU)

OBS.: O _KVM_ é para deixar a execução ainda mais rápida. Mas ele não é obrigatório, OK? Para poder usá-lo existe uma série de peculiaridades, tais como habilitar as opções de virtualização na sua _BIOS_ (isso é mais comum em laptops) e assegurar-se de que o módulo adequado do kernel foi carregado (geralmente `kvm\_intel` ou `kvm\_amd`). Você pode conferir isso com o comando:

```shell
lsmod | grep kvm
```

Se ver alguma saída, existem boas chances de o módulo correto do _KVM_ já ter sido carregado pelo seu kernel. Para fins de comparação, essa é a minha saída:

```shell
kvm_intel 131191 3
kvm 388773 1 kvm_intel
```

_Happy hacking!_
