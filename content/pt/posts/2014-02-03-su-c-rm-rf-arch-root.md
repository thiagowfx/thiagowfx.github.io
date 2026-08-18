---
title: "su -c \"rm -rf /arch-root\""
date: 2014-02-03T13:26:09-03:00
tags:
  - dev
  - legacy
---

Você sabe, o Arch não te deixa dar 'sudo rm -rf /'. Algo me diz que isso não é
exatamente do Arch, deve ser de algum componente do sistema, anyway...sim, eu já
tentei dar *wipe* no sistema antes, só de zueira, e – acredite – era numa hora
em que eu *não* podia perder tempo, *maaaaas*, ele não me deixou fazer isso =/

OK, daqui a alguns minutos eu estarei removendo o meu querido Arch Linux. Todo
customizado, todo tweakado, cheio de firulas (ainda assim com esperanças de
estar o mais KISS possível). Eu tomei a decisão de *não* fazer um backup do
mesmo com o CloneZilla, para não ter a tentação de voltar ao estado em que ele
estava antes.

A questão é: porque eu vou fazer isso? Por que, criatura??? Você encontrou o que
você considera a melhor distro de Linux que já conheceu, super estável (mesmo *
rolling release / bleeding edge* like hmmmm...), super customizável (e
customizada), com [uma excelente documentação
(/wiki)](http://wiki.archlinux.org) com uma comunidade que combina
perfeitamente com você, com uma [vasta quantidade de
pacotes](http://packages.archlinux.org/) +
[PKGBUILDs](https://aur.archlinux.org/), com um [sistema de compilação e build
de pacotes super simples](https://wiki.archlinux.org/index.php/Makepkg), *aaaaaaa*.... (você, usuário de Arch, continua essa lista por mim).

Ora, vejamos. Eu cheguei num estado em que eu me considero um *superuser* de
Linux (ainda assim, isso não quer dizer nada, tem muuuuuuuuuuuita coisa pra
aprender ainda!), e um usuário intermediário/avançado de Arch Linux. Aprendi
tudo o que eu considerei interessante. Muitas opções do pacman, vários
[dotfiles](https://github.com/thiagowfx/dotfiles), [custom
kernel](http://repo-ck.com/), [como reportar bugs](https://bugs.archlinux.org/)
(e vê-los sendo fixados!), como tirar dúvidas e interagir com [uma
comunidade](https://bbs.archlinux.org/) bem peculiar, ah, foram tantas coisas.
Não me lembro ao certo durante quanto tempo usei o Arch, mas acho que passei de
4 meses.

Acabou que cheguei em um estado em que eu só uso o sistema. Não há muito mais o
que aprender (a menos que o meu próximo passo fosse se tornar um *developer* do
Arch Linux, ou então aprender um conjunto de coisas que seriam *específicas*
demais, e não necessariamente úteis no geral). E eu, depois de desenvolver [um
histórico de testar várias distros, uma atrás da outra]({{< ref
"2013-09-07-era-uma-vez-kernel-panic-uma-historia-de-amor-parte-1" >}}), ainda
tenho esse impulso. A verdade é que eu nunca conheci nenhuma distro tão
profundamente, porque eu sempre migrava de uma para outra assim que eu saía da
minha zona de conforto. Mas, agora, depois de ter ficado em uma por tempo
suficiente, e **gostado pra caramba do Arch**, agora eu sinto que o próximo
passo *natural* é o de largá-lo. Oh yeah, a forma de descobrir se você
*realmente* vai sentir falta pra caramba de alguma coisa é largando-a por um
tempo. E eu tenho certeza de que vou me sentir extremamente desconfortável (pelo
menos no começo) utilizando qualquer outra distro, porque me acostumei pra
caramba com muitas peculiaridades do Arch. Gostaria de compartilhar aqui os meus
stats de uso do zsh durante o tempo que usei o Arch:

```
1 1452 14.5215% sudo
2 1108 11.0811% pacman
3 573 5.73057% ls
4 464 4.64046% cd
5 442 4.42044% cower
6 378 3.78038% emq
7 337 3.37034% man
8 337 3.37034% cat
9 229 2.29023% echo
10 225 2.25023% rm
11 191 1.91019% git
12 107 1.07011% mv
13 99 0.990099% synclient
14 92 0.920092% wine
15 90 0.90009% which
16 87 0.870087% pkgfile
17 84 0.840084% less
18 77 0.770077% find
19 72 0.720072% pkill
20 67 0.670067% mkdir
```

Colunas: ranking, quantidade de vezes que o comando foi chamado, porcentagem de
uso do comando e nome do comando / programa.

**Update (2026-08-18)**: Já não me lembro mais do que significa `synclient`.

O **pacman** é o gerenciador de pacotes do Arch (eu uso ele *pra caramba*), e o
**cower** é um AUR Helper (basicamente, uma ferramenta que me ajuda a obter (e,
posteriormente, instalar) pacotes não-oficiais do Arch). O **emq** é
simplesmente um alias para `emacs -nw` (algo como 'emacs quiet'). O **pkgfile**
também é específico do Arch.

OK, saudades pré-registradas, *what's next?* Eu escolhi instalar o openSUSE. Eu
sempre coloquei o openSUSE como a minha segunda melhor distro pessoal, apesar de
só tê-lo usado por uma semana. Existe um conjunto de coisas que eu gosto nela, e
que só agora vou poder confirmar se *realmente* gosto. Por que não Ubuntu, Linux
Mint, Elementary OS, Debian, Fedora, CentOS, ...? Por quê?????? Well, se eu
fosse instalar uma dessas distros para uso *pessoal*, eu instalaria ou o Debian
ou o **X**Ubuntu. Eu não gosto da interface Unity do Ubuntu por um conjunto de
motivos; o Mint e o Elementary eu deixo como recomendações para novos usuários,
mas eles não oferecem nenhuma super vantagem se você é um usuário mais avançado;
o Fedora tem algumas *annoyances*. O `yum` é muito bom, mas o problema são
outros aspectos do Fedora. E o debian? Ah, eu só não instalaria o Debian para
meu desktop pessoal simplesmente porque os pacotes dele são meio *outdated*...a
segunda distro que mais se aproxima de *rolling release* (uma feature da qual
sentirei bastante falta), depois do Arch, eu acredito que seja o openSUSE*.

Então...vamos lá, o máximo que pode acontecer é eu ficar com raiva do
openSUSE...nesse caso, provavelmente eu teria que mergulhar no
[distrowatch](http://distrowatch.com/) para procurar uma outra distro.
