---
title: "Retrospectiva 2013 (blablabla)"
url: https://perrotta.dev/pt/2013/12/retrospectiva-2013-blablabla/
last_updated: 2026-04-22
---


Esse post é bem mais específico do que o título pode deixar a entender. Já
existem emissoras de TV capitalistas que fazem retrospectivas gerais sob suas
próprias visões capitalistas. *Capitalista* é uma palavra bem genérica nesse
contexto, mas é melhor deixar assim mesmo, não preciso entrar em detalhes nisso.

Em vez disso, esse post é um pequeno resumo de minhas conclusões e aventuras
desse ano. Está muito longe de cobrir tudo, senão ele ficaria enorme. Então
selecionei alguns tópicos.

Adicionalmente, eu vou deixar claro – de antemão – que não vou incluir nenhum
link aqui. Usualmente eu faço isso, mas dá um certo trabalho, comparado ao
retorno que eu ganho com isso. Então, qualquer coisa simplesmente utilize os
arquivos ou a função de pesquisar do Wordpress.

## (GNU? /) Linux --> Arch Linux

Acho justo começar com isso, até porque provavelmente é o tópico do qual mais
falo nesse blog. Esse ano eu testei distros *pra caramba*. Mesmo. Foram várias
experiências e aventuras novas. Em geral, quando você testa algo novo,
geralmente as coisas que mais te chamam a atenção inicialmente costumam ser o
*looking & feel* e o número de pessoas que já se interessaram por aquilo. A
primeira coisa está ligada à natureza humana, que é bastante estimulada pela
visão. Já a segunda pode ser mais explicada pelo *networking effect* (veja a
Wikipedia).

Então, naturalmente as distros que mais me impressionaram foram o Elementary OS,
o Linux Mint e o openSUSE. Suas interfaces padrões são bastante limpas
(especialmente a do Elementary) e bonitas. No entanto, a distro que mais me
agrada hoje é simplesmente uma caixa preta. Sem desenhos e ícones, sem X, sem
display manager, sem programas, sem nada. Pelo menos no começo...preciso dizer
que estou falando do **Arch**?

Foi bastante interessante a forma que eu o conheci e que passei a utilizá-lo. Um
amigo que falou que usava. Daí eu me interessei (olha o networking effect aí,
gente...). A verdade é que o processo de instalação do Arch é bem mais peculiar
do que o das outras distros. Então eu não consegui instalar ele de primeira (e
    nem me interessei muito, também). Deixei isso pra lá e continuei utilizando
    o que eu estava utilizando na época (provavelmente era o openSUSE, mas eu
    estava mudando de distro toda hora).

Numa segunda tentativa, eu nem lembro qual foi o contexto, mas eu lembro que, na
teoria, instalei tudo direitinho. Eu já tinha um bom conhecimento sobre
partições de MBR. Não tive dificuldade em criá-las com o cfdisk. Só que eu não
criei um filesystem (ext4) pra elas...então sabe-se lá o que aconteceu, ficou a
maior bagunça no negócio. Não afetou nada porque eu tinha utilizado um HD só
para isso. Depois de descobrir que todo o meu processo de instalação foi por
água (HD) abaixo, deixei isso pra lá de novo.

Numa terceira tentativa, eu fui seduzido pelo projeto Archbang (Arch Linux
out-of-the-box com o Openbox), cujo processo de instalação é bem mais
*straightforward*. Mas só cheguei a utilizá-lo por uma semana. Não era
tão completo quanto eu queria (veja bem, todos começamos com o mundo
Ubuntu/deb ou Fedora/rpm...acostumados com tudo na mão, configurado
bonitinho e tudo o mais).  Mas foi nele que comecei a gostar do pacman
(o **pac** kage **man** ager do Arch).

Então conheci o Manjaro. O Manjaro é aquele tipo de distro que as pessoas que
gostam de utilizar a expressão "criado a leite com pêra / danoninho" ficariam
encantadas em utilizar. É uma sensação meio única. Ele é derivado do Arch. Eu
utilizei ele por umas duas semanas no meu notebook antigo, e depois que eu me
livrei dele, caramba, foi uma das melhores coisas que já fiz. Eu não sei
explicar, mas eu passei a ter um extremo desprezo por essa distro.

Sabe-se lá em qual ponto dessa história, eu tentei instalar o Arch pela terceira
vez. Daí: pronto, nunca mais tirei ele. Só tive que reinstalá-lo mais uma vez
depois que comprei um notebook novo, que tinha UEFI, SSD etc. Só que eu estava
com pressa, então eu caí em tentação e instalei primeiro o Linux Mint 15 (na
época), o qual ficou por lá por umas duas ou três semanas. Depois reinstalei o
Arch (agora eu já sabia =P) e pronto, aí nunca mais tirei ele. Até agora, estou
com a mesma instalação dessa época, talvez façam uns 2 meses. E provavelmente
vou utilizá-lo permanentemente, a menos que apareça uma distro para me fazer
mudar de opinião, o que eu acho bem difícil, dado que eu já testei várias delas
(SteamOS não vale ^^). Se eu mudar de sistema, vai ser para o OS X. Mas eu não
tenho certeza se gosto do mundo Apple ou não. Não posso detestá-lo porque nunca
o testei direito, a não ser uma vez numa máquina virtual (dica: achei horrível,
se for para falar de experiência. Talvez as pessoas gostem mais seja da
arquitetura dele ou das aplicações que ele suporta. Mas enfim...). Mas, de mundo
Linux, estou satisfeito aqui.

Ah, antes de encerrar esse tópico, deixa só eu falar algumas coisas do Arch. O
pacman (já falei antes dele) é um dos melhores package managers que já vi.
Melhor, nesse caso, significa mais simples (KISS) e poderoso ao mesmo tempo. O
segundo melhor package manager que já testei foi o zypper, do openSUSE, e é por
isso que eu digo que o openSUSE é a minha segunda distribuição para uso pessoal.
No fundo, aprendi isso, o que mais define uma distro é o seu package manager. O
restante são acessórios, localizações de arquivos, organizações de arquivos,
sistema de init (systemd, openRC, upstart etc). Programas? Não a longo prazo.
Programas que já vêm pré-instalados só fazem diferença se a distro for usada num
LiveCD, ou se você quiser instalá-la e usá-la já, out-of-the-box. Nesse sentido,
continuo a admirar o Puppy Linux e o System Rescue CD. Clonezilla não vale...

Outra coisa: a Wiki do Arch é uma das melhores fontes de documentação que já vi.
Melhores = mais organizadas e completas. E é por isso que eu faço questão de
ajudar a editá-la. Não faço isso com muita frequência, pelo menos não hoje, mas
sempre que eu leio uma *wiki entry* extensivamente, costumo acrescentar um
detalhezinho ou outro. A verdade é que na maioria das vezes isso não precisa ser
feito. A menos que sejam acrescentados detalhes para deixá-la *bloated*, o que
é contra a filosofia do Arch. Mas, fora isso, ela vai muito bem, obrigado.

A comunidade do Arch é fantástica. Uma das comunidades mais inteligentes que já
conheci. Comunidades como a do Ubuntu também têm pessoas muito inteligentes, sem
dúvidas. O "problema" é que ela é uma distro para beginners, o que significa que
os fóruns sempre estarão cheios de informações *triviais*. OK, estou
generalizando um pouco, mas...só quero dizer que o fórum do Arch é um lugar
repleto de conhecimento. Dificilmente eu entendo alguma coisa de lá de cara.
Geralmente é sempre algum assunto mais avançado. Isso mesmo no 'Newbie Corner'!
Mas isso é muito bom, porque significa que sempre estou aprendendo alguma coisa.
Além disso, a comunidade de lá é bastante intolerante com gente preguiçosa, que
quer tudo na mão etc, etc e etc. Isto é, existe uma filosofia **bastante forte**
no Arch que diz que você tem que fazer a sua parte quando quiser ajuda/suporte.
O que significa que você tem que pesquisar primeiro. Se esforçar um pouco. Se
você não se esforça nem por você mesmo, a comunidade do Arch não fará isso por
você. No começo isso parece uma atitude elitista, arrogante ou antipática
(entenda como quiser) mas, a verdade é que **hoje** eu acho uma ótima atitude. É
esse tipo que coisa que faz com que a comunidade do Arch seja extremamente
inteligente (esforçada, pelo menos, certo?) e faz com que pessoas que não querem
**se** ajudar (e, portanto, que não vão ajudar a comunidade) se afastem de lá.
Sem contar que evita a duplicação de tópicos no fórum etc. Isso é muito bom
porque também faz com que a maioria dos usuários do Arch contribuam de volta
para a comunidade de alguma forma. Seja pela wiki, pelo fórum, reportando bugs,
etc. Você se sente muito mais "em casa", e "à vontade", para fazer isso.  Estou
falando sério! Eu nunca me senti à vontade para reportar bugs (por exemplo) no
Linux Mint. No Arch você é bastante incentivado a fazer esse tipo de coisa. Por
sinal, eu já fiz isso uma vez, e logo no mesmo dia o bug já foi corrigido (no
caso, era um erro de dependência, acho que na hora da compilação, ou de pacote,
algo similar).

Já que eu falei bastante do Arch, vou deixar uma mensagem aqui: se você se
interessou por isso, tente experimentá-lo. Se não conseguir, procure suporte nos
fóruns (fazendo a sua parte de pesquisar primeiro...) oficiais, ou mesmo comigo.
Faço questão de ajudá-lo! Mas, para isso, você vai ter que querer se ajudar
primeiro, como falei no parágrafo anterior. O esforço pessoal é fundamental.
Devo dizer que a comunidade BR do Arch é meio parada (pelo menos nos fóruns).
Mas, lá fora, ele é bem mais popular.

Tem uma outra coisa bastante legal que eu não falei (eu não falei nem que o Arch
é rolling release...como eu disse, vá pesquisá-lo você mesmo =P). O **AUR**.
Arch User Repository.  É um conjunto de scripts que os usuários do Arch criam
para criar pacotes, para que os programas fiquem integrados com a distro. Cara,
o AUR (junto com os repositórios oficiais) tem o catálogo mais completo de
software que já conheci. Acho que ele supera os PPAs do Launchpad e o Build
Service do openSUSE. Todo programa que já imaginei está lá (na verdade, um
script de como obter/compilar/instalar o programa). E, se não estiver, sempre
tem alguém da comunidade para incluí-lo lá. Eu já tentei fazer isso, mas não
consigo encontrar um único programa que não esteja lá. Pelo menos dos que eu
queria usar, é claro. Ainda não precisei criar um pacote.

Agora chega disso senão esse tópico vai ser só do Arch.

## Programação

Esse ano aumentei de forma significativa o meu conhecimento de C/C++.
Especialmente porque desenvolvi uma biblioteca de grafos como parte de um
trabalho da disciplina de Teoria dos Grafos da faculdade. Também por causa da
Maratona. Isso me fez decidir que C++ é uma linguagem importante pra mim.
Provavelmente eu vou aprender ainda mais no futuro. Atualmente eu estou lendo um
livro de programação de QT (um Toolkit de GUI) com C++, por exemplo.  Digo isso
porque cheguei a um ponto em que eu ia deixar C++ de lado. Ultimamente as
linguagens de alto nível, rápidas, 'mamatas',  "etc etc e etc" estão dominando
as coisas. You know, aquela história de visual programming, Ruby, Python,
Haskell  Uma chuva de alto nível. E desenvolvimento web. Eu fui seduzido por
elas e por isso ia deixar coisas como Java e C++ de lado. Médio nível,
sabe...(há quem diga que Java é alto nível, só que você escreve demais em Java,
então...).

Mas esse ano foi importante para eu concluir que C++ é algo importante pra mim.
Mesmo que eu não vá usá-lo no futuro. Não vou deixar de perder nada se continuar
estudando ele.

Também vi bastante confusão dizendo que C++ é uma péssima linguagem. Linus
Torvalds e Eric Raymond que o digam. Enfim, todo esse choque cultural de
opiniões chegou a tal ponto em deixar essa linguagem destacada na minha vida.

Ah, o C também! Vai depender da aplicação. C++ é melhor para trabalhar com
classes. Mas ainda há muitos projetos bons feitos em C puro.

Outra coisa: Python e Bash são bastante úteis. Também decidi que vou aprender
mais sobre eles no futuro. Python 3 em vez de Python 2, muito provavelmente.

Java. Hummmmmmmm. Java. Que coisa complicada, todo mundo odeia Java. Vou dizer o
seguinte: Java ainda é útil por causa do Android. Vou aprender (estou
aprendendo) Android, então ainda vou considerar Java na minha vida.

Racket, Emacs Lisp e Common Lisp. Esse ano fiz um curso no Coursera que me
deixou **encantado** com as linguagens funcionais. Não importa o que eu faça da
minha vida, eu vou estudar mais sobre elas. É um tópico muito lindo, muito bem
feito. Não sei como ainda ensinam **hoje** Pascal, FORTRAN e uma linguagem
maluca lá de Python na Web, da qual não me recordo o nome agora, nos primeiros
períodos de algumas faculdades ou de ensino médio. Racket é uma ótima linguagem
para ensinar programação pra alguém que nunca fez isso. Aiai.

Sobre o Emacs: desde o ano passado eu comecei a aprendê-lo, sendo que passei a
utilizá-lo no cotidiano mais esse ano. Atualmente eu uso inclusive o Org mode
dele. É uma ferramenta fantástica.  Já tive muito receio de "ficar para trás"
por não usar o Vim, que é muito mais popular do que o Emacs – convenhamos. Mas a
verdade é que isso não importa. No fim das contas, vale mais saber utilizar um
editor, não importa qual. Além do mais, posteriormente descobri que o Emacs é
bem mais poderoso e fácil de estender do que o vim. Então, a longo prazo, ele é
uma decisão bem mais viável para mim. O Emacs assim como a sua Wiki são muito
grandes, existem muitos scripts para serem explorados...é melhor só ir
aprendendo sob demanda, por uma questão de que há outras coisas mais importantes
para serem estudadas e feitas.

Eu posso continuar citando várias linguagens aqui infinitamente. Estou dizendo
as que eu tenho mais contato, mais ou menos por grau de familiariadade, mas acho
que já chega. Sem contar que também existem vários utilitários isolados, como o
grep, o gcc, o gdb, o git, o tar, etc.

Sobre o git: é um ótimo DVCS para ser aprendido. Muito bom mesmo. Mas ele também
é muito grande...sempre há o que aprender, okay? Eu ainda quero aprender SVN ou
BZR, mais para entender o que é um VCS do que por querer aprendê-los, porque eu
já acho o git ótimo. É aquela mesma história: você só entende o que é uma distro
de Linux quando testa várias delas. E só entende o que é um VCS quando testa
vários...por aí vai. Agora, o git é maravilhoso. Todos os projetos que considero
importantes estão o utilizando.  Vale a pena aprendê-lo sob demanda, que nem o
Emacs.

LaTeX: show. Ainda bem que não precisei aprender troff. Nem TeX puro. O LaTeX é
bastante straightforward, e existe uma ótima comunidade de Q&A para ele no Stack
Exchange, então não há nem o que reclamar. E também o texlive é bastante
estável. Continuo admirando essa ferramenta. Agora, eu devo dizer que o LyX é
uma ótima front-end para ele quando estamos com pressa. A menos que seja um
documento longo a ser desenvolvido, é muito mais conveniente utilizar LyX do que
LaTeX. O Evil Red Text te deixa fazer tudo o que quiser.

Office: o Libre Office vem ficando cada vez mais maduro. Tem um lugar na
Alemanha que já o adotou ele como padrão. Assim como um lugar no Rio Grande do
Sul. Anyways. Eu prefiro utilizar LaTeX. Mas, se tiver que ser rápido, gosto do
Google Docs. A verdade é que editar documentos de maneira compartilhada é bem
mais atrativo do que qualquer coisa que o LibreOffice (ou o Microsoft Office)
possam vir a oferecer. Aposto na plataforma do Google.

Terminal: zsh é fantástico. Prefiro ele ao bash. Mas, os dois são muito
poderosos.

Também existem várias linguagens de Markup rápidas. Tipo Markdown. É a que eu
**mais** gosto. Na verdade, descobri que existem linguagens até demais
assim...tem o tal do Restructured Text, e mais uma porrada de coisas. Cada vez
tem um formato diferente no README de algum projeto do github.

"O que mais aprendi esse ano"? Poxa: SSH (daemon e acesso), FTP, telnet (eu
jurava que ninguém usava mais isso, mas usam sim), SAMBA (desisti disso, SFTP é
bem melhor), rsync (fantástico! Eu gosto do Unison, mas o rsync puro é muito
poderoso), UML (o basicão, para representar diagramas de classes). Em geral, e
isso foi facilitado por usar Linux, eu tentei reter um conhecimento mais geral.
Não super me aprofundei em nada, talvez apenas um pouquinho em C++.
Provavelmente existe um item ou outro que eu esqueci de citar, mas não importa.
Esse post não é um portfólio, é apenas um registro das coisas que eu aprendi. Em
particular, (em geral) trocas de experiências em quaisquer dessas linguagens que
citei sempre serão bem-vindas. Se você quiser conversar, é só dizer. No entanto,
devo dizer que prefiro, pelo menos a partir do ano que vem, começar a aplicar
tudo isso que aprendi em algo mais útil, ya know, em algum projeto, right?

A última coisa que eu estava aprendendo era como criar pacotes no Arch Linux
(makepkg, PKGBUILD e companhia).

## Livros

Esse ano voltei a ler bastante. A minha tentativa de meta é ler 24 livros por
ano. Em particular, é bastante fácil *trackear* isso se você usa o Goodreads. Eu
atingi essa meta no ano passado e também esse ano. No ano retrasado? Não me
lembro, só comecei a utilizar o Goodreads em 2012. Se quiser, pode me adicionar
lá. Infelizmente não é todo mundo que gosta de uma rede social de livros.

No ano passado e no início desse ano li mais livros de histórias / literatura,
digamos assim. Séries como O ladrão de raios (Percy Jackson), A Bússola de Ouro
(Philip Pullman), O Senhor dos Anéis (ah, livro longo pra caramba), etc.
Ultimamente eu tenho lido mais autobiografias e livros de software livre ou de
temas de informática. Por exemplo, recentemente li uns livros do Nicholas Carr e
do Eric Raymond.  Sim, faz tempo pra caramba (1 ano é bastante tempo, poxa) que
    não leio nenhuma ficção haha. Preciso relaxar um pouco. Mas, confesso que
    estou satisfeito com as minhas leituras atuais. Bom, todo o meu histórico de
    leitura está no Goodreads, não vou citar tudo aqui, esses foram os
    principais, eu acho. Sempre me escapa algum.

Não preciso dizer que ler no Android é bem mais confortável para os olhos do que
ler no Symbian. Apesar de tudo, ler no Symbian é muito mais confortável para os
dedos. Ah, touch faz mal. Aquela história de emacs *pinky* mais touch *screen*
de Android...haja massagem nos dedos.

## Séries / Filmes

Não. Simplesmente não. Okay, desde 2011 eu passei a indexar fortemente tudo o
que eu vejo. Em geral utilizo o Filmow para isso. E, você sabe, geralmente
indexação implica em seguir um padrão. Da mesma forma que o Goodreads me fez
passar a ler mais frequentemente e regularmente, o Filmow me fez passar a
assistir mais séries e filmes com frequência. Note que em geral eu não estou nem
aí se eu não conheço um ator ou atriz X ou um filme Y ou um diretor Z ou uma
produção W....não, eu acho isso *trivia*, para mim não é importante. Assisto a
séries e filmes para relaxar, e não para conhecer as coisas.

Agora você deve estar se perguntando porque o "não, simplesmente não" no início
do parágrafo anterior. Ah, é porque esse ano eu não assisti quase nada =/. Pelo
    menos não comparado ao ano passado (espere até eu falar de *gaming*). De
    série, eu assisti todas as temporadas de The Office, devo dizer que achei
    uma série bastante boa, um "mockumentary" para variar as sitcoms; continuei
    a assistir The Big Bang Theory e, nesse último mês, voltei a assistir How I
    Met Your Mother. É incrível, 1 ano se passou mas ainda não comecei a
    assistir Game of Thrones. Estava na minha watchlist desde o início desse
    ano...bom, já vi que vai ficar para ano que vem. Vamos ver se consigo
    assisti-la antes da quarta temporada começar, né?

Sobre filmes, bah, eu não gosto de falar de filmes de modo individual, em geral
não vale a pena (documentário costuma valer mais). Assisti poucos, bem menos do
que o ano passado, mas alguns valeram a pena.

## Gaming

Não. Não. Não. Não. Não. Não. Não. Não. Não. Não. Não. Não. Não. Não. Não. Não.
Não. Não.

Não joguei nada esse ano. Até que isso é bom, sabe, me dedico mais para a
faculdade...

Nah, mas eu sempre gostei de jogar, mais do que ver séries / filmes. Por que não
joguei nada esse ano? Bom, o motivo principal foi por usar praticamente só o
Linux. As possibilidades de gaming são bem mais limitadas. Mas, felizmente foi
também nesse ano que a Steam começou a se expandir para esse mundo. Espero que
no ano que vem eu possa desfrutar de alguns títulos de lá. Eu não sou um super
fã da Steam (conheço gente pra caramba que é fanático por ela), mas aprecio o
modelo de negócios deles. Diminuem bastante a pirataria de jogos, porque suas
promoções são frequentemente viáveis. A outra coisa é o hardware. Atualmente não
tenho uma placa de vídeo externa, apenas a APU integrada da Intel (a boa e velha
Intel Graphics HD 4000), então isso também contribui para diminuir **pra
caramba** as minhas possibilidades de gaming. Mal rodo dota 2 no Linux...até
vai, mas com muito sacrifício, e com as configurações todas no mínimo.

O último melhor jogo que eu já joguei foi, sem dúvidas, Portal 2. Se a Steam
liberá-lo para o Linux, anota aí, eu vou jogá-lo **de novo**. Mas isso foi ano
passado, no início dele, faz bastante tempos. "Thinking with portals" é uma
ótima forma de puzzle, okay?

Por outro lado, sou razoavelmente ativo no portal Kongregate. Esse ano
apareceram uns novos indies legaizinhos, assim como algumas continuações de
jogos. Sempre tem algo interessante por lá. Só que o Flash está morrendo. Se
eles não se reinventarem, em breve não vai ter muito o que ser feito por lá.

## Random

Existem vários outros tópicos sobre os quais eu poderia falar , tais como
idiomas, organização de projetos, músicas, vídeos (leia: YouTube e Vimeo), IRC,
fóruns de discussão (BBS), redes sociais (Twitter, Google+, Facebook, identi.ca
que morreu esse ano), Android, um outro post estilo 'sugestão de referências'
para outra matéria que não Cálculo, Coursera, Reddit, sei lá. Sempre tem alguma
coisa legal pra falar desses tópicos que citei. Mas esse post já está bem
grande. Sei lá, dependendo do número de *views* e/ou feedback que eu receber,
somado à minha paciência de digitar isso tudo (porque falar sobre essas coisas é
legal; o que dá trabalho é tomar tempo para digitar), de repente eu escrevo uma
continuação. Mas acho que não vou fazer isso.

Por sinal: você pode se perguntar porque eu escrevi esse post. Em geral, eu
gosto de escrever, e esse post foi uma forma de falar de todos os assuntos que
eu falaria nesse blog em um único post, puxando vários assuntos aleatórios daqui
e dali, resumindo e tudo o mais. Então no fundo eu escrevi isso porque acho uma
atividade prazerosa. Além do mais, ao escrever sobre esse tipo de coisa, as
ideias se esclarecem muito mais do que se você simplesmente (apenas) pensar
nelas.  Naturalmente, por escrever tanto, você deve ter notado que eu quase não
utilizei *pronomes* oblíquos (por exemplo: usei ele em vez de o usei), e nem me
dei ao trabalho de escrever todas as frases de forma ótima. Porque senão a
atividade deixaria de ser prazerosa, e portanto não haveria motivos para eu
escrever isso tudo.

Finalizo falando dum assunto que não deve passar despercebido.

## Blog

Meu primeiro post nesse blog foi em Janeiro. No começo, pensei em criar um blog
de tutoriais, para ensinar as pessoas a fazerem algumas coisas. E divulgar
algumas notícias aleatórias. Procure meu primeiro post se for curioso. Mas
percebi que isso seria inútil. Em tempos de Facebook, Twitter e etc, com a
disputa acirrada pela atenção da informação, as pessoas tornaram-se extremamente
ansiosas (e, frequentemente, mas não necessariamente sempre, fúteis), de modo
que querem apenas ler fragmentos de notícia de maneira rápida. E, na maior parte
das vezes, prazerosas. Isso, em geral, significa fuçar a vida dos outros e
compartilhar memes, ou flood. Nicholas Carr que confirme isso.

Então, resolvi criar um blog pessoal. E, na época que decidi isso, já conhecia
vários outros blogs pessoais. De modo que eu já entendia mais ou menos o que as
pessoas gostavam de postar sobre si mesmas e sobre seus cotidianos, e já tinha
inspiração suficiente para decidir também fazer isso aqui.

No começo, além de eu não saber muito bem qual seria o nicho da coisa, eu
postava bem menos frequentemente. E tinha um número de views bem pequeno também.

Atualmente, posto de maneira mais ou menos regular; mas, ao acaso, não me sinto
obrigado a fazer isso. Só o faço quando tenho tempo, vontade  e um tema que eu
considero interessante ou útil. Ás vezes só posto para deixar um conhecimento
registrado e compartilhado.

O meu número de views não é nada sensacional. Mas, considerando o tipo de posts
que escrevo (aquilo que eu falei: não é nada geral, de memes ou de flood), eu
estou satisfeito. Especialmente mais ultimamente, no qual ele está ligeiramente
maior e regular do que era no começo. Não ligo muito pra isso porque não
monetizo nada por aqui. Isso, repito, é um blog pessoal. Naturalmente, se eu
quisesse ganhar algum dinheiro com propagandas, provavelmente teria que deixar
de postar algumas coisas que me interessam e passar a postar "o que o povo
gosta", visando atrair o maior número possível de views. Mas aí essa atividade
deixaria de ser prazerosa.

Em particular, escrevo alguns posts em inglês. Isso começou para eu treinar o
meu inglês. Depois de um tempo, ao divulgar meu blog em alguns canais, percebi
que atingi um número significativo de views estrangeiros. Hoje fiquei surpreso
quando vi que alguém utilizou o google tradutor para traduzir um dos meus posts
para o holandês. Whooooa, quem diria ahahaha. Também noto um tráfegozinho ou
outro pelo duckduckgo.  Uns poucos pelo Reader do Wordpress. A maioria é pelo
Facebook (isso é que dá a centralização de informação essencialmente em uma
única rede...). O meu número de views máximo em um único dia foi algo em torno
de 300. Cara, que orgulho hahaha. Nunca vi tantas bandeiras (de países)
diferentes. Isso foi em um dos posts da Openbox Challenge. Por outro lado, já
teve post sem view nenhum #fail haha.

Esse negócio de views é engraçado. Por eu não ter compromisso nenhum com isso, é
prazeroso ver um pico de vez em quando. E dá para entender porque alguns blogs
conseguem render dinheiro. Sinto que se eu me esforçasse para escrever um blog
específico (digamos, sobre Android, ou Linux, ou algo aleatório), provavelmente
eu ganharia um bom dinheirinho com isso. No entanto, eu não escondo que sou
contra propagandas intrusivas, e já recomendei Adblocks aqui várias vezes.

## Conclusão

Pronto, termino o post aqui. Eu ia escrever uma TODO list para 2014, mas deixa
isso pra outra hora (ou pra lá). Word count: ~4500.

*Bis Bald (ou: return 42;)*.

