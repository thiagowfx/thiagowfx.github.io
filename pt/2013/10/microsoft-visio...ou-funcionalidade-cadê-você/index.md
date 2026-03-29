
Recentemente tive que trabalhar com um pouquinho de
[UML](http://en.wikipedia.org/wiki/UML). A verdade é que UML parece meio *old
school* hoje em dia, aparentemente existem algumas formas melhores de modelar e
abstrair problemas do que ela. Mas acho que ainda tem a sua importância.
Principalmente **didática**, em linguagens que suportam
[OOP](http://en.wikipedia.org/wiki/Object-oriented_programming). (PS.: Se você é
da área de TI e não sabe o que é UML, recomendo fortemente aprender algo sobre!)

Meu primeiro post mais resumido; ficando legal vou passar a economizar mais
palavras e tempo nas próximas vezes. Especialmente no *journal*. O problema de
escrever pouco é que sempre fica uma sensação de informação incompleta. Deixa
isso para as mídias / a imprensa, elas já fazem isso muito bem. Não é meu
objetivo mostrar apenas um lado da moeda.

Anyway. Existem várias ferramentas (*softwares*) para modelar UML. Algumas open
source / FOSS e outras proprietárias. Exemplo de open source:
[Dia](https://projects.gnome.org/dia/) (bastante elegante e KISS, pena que meio
descontinuado). Proprietária? [Microsoft
Visio](http://office.microsoft.com/en-us/visio/). Também existe uma ferramenta
chamada [papel](http://en.wikipedia.org/wiki/Paper) (ou quadro negro, o leitor é
quem sabe) que faz isso perfeitamente.

Eu comecei o meu trabalho com uma outra ferramenta open source, porque o Dia era
KISS até demais para meus propósitos. E essa ferramenta se mostrou bastante boa.
Beleza. Mas eu, sempre curioso em testar novas ferramentas, resolvi usar a
oportunidade para testar o Visio.

Eu instalei o Visio 2010. Legal. Parecia razoável. Nada extravagante. Com uma
ênfase um pouco desnecessária nos efeitos e no design da coisa. Mas é ótimo para
impressionar e incluir em slides, por exemplo. Não achei tãaaao bom (custo de
tempo / benefício de visualizar bem) para modelar, mas ele é realmente ótimo
para incluir em apresentações ou páginas por aí.

Mas então, estamos em 2013...resolvi testar o Visio 2013. Suuuuper pesado. Aiai.
KISS, cadê você? Mas tá bom. Pensei que valeria a pena ocupar um pouquinho mais
de espaço extra em disco e comer um pouquinho mais de RAM, e CPU, renderizar
direito a coisa. Desde que obtivesse compensações, certo?

**MAS NÃO**. O Visio 2013 se mostrou com uma redução de funcionalidades. Os
efeitos cresceram. Mas a funcionalidade sumiu. Naturalmente, me refiro ao UML.
Não testei as outras coisas, não posso afirmar nada sobre elas. Mas veja isso:

- Visio 2003: eu não testei, mas li no Stack Overflow (não guardei o link,
  *sorry*)  que ele permitia *code generation* a partir de um diagrama de
  classes. Wow, legal né? Boa parte dos softwares FOSS que eu achei fazem isso
  (inclusive o dia, com um programa escrito em python chamado `dia2code`).

- Visio 2010: bom, disse que testei. Ele **não** tem mais esse recurso.
  Inclusive [as pessoas costumam dizer que isso não é lá uma boa
  prática](http://stackoverflow.com/questions/2015893/create-c-code-from-visio-uml-diagram).
  Mas acho útil para quem é iniciante. Precisava ter removido essa
  funcionalidade tão boa? Quase todos os outros softwares têm isso. Posso
  enumerar: StarUML, ArgoUML, Umbrello. Lamentável.

- Visio 2013: não, não incluíram de novo o *code generation*. Mas sabe o que me
  deixa chateado? Tiraram mais funcionalidade ainda do UML. No 2010 tinha um
  recurso chamado *model explorer*, era uma forma de visualizar melhor e, até
  mesmo, de editar melhor os atributos e os métodos das classes. Não tem mais no
  2013. (Disclaimer: se tiver, o recurso está bem escondido da interface do
  usuário e eu não consegui encontrar através de pesquisas rápidas no Google. O
  que quer dizer, **na prática**, que não tem. Mas acho que esse recurso não
  existe mais mesmo.)

Ou seja, alguém por favor me diga o que o time desenvolvedor do Visio tem na
cabeça. Removendo cada vez mais funcionalidades ao longo do tempo para
acrescentar efeitos e mais efeitos? Não quero beleza, quero poder modelar
direito.

