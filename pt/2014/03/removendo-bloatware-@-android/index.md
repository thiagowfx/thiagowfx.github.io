---
title: "(Removendo) Bloatware @ Android"
url: https://perrotta.dev/pt/2014/03/removendo-bloatware-@-android/
last_updated: 2026-04-12
---


Recentemente tive contato com um *Stock Android* 4.4.x (KitKat) e, *whooooa*,
como eu tinha me esquecido o quanto um Android novo era *bloated*, cheio de
firulas e coisas desnecessárias, que só complicam a usabilidade e a compreensão
do usuário.

Vou utilizar um vocabulário relativamente mais amigável, já que esse post
pretende dar alguma luz a um usuário não experiente (ou experiente).

## Motivação

Vejamos, em primeiro lugar eu vou reforçar o que eu acabei de falar: **qual o
objetivo disso, pra quê??** Se o público alvo for usuários experientes, eles vão
ficar extremamente descontentes e insatisfeitos, porque serão expostos a firulas
as quais eles não querem. Você poderia argumentar o seguinte: "ah, então é só
eles removerem essas coisas. Certo?" Não. Errado. Quer dizer, estaria certo, o
problema é que não dá para desinstalar programas "de fábrica" *por default* – a
menos que você ganhe acesso *root* no seu Android. Então, porque não a)
distribuir *smartphones* com acesso root *out-of-the-box* (=por padrão) ou b)
fazer com que os aplicativos que já vêm instalados não tenham status "de
fábrica", o que significa que eles poderiam ser facilmente removidos.

Por outro lado, se o público alvo for usuários não experientes (e é, essa é a
maior parte do *market share* do Android), então para que ficar incluindo um
monte de funções, aplicativos e firulas que esses usuários nunca usarão? Pior
ainda, muitos deles em inglês (estamos falando de usuários não experientes, nem
todos sabem inglês). Naturalmente, não se pode agradar a todos, sempre vai haver
alguma parcela dos usuários que terá que se descontentar um pouquinho, isso em
si seria extremamente natural. O problema é que a parcela é enorme, e o
descontentamento não é só *um pouquinho*. Bom, você pode dizer que a maioria das
pessoas não está nem aí / não liga para isso (é verdade). Então, justamente
**por não ligarem** é que esses "extras" (a partir de agora me refiro a isso
como **bloat/bloatware** poderiam (deveriam?) ser reduzidos ao mínimo possível.
Aí não tem como falar disso sem falar no KISS (~Keep it Simple); provavelmente
esse é o acrônimo que eu mais uso aqui, mas é porque é um conceito que a maioria
das pessoas e dos fabricantes parecem ignorar completamente. Como Albert
Einstein disse uma vez, ~"mantenha as coisas o mais simples possível, mas não
simplórias". Não se trata de disponibilizar só o kernel para o usuário, não é,
*caramba*, mas também não há a necessidade de incluir um monte de funções só
para complicar a vida dele. Aí você diz: ah, mas a maioria dos Androids possui
algum aplicativo "helper", que vem com um tutorial e instruções de uso das
funções mais importantes do aparelho. Mas esse é outro erro, parece ajudar, mas
na verdade só complica. Segundo Donald Norman, um produto com um design bom é um
produto que **dispensa** tutoriais, textos explicativos e/ou manuais. Ele é
intuitivo, de forma que o usuário consegue perceber o objetivo de seu uso e como
usá-lo "automagicamente" (pequena analogia: imagine um elevador, você entra
nele, aperta o botão, e vai para o andar que você quer. Isso é um exemplo de bom
design. Agora, se em determinado elevador você precisar parar para ler as
instruções de como operá-lo, isso é (em geral) um *design* ruim. Exceções
existem, cuidado para não generalizar esse argumento!).

Vou parar por aqui, esse assunto está longe de ser *exaustado* apenas com dois
parágrafos, **mas** acho que isso já resume a minha motivação por trás desse
*post*.

## Algumas *guidelines*

Nessa seção: algumas coisas que você pode fazer (ou pelo menos tentar fazer, ou
se informar sobre) para reduzir o *bloat*.

Note que eu também vou incluir algumas *features*. Dependendo do seu ponto de
vista, elas também podem ser *bloat* (isto é, você apenas estaria trocando um
*bloat* por outro). No final, o produto perfeito não é genérico, mas sim
*tailored* e adaptado para as necessidades de cada usuário (mesmo que o próprio
usuário não esteja ciente do que ele mesmo quer).

- Primeiro de tudo: REMOVA todos os aplicativos **default** que você não
  **instalaria** caso eles não viessem nativamente. Por exemplo: você baixaria o
  jogo XXXX sag(?) ou o aplicativo da rede social YYYY caso ele não viesse junto
  com o seu Android? Não? **Então remova ele**!

- Aí vem o problema do tópico anterior: você não vai conseguir (em geral)
  remover esses aplicativos. Então, o que você pode fazer? a) root (apenas se o
  seu aparelho for suficientemente popular, e você for um usuário mais
  experiente, disposto a se arriscar um pouquinho) ou b) desativar os
  aplicativos. Não é tão bom quanto remover, mas pelo menos eles não ficarão
  rodando em segundo plano, nem aparecerão na sua *app drawer.*

- Instale o [Notification
  Toggle](https://play.google.com/store/apps/details?id=de.j4velin.notificationToggle).
  Ótimo design, isso deveria ser nativo em todos os Androids.

- Instale um *launcher*! O Launcher nativo do Android é limitado até demais.
  Agora, cuidado aqui. Dependendo do *launcher* que você instalar e das
  configurações que vocẽ for *tweakar* depois, isso pode acabar trazendo mais
  *bloat* pro seu smartphone. Eu gosto do
  [Apex](https://play.google.com/store/apps/details?id=com.anddoes.launcher).

- Aprenda como limpar a cache do seu dispositivo. Dá para fazer isso através de
  um aplicativo, ou manualmente. Não convém fazer isso com muita frequência, mas
  de vez em quando é uma boa ideia.

- Desative a localização (GPS, Wi-Fi e redes móveis). A menos que você use com
  frequência algum aplicativo relacionado a isso. Sério, não 'venda' seus dados
  de localização tão facilmente.

- Instale um *browser* decente! O Stock Browser do Android é muito ruim. Dentre
  as recomendações, Chrome, Firefox ou Dolphin (não necessariamente nessa
  ordem). O Opera Mini ainda é útil para navegar no 3G e economizar mais dados.

- Desative o *bluetooth*. Quase ninguém usa isso hoje em dia. A única vez que
  eu usei isso foi para se comunicar com o meu notebook. Economiza bateria.

- Retire todos os *widgets* que vieram por padrão na sua *Home Screen*. A
  menos que você realmente precise deles... (é tão importante assim saber o
  clima / a temperatura toda hora?)

- Desative o *Google Now*. Ser interrompido toda hora com notificações é
  contraprodutivo. A menos que isso seja importante para você...

- Perceba, esses itens são apenas recomendações, pode ser que um aspecto ou
  outro seja importante para você, eu não vou mais ficar repetindo isso, acho
  que já deu para captar a mensagem.

- [Adblock](https://f-droid.org/repository/browse/?fdfilter=adaway&fdid=org.adaway)!
  Funciona **bem pra caramba**, um dos aplicativos que eu mais prezo. Precisa de
  root!

- Desative as transições / animações / haptic feedback / audio feedback.
  Traduzindo: desativar os efeitos visuais quando você muda de tela, desativar a
  vibração quando você toca em um botão (virtual) ou numa tecla (do teclado
  virtual), desativar o barulho de quando você toca em algo. Procure isso na
  configurações (*settings*). Geralmente está lá para o final, nas últimas
  opções.

- Revise os aplicativos que vieram por padrão na sua *Home Screen*. Você não
  precisa usar os que vieram (mas, provavelmente você irá querer alguns, como o
  dos contatos e o do telefone, assim como o web browser – senão, eu me pergunto
  qual é o objetivo do seu smartphone).

- Sincronização *upstream* com o fabricante: você não precisa disso, desative
  isso. Explicando melhor: geralmente os fabricantes disponibilizam algum
  aplicativo para sincronizar ou ajudar você a fazer alguma coisa. Isso varia
  bastante de um para o outro, e até mesmo o mesmo fabricante costuma mudar o
  nome desses aplicativos de uma versão do Android para outra. Note que eu
  **não** me refiro à sincronização do Google.

- Instale uma "*store" alternativa, com ***softwares livres***!
  [F-Droid](https://f-droid.org/). Se você, além disso, puder utilizar algum
  *software* de lá (em vez de um *closed source*), melhor ainda.

Vou parar por aqui. Esse post pode muito bem ter uma continuação no futuro,
ainda daria para falar de outras coisas. Tenho certeza de que você não conhecia
pelo menos um item que estava aí em cima. Assim como eu ainda não conheço outros
que não estão aí em cima. Sempre tem alguma coisinha nova para aprender, ou
alguma dica nova para melhorar a usabilidade. Aceito sugestões!

