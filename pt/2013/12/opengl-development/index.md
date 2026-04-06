---
title: "OpenGL Development"
url: https://perrotta.dev/pt/2013/12/opengl-development/
last_updated: 2026-03-09
---


Nesse post vou resumir um pouquinho sobre o que venho aprendendo em OpenGL. Com
ênfase em **resumir**. Não dá para explicar todos os conceitos aqui; essa é uma
área muito grande; tanto quando a da Maratona. Esse também não é um tutorial de
OpenGL, de modo que não vou explicar tudo desde o começo, mas vou falar várias
coisas de modo mais ou menos solto. Então, qual o objetivo desse post? Fixar e
compartilhar ideias. E, quem sabe, esclarecê-las também =P. Para tirar o maior
proveito do que eu falar aqui, você vai ter que correr atrás das principais
palavras chaves e termos que eu listar. Por correr atrás, entenda pesquisar no
Google e ler tutoriais, wikis e manuais. Compilar também pode fazer bem
eventualmente. Nesse caso, utilize esse post como um guia para saber o que você
deve pesquisar e/ou estudar de OpenGL. Aceito sugestões para aumentar ainda mais
essa lista. Obrigado, e agora vamos lá.

**Disclaimer**: a maioria das coisas que estou escrevendo aqui vêm da minha
cabeça, de modo que podem ser que *não* estejam corretas caso a) eu tenha me
lembrado errado delas e/ou b) eu as tenha entendido errado "at the first place".
Correções sempre serão aceitas! E o motivo para eu fazer desta forma é bem
simples: se for para ficar pesquisando informação por informação, eu prefiro
escrever um livro ou referência; ademais, isso seria duplicação de conteúdo: pra
que replicar aqui o que você pode encontrar através de uma simples pesquisa?

List-style:

- **Convém entender a diferença entre DirectX e OpenGL.** O primeiro é um
  formato proprietário, da Microsoft, e o segundo originou-se a partir do Iris
  GL (que era proprietário), mas agora é aberto. Versões mais ou menos atuais do
  DirectX: 10, 11. E do OpenGL: 3.0, 3.1, 3.2, 3.3, 4.0, 4.1, 4.2, 4.3, 4.4. Em
  particular, o 3.3 é o mais compatível possível com hardware antigo, buscando
  acrescentar o máximo possível das novidades do 4.0. O 4.0 não é 100%
  compatível com os anteriores (outros conceitos foram acrescentados).

- **O que torna o OpenGL tão bom** é que, além de ele ser aberto, é possível que
  *graphics vendors* criem suas próprias extensões a partir dele. Extensões são
  do tipo GL_NV (nvidia), GL_ARB (da architecture board do openGL), GL_IBM. Em
      geral: GL_. (Comentário: projetos bem sucedidos permitem extensões.
      Firefox, Chromium, gedit, Eclipse etc.)

- **O OpenGL é, a princípio, apenas uma API** padrão para elementos gráficos. O
  que significa que ele é apenas uma especificação de como as funções / métodos
  etc devem funcionar. Mas ele, em si, não é implementação nenhuma. Exemplos de
  implementação no Linux: **Mesa** (atualmente: versão 9, 10), nvidia
  proprietary drivers (versão 300 e pouco), nouveau (nvidia open source drivers)
  e flgrx AMD catalyst driver.

- **O OpenGL é uma abstração que diz como converter geometria em objeto**.
  Suporta 3D e 2D. As placas gráficas / de vídeo possuem uma facilidade enorme
  em realizar operações com ponto flutuante (inclusive de 4 em 4 ~coordenadas).
  Elas também possuem uma grande quantidade de cores, admitindo processamento
  paralelo.

- **O OpenGL não especifica** como obter entrada do usuário, reproduzir áudio ou
  controlar janelas (por exemplo, do Windows ou do Xorg). Isso tem que ser feito
  através de bibliotecas externas. Um exemplo para controlar janelas: FreeGLUT.

- **O GLEW** é uma forma fácil de tornar programas OpenGL cross-plataforma, pois
  ele dá um "probe" no sistema para detectar quais extensões OpenGL ele suporta
  (e, portanto, quais podem ser carregadas e utilizadas). Em particular, o
  comando **glxinfo** do Linux diz bastante informação sobre essas extensões;
  mais do que isso, também diz quais implementações de OpenGL estão disponíveis.
  Faça `glxinfo | grep OpenGL` e seja feliz.

- Para testar o seu OpenGL e sua frame rate, instale a biblioteca mesa-demos (no
  Arch Linux e no Ubuntu são assim; o nome pode variar de distro para distro) e
  rode o progrma **glxgears**. Outro .programa útil: **glxgears_pixmap**. De 5
  em 5s você vê o seu frame rate.

- **Vsync** é sincronização vertical, com o monitor, geralmente de 60Hz. Visa
  evitar **tearing**. Você pode desabilitá-lo facilmente através do "Nvidia X
  Server Settings" ou do `~/.drirc`; veja
  [https://wiki.archlinux.org/index.php/Intel_Graphics](https://wiki.archlinux.org/index.php/Intel_Graphics).

- Você pode **programar em OpenGL** através de diversos **language bindings**. O
  mais popular, até onde sei, é através de C/C++. **gcc** é um ótimo compilador.
  Lembrar de utilizar flags para indicar as bibliotecas OpenGL (exemplo:
  `-lGLEW`).

- Uma boa IDE para editar OpenGL é o **Qt Creator**. Em particular, o Emacs
  também é bastante bom (para qualquer coisa de propósito geral, inclusive
  isso).

- **Para um programa OpenGL poder rodar**, a primeira coisa de que ele precisa é
  estabelecer um **contexto**, o que significa preparar o ambiente para ele.
  Depois de estabelecido um contexto com sucesso, o programador pode começar a
  executar comandos OpenGL.

- **Quem regula as especificações do OpenGL**: SGI (comitê) e ARB (architecture
  board).

- GLSL: GL shading language. Isso é algo grande, ainda preciso pesquisar melhor.

- WebGL: OpenGL embedado em web browsers!

- **Double Buffer / Swap Buffers**. {front buffer, back buffer}

- **Handle**: referência abstrata a uma janela, widget, etc. Uma espécie de
  ponteiro mais avançado. Exemplo: window handle.

- Conceito de **ViewPort** de uma scene

- **Software Pipeline**: application layer = criar windows, threads, etc
  (exemplo: Xorg). Abstraction layer = OpenGL API (por exemplo!). Depois disso
  vem o driver de vídeo da placa de vídeo, e a placa de vídeo em si.

Isso é só o começo. Esse post poderá ou não ter uma continuação mais tarde.

