
Ah, sempre que eu logo no Windows acabo implicando com alguma coisa. A última da
vez foi a renderização das fontes. A renderização de fontes no Linux é muito
boa, chega aos pés (isso se não passar) da do Mac. Especialmente se você
utilizar o
[infinality](https://wiki.archlinux.org/index.php/Infinality-bundle+fonts)
([upstream](http://www.infinality.net/blog/)). Agora, a renderização do Windows
é...feia. Quando você abre o seu *browser* e vê aquela página cheia de Times
New Roman para todo o lado...errrrgh. Não estamos mais no início dos anos 2000,
algumas coisas podem melhorar.

Com um pouco de [serendipidade](https://pt.wikipedia.org/wiki/Serendipidade)
(minha palavra predileta nos últimos tempos), encontrei o
[MacType](https://code.google.com/p/mactype/). Esse é um projeto que promete
melhorar a renderização das fontes no Windows (do 7 para cima, por favor). Não
tem muito o que falar: instale, experimente e perceba a diferença!

Note que esse projeto é desenvolvido em japonês (bem, alguma língua oriental).
Então, em algumas partes da instalação (e mesmo na pós-instalação), pode ser que
você não veja caracteres, ou que veja caracteres em forma de quadrado. Nesse
caso, procure a opção para trocar o idioma para inglês; depois disso, é super
intuitivo.

Mais uma nota: você só precisa abrir e configurar o programa uma única vez.
Existem várias opções para salvar as opções de renderização: você pode utilizar
o registro do Windows (uma boa opção!) e um serviço do Windows (outra boa
opção). Eu optei pela segunda, não me deu dor de cabeça.  Existe também a
possibilidade de aplicar a renderização apenas para algumas janelas, acho, e
também a de controlar as opções pelo system tray. Não há necessidade disso,
convenhamos; ou você utiliza em todos os lugares, ou não utiliza: seja
consistente. Note que se você escolher a opção de registro, a renderização só
terá efeito após a reinicialização do computador.

Finalmente, uma **mini review**: achei a nova renderização muito boa. Dá até
gosto de ficar lendo. Aproxima-se relativamente bem da qualidade de renderização
do Linux (ou, do Mac, que é o que o nome do projeto sugere). Notei que o mactype
    está disponível no [chocolatey](http://chocolatey.org/packages/mactype) (é
    uma pena que eu só tenha visto isso depois que o instalei manualmente),
    então, se quiser automatizar o processo:

```
cinst mactype
```

