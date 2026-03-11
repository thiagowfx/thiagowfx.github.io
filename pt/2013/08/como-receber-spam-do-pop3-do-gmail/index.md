
O leitor não precisa se assustar com o título do post, é isso mesmo que você
leu.

Se você possui múltiplas contas do gmail e redireciona todas elas para uma única
conta **master** via **POP3**, provavelmente os e-mails que são marcados como
spam nas outras contas **não** são recebidos pela conta master (não
automaticamente).

Recentemente eu notei isso, pois deixei de receber um e-mail importante da
plataforma da minha universidade (SIGA, para os mais chegados) justamente porque
ele foi marcado como spam.

Aqui está o que você pode fazer para receber os spams:

1 - Logue na conta que você vai reconfigurar para encaminhar os spams para a sua
conta master.

2 - Vá criar um filtro. Se você usa o gmail deveria saber fazer isso...

3 - Faça como na imagem abaixo, adicionando "is:spam" no campo correto, depois
continue para "Criar filtro com essa pesquisa"

4 - Agora adicione um endereço de e-mail de encaminhamento (ou escolha um, caso
já o tenha feito). Depois marque as opções abaixo e aplique o filtro.

5 - Como garantir que isso funciona? Você precisará de um e-mail externo. Sugiro
enviar um e-mail para a conta que acabou de ser configurada com o
[seguinte](http://spamassassin.apache.org/gtube/gtube.txt) conteúdo.
[Esse](http://www.emailspamtest.com/index.aspx) website acusa esse conteúdo como
spam.

Bom, sendo os filtros de spam do gmail inteligentes o suficiente, dessa maneira
é bem provável que o spam encaminhado agora caia novamente na sua caixa de spam,
mas dessa vez finalmente na da sua conta master.

Essa é uma maneira de juntar todos os seus spams em uma única caixa de spam. Vai
que aparece um e-mail importante, falso positivo, por lá...

Fonte inicial: [http://hints.macworld.com/article.php?story=20071024104204246](http://hints.macworld.com/article.php?story=20071024104204246)

