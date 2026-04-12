---
title: São tantas licenças...
date: 2013-08-22T18:43:51-03:00
tags:
  - dev
  - legacy
---

Existem tantas licenças de software hoje em dia! Se você está disposto a criar
um software ou mesmo algum conteúdo desde artes e figuras até legendas de
vídeos, pode ser tão chato escolher uma licença para isso que muitas vezes essa
questão é simplesmente ignorada. Esse post tenta resumir um pouco desse
emaranhado de licenças.

(A motivação de escrever esse post é do próprio autor, que até então se
encontrava no caos e não sabia muito bem que tipo de licença utilizar para
distribuir software ou códigos. Esse é meu primeiro post criado em Markdown e
depois transcrito para cá)

**Software Livre**. Deve possuir 4 liberdades fundamentais e **essenciais**:

- 0 - executar o programa;

- 1 - **acesso ao código-fonte (open source = código aberto)**: estudar como ele
  funciona e adaptá-lo às suas necessidades

- 2 - distribuir cópias livremente (para ajudar o próximo)

- 3 - melhorar o programa e liberar seus aperfeiçoamentos, para que toda a
  comunidade se beneficie.

Esse tipo de licença foi idealizada por **Richard Stallman**, que criou a **Free
Software Foundation**. Ela é fortemente defendida por ele até hoje.

A licença mais comum que engloba esses 4 princípios de liberdade é a **GNU GPL
License**. Adicionalmente, ela também exige que quaisquer trabalhos derivados
mantenham a mesma licença. Exemplo de software com essa licença: GNU Emacs.

Mais informações: [GNU GPL](http://www.gnu.org/licenses/gpl.html)

Também existe a LGPL, que é um pouco mais liberal nesse sentido. Ela é
praticamente igual à GNU GPL, exceto que não exige que obras derivadas tenham a
mesma licença original. Exemplo de software: Tomboy.

Mais informações: [LGPL](http://www.gnu.org/licenses/lgpl.html)

Note que em inglês o termo **free** pode ser ambíguo, podendo se referir tanto a
*gratuito* como a *livre*. O Stallman sempre deixa bem claro que a GNU GPL se
refere ao segundo significado. Você pode ganhar dinheiro com software livre: não
há nenhuma restrição de mantê-lo grátis. Um exemplo típico: para realizar
manutenções.

Em português não há esse problema, temos pelo menos dois termos distintos para
acabar com a confusão: *grátis* e *livre*.

A **GNU GPL** é dita um tipo de *licença copyleft*.

Uma outra licença é a [*BSD*](http://opensource.org/licenses/BSD-3-Clause),
dita *licença permissiva*. Eu particularmente achei um pouco difícil entendê-la
por completo, em vez disso acho mais fácil entender algumas coisas a respeito
dela comparando-a com a GNU GPL.

- Ela é uma licença permissiva, no sentido de que é quase um domínio público,
  ela permite quase tudo, desde que a priori o autor original da obra seja
  citado.

- Existem várias variantes da licença BSD, cada qual com seus autores, e isso às
  vezes é visto como algo *annoying*.

- Talvez a principal diferença com relação à **GNU GPL**: a licença **BSD**
  permite que seu software seja incorporado a produtos proprietários. Lembrando
  que a **GNU GPL** exigiria que o produto ao qual ela fosse incorporado deveria
  também ser distribuído sob ela própria. Nesse sentido, por exemplo, código do
  *FreeBSD* (sistema operacional) pode ser vastamente incorporado e utilizado
  por aí, "sem remorso" (desde que os autores sejam citados...).

- Note que isso é um ponto fundamental: a **GNU GPL** defende o software livre,
  e o fato de ter que manter um produto distribuído sobre ela é uma forma de
  incentivar o uso e o crescimento do mesmo. Enquanto que a **BSD** acredita
  que seu software pode ajudar a melhorar (por exemplo) a qualidade de softwares
  em geral, sejam eles proprietários ou não. Mais informações: [BSD vs
  GNU](http://pt.wikipedia.org/wiki/Licen%C3%A7as_BSD_e_GPL).

- Uma passagem interessante (em inglês) encontrada
  [aqui](http://programmers.stackexchange.com/questions/82321/why-do-people-pick-the-mit-license-over-bsd-if-bsds-non-endorsement-clause-i):

> A friend of mine once pointed out that licenses tell you what the license
  authors were scared of.
>
> If you're scared of having your name dragged through the mud, then the BSD
> license will seem better. If you're scared of having your software put into a
> proprietary piece of software, then the GPL will seem better. Whatever the
> license, the author chooses it because it protects them against what they are
> afraid of.
>
> Different people have different concerns and so use different licenses.

A licença **MIT** é bem parecida com a **BSD** versão "3-clause". Uma diferença
é que ela é bem mais simples, a menor de todas.

- Você pode usar, copiar e modificar o software da maneira que bem entender e
  ninguém pode impedir você de usá-lo em qualquer projeto (inclusive
  proprietários), ou copiá-lo e modificá-lo.

- Você pode distribui-lo como bem entender. Grátis ou vendendo. Sem restrições.

- A única restrição é o produto deve ser acompanhado com a licença.

A **MIT** é a licença menos restritiva. Note que a **BSD** exige *disclaimers*
de garantia. Mais informações
[aqui](http://www.smashingmagazine.com/2010/03/24/a-short-guide-to-open-source-and-similar-licenses/).

Também existe a **Apache**:

- Os direitos da licença são perpétuos

- São garantidos no mundo inteiro (não apenas em um país, por exemplo)

- São garantidos de graça e sem quaisquer tipo de *royalties*

- São não exclusivos: qualquer um pode usar a obra

- Nenhum desses direitos pode ser tirado uma vez que sejam dados. (Isto é: ninguém pode chegar e dizer "você não pode mais usar isso agora")

Além disso, a licença deve ser mantida caso alguém modifique o produto. E os
créditos devem ser devidamente dados.

Ou seja, a Apache parece ser uma boa segunda opção, no que diz respeito a
software livre, depois da **GPL**. Ela é a licença que o Google costuma usar em
seus produtos que são abertos.

Existem outras licenças populares que eu não abordei aqui, como a **creative
commons** a da **Mozilla**. Também existe um conceito de distribuir software
sob licenças mistas / híbridas.

A ideia desse post foi definir e resumir as principais diferenças entre as
várias licenças existentes hoje em dia que tem mais a ver com **open source** e
**software** em particular. Lembrando que temos 2 licenças permissivas: **MIT**
e **BSD**; e também 2 licenças livres: **GPL** e **Apache**.
