
Uma vez que você se acostuma com **package managers** no Linux, é bastante inconveniente voltar à vibe de ficar instalando programa por programa no Windows, clicando em 'next' o tempo todo.

Para resolver isso foi criado o [chocolatey](http://chocolatey.org/), um repositório com vários pacotes para o Windows, descrevendo-o a grosso modo.

Eu o uso há bastante tempo, para falar a verdade. Só que agora me apareceu um novo problema: como reproduzir a mesma instalação em vários computadores diferentes, de uma vez só?

Motivado por isso, criei um repositório com o sugestivo nome de [windows-setups-nevermore](https://github.com/thiagowfx/windows-setups-nevermore). As instruções estão no arquivo README. Resumidamente, basta você especificar todos os pacotes que você quer em um arquivo chamado `packages.config`, depois executar o arquivo `setup.cmd`. E voilà, em poucos minutos todos os seus programas serão **automagicamente** instalados, adicionados ao PATH e ao menu iniciar.

Naturalmente isso se limita, *a priori*, somente aos pacotes na galeria/catálogo do chocolatey. Se o pacote que você quiser não estiver lá, você terá que adicioná-lo sozinho, ou instalá-lo manualmente, o que for preferível. Além do mais, só estão lá os programas cujas licenças admitem que eles sejam redistribuídos (você não vai encontrar o Microsoft Office lá, por exemplo).

**Update (2014-07-07):** esse método provavelmente não instala bloatware -- por exemplo, as diversas barras de ferramentas ou outros plug-ins para seus web browsers. No entanto, a melhor forma de comprovar isso é ou analisando o código-fonte do pacote ou instalando-o.

