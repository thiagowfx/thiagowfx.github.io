---
title: "Como rodar JNLP no Linux"
url: https://perrotta.dev/pt/2013/09/como-rodar-jnlp-no-linux/
last_updated: 2026-03-02
---


Da série "quem ainda precisa de Java nesses tempos sombrios"?

Esse post é mais um post do estilo do [Everyday Linux User
Blog](http://www.everydaylinuxuser.com/)do que um "faça isso e aquilo e agora
rode seu JNLP". Assim é mais legal e divertido (:

Já que toda boa história tem um *background:*recentemente (a.k.a. hoje) começou
o curso [Linear and Integer
Programming](https://class.coursera.org/linearprogramming-001/class) no
Coursera, e o pessoal da MathWorks resolveu distribuir a licença do MatLab de
graça por um período de alguns meses para os e-alunos que resolverem fazer o
curso.

O problema é que para instalar o MatLab precisamos de...Java! Pelo menos para
baixar o instalador. Eu não sei se após isso ele é necessário. Bom, baixei um
arquivo bem sugestivo chamado "download_agent" para fazer isso.

Faz muito tempo que não clico duas vezes em um arquivo executável pelo
gerenciador de arquivos (no meu caso era o Thunar), mas resolvi fazer isso só
para ver no que ia dar. Abriu uma página do Firefox com todo o código fonte do
que eu descobri ser um arquivo **JNPL.** Para quem não conhece, isso é um arquivo
do **Java Web Start**.

Então eu procedi da maneira tradicional, certo?

```shell
chmod +x download_agent && ./download_agent &
```

Mas isso naturalmente não deu certo (e nem era para dar, pois isso não é um
*script*). Qual a segunda opção mais intuitiva?

```shell
java download_agent
```

Muito bem. Mas isso também não funcionou. Esse não é um arquivo em Java, mas sim
um Java Web Start (a.k.a. JWS). O que fazemos? Consultamos o
[oráculo](www.google.com.br), é claro. A resposta dele é que eu preciso de um
arquivo chamado **javaws**. Fui ver se ele estava instalado e logo me
decepcionei.

Se você não sabe qual pacote utilizar, o que você faz? Que tal...pesquisar no
Google? Bom, essa é uma boa opção, mas há um método mais inteligente e elegante
(como os matemáticos gostam de dizer). Se você sabe usar bem o gerenciador de
pacotes (*package manager*) da sua distro, basta você perguntar a ele: ó meu
gerenciador, qual pacote tem o arquivo **javaws**??

Faça isso da forma que ele entenda, por favor =P

No **Arch Linux**, use *pkgfile javaws* e você vai ter o seguinte output:

```
extra/bash-completion
extra/icedtea-web-java7
community/cuda
community/processing
```

Com um pouco de bom senso (ou experiência?) você sabe que o pacote que você quer
é o icedtea-web-java7. E aproveita a "rolling releaseness" para ficar com a
versão mais atualizada (-;

Se você usa uma distro com apt-get (Ubuntu, Linux Mint, Elementary OS, ...), se
não me engano o comando

```shell
apt-file run javaws
```

...**provavelmente** vai retornar os pacotes que te interessam. Não tenho certeza,
se não for isso, pesquise! Com o yum (Fedora), acho que a versão do comando é:

```shell
yum whatprovides javaws
```

E no openSUSE, muito provavelmente:

```shell
zypper wp javaws
```

Sinto muito por não poder confirmar os últimos 3 comandos, atualmente não estou
com essas distros instaladas, mas isso é o que me veio à memória agora.

Depois de encontrar o pacote mais adequado, instale-o!

```shell
sudo apt-get install nome_do_pacote
```

```shell
sudo yum install nome_do_pacote
```

```shell
sudo zypper in nome_do_pacote
```

E então rode o programa JNLP com:

```shell
gksudo javaws download_agent
```

E seja feliz.

Obrigado por ler.

