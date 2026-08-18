---
title: "Era uma vez...kernel panic, uma história de amor (Parte 1.5)"
url: https://perrotta.dev/pt/2013/09/era-uma-vez...kernel-panic-uma-hist%C3%B3ria-de-amor-parte-1.5/
last_updated: 2026-08-19
---


Esse post é a semicontinuação [desse post]({{< ref
"2013-09-07-era-uma-vez-kernel-panic-uma-historia-de-amor-parte-1" >}}). Ele não
é dependente do anterior, mas acho que a experiência da leitura fica mais rica
se você seguir a ordemproposta.

Já comecei a escrever a parte 2, mas ainda falta bastante coisa para colocar lá
(não está tão grande assim...). Então resolvi criar uma parte intermediária
(pergunta: por que não terminar a parte 2 logo? resposta: ...).

Então, vou falar de uma situação recorrente na minha experiência com Linux (eu
não vou mais escrever GNU/Linux. Estou farto. Mais sobre isso num post futuro,
inclusive se você não souber o porquê de escrever GNU antes, mas acredito que
saiba): **instalar distros**! Uma distro após a outra! *Psicologicamente*
sentindo-se insatisfeito, deletando tudo o que foi feito até o momento, e
começando tudo do zero, com uma distro completamente diferente (às vezes não tão
diferente assim, uma simples derivada).

## Introdução

Primeiro, você sabe qual é a **sensação** de instalar uma distro nova após estar
farto (ou talvez simplesmente cansado, ou então querendo novas aventuras. Todas
essas situações já aconteceram comigo, viu? Acho que com mais frequência a
última.) da antiga? A analogia a isso é você imaginar o seu *Windows 7* (ou 8.1?
Leitor moderninho) todo **poluído**, todo instalado de porcarias, algumas delas
as quais você mesmo incluiu e se arrependeu depois – mesmo que tenha deletado o
programa, ficam configurações, pastas temporárias, cache, chaves de registro,
etc –, outras delas sendo vírus adquiridos espontaneamente durante sua
navegação insegura na web, e então você resolve deletar isso tudo e começar do
zero. A palavra mágica nesse mundo é **FORMATAR**.

Com Linux, em geral, não *se formata*. Isso é algo desnecessário. Pessoalmente,
nunca reinstalei a mesma distro como uma tentativa de limpar o sistema (a menos
que você faça alguma besteira logo após – ou durante! – a instalação do mesmo.
Isso já aconteceu comigo, é claro). Existem maneiras mais eficientes de fazer
isso sem ter que reinstalá-lo do zero. Uma delas é brincar com o gerenciador de
pacotes. A outra é você simplesmente reinstalar a partição `/`, preservando a
`/home` e talvez a `/etc` e mais algumas outras configurações também.

No entanto, é recorrente você querer mudar de uma distro para a outra. Apesar de
você poder simplesmente instalar a raiz (`/`) e manter as outras configurações,
em geral a experiência vai ser mais **limpa** se você fizer a instalação do zero
(apenas copiando seus arquivos pessoais depois = provavelmente apenas a `/home`.
Mas não a `/home` inteira!).

## Mini Index de distros que usei

OK. Qual é a disso? Eu ia deixar para escrever isso na parte 2, mas na verdade
vai ficar bem melhor se eu escrever aqui. Eis o meu ciclo de distros desde que
usei o Ubuntu pela primeira vez até hoje (vou incluir os Window Managers também):

- Ubuntu (março 2012 - 1 mês)
- Ubuntu com KDE
- Kubuntu ==> para aproveitar KDE no Ubuntu de forma mais integrada
- LinuxMint KDE (mais de 2 meses. Talvez 3?)
- Fedora KDE (eu falei que eu era *fanboy* do KDE nessa época...) (vários meses)
- openSUSE KDE (1 ou 2 semanas)
- openSUSE KDE – tentativa com Tumbleweed (2 dias. Aiai...)
- LinuxMint Cinnamon (mas estava muito bugado, caramba...)
- Ubuntu com Unity (1 mês pelo menos) (aí você percebe como ele buga também...)
- Sabayon Gnome 3 (alguns dias, menos de uma semana)
- Manjaro XFCE (mais de 1 mês)
- Arch Linux Console Only (alguns dias)
- Arch Linux Fluxbox (no mínimo 2 meses)
- Fedora LXDE (no notebook, em paralelo com o Arch)
- Arch Linux Fluxbox (no notebook, agora tudo Arch o/)
- (agora): Migrando para o Arch Linux Cinnamon (Linux Mint feeling)

Coloquei a duração / data nas que eu lembrei. Não é absolutamente preciso, mas
dá para ter uma noção.

Em particular, em alguns momentos de migração, testei **muitas** distros. Se
você tomar as primeiras 50 distros do [*distrowatch*](www.distrowatch.com), acho
que já testei mais da metade delas. **Talvez** tenha chegado a umas 40, se somar
as que eu testei em máquina virtual também. Não sei.

Mas tá, isso aqui não é uma competição pra ver quem usou mais distros hahaha. O
leitor não precisa ficar triste. Inclusive, eu o encorajo a testar todas as
primeiras 50 distros do distrowatch. Posso garantir: você sempre vai perceber
uma diferença entre elas. Sempre tem uma diferença significativa, isso é
incrível, mesmo que todas usem como base o mesmo kernel, que é o que faz essa
mágica poder funcionar na prática (ops, mesmo kernel? Uma das diferenças entre
distros é que algumas usam um kernel bastante *outdated*...)

Para que eu usei todas essas distros? Note que as que estão listadas ali em cima
são as que eu usei como distros principais. Não vou falar das distros que
somente testei. Muito bem, vamos lá, talvez tenha valido a pena ler essa
enrolação toda para ler a parte mais legal.

## Ah, o Design

Primeiro: se você só usou um único sistema na sua vida (Windows ou Mac), você
não sabe o que é um sistema. **Não sabe**. Dizer que usou Windows XP e Windows 7
não vale... a verdade é que isso se aplica para qualquer outra coisa, não apenas
computadores. Se você só usou um único celular / smartphone, você **não sabe** o
conceito de um smartphone. Se você só foi cliente de uma única operadora, **não
sabe** o que é uma operadora de celular (ou melhor: o que uma boa operadora pode
te oferecer). E se você só teve um único carro? Não sabe o que é um carro
também? Claro que isso é exagerado. Você certamente sabe para que cada um desses
itens serve. Senão não estaria lendo até aqui, certo? A questão central está em
torno do [**design**](http://en.wikipedia.org/wiki/Design), **de saber o que
pode ou não ser feito e, principalmente, como** pode ser feito. De pensar
outras formas diferentes de fazer as mesmas coisas.

A verdade é que não existe um único **melhor** produto (salvo raras exceções.
Confesso que não consigo pensar em nenhuma agora), porque o produto *ideal*
constituiria somente das melhores partes de todas as variantes de um mesmo
produto. Um exemplo? Tome Android e iOS. Sem defender um ou outro aqui, não há
como dizer que um deles é melhor que o outro e ponto. Naturalmente, o iOS é
muito melhor em algumas coisas (design, facilidade para o usuário mais leigo) e
o Android é muito melhor para as outras (plataforma mais aberta. Mais?). Um OS
mobile ideal incorporaria as melhores características dos dois. E do esquecido
amigo Windows Phone também. Acho que ele deve ter alguma coisa boa, uma coisinha
que seja...

Acabei de me lembrar de um exemplo diferente mas que acho mais recorrente. **Web
browsers**. Use o Internet Explorer por uma semana. Depois use o Google Chrome
por uma semana. Ou qualquer outro navegador de sua preferência (no momento desse
post, o meu browser predileto é o Firefox. É importante ressaltar o tempo. As
preferências podem mudar em um único dia nesse mundo acelerado). Aposto que o
leitor vai perceber algumas diferenças. Talvez *muitas*. Que diferenças?
**Diferenças de design**! A minha teoria é que tudo está no *design*. De
entender **para que** determinado produto foi feito ou produzido (ou
desenvolvido).

É por isso – por exemplo – que a Apple é uma empresa tão valorizada e bem
sucedida (no momento desse post, eu nunca usei nenhum produto da Apple. Exceto o
Safari no Windows uma única vez para testá-lo...). Ela se importa (ou melhor:
Steve Jobs se importava bastante) com o design de seus produtos. A arte do
design é a arte de projetar algo para determinado fim de maneira eficiente
**para esse fim**.

Segundo [Donald Norman](http://en.wikipedia.org/wiki/Donald_Norman), um dos
caras mais incríveis que já li (eu não li o cara, mas viva o vício de linguagem.
*Metonímia*, na época do vestibular), em seu [The design of everyday
things](http://www.goodreads.com/book/show/840.The_Design_of_Everyday_Things)
(ótimo livro sobre design) diz que para um produto ter um bom design, ele não
deve vir com absolutamente (ou, pelo menos, com o mínimo possível) nenhuma
instrução / rótulo. Deve ser tão **intuitivo** quanto for possível *para o
contexto em que foi criado*, de modo que *o público alvo desse contexto* que for
usá-lo o faça da forma mais imediata (e fácil, na melhor das hipóteses. Fácil
para essa pessoa) possível.

Muito bem. E o que isso tem a ver com **distros**?

## Distro Paradise

**TUDO**!

(A partir desse ponto eu me sinto incomodado em continuar escrevendo porque acho
que o leitor deve estar cansado. Esse texto não é nada (em termos de tamanho),
mas no nosso mundo cheio de informações corriqueiras na qual a ansiedade da
juventude vai a mil, já é suficiente para deixar qualquer um (talvez inclusive
eu) aborrecido. Então eu vou terminar já já e deixar o restante para a parte 2.
Ou para a parte phi = 1,680..., se eu me empolgar com essa numeração)

Caramba, existe esse troço maldito chamado [Linux](http://www.kernel.org). É uma
das coisas mais descentralizadas que já vi (isso faz parte da beleza da coisa).
Vá no [distrowatch](http://www.distrowatch.com) e veja quantas distros você
consegue contar. Achou pouca coisa? Então olhe esse [belo
diagrama](http://upload.wikimedia.org/wikipedia/commons/1/1b/Linux_Distribution_Timeline.svg)
da Wikipédia. Conseguiu se convencer?

E para que existem tantas delas??? Linux não é uma coisa só?

Cada distro está focada em um **propósito** diferente. Algumas vão além e também
têm uma **filosofia** e uns **valores** diferentes. Isso pode ser dito de outra
forma: cada distro tem **foco** em determinadas questões, cada distro tem um
**DESIGN** diferente em mente, o que inclui um planejamento dos usuários-alvo,
plataformas, quais programas e aplicativos devem ser incluídos, e por aí vai.

Por exemplo, o Knoppix é uma ótima distro para ser rodada no modo live, a partir
de um Pen-drive (USB Flash Drive). O Ubuntu é uma boa distro de desktop para
iniciantes. O Debian é ótimo para servidores. O Arch Linux é ótimo para poder
controlar todo o comportamento da máquina. E a lista cresce indefinidamente, com
múltiplas possibilidades. Existem distros especializadas para tudo o que você
imaginar. Anti-vírus (não me recordo agora). Recovery (System Rescue CD).
Gerenciar particionamento de discos (Parted Magic). Clonar e fazer backup de
discos (Clonezilla). Multimídia (Ubuntu Studio).

Não apenas especializações de funções, mas também de filosofia e de design. O
openSUSE é ótimo para expor várias (muitas) configurações do sistema na
interface do usuário (GUI) com o seu YAST. O LinuxMint é "simples e elegante"
(como eles mesmos dizem). O Xubuntu e o Lubuntu são leves. O Parabola e o
gNewSense só suportam (SÓ é só mesmo) software livre. O Fedora suporta vários
valores de software livre e de união da comunidade (ver [Fedora Core
Values](http://fedoraproject.org/wiki/Foundations)). E sério, dá para ficar
falando disso aqui indefinidamente.

Esse post misturou um pouco de várias coisas. E, na verdade, a intenção dessa
série de posts é exatamente essa. Experiência é algo caótico. **Que bom**. (Ou:
problemas da vida real não aparecem numa ordem bonitinha, são caóticos também)

Encerro esse post dizendo que UEFI **ainda** é um troço extremamente chato para
integrar o Linux com o Windows em dual boot. Espero (ainda espero) fazer um mini
guia sobre isso em breve. Mas antes disso eu preciso me entender eu mesmo com
esse troço.

Até a próxima parte (a próxima vai ser a 2 mesmo, prometo).

