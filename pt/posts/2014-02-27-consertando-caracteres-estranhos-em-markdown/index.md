
Ao converter um documento para Markdown com a sua _engine_ preferida, se você se
deparar com caracteres estranhos, do tipo:

> histÃ³ria de um programador e sua (possÃ­vel) evoluÃ§Ã£o Ã© recomendado para
> quem estÃ¡ da computaÃ§Ã£o

É bastante fácil resolver isso: o problema é em relação ao _encoding /_ à
codificação do seu documento. Basta forçar o UTF-8, com a seguinte tag (pode
colocar no início do seu documento, por exemplo):

```html
<meta http-equiv='Content-Type' content='text/html; charset=utf-8' />
```

Originalmente extraído do Stack Overflow (novidade...). Durante muito tempo
fiquei com esse problema, deixando de usar Markdown por causa disso...não mais
=P

