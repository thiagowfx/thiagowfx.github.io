---
title: "OpenPGP"
url: https://perrotta.dev/pt/2014/05/openpgp/
last_updated: 2026-05-25
---


Em meu [último post]({{< ref "2014-04-26-openpgp" >}}) incluí uma porção de
referências introdutórias ao tema, que são suficientes para que você comece a
utilizar o GNUPG. Agora eu mesmo já comecei a utilizá-lo publicamente. Em suma,
as duas principais razões para se ter uma chave pública são:

- **Autenticação**: assinar (=validar) arquivos; isto é, se eu distribuir
  (digamos) um software para você, e eu assiná-lo com a minha chave privada,
  você poderá utilizar a minha chave pública para conferir se aquele arquivo foi
  realmente assinado por mim. Caso alguém (um *man in the middle*) pegue o meu
  arquivo original e o falsifique, fazendo-o se passar por mim, você poderá
  detectar que o arquivo é falso, pois a minha chave pública invalidará a
  assinatura desse software. Em outras palavras: a minha chave privada (que só
  eu tenho) é utilizada para assinar arquivos ou documentos; e a minha chave
  pública (disponível para todos) é utilizada como um validador da minha
  assinatura digital/eletrônica. Legal, né? Quer ver um exemplo? [*
  Aqui*](https://mailman.archlinux.org/pipermail/aur-general/2014-May/028299.html),
  meu primeiro e-mail validado com a minha chave.

- **Criptografia**: se você quiser me enviar uma mensagem criptografada, basta
  você utilizar a minha chave pública para criptografá-la. Desse modo, somente
  eu (dono da minha chave privada) serei capaz de descriptografá-la. Da mesma
  maneira, se você me enviar a sua chave pública, eu poderei enviar uma mensagem
  criptografada para você (e somente você, com a sua chave privada, poderá
  descriptografá-la).

Essas razões não parecem importantes o suficiente para você? Veja bem, estamos
entrando cada vez mais numa era (se é que já não entramos nela)
predominantemente digital. Proteger a autenticidade e a privacidade do que
postamos na rede é algo que vai adquirir cada vez mais importância.
Naturalmente, ninguém vai assinar um post no facebook ou no twitter, isso é
exagero (Será mesmo? Talvez daqui a uns anos não seja mais).

Mas eu acredito que toda corporação decente deveria incentivar os seus
funcionários a enviar mensagens assinadas com suas chaves pessoais. Mais do que
isso, toda corporação deveria ter um modelo de **Web of Trust** com todas as
chaves de seus funcionários. Não se trata de paranoia ou de super proteger
informações as quais não valem tanto esforço de serem super protegidas, mas é um
passo básico na direção da privacidade moderna! O OpenPGP foi criado em 1991
([referência](https://en.wikipedia.org/wiki/OpenPGP#OpenPGP)), agora estamos em
2014, será que isso é demais?

Vou lançar um **desafio**: me envie uma mensagem criptografada com a [minha
chave
pública](http://pgp.mit.edu/pks/lookup?op=vindex&search=0x755D25D2A905373C)! Se
quiser, envie nessa mensagem também a sua própria chave pública, assim eu posso
te responder (também) de modo criptografado. Os links do meu [post anterior]({{<
ref "2014-04-26-openpgp" >}}) são suficientes para você aprender como fazer
isso. Eu espero que você se surpreenda com isso, muita gente boa troca mensagens
assim.

Se eu receber pelo menos um e-mail, vou considerar escrever mais coisas a
respeito de OpenPGP.

Além disso, espero criar as minhas próprias carteiras digitais {bitcoin,
litecoin, dogecoin} em breve. Naturalmente, seguidas de posts de divulgação
sobre elas!

**Happy GPG'ing!**

**Update**: confundir PGP e GPG é algo bastante comum. Acho que já aprendi a
diferença, ao menos não cometi nenhum erro nesse post sobre isso (no post
anterior eu cometi...). O nome bonito da coisa é OpenPGP; gpg é o comando (no
linux) que a gente usa para gerenciar as chaves. GPG vem de "GNU Privacy
Guard").

