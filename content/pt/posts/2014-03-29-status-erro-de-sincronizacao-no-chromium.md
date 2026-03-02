---
title: "Erro de sincronização no Chromium"
date: 2014-03-29T00:14:06-03:00
tags:
  - dev
  - legacy
---

Faz uns dias que noto que a sincronização dos meus favoritos no Chromium não
estava sendo realizada corretamente. Com um pouco de investigação, descobri que
o domínio `clients4.google.com` (utilizado para o servidor de sync, pelo menos
no meu caso) estava bloqueado no meu Arch (adivinha [por causa de
que]({{< ref "2014-03-02-bloqueando-websites-ads-malware-no-linux" >}})...).

Moral da história: cuidado, muito cuidado, com os seus *próprios* filtros.

OBS.: escreva `chrome://sync-internals` (ou `chrome://sync`) na barra de
endereços e seja feliz.
