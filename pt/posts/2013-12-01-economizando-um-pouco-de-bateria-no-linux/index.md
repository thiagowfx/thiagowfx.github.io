
Bateria = paranoia. Não parece correto, do ponto de vista de um usuário [e] no
que diz respeito a design, que ele fique se preocupando excessivamente com a
taxa de bateria que seus dispositivos consomem. Mas, pelo menos em 2013, essa
realidade ainda está distante de ser mudada, ao menos no que diz respeito a
smartphones, tablets e laptops (futuros usuários de smart watches talvez não
tenham esse problema...). Eu sou obrigado a dizer que usuários de Mac
**talvez** não tenham esse problema (*shame on me* por mencionar a Apple no
primeiro parágrafo). Eu não posso garantir, mas aparentemente esses
dispositivos têm um quê de especial no que diz respeito a bateria. Pelo menos
o [Jeff](http://www.codinghorror.com/blog/2013/10/why-does-windows-have-terrible-battery-life.html) (do
Stack Overflow) confirma isso.

Não espere um tutorial explícito: aqui eu vou apenas descrever algumas coisas
que eu fiz/faço para economizar um pouco das minhas baterias. Elas são 100%
corretas? Não necessariamente (podem até ser que gastem mais bateria do que o
normal, mas eu espero que não =P). Elas são seguras? Depende do quanto você é
disposto a se arriscar. Na hora do apelo, "não mexa em algo que já está
funcionando". No final das contas, podem simplesmente fazer parte de um efeito
placebo. A intuição humana é algo em que não se pode confiar. A única forma de
realmente garantir que essas coisas funcionam é através de medidas e/ou de uma
avaliação específica. Muito bem, agora que você já leu esse *disclaimer*,
continue a ler se achou que essas firulas são para você.

## Baterias, então

A melhor forma que eu conheço de medir quais processos gastam mais energia por
unidade de tempo no Linux é com o utilitário **powertop**, da Intel. É bem
provável que a sua distribuição o tenha em seus repositórios oficiais. No Arch,
ele está no repositório community.

Para rodá-lo: *sudo powertop*. Se você quiser ver as medições mais
rapidamente, `sudo powertop --time=1` pode ser mais útil. Se algo
estiver consumindo mais de 1W, provavelmente pode ser eliminado. Exceto
o touchpad / teclado e a tela, é claro. A tela é o que mais gasta,
em geral. A minha fica entre 1.2 W e 3W, dependendo do nível de brilho
(às vezes salta pra 4W). Sinto-me confortável com 50~70%, então gasto
algo próximo a 2W, em média.

Recentemente notei que a minha webcam estava gastando mais de 1W. E isso é
péssimo, porque eu sequer a estava utilizando. Quando eu a utilizo (digamos,
através do aplicativo **cheese** do gnome), gasto mais de 3–4 W. Pelo Google
Hangouts imagino que seja algo em torno disso, talvez até um pouco mais, por ser
no browser.

Então resolvi não carregar mais o módulo do kernel da câmera. Criei o arquivo
`/etc/modprobe.d/blacklist.conf`, e adicionei a seguinte linha a ele:

```
blacklist uvcvideo
```

Para desativar esse módulo enquanto o sistema está sendo executado, `sudo rmmod uvcvideo`.
Se você tomar uma mensagem de erro dizendo que o módulo está em uso,
um `sudo rmmod -f uvcvideo` pode bastar (f = force).

Para reativar o módulo, `sudo modprobe uvcvideo`. Você pode ler mais  no [Ask
Ubuntu](http://askubuntu.com/questions/166809/how-can-i-disable-my-webcam).

Outra coisa que pode gastar bastante bateria: o **conky**! Nesse caso, basta
aumentar o intervalo de update (coloquei 5s). Quando estava com 1s, gastava ~1W.

Mais que isso, para um usuário típico, talvez jogos ou efeitos de desktop podem
consumir uma bateria razoável. O Flash Player (via Chromium / Pepper engine)
também consome. Não parei para medir o quanto o Unity gasta, mas acredito que
ele consuma algo razoável.  Não preciso dizer que máquinas virtuais também comem
muita bateria, certo? Afinal, são dois sistemas rodando em uma única máquina.

Dependendo do window manager / desktop environment escolhido, a bateria também
pode ser afetada. O KDE e o GNOME gastam mais, por carregarem mais recursos e
bibliotecas. O XFCE, LXDE, Fluxbox, Openbox, EDE, dentre muitos outros, são mais
leves.

Algo que pode ser útil (não acho tanto assim, mas "vai que"): utilizar algum
*daemon* ou programa para controlar o tempo em que o laptop vai se suspender
automaticamente ou hibernar, quando inativo por determinado tempo.

Também posso dizer que um SSD consome menos bateria do que o HDD. Não tenho
benchmarking para isso, no entanto. O quanto faz diferença? Talvez o site da
Phronix contenha alguma informação do tipo.

No fim das contas: o que é util? Depende do quanto você vai sacrificar *features* por economia de bateria.
Certamente rodar um window manager com menos de 1000 linhas de código (existem vários do tipo por aí! Veja
[https://wiki.archlinux.org/index.php/Window_manager](https://wiki.archlinux.org/index.php/Window_manager))
vai ajudar. Não utilizar *compositing effects* no desktop também.

Termino deixando o output do meu **powertop**. Esse post foi genérico, até
porque não dá para ser específico. Cada um tem o seu dispositivo e ambiente. Eu
posso cancelar as coisas que gastam mais energia no meu ambiente através do **meu**
output; mas o seu provavelmente é diferente. Então, só posso recomendar a
utilização do bom senso, e apenas cancelar os programas / processos que
realmente não forem tão relevantes assim.

