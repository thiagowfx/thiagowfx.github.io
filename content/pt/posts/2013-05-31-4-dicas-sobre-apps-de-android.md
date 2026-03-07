---
title: 4 dicas sobre apps de Android
date: 2013-05-31T20:51:17-03:00
tags:
  - dev
  - legacy
---

Após usar o Android Jelly Bean durante mais de um mês e adquirir uma
maturidade razoável com o sistema, compartilho aqui algumas experiências sobre
aplicativos através de algumas dicas simples e práticas.

*OBS*.: Os itens abaixo não listados por ordem de relevância.

**1) Não instale aplicativos matadores de memória.**

Na *play store* existem diversos aplicativos que prometem agilizar o sistema
matando outros aplicativos, recuperando, assim, preciosa memória RAM. Dois
deles podem ser conferidos em [1](https://play.google.com/store/apps/details?id=mobi.infolife.taskmanager)e
[2](https://play.google.com/store/apps/details?id=biz.stachibana.TaskKiller&hl=pt_BR).
Alguns desses apps, inclusive, permitem que a "limpeza de memória" seja
programada para ser feita periodicamente.

Isso pode atrair muitos usuários, especialmente aqueles que fazem um uso
intenso (multitarefa) de seus aparelhos e notam certa lentidão. Só que existem
2 problemas com esses aplicativos.

Primeiro, eles podem tornar o sistema instável. Forçar o fechamento de um aplicativo pode causar consequências não muito convenientes (especialmente no modo de limpeza automática, no qual qualquer aplicativo em segundo plano pode ser fechado a qualquer momento). Especialmente se um aplicativo do sistema for fechado (talvez você não perceba nenhum dano grave se o importante Facebook for fechado do nada, mas e se algum serviço do Android o for?) Se existe algum aplicativo em particular que não se comporte muito bem, existem maneiras mais eficientes de monitorar o seu comportamento (por exemplo, [3](https://play.google.com/store/apps/details?id=com.zomut.watchdoglite&hl=pt_BR)).

Segundo, matar memória dessa maneira é contra a filosofia (existe uma palavra
melhor para isso...que tal, **design**?) do Android. É comum o usuário fazer
uma analogia com sistemas operacionais de desktop, especialmente com o
Windows, achando que fechar muitos programas que estão abertos no momento
tornaria a navegação mais rápida, já que memória RAM seria liberada (para o
Windows, isso é realmente verdade! Rodar menos programas, em geral, propicia
uma velocidade maior, já que a CPU fica menos sobrecarregada). O problema é
que o Android não é um sistema operacional de desktop e, portanto, ele
gerencia memória de maneira um pouco diferente. Ele possui um modo mais
eficiente de gerenciar quais aplicativos estão sendo usados pelo usuário no
momento e de prever quais aplicativos o usuário pode querer usar num futuro
próximo (isto não é completamente verdade, mas a ideia é mais ou menos essa).

**2) Não instale aplicativos demais.**

Isso pode parecer fútil, mas não é. A maioria dos apps para Android utiliza
**serviços**, que são uma forma de execução de apps no segundo plano. Assim,
mesmo que você esteja com o Facebook ou o Dropbox fechados, por exemplo, eles
ainda estarão rodando em segundo plano. O problema é que, quanto mais apps
você tiver instalados, mais provável é que você tenha mais serviços rodando.
Desse modo, mais lento o seu aparelho fica. Você não precisa se preocupar, em
geral, se tiver poucos aplicativos instalados. Alguns sequer usam serviços
(por exemplo: um aplicativo de calculadora não tem necessidade de rodar em
segundo plano).

No entanto, instalar muitos aplicativos que usam serviços começa a causar uma
pequena diminuição na velocidade do aparelho. Isso não é tão grave assim,
somente se você tiver aplicativos demais. Nesse caso, uma solução seria rootear
o seu aparelho para controlar quais serviços você deseja que sejam executados e
quais você deseja desativar. No entanto, essa solução é avançada para o usuário
típico, então, a menos que você seja um superusuário, é melhor instalar apenas o
que você realmente usa (em outras palavras: não encha sua *app drawer* com
*bloatware*...).

Reiterando: se você só tem apps de redes sociais (que não são muitos para as
*mainstream*), por exemplo, você não precisa se preocupar com isso.

3) **Não confie em qualquer aplicativo.**

Cheque sempre as permissões dos aplicativos antes de instalá-los. Você
não irá querer, por exemplo, que um aplicativo de lanterna ou
de calculadora tenha acesso aos seus contatos. Muito menos a sua
localização. *Tracking* de informações de usuários é o que mais
tem por aí hoje em dia.

No entanto, note que é comum a maioria dos apps pedir permissão de acesso à
internet (sim, mesmo um app de lanterna). Isso é normal pois, em geral, eles só
querem dados para **propagandas (ads)**. Assim, não precisa ficar paranoico com
esse tipo de permissão. Agora, atente sempre as outras permissões! Veja se elas
são realmente necessárias. Se não forem, procure outro aplicativo. (Uma opção
mais avançada, se você tiver um android rooteado, é instalar apps que controlem
o que cada app tem ou não permissão de acesso).

**4) Resista à tentação de comprar tudo o que você vê.**

Isso só é um potencial problema para quem tem cartão de crédito integrado com a
conta do Google. Em tempos de web 3.0, é muito fácil comprar livros, filmes e
aplicativos (yeah, estou falando da play store). MUITO FÁCIL E MUITO BARATO.
Agora, muitas coisas baratas somadas = peso no seu bolso! Resista à tentação de
comprar tudo quanto é aplicativo. Você não precisa comprar as versões PRO de
cada aplicação específica. NÃO PRECISA! A menos que você conheça uma ou duas
aplicações muito boas, vá em frente, compre-as. Mas não compre
(desnecessariamente) tudo o que você ver pela frente, nem que sejam apenas 2
reais (2 reais x 30 aplicativos = 60 reais, por exemplo). Sem contar que muitas
vezes existe outro app grátis que tem a função que você procura.

Bom, é isso. As dicas são bastante simples, mas às vezes não nos damos conta
delas tão explicitamente. É sempre bom reforçar a importância delas.
