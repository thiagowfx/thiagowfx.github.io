---
title: "Novidades do AUR4"
date: 2015-06-17T02:37:43-03:00
draft: true
tags:
  - dev
  - legacy
  - linux
---

Contexto: https://aur4.archlinux.org/

Daqui a algumas semanas esse link estará quebrado e se transformará
em: https://aur.archlinux.org/

Eu ainda tenho que testá-las...mas, notei o seguinte:

1. **Co-maintainers**: mais de uma pessoa vai ter permissão para atualizar os
   PKGBUILDs. Isso é bastante útil, principalmente para os projetos mais
   relevantes atualmente de lá (dropbox, chromium-pepper-flash, etc).
2. Gerenciamento dos PKGBUILDs e da infraestrutura foi toda migrada para o
   **Git**. Vamos ver se um dia os repositórios oficiais também farão isso. Por
   enquanto eles utilizam subversion ainda. Talvez subversion não seja tão ruim
   mesmo, essa mentalidade de achar que git é bom para tudo não necessariamente
   está correta, certo?
3. **Keywords**: os maintainers poderão incluir palavras-chaves arbitrárias
   associadas aos seus pacotes, para ajudá-los a serem mais facilmente
   encontrados nas buscas. Por sinal, as "categorias sumiram. O que é bom, já
   que ninguém usava aquilo direito mesmo.

**Update (2015-06-18)**: Sobre **2)**, isso é um *big deal*. Significa que tudo
que passar pelo AUR vai ficar permanentemente gravado, cada pacote com o seu
próprio histórico de *commits*. Existe uma interface web *cgit* onde esse
histórico pode ser visualizado – isto é, analogamente aos pacotes oficiais! No
que diz respeito à infraestrutura, isso é uma enorme evolução.

Ademais, mal passaram umas 2–3 semanas e olha só (AUR --> AUR4):

- Pacotes: 56975 --> 14493
- Pacotes órfãos: 15872 --> 89

Em primeiro lugar, muitos pacotes foram migrados. Cerca de 25%. Comparado com
outras distribuições, e considerando que esse é um repositório não-oficial, isso
é **muita** coisa, e mostra que existem vários *maintainers* ativos por aí –
houve um dia em que eu achava que o Arch era muito pequeno em termos de
comunidade, mas não é e está aí a prova. Na verdade, eu acho o tamanho do mesmo
bastante ideal, nem tão grande (o que evita algumas coisas como *help
vampirism*) e nem tão pequeno.

Mas enfim, e em segundo lugar: isso é um enorme *cleanup* do AUR. Muitos pacotes
que não eram mantidos agora vão simplesmente sumir ou, pelo menos, não ser
migrados. Isso é bom porque aumenta a qualidade dos pacotes do AUR, no geral –
já que menos pacotes desatualizados e eventualmente ruins / não funcionando
estarão no AUR4.

Ver o AUR evoluir assim é muito legal e me dá gosto de ter escolhido o Arch como
distribuição e comunidade principal. Quando algum dia a coisa explodir, ainda
temos o {G,F}untoo, mas ainda vai demorar bastante para isso acontecer.

*makepkg not war*
