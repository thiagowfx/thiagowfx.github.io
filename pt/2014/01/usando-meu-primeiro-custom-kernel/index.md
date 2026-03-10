
Faz 2 dias que venho testando o Kernel
[Linux-ck](https://wiki.archlinux.org/index.php/Linux-ck), cuja diferença em
relação ao kernel mainline é basicamente a aplicação de um conjunto de patches
("ck"), os quais [Con Kolivas](https://en.wikipedia.org/wiki/Con_Kolivas)
mantêm, e o [Brainfuck
Scheduler](https://en.wikipedia.org/wiki/Brain_Fuck_Scheduler) (BFS), o qual
aparentemente é uma boa escolha para um desktop / notebook com poucos cores
(isto é, se você tiver mais de 4096 cores, por favor *não* utilize o BFS – é
sério, eu li isso em algum lugar. Se sua CPU *só* tiver 128 cores, pode usar!).
No Arch, a facilidade de utilizar / compilar um kernel customizado é enorme, já
que ele te dá toda a flexibilidade para isso (no Gentoo também, pra não dizer
que eu só falo do Arch =P). Além do mais, existe um repositório com o kernel já
compilado para diferentes arquiteturas, conhecido como
[repo-ck](https://wiki.archlinux.org/index.php/Repo-ck), mantido pelo usuário
*graysky* da comunidade do Arch.

OK, e por que utilizar um custom kernel? *Por nada*, só por hobby mesmo, talvez
pelo mesmo motivo de testar uma nova ROM para Android. Bom, diz-se por aí que
você pode ter um desempenho ligeiramente maior (mas nada *super* notável) se
utilizar o linux-ck satisfazendo algumas condições: alguns stats podem ser
vistos [aqui](http://repo-ck.com/stats.pdf) (na verdade, esses stats são apenas
*trivia* dos usuários de linux-ck, não tem nada de desempenho lá, pelo menos
não até hoje). [Esses](http://repo-ck.com/bench/cpu_schedulers_compared.pdf)
são os stats de desempenho.

Da Wiki do Arch,

> A major benefit of using the BFS is increased responsiveness. The benefits
> however, are not limited to desktop feel. Graysky put together some
> non-responsiveness based benchmarks to compare it to the CFS contained in the
> "stock" linux kernel. Seven different machines were used to see if
> differences exist and, to what degree they scale using performance based
> metrics. Again, these end-points were never factors in the primary design
> goals of the bfs. Results were encouraging.
>
> Many Archers elect to use this package for the BFS' excellent desktop
> interactivity and responsiveness under any load situation. Additionally, the
> bfs imparts performance gains beyond interactivity.

É isso. Por sinal, se você quiser instalar o kernel ck para se divertir um
pouquinho, siga as instruções do repo ck (link acima). O processo deve ser
bastante *straightforward* maaaaas, qualquer dúvida pergunta aí.

