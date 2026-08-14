---
title: "Era uma vez...kernel panic, uma história de amor (Parte 1)"
url: https://perrotta.dev/pt/posts/2013-09-07-era-uma-vez-kernel-panic-uma-historia-de-amor-parte-1/
last_updated: 2026-08-14
---


Eu comecei a escrever esse post faz uns 3 meses, no dia dos namorados desse ano
(isso explica o título sugestivo do post). Mas tinha desistido porque eu não ia
conseguir expressar, na época, todas as ideias que eu queria. E nem vou hoje, se
querem saber. (Saber) expressar todas as ideias é uma arte difícil! Mas decidi
editar o post e acrescentar mais algumas coisas nele para publicá-lo, *anyway*.

Por sinal, devo dizer que escrever um post para lê-lo três meses depois faz com
que você aprenda bastante e reflita sobre sua própria maneira de se expressar!
Bom, segue o post abaixo. Desafio o leitor atento para perceber a diferença do
que eu escrevi hoje e do que eu escrevi três meses atrás.

Nesse post vou falar um pouco sobre a minha (não apenas a minha) experiência com
GNU/Linux. Em particular...dos momentos mais difíceis!

Antigamente as coisas eram mais difíceis para a galera *open source*. Mas que
coisas? Estou falando do hardware. Era extremamente difícil encontrar drivers
apropriados para os hardwares da época. Placa-mãe, placa de vídeo, placa de
rede, placa de som...ah, são tantas placas!

Então a comunidade *open source* começou a escrever os seus próprios drivers.
Isso parecia que não iria dar muito resultado no começo mas, hoje em dia, graças
ao esforço dela, hoje temos uma compatibilidade de drivers muito grande com os
kerneis atuais do GNU/Linux. Muito grande não significa 100%! Apesar da maioria
das distros de GNU/Linux ter facilitado bastante seu processo de instalação e
funcionar muito bem hoje em dia *out-of-the-box* (por exemplo, o Ubuntu), sem
precisar de uma busca específica por drivers e da instalação dos mesmos
manualmente – e, pior ainda, a *compilação* de alguns componentes dos mesmos –
nem tudo são flores.

Ainda vejo por aí algumas pessoas com dificuldades em ter um ambiente GNU/Linux
100% funcional. Especialmente em hardware mais recente. O grande problema é que
as grandes companhias se recusam (em geral) a disponibilizar drivers abertos
para GNU/Linux. Daí, fica mais trabalhoso para a comunidade...

Um bom exemplo é a AMD. Ela tem seu driver proprietário, o famoso *catalyst*,
frequentemente conhecido por ter **alguns** problemas
([cinnamon](https://bugs.launchpad.net/linuxmint/+bug/1208573), [Elementary
OS](https://bugs.launchpad.net/elementaryos/+bug/1017091), [Bugs no
Launchpad](https://bugs.launchpad.net/bugs/+bugs?field.searchtext=catalyst&search=Search+Bug+Reports&field.scope=all&field.scope.target=)).
O driver ser proprietário significa que seu código não é aberto, o que é ruim,
já que ele não pode se beneficiar das melhorias que a comunidade *open source*
poderia lhe proporcionar. No entanto, essa questão é um dilema para a empresa,
porque abrir seu código fonte pode potencialmente implicar em que outras
empresas concorrentes descubram seus segredos de produtos, possivelmente criando
prejuízos à AMD. A questão de software open source de empresas **SEMPRE** vai
ter esse dilema. Naturalmente, não é necessário utilizar o driver proprietário
da AMD (hoje na versao 13.8 BETA). Também é possível utilizar os drivers da
própria comunidade. Só que esses drivers são genéricos e, na maioria das vezes,
não tiram todo o proveito da sua placa gráfica, o que significa que o suporte a
3D, dentre algumas possíveis otimizações, não serão completamente (ou sequer)
aproveitados.

E, ainda hoje em dia, é bastante surreal rodar um ambiente **COMPLETEMENTE,
100%** livre (ou mesmo open source. Existe uma diferença técnica entre livre e
open source, mas isso fica para outro dia). A idealização do Stallman ainda está
longe de ser COMPLETAMENTE implantada (apesar de que, felizmente, boa parte do
que ele tinha em mente foi difundido por aí). Por que eu estou falando isso?
Bom, por acaso você conhece alguma pessoa (incluindo você mesmo) que utiliza [um
desses sistemas aqui](http://www.gnu.org/distros/free-distros.html)? Mesmo  os
mais populares dentre eles (Parabola e gNewSense)??? Acho que não, não é?

E, o pior ainda, algumas empresas ainda tomam iniciativa para dificultar mais
ainda a instalação de GNU/Linux em seus computadores. É claro que estou falando
da Microsoft e do *secure boot*, incluído através da UEFI. Um exemplo prático:
se você tem uma BIOS gráfica, toda moderna e tal, é bem provável que o seu
computador tenha suporte a UEFI e, portanto (mas não necessariamente) ele deve
possuir *secure boot*. Qual o problema do *secure boot*? É basicamente uma
forma que a Microsoft inventou para impedir que software "malicioso" seja
carregado e executado durante o boot do sistema (Windows). Isso dificulta a
instalação de GNU/Linux, que fica sendo reconhecido como "malicioso".

Então podemos sempre entrar na filosofia: isso é necessariamente algo ruim?
Depende. Por mais que você cisme em ser *fanboy* e atacar a Microsoft, [talvez
seja mais inteligente pensar duas vezes antes de falar alguma
coisa](http://www.extremetech.com/computing/96985-demystifying-uefi-the-long-overdue-bios-replacement).
A tentação pode não ser algo bom aqui. De qualquer modo, o UEFI dificulta
bastante, em alguns modelos novos de *notebooks*, a vida de usuários de
GNU/Linux. Isso significa que boa parte de potenciais novos usuários podem se
afastar facilmente dele. O que também significa que os usuários que forem
continuar a usá-lo provavelmente são mais fiéis à (política?) filosofica open
source. Isso pode ser uma grande bobagem, ou não. Tudo depende desses usuários.
Depois vou escrever um post falando melhor sobre o que eu penso disso.

Ah, isso foi um *background.* Talvez um pouco extenso...mas enfim. Eu disse que
ia descrever a minha experiência, então vamos lá. Vou tentar fazer isso de modo
mais ou menos cronológico.

**A minha primeira distro foi o Ubuntu.** Acho que ela é a primeira distro
de muita gente (desde meados de 2010 até hoje que ele é popular, creio). Comecei
a utilizar GNU/Linux em abril do ano passado, logo quando entrei na
universidade. A minha motivação inicial para fazer isso foi mais simples do que
parece: queria utilizar algo diferente. Nós humanos (ou jovens?) sempre, por
natureza, somos curiosos e buscamos sempre experiências novas. A diferença é
que nem todos buscam experiências muito boas.

Gostei bastante do sistema. Na época, **por uma sorte inexplicável**, a
interface com a qual fiquei em contato foi o bom e velho [GNOME 2.32.](https://help.gnome.org/misc/release-notes/2.32/) Por que sorte? Porque nessa
época o Ubuntu da Canonical já adotava o [Unity](https://unity.ubuntu.com/) como
interface padrão. E eu fui descobrir depois que eu não gostava do Unity (como
interface). [Muita gente não gostou dessa ideia](https://www.google.com.br/search?q=ubuntu+nao+é+uma+democracia) de a Canonical
resolver desenvolver o Unity...mas isso é outra história (tudo sempre é outra
história, isso é inevitável. Ou então vamos ter um post falando sobre [a
história de tudo](http://www.skoob.com.br/livro/1676-breve_historia_de_quase_tudo)).

Por sinal, foi ao descobrir o Unity que eu entendi um pouco melhor a motivação e
o projeto do Ubuntu. E passei a apoiar e a gostar disso, e a conhecer o grande
Mark Shuttleworth. É graças ao Ubuntu que hoje em dia existem produtos como o
Steam e o Skype para Linux. Pelo menos foi graças a ele que essas coisas
passaram a existir **logo** nesse mundo.

Ah, aquela sorte que eu expliquei na verdade é bem explicável. Ela era
inexplicável *na época*. A questão era que o Unity queria suporte 3D para rodar
na minha placa gráfica, mas por algum motivo o software não foi instalado
corretamente (automaticamente, na verdade...). Foi por isso que o GNOME assumiu.
Bom, não importa. A questão é que isso proporcionou um ambiente *user-friendly*
com o qual eu me senti bastante à vontade na época, tanto quanto no Windows 7.

Um mês depois, descobri que poderíamos escolher outras **interfaces** (eu
chamava assim na época, é claro, mas os termos mais adequados são **window
manager** e **desktop environment**). Resolvi experimentar o [KDE](http://kde.org/) (que sempre foi conhecido por ser rival do GNOME, diga-se de
passagem).

Foi aí que comecei a aprender e descobrir um pouco da filosofia desse mundo.
Tive que me cadastrar em alguns fóruns e realizar algumas pesquisas básicas para
descobrir um pouco mais sobre como a coisa toda funcionava e o que eu deveria
fazer para trocar de ambiente gráfico. Isso tudo foi muito bom e produtivo, é
claro, pois me proporcionou bastante conhecimento na época. Bastante....hahaha,
tenho que rir disso. Nós sempre achamos que aprendemos bastante quando sabemos
**só um pouquinho mais**. Isso é bobagem. A humildade e o reconhecimento da
própria ignorância são dois valores importantes. Quando mais você aprende, mais
você sabe que não sabia e que **paradoxalmente, ou não, continua sem
saber**. Essa é a beleza do conhecimento! A conclusão? Apenas abra os olhos, se
você conhece alguém que diz que sabe (ou acha que sabe) *bastante* de alguma
coisa, ou ela tem bastante experiência com aquilo, ou ela é ingênua no que diz
respeito ao conhecimento. Maaaas enfim.

Instalei o KDE. Caramba, aquilo realmente era um mundo novo! Cheio de
configurações e de personalizações, customizações, firulas e tudo o mais. E eu
amava aquilo. A possibilidade de poder configurar praticamente todos os aspectos
de cada programa e de alguns componentes do sistema, aquilo era uma coisa tão
linda! Especialmente para quem não estava acostumado a fazer esse tipo de coisa,
é claro. Eu me tornei fã do KDE durante muito tempo, estendendo a minha opção
por ele durante muito tempo, inclusive em outras distribuições.

Ah, vale informar que eu instalei o KDE foi dentro do próprio Ubuntu. Podendo
inclusive voltar para o GNOME a hora que eu quisesse. Estava descobrindo a
beleza do que era um **display manager**. Os dois desktop environments ficavam
instalados no sistema ao mesmo tempo, e eu poderia escolher qual deles eu
gostaria de usar na hora do *login*.

Depois de um tempo fui descobrindo mais liberdades e me aventurando mais nesse
mundo. Vou continuar essa história numa segunda parte desse post. Ainda tem
bastante coisa para ser contada. Até lá!

