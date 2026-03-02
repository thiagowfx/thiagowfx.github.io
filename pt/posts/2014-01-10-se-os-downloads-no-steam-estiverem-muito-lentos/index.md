
Faz pelo menos mais de 2 semanas que eu estou baixando o Left 4 Dead 2 a meros
10 KB/s, com eventuais picos de 60 KB/s no Steam. Isso me lembra da minha
velocidade *banda larga* de 2009... 5 anos, nem parece. Agora a minha velocidade
de download atual é de ~800-1100 KB/s.

Eis algumas coisas que você pode tentar fazer se a sua velocidade no Steam for
lenta:

- Mudar o seu plano de banda larga! Ou, mudar de ISP logo...

- Mudar o mirror do Steam. Em geral, Steam > Settings > Downloads > Download
  Region.

- Mudar o seu DNS! Procure DNS do Google ou DNS do OpenDNS. Com um pouco mais de
  trabalho, utilizar um programa como o
  [dnsmasq](https://en.wikipedia.org/wiki/Dnsmasq).

Para mim a solução que deu certo foi a terceira. Na verdade, como eu posso
confirmar que foi realmente ela que deu certo? Bom, eu estava há 3 semanas com a
mesma velocidade horrível, mas logo quando a apliquei a minha velocidade voltou
ao normal. Realmente acho que pro meu caso mudar o DNS e/ou usar o `dnsmasq`
valeram a pena. Qual dessas duas medidas influenciou mais eu já não sei.

No Linux, para ver os seus servidores de DNS atuais, use:

```shell
less /etc/resolv.conf
```

