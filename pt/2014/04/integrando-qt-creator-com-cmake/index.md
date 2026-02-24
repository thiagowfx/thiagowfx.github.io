
**TL;DR**: movendo o estilo de desenvolvimento de Emacs + programa na linha de
comando para QT Creator + programa com interface gráfica (em...QT, é claro!).

Existem basicamente duas etapas para realizar essa transição. A primeira é tão
ridiculamente fácil, que nem precisaria ficar registrada aqui. Apesar disso, não
parece ser tão trivial ou que vá funcionar *out-of-the-box*, então vou
documentá-la aqui assim mesmo.

Já a segunda requer um pouco de entendimento sobre como o **cmake** e o **qmake**
(ferramenta de gerenciamento de compilação utilizada por*default* por um projeto
do QT Creator) funcionam.

- OBS.: QT5. Mas, você também pode aplicar o que está escrito aqui para QT4. Com
  alguns cuidados.

## Primeira etapa

1-) Assegure-se de que o seu projeto em cmake funciona corretamente. A estrutura
atual dele deverá ser similar à seguinte:

- ProjectTopLevelDir/

- **ProjectTopLevelDir/CMakeLists.txt**(arquivo top-level de configuração do cmake)

- ProjectTopLevelDir/src/ (código-fonte do projeto)

- ProjectTopLevelDir/build/ (onde o projeto é compilado)

Existe uma variação comum para o caminho de *build*:

- ProjectTopLevelDir/../build/

Tanto faz a variação adotada. No entanto, ao utilizarmos o QT Creator, o *wizard*de importação de projeto nos recomendará a segunda, por*default*.

2-) Abra o QT Creator, clique em *Open File or Project*, e importe o
CMakeLists.txt indicado no item anterior. É importante importar o CMakeLists.txt
mais **top-level** do seu projeto.

3-) A pasta de build especificada pode ser a mesma que a anterior. Ou, você pode
adotar o padrão sugerido pelo *wizard*, que é algo do tipo
**ProjectTopLevelDir-build/**(a segunda variação, como eu disse anteriormente).

4-) Clique em "Run CMake". Você provavelmente irá querer o "Unix Generator
(Desktop)".

5-) Sente-se e espere a mágica acontecer. Brincadeira, não é mágica, na verdade
é um comportamento muito bem definido. O que o Qt Creator faz
*behind-the-scenes*é, basicamente, rodar o cmake para gerar um .cbp (output de
projeto para o Code::Blocks, mas que o Qt Creator sabe interpretar também --
thank you!), em vez de um usual Makefile. Esse .cbp configura o ambiente do Qt
Creator para o seu novo projeto.

6-) Clique em **Finish.**

## Segunda etapa - preliminares

Agora você vai notar que o botão de "play" (**Run**, atalho Control-R)
construirá o seu projeto corretamente e, provavelmente, também rodará o
executável correto. Isso indica o fim da primeira parte.

Se você realizar quaisquer modificações significativas no seu projeto (no que
diz respeito à estrutura dele, ou algum CMakeLists.txt), assegure-se de rodar o
CMake novamente. Você pode fazer isso clicando com o botão direito no projeto
(na sidebar da esquerda) e depois em "Run CMake".

E daí você percebe que especificar etapas em linha de comando é algo bem mais
fácil e **preciso** do que especificar etapas em uma IDE. Além do mais, daqui a
algumas versões, a interface do Qt Creator pode mudar, e o que eu acabei de
descrever aqui terá de ser reaprendido / readaptado. Use o bom senso.

Muito bem, na segunda etapa dispensaremos **completamente** a ferramenta
**qmake**, passando a utilizar somente o **cmake.**Assumiremos que você quer
criar uma interface em Qt. Se você só quiser utilizar o QT Creator, sem criar
nenhuma interface, então você pode parar na etapa 1.

## Segunda etapa - agora sim

1-) Abra o seu CMakeLists.txt top-level num editor de texto. Pode ser no próprio Qt Creator, ou não, tanto faz.

2-) Vá para o final desse arquivo. Vamos adicionar as seguintes instruções lá:

https://gist.github.com/thiagowfx/10549532

3-) Comentários:

- Note que essa é a instrução de um dos meus projetos. Toda a parte onde contém "raytracer" você deve mudar de acordo com o seu próprio projeto.

- A parte do **automoc**é essencial se você utiliza **signals e slots.**

- A parte do **wrap_ui** é essencial se você utiliza o Qt Designer para criar um arquivo .ui. Se você criou o seu código "na mão", não precisa. O que a **wrap_ui** faz é invocar o **uic**(ui compiler) do Qt nos arquivos .ui especificados. Isso é exatamente o que o **qmake** faz*behind-the-scenes*(assim como a parte do **moc**, descrita no item anterior).

- Se você utiliza *resources,*também é necessário adicionar uma instrução para isso. Ela não existe no meu exemplo. Olhe as referências no fim desse post.

- Depois de criar quaisquer executáveis, é importante linká-los com a biblioteca do Qt. É para isso que a parte **use_modules** serve.

Depois disso, o seu projeto está sendo completamente gerenciado pelo **cmake.**Sem necessidade de **qmake.**

## Referências

- Sugiro olhar o meu repositório no Github,
  [open-bookmarks](https://github.com/thiagowfx/open-bookmarks). Olha a parte
  que fala de cmake com qt5. Vou deixar uma cópia dessas referências aqui, no
  entanto, se eu adicionar quaisquer referências no futuro, elas serão
  adicionadas no repositório, e não nesse post.

**Referências:**

- [http://www.kdab.com/using-cmake-with-qt-5/](http://www.kdab.com/using-cmake-with-qt-5/)

- [https://blogs.kde.org/node/4495](https://blogs.kde.org/node/4495)

- [http://qt-project.org/doc/qt-5/cmake-manual.html](http://qt-project.org/doc/qt-5/cmake-manual.html)

- [http://www.itk.org/pipermail/insight-users/2009-October/032974.html](http://www.itk.org/pipermail/insight-users/2009-October/032974.html)

- [http://www.executionunit.com/blog/2014/01/22/moving-from-qmake-to-cmake/](http://www.executionunit.com/blog/2014/01/22/moving-from-qmake-to-cmake/)

