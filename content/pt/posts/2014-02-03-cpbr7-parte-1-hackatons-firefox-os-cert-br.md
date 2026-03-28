---
title: "#CPBR7 - Parte 1 - Hackatons (Firefox OS + CERT.br)"
date: 2014-02-03T23:58:25-03:00
tags:
  - dev
  - legacy
  - serenity
---

Ah, é claro que eu ia escrever algo sobre a Campus Party aqui! A princípio
pensei em escrever um único post gigante. Só haveria dois probleminhas em
relação a isso: a) ele seria **gigante** (não disse?) ==> eu perderia tempo
demais pra estruturar tudo, e as pessoas provavelmente não leriam tudo direito,
etc, etc e etc e b) existe um equilíbrio entre ansiedade, lembrar-se bem dos
fatos, se focar no que você vai escrever x misturar vários pensamentos, escrever
melhor e não dormir tão tarde para poder ir à faculdade direito...

Então, vamos lá: participei de duas competições. A primeira foi relacionada à
comunidade da Mozilla Brasil (da qual, tenho que dizer, gostei pra caramba! Foi
ela, inclusive, que me motivou a escrever [esse outro
post](http://thiagoperrotta.wordpress.com/2014/02/01/software-e-outras-coisas-livres-revisitados-parte-0-0-01/).
A outra foi do CERT.br. Bom, tenho uma informação ruim e outra boa. Vamos
começar pela ruim...

## Firefox OS

Sobre a hackathon da Mozilla, a proposta foi de criar um app para o Firefox OS.
Foram dadas várias palestras sobre o Firefox OS, acho que pelo menos 3 (ah, mas
a Mozilla deu várias outras palestras também!!!). Eu só vi a segunda, até onde
sei. Na Campus Party, são muitas palestras acontecendo *ao mesmo tempo* (li em
algum lugar que são necessárias 500 horas para ver tudo... o/o/). Provavelmente,
no momento das outras palestras, eu devia estar vendo alguma outra coisa (ou
fazendo alguma outra coisa, *who knows*). De qualquer forma, depois de ver a
segunda palestra, dada pelo [Andre Garzia](https://andregarzia.com/), eu fiquei
fascinado com o Firefox OS. Achei a sua simplicidade uma coisa incrível (se eu
falar que me lembrou do Arch Linux...é people, qualquer palavra relacionada à
KISS ou simplicidade me lembra do Arch, sorry. Ah não, eu acabei de deletar o
Arch, isso vai me deixar triste...). Sério mesmo. Antigamente eu via o Firefox
OS como "ah não, droga, mais uma opção no mercado." Quer dizer, o *droga* é só
pelo *mais uma opção*, porque mais um sistema livre / open source nunca é demais
(agora vai contar quantas distros de Linux existem e o que eu acabei de dizer
torna-se um paradoxo). Muito bem, passei a ver o sistema deles como "caramba,
isso não é só mais um, na verdade é mais uma alternativa, bastante boa – e
simples!". Claro, não vai competir com o Android, duvido que isso aconteça tanto
a curto quanto a longo prazo, mas a beleza da coisa é justamente essa – ele não
foi feito para competir com o Android, mas sim para ser simplesmente uma outra
opção. Da mesma forma que um smartphone não foi feito para completir com um
tablet (-- oi? Aí você coloca o Samsung Galaxy Note (3!!!) no meio...).

Eu gostei tanto do Firefox OS, que eu resolvi tentar criar um aplicativo para o
mesmo. A ideia por trás de um app no Firefox OS é saber usar HTML5, CSS3 e
Javascript. Basicamente, você constrói um aplicativo da mesma forma que constrói
uma interface / tecnologia para a web. A curva de aprendizado para aprender a
programar para o Firefox OS é quase zero se você já sabe programar para a web.
Well, eu quase não sabia nada de web...eu aprendi HTML quando eu estava na minha
8ª série (uns 13 anos), e CSS um pouquinho depois. Mas foi um aprendizado super
*light*, coisa de só querer saber usar. Naquela época nem ensino técnico eu
fazia...basicamente, depois disso, eu quase nunca mais aprendi nada nem de HTML
nem de CSS. E sobre a parte de Javascript? Eu nunca estudei **nada** de
Javascript. Aí você pensa: cacete, pra que se envolver com esta droga se você
não sabe nada? Eu não sei o que me deu, mas eu simplesmente quis participar
disso, talvez por realmente ter-me impressionado com o sistema.

Então, vamos lá, a primeira coisa que eu precisava era de uma ideia. Não podia
ser nada muito complicado, afinal eu não sabia *quase* nada de web... No final
das contas, encontrar uma ideia foi algo bastante difícil. A minha ideia acabou
sendo uma adaptação de algo que já existia. Só que eu resolvi escrever o meu
próprio código-fonte, a minha própria lógica de implementação e o meu próprio
layout. Não era questão de reinventar a roda (Andrew Hunt e David Thomas não
iriam gostar disso...), mas sim que o código das implementações que já existiam
eram fechados. E eu perguntei antes, para a galera da Mozilla, se tinha algum
problema adaptar uma ideia já existente. Veja bem, não era cópia de código +
adaptaçãozinha pra interface mobile. Eles disseram que tudo OK. Eu realmente
criei as coisas do zero (CSS, conteúdo, HTML, lógica Javascript, organização dos
arquivos, blablabla).

Fiz o aplicativo em dois dias (não que houvesse muito tempo mesmo...). No
primeiro dia, basicamente me importei com o HTML e com o CSS (=layout da coisa
toda). No segundo dia, com a lógica javascript. Da série "vamos deixar o mais
difícil para mais tarde...".

Na verdade, HTML é ridiculamente fácil (se você não utilizar nada avançado). A
minha maior dificuldade no primeiro dia foi o CSS. Então...depois de muito
trabalho, consegui o *meu* layout perfeito. Obrigado DuckDuckGo + Google! Bela
parceria. Obrigado também ao Emacs... (não que essas coisas realmente
importassem, no final das contas).

No segundo dia a coisa foi mais feia. Você tem que dividir o seu tempo. Tem que
achar o equilíbrio certo (leia -> ótimo!) entre ler tutoriais de javascript (e
como obter esses tutoriais: videoaulas, tutoriais, posts de blog, wikis, stack
overflow, ...?) e implementar a lógica do seu aplicativo. Tá legal, depois de
apanhar um pouco, consegui fazer a coisa funcionar. Mesmo sem não saber quase
nada dessas coisas. Não sei quanto tempo perdi ao todo, mas acho que foi mais de
8 horas. Umas 4h em cada dia. Talvez 10h. Enfim, poderia estar utilizando esse
tempo para assistir palestras...(perdi algumas palestras que queria ver!!!
*Damn...*).

Depois, a entrega do aplicativo era via github. Se alguém tiver curiosidade,
[esse](https://github.com/thiagowfx/Riddlefox) foi o aplicativo que eu
desenvolvi, liberado sob a licença MIT. Aceito sugestões de como melhorá-lo,
mesmo que o hackathon já tenha acabado.

*Aparentemente* eu não ganhei a
competição...[aaaaaaaaaaaaaaa](http://www.youtube.com/watch?v=Zcps2fJKuAI) (está
bem, essa música tocou lá uma vez). Mas, tudo bem. Aprendi bastante sobre
programação para a web (mesmo com um simples app!) e também sobre hackathons.
Nunca tinha participado antes de uma hackaton. Além disso, sequer esperava que
fosse participar de um! Até onde sei, só iria à CP para me divertir. Tudo isso
foi muito por acaso. Agradeço à comunidade da Mozilla Brasil pela oportunidade,
e também especialmente ao [André](http://andregarzia.com/) (que citei
antes) por tirar algumas de minhas dúvidas (e também por me despertar em relação
à simplicidade (beleza!) do Firefox OS). Também agradeço ao meus amigos que me
ajudaram a testar o aplicativo. Valeu a experiência.

O resultado só seria divulgado após a Campus Party, uma pessoa da comunidade me
disse isso. Mas depois descobri (por e-mail) que a premiação seria divulgada no
sábado (um dia depois que me avisaram que não seria divulgada ali), mas me
enviaram um e-mail avisando sobre isso somente duas horas antes da mesma. Acabei
não vendo os vencedores. Por isso, nem sei se ganhei. É mais provável que não.
Estou esperando a resposta deles =/

## CERT.BR

Agora vem a parte boa. Really, eu falei mais da parte ruim do que vou falar da
boa agora, porque aprendemos mais com os nossos erros (na verdade, o 'erro' aqui
é não conseguir uma colocação suficientemente boa) do que com nossos acertos.

A outra competição da qual eu participei não foi exatamente uma hackathon. Foi
uma competição individual, promovida pelo CERT.br. Intitulada **desafio
forense**. A palestra começava duas e meia da tarde. O desafio deveria ser
completado até seis e meia da tarde. Tivemos em torno de meia hora (talvez 40
minutos) de palestra, a qual nos explicou a ideia básica sobre como era o
desafio, quais ferramentas deveriam ser utilizadas no mesmo, e o que deveria ser
feito. Eu não esperava participar desse desafio também. Tudo ocorreu bastante
por acaso. De qualquer modo, participei. A palestra nos apresentou algumas
ferramentas forenses das quais eu nunca tinha ouvido falar (só tinha ouvido
falar do wireshark, mas não sabia usá-lo também...). Ou seja, tudo novo. Por que
é que eu ia fazer aquilo, não sei mexer em nada...

Eu estava com uma desvantagem. O meu notebook estava carregado em torno de 50%,
e eu não tinha rede. Os pontos de rede, para os ouvintes das palestras, eram
extremamente limitados (não tinha Wi-fi, só para constar). Assim como as
tomadas...E a bateria do meu notebook (na verdade, ultrabook, quem liga) é
péssima (2h, o que significava que eu só tinha 1 hora pra completar o desafio,
claramente não iria ter tempo o suficiente).

Para realizarmos o desafio, nos foi provida uma máquina virtual. A senha para o
acesso da mesma só seria liberada após a palestra. Durante a palestra, cerca de
20 mídias foram passadas para os participantes (pen-drives e CD-ROMs), para que
os mesmos pudessem realizar suas respectivas cópias do ambiente do desafio. O
ambiente era um Ubuntu da vida (nunca escolhem outra distro...). Já equipado com
as ferramentas que iríamos utilizar, e também com os arquivos o qual iríamos
tentar crackear (na verdade, analisar).

Eu espero que não tenha ficado ambíguo a ponto de você achar que eram
necessários 20 pendrives para instalar o ambiente da palestra...não estamos mais
na década de 90 onde eram precisos muitos disquetes para instalar um simples
sistema operacional....

Logo quando a palestra acabou, saí correndo de lá para uma bancada. Eu precisava
de uma tomada o mais rápido possível. Já não havia mais tomadas livres. Isso foi
péssimo para mim. Durante o desafio, os palestrantes iriam dar algumas dicas.
Além do mais, o último slide continha um resumo de como usar as ferramentas. E
eu estava sem um caderno na ocasião, então não pude anotar nem isso..."oh céus".
Mas enfim. Eu carreguei o meu notebook um pouco, cerca de 20 minutos, talvez até
uns 65% por cento, não me lembro ao certo, e então saí correndo de volta para o
local da palestra. Sabe, enquanto carregava a bateria eu tentei ler alguma coisa
útil na internet, mas não tinha muito o que ler. Você sabe, eu não poderia
prosseguir direito sem o resumo, ou quem sabe sem as dicas.

E vou te dizer, o desafio estava segmentado assim: tinham várias partes, e
conforme você completasse uma parte tinha que avisar a algum palestrante (eu
devia dizer 'responsável', mas vou continuar dizendo 'palestrante') sobre o seu
progresso. Isso teoricamente seria útil caso todo mundo empatasse. Então, mesmo
que eu conseguisse avançar alguma coisa, teria que voltar lá e cá para avisar a
algum palestrante.

Tudo bem. Voltei para lá, e decidi que iria ficar lá até a minha bateria acabar.
Até que em certo ponto as pessoas estavam desistindo. Consegui uma tomada,
finalmente!!! Mas só depois de mais de uma hora desde o início da palestra
(depois de 16h, provavelmente). Pelo menos assim eu fiquei mais seguro e pude
pensar no desafio com mais calma. Você sabe, uma máquina virtual come a bateria
que é uma beleza.

Consegui ir prosseguindo. Bem aos pouquinhos, mas consegui. Em particular, a
primeira parte foi a mais difícil (estranho, não?). Eu interpretei errado o que
era para fazer. Talvez tenha perdido alguma dica. Não sei, não estava lá nos
primeiros minutos do desafio...mas só sei que demorei mais de meia hora até
consegui algum progresso. Quando consegui, fiquei ansioso (e contente!) pra
caramba. Saí avisando aos caras que nem um maluco que eu consegui passar da
parte tal.

Depois da primeira parte, tive mais facilidade. Completei as partes subsequentes
em cada vez menos tempo. Estava indo tão bem que mudei as minhas esperanças.
Achei (=passei a achar) que eu tinha uma oportunidade de ganhar alguma coisa.
Nem que fosse algum brindezinho de recordação (tinham 3 prêmios para os 3
primeiros lugares, mais alguns brindes para os outros participantes que
conseguissem terminar o desafio forense).

Perto de 18 horas eu estava praticamente completando o desafio. Faltava só mais
uns empurrõezinhos. Bateria realmente deixou de ser um problema. E a esperança
de ganhar se apoderava cada vez mais de mim. Na verdade, pouco me importava qual
fosse o prêmio. Eu realmente gostei do desafio, do jeito que o estruturaram, das
suas etapas. Achei bastante bacana. Realmente me diverti fazendo aquilo. E cada
vez mais eu chamava algum palestrante para ir avisando sobre o meu progresso...

Enfim, depois de bastante trabalho, consegui completar o desafio!!!! Aquilo,
para mim, foi sensacional. Cheguei ali sem conhecer nada, depois tive os
problemas de não ter uma única folha para fazer anotações, e de ter pouca
bateria (50% é pouco se 100% = 2 horas é pouco pra você). Realmente achei que
essas duas desvantagens poderiam ser cruciais para que tudo pudesse dar errado,
mas eu consegui! Me senti super orgulhoso com um toque de humildade ('você tinha
tudo pra perder, mas ganhou, seu maldito!').

Descobri que cheguei em segundo lugar. O primeiro lugar tinha completado o
desafio uns 25 min antes de mim. É engraçado, porque se não fosse a história da
bateria e de eu travar na primeira parte, *talvez*, *talvez* eu pudesse até
chegar em primeiro lugar (mas, na boa? Nem me importa). Mas eu juro que eu não
tive nenhum remorso. Em geral eu sou uma pessoa bastante competitiva. Se eu não
chegar em primeiro geralmente eu tendo a ficar meio, hmmmm – ya know – com o
desafio e com os que ficaram na minha frente. Mas caramba, acho que aprendi mais
uma lição de maturidade ali, porque não senti nenhuma raiva do primeiro cara
(mesmo que eu tivesse ficado em desvantagem). Achei a competição tão bonita, o
pessoal do CERT.br tão bacana, que meu espírito competitivo compreendeu tudo e
se encantou pra caramba com aquilo.

O prêmio do segundo lugar foi um Kindle PaperWhite, da Amazon (um leitor de
livros, *um ótimo* leitor de livros – só é uma pena que não leia EPUB...). Eu
queria algo desse tipo há muito tempo. É sério, eu sou um leitor pesado de
e-books, sempre li pra caramba no meu Symbian de pouco mais de duas polegadas, e
atualmente no meu Android de 4.3''. Um e-reader foi um prêmio que deixou a
competição ainda mais perfeita!!! Não preciso dizer que a qualidade de leitura
dele é bem melhor. Ainda não o testei com um livro meu, mas estou impressionado,
gostei de verdade do meu prêmio. O primeiro lugar ganhou um Samsung Galaxy Note
(é mais caro, mas não seria tão útil pra mim, já tenho um Android. Só que fosse
o Galaxy Note 2...) Mas sério, um prêmio diferente me deixou mais animado ainda.
Nem que fosse um...ahn, sei lá, fala aí alguma coisa. Nem que fosse um Windows
Phone ou um Blackberryzinho. Ganhar alguma coisa que você não tem mas que você
sempre quis – e ainda de forma inesperada, e ainda graças ao seu esforço /
talento // nesse caso mais esforço mesmo – é muito bom! Curiosamente, a história
do DRM e da 'não-liberdade' da Amazon poderia gerar controvérsias nesse
    meio...mas isso fica para outro dia, okay? Acho que não vou me decepcionar
    com DRM, para tudo dá-se um jeito.

### Conclusões?

Tente. Tentar é muito bom. Especialmente quando você pode errar. No mercado, no
mundo real, errar é extremamente custoso, a solução tem que aparecer, por melhor
ou pior que seja. Mas, num clima acadêmico, ou num clima 'campus party' (que é
um clima único, bastante peculiar, ótimo, sem palavras!), vale bastante a pena
tentar, mesmo que você não saiba de porcaria nenhuma. Felizmente eu tive duas
experiências – uma ruim e uma boa –, o que é um complemento perfeito em relação
ao outro. A gente fica chateado quando não ganha, mas o esforço sempre vale.

### Off-topic

Tanto o pessoal da Mozilla Brasil, quando o pessoal do CERT.br foram simpáticos
e gente boa *pra caramba*. Mais bônus ainda pela participação num ótimo
ambiente. Porque existiam várias competições por lá, eu poderia muito bem ter
escolhido a de uma empresa ou comunidade que não fosse lá tão amigável, ou
enfim. Vale mais a comunidade. Voltei a utilizar o Firefox (=saí do chromium)
só por causa da comunidade da Mozilla Brasil.

É isso aí, em breve eu continuo a escrever sobre a minha experiência na Campus
Party, falando de outros aspectos, espero que tenham achado o post bacana. =)

*Criado com Emacs.*
