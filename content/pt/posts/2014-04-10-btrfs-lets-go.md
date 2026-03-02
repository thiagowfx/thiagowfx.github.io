---
title: "btrfs, let's go"
date: 2014-04-10T21:48:36-03:00
tags:
  - dev
  - legacy
---

Hoje ouvi num *podcast* que o Facebook em breve usará o sistema de arquivos
*btrfs* em seus servidores. Link upstream em
[1](http://www.theinquirer.net/inquirer/news/2336904/facebook-will-trial-btrfs-linux-file-system-in-its-data-centres).
Servidores reais! De produção. R-E-A-I-S.

(OK, não são todos os servidores, mas isso já é um começo. Uma bateria de
testes.)

Isso possui algumas implicações bem interessantes:

- Os dias de *ext4* como o filesystem principal do Linux podem estar contados.
  Na verdade, é dito que o btrfs **não** foi criado para substituir o ext4, ele
  seria apenas mais uma opção. Mas, o ext4 não vai ficar no topo para sempre...

- Quando uma super empresa resolve tomar uma decisão como essa, significa que
  eles não vêem mais o btrfs como uma brincadeirinha. Além do mais, note que a
  versão 13.2 do openSUSE provavelmente trará o btrfs como filesystem padrão.
  Lembrando que o openSUSE (assim como o Fedora, e o Arch) é uma das distros
  mais pioneiras no que diz respeito a adotar novas tecnologias.

Ou seja, usar o *btrfs* como filesystem principal no...DESKTOP pode começar a
ser uma boa ideia. Pessoalmente, só não migrei para o btrfs por dois motivos.

- sem swap!
- dor de cabeça

Na verdade, o primeiro motivo ocupa 90% de espaço. Dor de cabeça é natural,
seria a mesma coisa se fosse para usar LVM, criptografar o HD/SSD inteiro ou
aderir à uma nova tecnologia com o qual não se está acostumado. Documentação não
falta! Migraria sem nenhum problema. Amanhã mesmo.

O grande problema é a falta de *swap*, é uma função que eu particularmente prezo
bastante. Naturalmente, não é algo super útil em servidores, mas em desktops ( /
notebooks, bah) é uma *feature* cômoda. Nada como acordar no dia seguinte e ver
todas as suas janelas e seu trabalho restaurado do último ponto onde estavam.

Um dia eu testo o *combo* máximo: btrfs + LVM + criptografia. No desktop. Na
verdade, acho que o btrfs dispensa LVM, aquelas *pools* dele devem ter uma
função similar a ela. Enfim.
