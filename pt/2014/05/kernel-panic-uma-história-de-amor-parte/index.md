---
title: "Kernel Panic, uma história de amor, parte ????"
url: https://perrotta.dev/pt/2014/05/kernel-panic-uma-hist%C3%B3ria-de-amor-parte/
last_updated: 2026-05-26
---


É, meus amigos, a minha (longa) jornada de exploração do mundo Linux Desktop
está praticamente chegando ao fim. Pessoalmente, já explorei tudo o que eu
queria. Foram 2 longos anos, e acredito que eu tenha atingido um nível de
maturidade razoavelmente bom, a ponto de recomendar a outras pessoas que se
interessam por TI fazerem o mesmo que eu fiz. Felizmente, várias (mas,
infelizmente, não todas) das minhas etapas ao longo dessa jornada estão
registradas (às vezes, documentadas também!) nesse blog.

OBS.: estou escrevendo esse post sem absolutamente nenhum link e nenhum tipo de
marcação (negrito, etc), isso é proposital.

O desafio final, necessário para o meu diploma autodidata, foi adiado o máximo
possível. Sim, ele é exatamente isso que você está pensando: testar o Gentoo.
Hoje o meu Grub possui entradas tanto do Arch quanto do Gentoo. Vou adiantar uma
coisa: a entrada do Gentoo é temporária. Assim que eu terminar de explorar todas
as features que parecerem interessantes de uma distro baseada em código-fonte,
do portage, do eix, equery, masks, slots, OpenRC, e mais todas as
    características peculiares do Gentoo, vou me desfazer dele.

Vale a pena dedicar pelo menos um parágrafo para falar sobre o porquê disso. Vai
ser só um, prometo. Desde o meu primeiro dia com Linux (com nada menos
que...Ubuntu! É, já falei disso aqui várias vezes), eu percebi que iria gostar
muito daquilo. Daquilo o quê? Tanto do design da coisa, quanto das comunidades,
de outras pessoas que também eram entusiastas por aquele design. Assim, tentei
me envolver com a comunidade do Ubuntu. Cadastrei-me no Launchpad, no fórum
Ubuntu-BR, no fórum oficial do Ubuntu (em inglês), tentei acessar o IRC do
`#ubuntu`, ixi, foram várias coisas desse tipo. Fiquei um tempo fazendo isso. Mas
não me senti 100% à vontade. Por quê? Porque parecia algo não muito natural. Não
era algo com que eu chegasse um fim de semana e estivesse super animado e
entusiasmado para postar no fórum do Ubuntu, não mesmo.

Ops, cá estou eu quebrando minha promessa e criando outro parágrafo...daí, eu
decidi partir para outra, fui para o mundo do KDE, tentei fazer parte da
comunidade deles, etc, etc, ficou esse ciclo, e depois testei uma distro atrás
da outra, valendo destacar que também tentei participar da comunidade do
openSUSE e do Fedora.

Só que existia um problema, nada disso parecia certo, nada disso parecia feliz,
natural. Parecia só uma modinha. Ah, um usuário de Linux novo, se juntar com a
comunidade. Tem um monte de wannabes por aí, colocando em seus blogs pessoais
vários símbolos de coisas relacionadas a open source e distros de Linux
(ops...eu sou um deles???). Sabe qual é o problema? O problema é quando você
inclui essas coisas sem sequer saber sobre o significado delas direito. Quando
você tem uma pressão interna para colocar um símbolo do (digamos) Ubuntu
relacionado a você, mas você mal sabe o que é o Ubuntu, com a maior parte da sua
experiência limitando-se apenas usar o sistema.

Uma das coisas que eu aprendi, um dos significados mais importantes e mais
(permita-me dizer) belos sobre esse mundo, é o significado de: COMUNIDADES.
Comunidades são uma coisa bastante complexa mas, uma vez que você entende o
propósito, a motivação, e o objetivo por trás de uma, tudo se torna
infinitamente mais fácil, e você passa automaticamente a entender sobre todas as
comunidades. Em outras palavras: conheça bem uma comunidade, e você conhecerá
todas!

A questão foi: depois de passar por todas aquelas comunidades de distros que
citei, e ter detestado isso tudo, de maneira frustrada, chegou um certo dia que
eu conheci a comunidade certa PARA MIM. É óbvio que eu estou falando da
comunidade do Arch Linux. Se a comunidade do Arch é perfeita? Para mim, é! Mas,
note que a resposta para "X é perfeito?" é relativa, e depende do referencial.
Perfeita para quem? Continuando com esse exemplo, para a maior parte das pessoas
que eu conheço, o Arch é uma das piores comunidades que você tem para
participar. Você tem que correr atrás para interagir com os outros membros (isto
é, ninguém vai fazer nada por você se você próprio não se esforçar), ela é
fortemente baseada em meritocracia (quanto mais você colaborar, mais os outros
membros vão reconhecer o seu valor dentro da comunidade. Nem todas são assim. Em
alguns lugares, o mais rico é o mais foda. Ou, quem tem as melhores redes de
contatos. Ou, quem dedica mais tempo (não necessariamente mais contribuições)
para a comunidade. Cada comunidade tem a sua própria forma de atribuir valores a
si mesma!), em manter as coisas simples e evitar complexidades e firulas
desnecessárias (o que, por exemplo, muitas vezes acaba com o conceito de "ser
fácil de usar de primeira", o que é claramente ruim para muita gente).

Ah, enfim, quanto uma comunidade é bem definida, os seus valores são bem
definidos. Para o Arch, existe o "Arch Way", para o Ubuntu, "Ubuntu code of
conduct", para o Fedora, "core values". Para o seu grupo de amigos (que também
forma uma comunidade!), talvez preferir pizza de Pepperonni (escrevi certo?) e
torcer para o time XXX de futebol (sorry, me recuso a citar qualquer time de
futebol brasileiro nesse espaço) sejam os valores da sua comunidade e, em
princípio, não há problema nenhum nisso!

Muito bem, vamos voltar a ter foco no tema do post (se é que ele tem um). Eu ia
escrever 3 posts separados, um falando sobre comunidades, um falando sobre o
Arch e sobre o Gentoo, e o outro falando sobre um pouco de tudo, mas acabou que
ficou tudo misturado aqui.

Sobre comunidades, uma das coisas que eu considero um MUST DO para qualquer
pessoa, é ler o sensacional "The art of community", do Jono Bacon (eu disse que
não vou indicar links, faça seu dever de casa e pesquise, caso se interesse).
Esse livro está disponível sob a Creative Commons, então você pode baixá-lo
gratuitamente. Jono Bacon é o atual Community Manager do Ubuntu, ele é
responsável por gerenciar uma boa parte da comunidade do Ubuntu, e de assegurar
que os interesses da Canonical estejam mais ou menos congruentes aos da
comunidade do Ubuntu. Ele também é um dos atuais hosts do Bad Voltage, um
podcast que gosto bastante.

Enfim, o negócio desse livro é que ele é uma lição de política, de comunidades,
de interação, de gestão, de (...), AH, de tudo. Um livro perfeito para se ler em
um ano de eleições, mostra o quão falha é a gestão do nosso Brasil. E também o
quanto algumas empresas desse mesmo país estão fadadas ao fracasso.
Naturalmente, essas são conclusões que uma leitura atenta lhe permite tirar.

Depois que li esse livro e refleti sobre a minha tentativa por procurar a
"comunidade perfeita", percebi que tudo isso se relacionava e fazia completo
sentido. Encontrar uma comunidade da qual você se sinta parte é uma sensação
muito boa!

Agora, já que eu estou falando de fazer parte, vale dizer outra coisa. O que é
preciso para fazer parte de uma comunidade? Há algumas que possuem os seus
métodos oficiais. "Fedora Ambassor" (acho que se escreve assim) é um exemplo de
badge oficial. Só vou dizer uma coisa sobre isso: existe uma vibe muito grande
de pseudocults e de pseudo community members nessa área (nessa = não me refiro
ao Fedora, não! Me refiro aos badges e tudo o mais). Pessoas que só querem um
badge de certa comunidade, mas que não sabem nem um pouco sobre a mesma, mas só
querem participar da organização para se promoverem, e ganharem algum nome,
aproveitando-se da reputação da organização. Bom, felizmente me orgulho de dizer
que na comunidade do Arch não existe a possibilidade disso acontecer,
simplesmente porque não há badges (bem, só em torno de umas 100 pessoas possuem
esses badges, então na prática é como se não houvesse; essas pessoas são os
usuários confiáveis ("trusted users") e mais outros, que contribuem DIRETAMENTE
para a manutenção da distro): a forma de você se envolver com a comunidade é se
envolvendo, e pronto. Não existe nenhum selo para ser exibido. A vantagem disso
é que pseudocults usualmente desistem fácil de comunidades desse jeito: ora
bolas, o objetivo é acumular badges, e não participar da comunidade em si.
Resumindo: participa quem quer, quando quer, PORQUE quer. Quer o quê? Ver a
comunidade crescer, evoluir, e se interagir cada vez mais! Sem selos.

O parágrafo anterior foi fortemente baseado no livro do Bacon, mas OK. Um resumo
mal feito, verdade. Quando um livro é sensacional, qualquer resumo dele é mal
feito, não tem como. Nada substitui o conteúdo original do livro.

OK, se você ainda está lendo isso, ou você está curioso para ver onde esse post
vai dar, ou talvez você tenha um espírito puro em relação a comunidades e não
seja pseudocult, portanto. Talvez você ainda esteja procurando a sua comunidade
perfeita. Enfim, você é especial, porque a maioria das pessoas já ficam de saco
cheio logo nos primeiros parágrafos desse texto xDD, aprendi a fazer isso com a
comunidade do Arch, viu como aprendemos coisas?

Mas, voltando a falar sério: essa é a minha terceira versão de um texto que eu
sempre quis escrever, de algo que eu sempre quis expressar. As duas primeiras
versões nunca foram publicadas, estão bagunçadas demais. Essa também está, mas
está bem menos, acredite. E, mesmo que eu escrevesse 10 vezes, continuaria
assim, sabe por quê? Porque quando tentamos falar de modo perfeito de algo no
qual acreditamos e de que somos entusiasmados, não tem como não misturar
sentimentos e pensamentos pessoais com o fluxo do texto. Isso só mostra que esse
tema é algo realmente bastante especial para você.

Mas, muito bem, essa parte foi um pouco (muito!?) filosófica. Vou escrever uma
outra parte, comparando o Gentoo ao Arch e, nessa, prometo que vou ser mais
objetivo. Além disso, existe uma possibilidade de que eu poste uma continuação
para esse post, com mais filosofia. Se você tiver curiosidade em ver os dois
primeiros rascunhos para esse post (uma bagunça...), deixe-me saber disso.

Até a próxima. E, vou reforçar: o meu conteúdo sobre Linux está em breve
chegando ao fim. Quer dizer, não sobre Linux, mas sobre Linux Desktop. Realmente
foi uma jornada bastante legal, mas eu vou me mover para outras áreas agora.
Qual? Muito possivelmente: ou redes/servidores/essas coisas, ou teoria de
linguagens de programação e de compiladores. Existem outras possibilidades, mas
essas são as mais prováveis. E, é claro, sempre tem um pedaço da maratona de
programação, mas sobre isso você sabe que eu escrevo em outro lugar.

