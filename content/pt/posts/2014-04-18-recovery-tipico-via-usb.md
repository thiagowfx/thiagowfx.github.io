---
title: "Recovery típico via USB"
date: 2014-04-18T13:38:36+00:00
tags:
  - dev
  - legacy
---

1. Meu computador não boota! E agora? Possíveis sintomas: tela preta congelada,
   tela de splash congelada, systemd travado, upstart travado, corrupção (fsck
   não ficou satisfeito), bootloader (grub,syslinux,EFI) mal configurado (ou não
   configurado)
2. Obter uma distro de Linux e gravá-la num USB Flash Drive (pendrive). Meu
   gosto pessoal: System rescue cd, Parted magic, Slitaz ou Arch Linux.
3. Bootar a distro e imediatamente abrir um console/emulador de terminal. Com
   interface gráfica ou não, a gosto.
4. `fdisk -l` para detectar os discos do computador. Detectar o disco cujo
   sistema está com problema. Geralmente o que contém a partição /boot ou /.
   Identificar as partições também é usualmente importante.
5. Se você precisar formatar alguma partição, `cfdisk` ou `parted`. Exemplo:
   `cfdisk /dev/sda1`.
6. Se você precisar (re)criar algum _filesystem_ , `mkfs` (por exemplo,
   `mkfs.ext4 -L "archroot" /dev/sda1`).
7. Para (re)montar o seu sistema de arquivos: (por exemplo) `mount /dev/sda1
   /mnt`.
8. chroot no sistema que você acabou de montar: `chroot /mnt`.
9. Para recuperar (na verdade, gerar novamente) o arquivo de configuração do
   grub dentro do chroot: `grub-mkconfig -o /boot/grub/grub.cfg`.
10. Para reinstalar o grub (fora do chroot!), use `grub-install`.
11. Explorar o diretório `/etc/systemd/system`.

Usualmente um desses passos é um caminho para resolver o problema. No final das
contas, as coisas são bastante específicas, dependem do contexto.
