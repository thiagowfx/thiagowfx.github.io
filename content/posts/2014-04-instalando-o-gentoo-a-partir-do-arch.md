---
title: Instalando o Gentoo a partir do Arch
date: 2014-05-01T02:20:00+00:00
tags:
  - classics
  - linux
  - portuguese
---

**TL;DR**: pequena TODO list sobre como instalar o Gentoo. Você vai passar 90% do seu tempo olhando para **texto** dando scroll na tela (processo demorado…).

<!--more-->

Esse é o método mais tradicional possível (e que me interessa) que pude constatar. Adapte-o para as suas próprias necessidades:

- Boote em um ambiente com o Arch (na verdade, você pode fazer isso a partir de qualquer distro decente).

- Crie uma partição `/`, do tipo ext4, para acomodar a instalação do Gentoo. De preferência, coloque um label decente lá. Sugestões de ferramentas para isso: `cfdisk` ou `gparted`.

- Monte essa partição em `/mnt/gentoo`.

- Continue a partir do [handbook](http:www.gentoo.org/doc/en/handbook/handbook-amd64.xml?part=1&chap=4) oficial do Gentoo – nesse caso, para a arquitetura amd64. No entanto, <b>atenção</b>. Use [esse](https:wiki.gentoo.org/wiki/Installation_alternatives) guia para perceber quais etapas de instalação e configuração são diferentes (em relação a se estivéssemos instalando pelo método oficial, a partir do live environment do gentoo), mais especificamente <b>da parte 4 à parte 6</b>.

- Baixe o `PKGBUILD` `gentoo-mirrorselect` do AUR.

- Use `mirrorselect -i -o` e então selecione interativamente os mirrors mais próximos da sua localização atual. Copie o valor da variável `GENTOO_MIRRORS` para o final do seu `/mnt/gentoo/etc/portage/make.conf`.

- Copie o seu `/etc/resolv.conf` para `/mnt/gentoo/etc/resolv.conf`. Isso é [importante](https:bbs.archlinux.org/viewtopic.php?id=95865) para ter conectividade dentro do ambiente de chroot.

- `CFLAGS` que recomendo para o `/etc/portake/make.conf` (<a href="https:forums.gentoo.org/viewtopic-t-933456-start-0.html">helper</a>):

```
-march=native -O2 -pipe
```

- A partir daqui, nada especial, apenas continue seguindo o handbook do gentoo, até a parte do bootloader.

- Chegando na parte do bootloader, optei por deixar o Arch gerenciá-lo. Nesse caso, basta rodar um típico `grub-mkconfig -o /boot/grub/grb.cfg` que o Gentoo deverá ser automaticamente detectado (supondo que o pacote `os-prober` esteja instalado).

- Configure a rede no Gentoo. Isso é bastante específico, mas o procedimento é bem parecido com a configuração da rede no Arch. A única questão é que, ao dar emerge no `wpa_supplicant` (no caso de você utilizar Wi-fi), vai demorar bastante até todas as dependências serem instaladas (esse é o ponto principal que me afastou do Gentoo até hoje. Sem pacotes binários, ter que compilar tudo localmente…ao menos, se no final a otimização do sistema for maior, poderia ter valido mais a pena.)

- Teste o Gentoo durante uma semana e diga o que você achou dele 😉

- Decida se você gosta mais do Gentoo ou do Arch. Isso vale tanto para o sistema, tanto para a comunidade. Não tenho ideia de como seja a comunidade do Gentoo (a do Arch eu já tinha uma boa noção de como era mesmo antes de ter o sistema instalado).

Valeu pessoal. Como sou 100% newbie no Gentoo, apreciarei quaisquer dicas! (Enquanto as dicas não aparecem, Wiki Pages e Forums Threads me esperam). Sabe, é bom, de vez em quando, ser newbie em alguma coisa. Claro que ser expert / muito bom / hacker em algumas aplicações é ótimo, mas eu acredito na importância de possuir uma boa base de conhecimento em geral (não necessariamente apenas para fins acadêmicos ou financeiros, mas também para satisfazer a mente: desafios são importantes!).

Ah, mais dois comentários:

- Terminando de escrever esse post e de editá-lo, a compilação dos (130) pacotes que o `wpa_supplicant` puxou não chegou nem na metade… (eu teria instalado uns três ou quatro Archs automatizados nesse tempo – tá bom, não vale comparar pacotes binários com código-fonte, eu sei)

- Esse é o meu terceiro ou quarto post utilizando o `org2blog` (do emacs). Já ficou bastante claro para mim que vou passar a usá-lo de maneira fixa. O único problema é que eu ainda não sei a sintaxe de formatação dele direito, é muita informação. Não é nem que não seja intuitiva, mas já tem LaTeX, BBCode, Markdown, aí eu tenho que aprender mais uma markup language. Mas, provavelmente vou me submeter a isso, o **orgmode** é sensacional para _management_ em geral.