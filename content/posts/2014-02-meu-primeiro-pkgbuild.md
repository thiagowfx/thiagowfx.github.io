---
title: 'Meu primeiro PKGBUILD'
date: 2014-02-13T20:08:00-03:00
tags:
  - classics
  - portuguese
---

Título mais legal: Meu primeiro PKGBUILD (eeeeeeeeeeeee). Mas não coloque
firulas como esse eeeeee em um título de post do Wordpress, obrigado.

Agora, eu ainda não sei o que é um metapost, eu ainda preciso definir
isso...mas, é algo entre journal e status.

Você sabe, do primeiro PKGBUILD a gente não se esquece. Mas que raios é isso?
Bom, a menos que você viva no meu mundo, ou a menos que você já tenha usado
o Arch Linux alguma vez, eu realmente não tinha nenhuma intenção de que você
soubesse isso. Alerta: os próximos 3 parágrafos são bem didáticos.

Um PKGBUILD é um simples script que diz como criar um pacote. É como uma
receita de bolo. Você diz tudo pra ele: baixa o código-fonte tal, compila de
tal jeito, extrai esse zip pra cá, põe esse arquivo em /usr/share, esse outro
em /etc, aplica o patch tal. Um pacote contém um programa. Se você está
acostumado com setups do Windows, um pacote é como se fosse um setup, um
programa de instalação. A diferença é que você não precisa seguir um wizard
gráfico, clicando em next toda hora. Você simplesmente pega o arquivo, executa
um único comando, e pronto, seu programa está instalado.

Existe uma curva (razoavelmente grandinha) para criar um bom pacote. Pegue um
setup do Windows, por exemplo. Se você quiser distribuir o seu programa legal
para outros usuários Windows, você vai demorar um bom tempo para criar um setup
.exe. Tem várias ferramentas para isso, é claro, e você pode simplificar o seu
trabalho, ou não. O próprio WinRAR tem uma utility de SFX que facilita bastante
esse processo. Mas, ainda assim, não acho isso *super elegante (mas é simples,
é verdade).

No Mundo Linux, nada é padronizado (maldição). Existem pacotes .deb, .rpm,
.tar.gz. Existem scripts que criam pacotes, como PKGBUILDs (Arch Linux),
ebuilds (Gentoo -- não sei bem se ebuild faz isso, é melhor você pesquisar para
confirmar), até o Slackware tem a sua forma simples de criar pacotes através de
um script. Para criar um bom pacote .deb, ou um bom pacote .rpm, você também
vai demorar razoavelmente.

Agora, eu tenho que dizer (de maneira suspeita, você deve saber) que um
PKGBUILD é perfeito. Uma das formas mais elegantes de manter e gerenciar
pacotes. A curva para você criar um pacote é bem pequena (curva de tempo entre
você querer criar um pacote e vê-lo efetivamente criado). Bom, supondo que você
pelo menos saiba o básico de shell scripting -- bash, ya know --, combinado?

Então, eu só queria compartilhar a minha primeira contribuição para
a comunidade do Arch. Ah, esqueci de dizer que qualquer usuário pode criar um
PKGBUILD e adicioná-lo num repositório no qual todos os outros usuários do Arch
têm acesso, sabia disso? Isso significa que qualquer um pode contribuir para
a comunidade (com pacotes -- na verdade, PKGBUILDS...!), e que a probabilidade
de você ter pensado em um programa open source popular (às vezes, até, não
popular também) que NÃO está no Arch User Repository é bem pequena. A todo
momento, sempre tem alguém adicionando (e atualizando, mantendo) esses pacotes.
Claro, nem tudo é perfeito, não tem um ou outro, mas enfim. Eu falei que
o PKGBUILD é perfeito, não que a disponibilidade de pacotes é perfeita...mas
é quase perfeita! :)

Na verdade, eu sempre quis criar (e manter) algum PKGBUILD, mas todos os
programas legais nos quais eu pensei simplesmente já são mantidos por alguém.
Nesse caso, recentemente criei uma adaptação de um outro PKGBUILD que já
existia (sério, se você encontrar algum programa ainda sem PKGBUILD no AUR, me
fala, que provavelmente eu vou querer criar um para ele). Não há necessidade de
reinventar a roda.

O meu PKGBUILD é esse [aqui](https://github.com/thiagowfx/PKGBUILDs/blob/aur3/arch-firefox-nightly-search/PKGBUILD):

```bash
pkgname=arch-firefox-nightly-search
pkgver=37.0a1
pkgrel=1
pkgdesc="Firefox Nightly Arch search engines (official packages, AUR, BBS, wiki and bugs)"
arch=('any')
url='http://www.archlinux.org/'
license=('GPL')
depends=('firefox-nightly')
source=('arch-bugs-fs.xml'
  'arch-bugs-t.xml'
  'arch-forum-a.xml'
  'arch-forum-c.xml'
  'arch-pkgs.xml'
  'arch-wiki.xml'
  'aur.xml')
md5sums=('df18835df1ea78bc3fc0e05f934b1e46'
         '0226a317c8bf23feaa80e21d1706f2d5'
         '4eaa3d26ac41077ee25b66127ad9ef0a'
         '2435c34ea6a012fe08a8d17a051e5f80'
         '403c346ce089ec56c2db67f9f3d87514'
         'dbb93d1e793b92252b69f65110b33c42'
         'b70839977625bceb3004dc62fb9e5a65')

package() {
  prefix="${pkgdir}/opt/firefox-${pkgver}/browser/searchplugins/"

  for file in ${source[@]}; do
    install -Dm644 "${srcdir}/${file}" "${prefix}/${file}"
  done
}
```

Você pode ver aqui como um PKGBUILD é bastante
simples "por dentro". Ele não tem nada de especial, é um PKGBUILD como outro
qualquer. Mas é o meu primeiro -- na verdade, isso faz com que ele seja
especial, sim. Acho que já dá para perceber o que ele faz.

Só para falar um pouquinho da minha experiência fazendo isso. Bom, foi difícil.
Mesmo adaptando um PKGBUILD já existente, foi difícil. Tudo que é novo, feito
pela primeira vez, é difícil, certo? Mas foi bastante legal. Na verdade, isso
é uma experiência extremamente fácil e ridícula.  Só foi difícil porque eu
nunca tinha feito isso antes. Mas essa que é a graça da coisa! Pior seria que
fosse uma atividade difícil mesmo para quem já está acostumado. Mas é por isso
que eu estou elogiando a simplicidade (e a elegância!) de um PKGBUILD. A Wiki
do Arch é bastante documentada. Não faltou tutorial ensinando sobre bons
padrões de scripting para "empacotamento", nem guias sobre como contribuir para
a comunidade.  E nem faltam exemplos, são mais de 40 mil PKGBUILDs espalhados
por aí (talvez já tenha chegado a 50k, não me lembro). Só para comparar,
o repositório do Debian tem em torno de 40 mil pacotes, se me lembro bem.
Então, dá para comparar a base de pacotes do Arch com a do Debian, o que
é impressionante (só não tem mais do que isso porque o Arch não é tão popular.
Isso também faz parte da beleza da coisa, mas é outra história).

Digo uma coisa: a melhor coisa (pare de repetir a palavra 'coisa'!) que você
pode fazer é interagir com a comunidade da sua distro (supondo que ela seja
minimamente ativa). É bastante fácil obter ajuda e ganhar experiência  com quem
já sabe. Eu não precisei fazer isso quando criei o meu pacote porque ele era
bastante simples, mas se ele fosse complexo eu certamente faria. E, de qualquer
modo, eu posso não ter lido nada recentemente, mas ao longo de alguns meses eu
estou sempre lendo outras pessoas pedirem suporte, e essa também é uma boa
forma de você acompanhar e aprender como fazer melhor alguma atividade.

Pronto, só queria deixar isso registrado aqui, obrigado por ler. Brincadeira.
Talvez esse post tenha servido para -- remotamente falando... -- querer
despertar o seu eu interior para criar um PKGBUILD também. Er...não.

Falando sério agora, se você que está lendo isso é um usuário de Linux faz
algum tempo, considere criar um pacote para a sua distribuição. De preferência,
um pacote de algo que ainda não foi empacotado. Ou então ajude um mantenedor
("maintainer" soa melhor) da sua distro a atualizar seu pacote.  Pode ser algo
simples. Talvez seja mais fácil criar um .deb e um .rpm do que eu afirmei aqui,
é só uma questão de prática.

Se você é um usuário de OS X, de Windows, ou de outra plataforma, aprecie
a beleza do que é ter uma boa base de pacotes para a sua plataforma. Na
verdade, eu acho que o OS X tem um gerenciador de pacotes (macports, não é?
Estou fora do mundo Apple, sorry), mas eu não sei o quanto é fácil para um
usuário criar um pacote lá (e, ainda, compartilhar com a comunidade do mesmo.
Se bem que a forma de compartilhar por lá é vendendo por 0,99 dólares, não é,
mas OK, ainda assim é compartilhar...). E no Windows, bom, existem até alguns
projetos de gerenciadores de pacotes para lá (como o chocolatey), mas
praticamente nenhum usuário usa (sequer conhece!) isso, então não é algo
tãaaaao valorizado. Mas OK.

Ainda existem gerenciadores de pacotes para várias linguagens de programação.
Npm, cabal, gem. É, acho que essa foi uma das melhores peças de software que já
inventaram, evita bastante dor de cabeça.

Sinta-se à vontade para deixar um comentário ou apontar um link sobre sua
experiência de criar pacotes em outra distribuição de Linux, ou em alguma
linguagem de programação.
