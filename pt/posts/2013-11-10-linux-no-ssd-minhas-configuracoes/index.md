---
title: "Linux no SSD: minhas configurações"
url: https://perrotta.dev/pt/posts/2013-11-10-linux-no-ssd-minhas-configuracoes/
last_updated: 2026-03-29
---


Uns dias atrás eu decidi instalar o Linux no meu SSD. Não fiz isso antes porque
achei que o *caching* do Windows que vem por default poderia me ser útil algum
dia. Bom...esse dia não chegou até hoje. Pessoalmente, acho que isso (isso =
fast boot + Intel Rapid Start no SSD) é mais marketing pra vender aparelhos do
que realmente é útil ou eficiente na prática. Na verdade, é um marketing
**ótimo**, pois parece realmente convencer muita gente.

> - "Olha, minha máquina boota em 5--9 segundos!"
>
> - "Que legal, hein!"

Quantas vezes ao dia você passa *bootando* sua máquina? O tempo de um único
acesso ao Facebook ou qualquer outra rede social é o tempo que você esperaria
numa máquina *old-school*, sem essas firulas (20--50 segundos?), até mesmo mais
que isso. Então dizer que é  "para otimizar o tempo" é bobagem.

Edit: esqueci de dizer que o SSD é de 32GB, conectado em mSATA, e o HDD de
500GB.

Então, vamos ao título: eu deletei as 2 partições do SSD concernentes ao
Windows. Uma era HFS, a outra eu não sei. Não pude ver nem pelo gerenciador de
discos do Windows nem pelo `gparted` ou `cfdisk` do Linux.

Imediatamente criei duas partições lá: uma `/boot`, sistema de arquivos ext4, com
512MB (isso é maior do que o necessário; metade disso poderia ser suficiente.
Mas, se você pensa em brincar ou usar/bootar múltiplos kernels, pode ser
interessante dar uma pequena folga); e, a outra, a root (ext4 também). Resolvi
preenchê-la com todo o espaço restante (~31 GB). Uma outra opção seria criar
duas partições: `/usr` e `/`, a primeira em torno de 7–12 GB e a root com o
restante. Isso varia a gosto e a propósito de uso do leitor.

Motivo: o SSD é mais eficiente para leitura do que para escrita. Na verdade, ele
tem um número limitado de ciclos de escrita. Então é melhor deixar lá apenas o
que for referente ao sistema operacional. Arquivos que tendem a variar mais,
como os de `/var` e `/home`, é melhor deixá-los no HDD.

Então, no HDD, eu criei `/var` com 12GB, uma partição extra com ~20GB (no caso
que eu precisar instalar outra distro) e o restante para `/home` (~200-1000 GB
dependendo do tamanho do HDD).

Depois, é só proceder a instalação como você faria normalmente. Só não se
esqueça de montar as 4 partições e depois adicioná-las ao `/etc/fstab`
(especialmente se você estiver instalando uma distro pela linha de comando -
leia Arch ou Gentoo).

Ah, não faz diferença se for GPT/EFI ou MBR. No sentido das partições, que quero
dizer. A diferença se dará basicamente apenas na hora de instalar o bootloader
(provavelmente o GRUB(2)). Na verdade, tende a ser melhor optar por GPT/EFI por
ser mais **moderno** e tudo o mais, mas isso é de cada um; eu particularmente
escolhi MBR (o leitor atento percebeu que eu não criei nenhuma partição de EFI).

## Tweaks

Existe muita paranoia por aí falando que seu SSD pode morrer *logo* se não for
usado direito, e blábláblá. Ele realmente pode ter uma vida útil menor, mas não
é **tanto** quanto alguns lugares dizem por aí. Diria que ele vai durar no
mínimo a quantidade de anos até a troca de aparelho (ah, a *obsolescência
tecnológica.*..).

O tweak mor é o que eu falei antes: usar o SSD mais para ser lido do que para
ser escrito. Isso já foi garantido durante a etapa de instalação.

Um pequeno tweak alternativo é dar **TRIM** no SSD de vez em quando. Recomendo
fortemente a leitura disso na [wiki do
Arch](https://wiki.archlinux.org/index.php/Solid_State_Drives) (em inglês).
Basicamente, você pode fazer isso via cron ou ao montar as partições do SSD. Uma
outra leitura interessante está no
[Reddit](http://www.reddit.com/r/archlinux/comments/rkwjm/what_should_i_keep_in_mind_when_installing_on_ssd/)
(em inglês, também).

E, no final das contas: entender que um SSD funciona de maneira diferente de um
HDD é um ótimo progresso.

## Primeiras Impressões

Ainda não testei o suficiente para poder falar sobre isso, mas tenho que dizer
que o sistema fica realmente mais rápido rodando a partir do SSD. Consigo até
10s de boot com um pouco de esforço (mas, como eu disse, isso não é realmente
importante pra mim, até porque depois de adicionar vários *targets* do systemd
esse tempo vai aumentar ligeiramente). O que demora mais é a checagem do
**fsck**. Talvez com **btrfs** pudesse ficar mais rápido ainda. Mas não acho que
tanto. De qualquer modo, o tempo de inicialização do XFCE é em menos de 1s
(acho). Mas está tudo *vanilla* ainda, só vale mesmo medir os tempos quando os
programas que realmente uso estiverem instalados.

Ah, conclusão, e o Windows? Bom, para dual bootar a `/home` deveria ser reduzida.
E o bootloader teria que ser ajustado. Se for instalação com EFI, teria que ter
uma partição de EFI também. De preferência seria melhor instalar o Windows
primeiro, mas o contrário também poderia ser feito (alerta: dá mais trabalho).
Eu vou virtualizá-lo no VirtualBox. Provavelmente rodando o openbox quando
precisar de muita memória.

**Update (2014-12-16):** hoje em dia eu faço assim: todo o meu SSD fica para a
raiz (30GB para `/`), sem partição de boot. O formato de arquivos que eu utilizo
é o btrfs, que possui algumas otimizações para SSDs.

