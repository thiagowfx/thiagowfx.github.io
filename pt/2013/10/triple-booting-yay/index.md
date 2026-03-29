
Hoje acabei de configurar o meu sistema para *triplobootar* (se o leitor me
permitir o neologismo).  Arch Linux, Windows 8 (Lenovo OEM) e Linux Mint 15
Cinnamon. Ah, a beleza do Arch Linux: você não precisa explicitar a versão dele,
afinal, não existe muito o conceito de versão do Arch. Ele está sempre
atualizado. Essa é a beleza de uma distribuição [rolling
release](http://en.wikipedia.org/wiki/Rolling_release). E é isso – não apenas
isso, OK – que me faz gostar do Arch.

Todos são 64 bits. Isso não seria nada de especial. Mas eu sempre instalei
sistemas 32 bits. E digo: não existe nada de mal nisso. Com a
[PAE](http://en.wikipedia.org/wiki/Physical_Address_Extension), certamente
memória não é um problema. E não existem **tantos** aplicativos otimizados para
64 bit assim, pra dizer que algum desempenho é algo *super* vantajoso. Na
verdade, eu sempre usei 32 bits mais porque eu só tinha 2GB de memória do que
por outra coisa. Mas, mesmo que tivesse 8GB, eu não reinstalaria o meu sistema
só para migrar para 64 bits. OK, chega de arquitetura.

Perceberam o vício de linguagem atual no parágrafo anterior? Não?
**Aplicativos**. A modinha é essa. É tão moda que chamamos de aplicativos até
mesmo as aplicações / os programas de desktop. Ó, mundo moderno.

O meu objetivo final é ter ambas a instalação do Arch e do Windows o mais
[KISS](https://en.wikipedia.org/wiki/KISS_principle) possível. Sem afetar o meu
*workflow* e o meu desempenho, é claro. O leitor já cansou (e ainda vai cansar
mais) de ler esse termo aqui. É um princípio que eu prezo muito, e que acho que
facilita bastante as coisas. KISS não é falta de funcionalidades. KISS é ter
somente as funcionalidades que você precisa, e não adicionar montes de
*features* que (provavelmente) nunca serão usadas.

Eu estou pensando seriamente em deletar o LinuxMint para instalar o openSUSE.
Sabe qual é o problema? Na verdade, isso não é um problema, é ambição, mas...uma
vez usando o Arch, a sua mentalidade muda completamente. Pelo menos usando ele
*de verdade* (acredite, esse post não é uma propaganda do Arch, outro dia eu
faço isso :D). Você começa a querer tudo atualizado. Na última versão possível.
E basta. Mesmo que você quase não use a aplicação, você quer ela. O último
commit estável do kernel. O último patch do *systemd*. Não importa. E,
coincidentemente, isso tem tudo a ver como o mundo caminha hoje.
Tecnologicamente (e não tecnologicamente também). É tudo muito rápido. Os prazos
são rápidos. O tempo **voa** com a derivada da velocidade maior que zero. Cada
vez maior. (A derivada, é claro. A velocidade aumentando já é implícito nessa
frase. Para bom entendedor, eu não precisaria estar explicando isso =p)

Tudo está configurado em (U)EFI. Isso foi a maior chateação. Se fosse MBR, seria
uma tarefa trivial pra mim. Talvez porque eu já cansei de instalar distros. Mas
EFI é uma coisa realmente nova. É daquele tipo que você no começo teme fazer
besteira no sistema. Mas, com o tempo, sente-se cada vez mais acostumado. Ou:
*se-estragar-agora-eu-sei-recuperar*. O sentimento é similar ao instalar uma
custom ROM, pela primeira vez, no Android.

O gerenciador é o GRUB. Eu ia usar o gummiboot, mas ele se recusou a instalar. E
não havia realmente necessidade de fazer isso. Eu sei já usar o GRUB, e ele
funcionou (e funciona bem até hoje). O gummiboot é mais simples que o GRUB, mas
já que não é simples de instalar, então tchau (sério, pra esse caso isso é
irrelevante. Por favor, não tenha a mesma mentalidade em outros casos. A *pain*
da instalação muitas vezes compensa no final. Veja o Arch).

Sabe porque eu fiz triple booting? Porque eu queria usar o Arch. Eu descobri que
ele é a distro que mais combina comigo (ou, melhor dizendo: a que mais serve
para mim e com a qual eu mais me agrado ficar). Só isso. Não precisa ser a mesma
coisa para você. Mas, eu sou uma pessoa inquieta no que diz respeito a testar
novas *features*. Estou sempre instalando uma distro nova. Elementary OS,
Fedora, openSUSE. Vale a pena. Sempre tem uma coisinha legal. E é uma forma de
satisfazer a curiosidade...

Vamos tomar uma outra linha nesse post, agora. Num post anterior eu falei sobre
design. [Nesse post
aqui](http://thiagoperrotta.wordpress.com/2013/09/27/era-uma-vezkernel-panic-uma-historia-de-amor-parte-1-5/).
Agora estou aplicando parte do que eu falei lá. Mais especificamente, sobre a
parte de 'usar as aplicações para a forma para qual seus projetistas a
projetaram para ser usadas'. Ou pelo menos quase isso. Eu vou seguir esse
princípio ao extremo. Pelo menos durante umas semanas. Se eu não gostar, ou se
não me for útil, obviamente, eu vou dar *opt-out*. Não há necessidade de criar
uma regra e se obrigar a adaptar a ela se ela não te satisfaz ou se você não
gosta dela. Por exemplo, o (princípio de) software livre está nas veias do
Stallman. Isso **É** ele. É um princípio radical e incômodo para muita gente
(talvez até mesmo para mim). É muito difícil utilizar **única e exclusivamente
**software livre**. Eu até queria fazer isso, mas pra minha realidade é
impraticável. Mas pra ele faz todo o sentido. Essa é a ideia de um princípio
seguido rigidamente.

*Anyways*. Agora estou postando isso aqui do Internet Explorer 10 do Windows 8
(não pretendo instalar o Firefox no Windows. Nem o Chrome. Nem o Opera. Mas isso
não significa que eu esteja utilizando o IE de maneira pura. Continuo usando
Adblock Plus (que eu nem sabia que existia para IE) e estou usando o
[startpage](http://www.startpage.com) como search engine)... Curiosamente, já
usei o Windows 8.1. Pra quem está falando de ficar nas últimas tecnologias
sempre...a questão aqui é que isso não é tão útil pra mim, **agora.** Neste
exato momento da minha linha do tempo, eu passo 95% do meu tempo no Linux. Então
é bobagem perder tempo atualizando freneticamente outros OSs. Veja bem:
atualizar os componentes do Windows continua sendo algo essencial (pelo menos
até certo ponto). Mas não o Windows em si.

Isso também tem a ver com outra coisa. Eu passei os últimos meses mais
configurando o meu sistema do que usando ele propriamente dito. Do que
contribuindo para projetos de software livre. Do que passando o tempo em fóruns
de discussão e em canais de IRC. Eu gosto dessas coisas. São *old school*, mas
provocam menos ansiedade. É óbvio que o Facebook e as comunidades do Google+ são
muito mais interativas do que esses primeiros canais de informação. Só que são
interativas até demais. É de enlouquecer se você não impuser um limite a você
mesmo. Notificações no web browser, no smartphone, a todo o momento. Isso é
péssimo. Falo isso principalmente porque terminei de ler, há pouco tempo, o
livro do [Nicholas Carr](http://www.goodreads.com/book/show/6966823-the-shallows). Esse livro é
**muito bom**. E faz muito sentido nos dias de hoje. Pode acreditar.
'Superresumidamente', ele conta a história, com argumentos científicos e com
várias citações de experimentos psicológicos e científicos de como a internet
está (e vem, e continua) alterando o nosso cérebro e a nossa forma de pensar.
Estamos entrando definitivamente num estado mental diferente. E bom, o que eu
mais disser vai ser vago. O cara escreve de maneira espetacular (eu li a versão
original, em inglês), eu não vou conseguir reproduzir essa teoria como ele.
Então, se você gostou dessas palavras, recomendo a leitura.

Planos futuros? Configurar o Arch do meu jeito e tentar documentar e juntar
algumas partes importantes. Eu atualmente faço isso no meu
[github](https://github.com/thiagowfx/dotfiles). Mas ainda há muitas coisas a
serem feitas. E eu quero organizar isso de modo mais sistemático. Se tudo ficar
bem legal, de repente eu faço uns screencasts sobre como configurar e
gerenciar esses arquivos. Ou, até mesmo, sobre como utilizar essas aplicações
também. Muita gente tem dificuldade nisso (bom, e também muita gente não liga
pra isso. Mas, se você ainda está lendo até aqui, provavelmente liga).

Após usar Linux por (mais de) um ano e meio, sinto uma necessidade natural de
contribuir para algum projeto livre (ou de código aberto. Mas, de preferência,
livre também). Com código, documentação, ou mesmo com ajuda a *newbies* (uma
palavra carinhosa – ou não – para 'iniciante'). Acho que essa 'necessidade' vem
da gratidão pelo sistema, que muitos voluntários contribuíram para ele se tornar
o que é hoje. Não apenas pela gratidão, mas também pelo contágio da dedicação e
do nível de *expertise* desses caras (dessas também, existem ótimas
    programadoras por aí =P) e, acima de tudo, pela admiração de alguns
    (projetos e desenvolvedores). Bom. As coisas vão caminhando com calma,
    certo? Mas não com **tanta** calma.

Obrigado por ler.

