---
title: "Desvendando (ou não) o btrfs"
url: https://perrotta.dev/pt/posts/2014-09-20-desvendando-ou-nao-o-btrfs/
last_updated: 2026-08-21
---


**Atenção**: o conteúdo a seguir é apenas uma **introdução**.

## Overview

Uma das coisas que mais demorei para fazer nesse mundo **Unix** foi brincar com
testar um filesystem diferente do **ext{2,3,4}**. Existem pelo menos duas
alternativas populares hoje em dia, para isso: no mundo BSD, o **ZFS**; e no
mundo Linux, o **btrfs**. Ambos são *filesystems* avançados, o que você pode
entender como "é melhor eu ficar longe disso para não fazer besteira" e "deve
ter uma porção de *features* que eu provavelmente nunca pensei em usar e/ou que
precisaria algum dia".

Muito bem, como eu estou usando Linux como meu sistema principal, resolvi partir
para o **btrfs**. É bem provável que o futuro ocorra da seguinte maneira: Ubuntu
com btrfs (esse é o presente, na verdade), depois algum BSD com ZFS
(provavelmente ou o FreeBSD ou o PC-BSD), e depois finalmente o meu querido e
eterno Arch Linux com…bem, se vai ser com btrfs ou com ext4 eu vou ver, mas é
bem possível que seja com btrfs.

Então, vamos lá. Em primeiro lugar, por que outro filesystem diferente do ext4?
A resposta para essa pergunta não é muito diferente da "por que outra distro?".
Utilizar tecnologias alternativas espontaneamente é, para mim, um **hobby**. *A
priori* não existe um motivo especial para fazer isso, mas essa é uma forma de
aprender mais e, se tiver sorte, descobrir algo legal e/ou útil.

## btrfs, vamos lá

Agora vamos às especificidades do btrfs. Em primeiro lugar, alguns ainda o
consideram experimental. Mas, convenhamos, ele é considerado experimental desde
vários anos atrás; hoje em dia eu diria que ele está razoavelmente estável, sim.
No meu sistema,

```shell
thiago@ideapad ~ % btrfs version
Btrfs v3.12
```

Inclusive, o instalador do openSUSE 13.1 oferece gentilmente se você quer
experimentar o *btrfs*. Além disso, o instalador do Fedora 20 suporta
perfeitamente um *filesystem setup* com btrfs. Já o instalador do Ubuntu 14.04
não possui nada específico em relação ao btrfs, mas você pode optar por usá-lo
especificando-o manualmente.

Uma desvantagem do btrfs – essa é possivelmente a maior delas **hoje** – é que
não existe suporte para **hibernar** o sistema. Na verdade, eu leio por aí de
que não existe suporte nem para **swap** sequer. Mas, eu estou utilizando swap
neste momento e não estou tendo problemas. Então, sei lá. O negócio de swap é
que ele é lento pra caramba, então o ideal é precisar não usá-lo de qualquer
forma. Com 4G de RAM infelizmente eu acabo utilizando-o uma vez ou outra…mas,
não abrindo muitos programas ao mesmo tempo dá para segurar a onda legal. Por
sinal, abrir vários programas ao mesmo tempo não é necessariamente benéfico de
qualquer forma, já que incentiva o *multitasking*, o que acaba aumentando
globalmente o tempo para realizar todas as tarefas que você pretende. Eu sou
cada vez mais fã e adepto das aplicações que podem restaurar os seus estados.
Isso é usualmente melhor do que contar com o sistema para restaurar todas as
suas aplicações. Exemplos de aplicações que fazem isso? Bem, temos os
navegadores, para começar (Firefox/Chromium). Alguns leitores de PDF também
abrem na última página que você leu (exemplo do meu favorito: zathura). Também
tem alguns players de vídeo que abrem o arquivo no último ponto assistido (ainda
estou para achar um aqui. Sei que existe, só não parei para procurar). Ou
players de música que salvam a última playlist (exemplo: audacious). Enfim, deu
para entender a ideia, não é? Até mesmo o Emacs, como editor de texto, salva a
última linha editada de dado arquivo.

Se você consegue viver sem hibernar o seu sistema, siga em frente.

O btrfs possui uma porção de features que eu nem sei direito para que servem, ou
mesmo como usá-las, mas vou tentar destrinchar algumas delas aqui.

A que mais me atrai é a feature de **snapshots**. Você pode criar um snapshot,
digamos, da sua **/home**. Um **snapshot** é como se fosse uma "foto", ou uma
marcação na linha do tempo de como os seus arquivos estavam em dado momento do
tempo (melhor ainda: não apenas **como**, mas **com que conteúdo** também). Ou
seja, se você criar um snapshot da sua home agora, daqui a um mês você pode
visualizar como ela estava hoje. E não é apenas visualizar, você também pode
copiar ou ler qualquer arquivo daquela época; pode até mesmo escrever neles. E
mais uma coisa: esse snapshot não é tão custoso como (digamos) a *feature* de
snapshot do VirtualBox: lá, se você quiser ver um snapshot, basicamente tem que
carregá-lo completamente (e no lugar do último); aqui no btrfs, um snapshot é
algo completamente transparente, que pode ser visualizado e manipulado a
qualquer hora, *on-line*, sem ter que carregá-lo completamente. Na prática, ele
se comporta como um diretório no seu filesystem.

Então, digamos, acabei de criar um snapshot da minha home assim:

```shell
% btrfs subvolume snapshot /home /home/snapshot-2014-09-20
```

Após fazer isso, aparece um diretório `/home/snapshot-2014-09-20` na minha
`/home` (surpresa?). O conteúdo desse diretório é exatamente o mesmo que o da
minha `/home`. E melhor ainda: o espaço em disco que isso ocupa é praticamente o
mesmo! Digamos, se a minha `/home` tiver 30GiB, então após a criação do snapshot
o espaço que isso tudo ocupa vai continuar a ser 30GiB (com possivelmente alguns
KiB ou MiB a mais para metadados, tudo bem). Não é uma cópia (digamos, para
ficar com 60GiB). Isso tem a ver com uma feature do btrfs que se chama
**copy-on-write**. Se você me perguntar o que isso significa, eu vou dizer que
não tenho certeza. Mesmo após ler várias fontes sobre isso, ainda é algo que me
confunde sobre como é o funcionamento disso. Mas, pelo menos, eu posso dizer que
**it just works** (^TM).

**Snapshots**, pra mim, já é algo suficiente para me fazer querer o btrfs. Mas
não para por aí. Existe o conceito de snapshots programados onde, digamos, você
pode configurar o seu sistema para criar um snapshot diariamente, digamos,
mantendo um limite de 20 deles. E por que isso é útil? Caramba, imagina que você
delete alguns arquivos sem querer (com `rm -rf`, ou mesmo na lixeira, se for
pelo gerenciador de arquivos). Aí basta que você volte em um snapshot anterior e
os recupere.

Quer mais? Então imagina que você crie um snapshot da sua partição raiz (`/`).
Agora você dá o temido

```shell
% sudo apt-get dist-upgrade
```

no Ubuntu, ou mesmo

```shell
% sudo emerge -uaDN @world
```

no Gentoo, ou

```shell
% sudo pacman -Syu
```

no Arch. E suponha que isso deixe o seu sistema sem **bootar**. E agora,
ferrou??? Não, não ferrou, você vai lá no snapshot do seu sistema, restaura ele,
e *boom*, tudo volta ao normal. Snapshots são muito bons para reparar danos de
eventuais upgrades desastrosos.

Tem mais. RAID. Existe suporte nativo de RAID no btrfs. Não vou falar muito
sobre isso aqui porque não estou usando isso agora, mas vejo certos casos em que
isso seria (é!) muito útil.

E tem mais ainda. Que eu não vou falar aqui porque eu mesmo não sei descrever as
outras features até então =P

## Referências

Vou deixar algumas boas referências sobre btrfs aqui:

- [http://www.funtoo.org/BTRFS_Fun](http://www.funtoo.org/BTRFS_Fun)

- [http://www.reddit.com/r/archlinux/comments/2cv6j7/btrfs_how_big_are_my_snapshots_really_and_how_do/](http://www.reddit.com/r/archlinux/comments/2cv6j7/btrfs_how_big_are_my_snapshots_really_and_how_do/)

- [http://snapper.io/](http://snapper.io/)

- [https://wiki.archlinux.org/index.php/Btrfs](https://wiki.archlinux.org/index.php/Btrfs)

- [https://wiki.archlinux.org/index.php/Snapper](https://wiki.archlinux.org/index.php/Snapper)

- [https://wiki.archlinux.org/index.php/Btrfs_-_Tips_and_tricks](https://wiki.archlinux.org/index.php/Btrfs_-_Tips_and_tricks)

- https://www.youtube.com/v/9H7e6BcI5Fo

Agora, vou continuar brincando com snapshots e possivelmente com outras features
desse filesystem. Não me arrependo de não ter instalado o Ubuntu com ext4, até
então. Até uma próxima.

**OBS.:** se eu escrever outro post sobre btrfs, ele provavelmente será em
inglês. Na verdade, o motivo para esse ter sido em português é porque eu não sei
tanto sobre btrfs para falar sobre ele de modo mais formal (é difícil escrever
de modo não-informal fora da sua língua-mãe, não acham?).

