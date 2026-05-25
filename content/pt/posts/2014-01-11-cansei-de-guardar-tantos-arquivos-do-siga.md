---
title: "Cansei de guardar tantos arquivos do SIGA"
date: 2014-01-11T23:23:54-03:00
tags:
  - dev
  - git
  - legacy
---

Isso aqui é o tremendo caos:

{A figura não existe mais}

Resultado de 2 anos de documentos, isso porque alguns foram deletados
manualmente de uns tempos para cá. OK, eu devo ter aprendido algo de útil em 2
anos, certo?

```shell
tar zcvf siga-2012-2013.tar.gz "SIGA and stuff"
```

Se você não tiver nada a perder, mande o seu `rm -rf`. Mas, por uma questão de
consciência, ainda não vou deletar documentos antigos. Mas isso não significa
que eu precise manter tudo bagunçado...vamos usar [controle de
versão](http://mercurial.selenic.com/)!

```shell
$ hg init
$ hg add doc.pdf boletim.pdf
$ hg commit -m "first commit"
```

Resultado mais limpo, obrigado:

{A figura não existe mais}

OK, agora vou repetir o que eu falei de forma mais amigável: se você não quiser
ter vários PDFs amontoados, você pode começar compactando tudo (zip, rar, tar,
você escolhe). A partir de então, vamos passar a ter **um único** PDF de cada
elemento (histórico, boletim, BOA...). Ao baixar um histórico ou boletim,
vamos substituir (=deletar o antigo e colocar o novo no lugar, tanto faz) o
anterior com o novo. Mas, caso seja necessário recuperar o anterior numa data
posterior, ele estará sempre guardado no nosso sistema de controle de versão
(que pode ser o mercurial, o git, etc — BTW, usualmente eu uso o `git`, só estou
usando o mercurial agora para fins de hobby/aprendizado). Resumindo: você passa
a externalizar o trabalho de manter múltiplas versões de arquivos, e basta.

Tá bom, se alguém realmente tenha se interessado por essa baboseira toda e
seguiu os comandos acima =P, caso você baixe um novo histórico e boletim e
queira atualizá-los no Mercurial, faça o seguinte:

- substitua os arquivos anteriores — certifique-se de sempre usar o mesmo nome,
  exemplo: `hist.pdf`;
- atualize seu repositório local:

```shell
hg commit -m "minha nota de física foi adicionada"
```

Agora, se você realmente precisar recuperar um arquivo antigo algum dia...bom, é
só pesquisar como fazer isso, não é difícil. A menos que você já esteja
acostumado a utilizar controle de versão, não vale a pena decorar isso agora
(mas sim *aprender*, quando você realmente precisar...).
