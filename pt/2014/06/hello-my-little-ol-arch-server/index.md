---
title: "Hello, my little ol' Arch Server"
url: https://perrotta.dev/pt/2014/06/hello-my-little-ol-arch-server/
last_updated: 2026-03-07
---


Durante os últimos dias venho brincando um pouco com configurações de
servidores. Não é a parte mais prazerosa de se administrar ou programar um
sistema, admito. Mas tem lá seus méritos.

Bem, eis alguns pedaços de conhecimento registrados aqui.

**Vanilla vs Patched**: você talvez se lembre de que uma vez eu inventei de
instalar ubuntu, centos, apache e opensuse, e aquilo era mais para ter uma visão
"big picture" da coisa. Atualmente estou testando configurações apenas no arch e
no debian, e são dois sistemas suficientemente diferentes porém que se completam
para que eu não precise testar em mais nenhum. A questão principal aqui é: no
Arch, os pacotes são minimamente alterados (usualmente, não são alterados); isto
é, eles são empacotados da mesma forma que **upstream** quer que esteja. Isso é
muito bom para você aprender como as coisas funcionam de maneira pura, e também
para perceber como várias distros tentam resolver várias coisas por você; às
vezes isso é bom, às vezes isso é ruim; no entanto, é melhor você se expor aos
problemas para entender como eles funcionam, na minha visão.

...percebemos que no debian tudo isso já funciona out-of-the-box (isto é, o
Apache já vem pré-configurado); enquanto que, no Arch, é necessário fazer umas
pequenas configurações (10 minutos se você quiser tentar entendê-las sem nunca
tê-las feito; 2 minutos se já sabe o que fazer), coisa de descomentar algumas
linhas ou acrescentar outras. Isso não é feito às escuras, tudo é muito bem
documentado na ArchWiki, para a qual eu tenho o orgulho de contribuir.

Outra diferença é em relação à localização padrão do DocumentRoot: no Arch
(logo, upstream) é `/srv/http`, no debian era (se não me engano) `/var/www`, e
no XAMPP é em `/opt/lampp/htdocs`. Nenhum padrão, isso dá dor de cabeça às
vezes.

Também estou realizando alguns testes com o nginx. Minha conclusão é que o nginx
é bem mais KISS do que o apache (e alguns dizem que ele é mais rápido também).
De fato, ele parece ser mais confortável de se trabalhar. Porém, ainda estou
tendo um pouco de dor de cabeça para integrá-lo com o PHP, através de FastCGI e
php-fpm. Provavelmente deixei escapar algum detalhe, alguma linha de
configuração, mas estou quase lá.

Outro aspecto legal é o PHPMyAdmin. Não é nada mal poder configurar todas as
suas tabelas de MySQL (ou MariaDB, se estiver no Arch, tecnologia iuhul) através
de uma interface intuitiva. O PhpMyAdmin vem pré-configurado tanto no Arch
quanto no Debian, o que me diz que ele realmente foi feito para facilitar a vida
de um administrador de sistemas.

Por outro lado, não achei absolutamente difícil utilizar a linha de comando do
mysql / mariadb. Pela pouca experiência que tenho hoje com MySQL, mas somada com
a minha boa experiência com linha de comando em geral, posso dizer que a
interface CLI do MySQL/MariaDB é bastante intuitiva. O problema é que você
precisa saber o que está fazendo (isso não é um problema, é?), precisa saber a
sintaxe dos comandos e tudo o mais, coisa que não é tão essencial no PhpMyAdmin.
Mas, ainda assim, não tem nada demais, só questão de se acostumar mesmo.

Apesar de toda a vibe e estabilidade do MySQL, estou considerando seriamente em
utilizar alguma tecnologia NoSQL para um futuro projeto. Acredito que sua
flexiblidade combine mais com meu modo de pensar do que o do MysQL, mas, cada
tecnologia possui seus méritos, tirarei minhas próprias conclusões acerca disso
no futuro.

Conectar o PHP com o MySQL é bastante fácil. Só questão de descomentar o módulo
correto no /etc/php/php.ini. Por sinal, tem bastantes módulos interessantes por
lá.

Vejamos…ah sim, usuários e permissões; é bom tomar bastante cuidado com isso! É
um assunto que pode dar dor de cabeça. Cada distro tem seus próprios usuários
para a web, e seus próprios conjuntos de permissões para que tudo funcione
corretamente (e para que o seu sistema não fique tão exposto para o mundo).
Posso dizer que se você não usar o chmod, chgrp ou chown sem querer, e deixar os
defaults quietos, provavelmente tudo vai correr bem. Isso assume que você não
vai fazer nada de anormal, o que…bem, pode nem sempre ser verdadeiro.

Mais uma coisa: use senhas seguras! Isso pode evitar dores de cabeça no futuro.
Por outro lado, cuidado para não utilizar senhas seguras demais e depois se
esquecer das mesmas. Se você utilizar algum software para administrá-las,
certifique-se de que a senha master dele seja ENORME, REALMENTE ENORME. E, se
possível, utilize algum método adicional para protegê-lo (2-factor auth, key,
etc).

É uma boa prática utilizar 100% da linha de comando para administrar o seu
server. Talvez com a exceção do PhpMyAdmin, eu acho que todo bom administrador
deveria saber fazer tudo pela linha de comando.

Bem, acho que até aqui isso resume parte da minha brincadeira. É claro que eu
não falei sobre uma porção de coisas, tem SSH, tem os arquivos de configuração,
tem LAMP/LEMP, tem todos os cenários mais extravagantes que você puder criar.
Mas esse é um começo. Para quem disse que ia começar a ler e estudar sobre o
assunto , sinto que estou no caminho certo e que comecei bem. Agora, o restante
desse caminho depende o que é que eu vou fazer com isso.

Até breve.

(Por sinal, o blog deve continuar congelado. Com exceção de posts como esse,
para marcar determinado badge/meta, o tempo de férias é curto, então não vou
tomá-lo para inventar posts que não precisam ser inventados)

