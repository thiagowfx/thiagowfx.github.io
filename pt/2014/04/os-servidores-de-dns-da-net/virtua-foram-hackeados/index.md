
Se você é usuário da NET, tome MUITO CUIDADO se, ao digitar um link no seu
navegador predileto, você se deparar com uma página falsa do Flash Player. **NÃO
CLIQUE EM NADA!!**

Isso não acontece só para o site do facebook, acontece para outros sites também.
Mas não acontece para todas as páginas. No meu caso, quando não acontece para
algumas páginas, é porque o servidor de DNS utilizado para consulta é algum
outro.

O motivo dessa página estar aparecendo é que **o DNS da Net foi hackeado**.

O servidor 201.6.4.116 é um dos servidores DNS da Net, e o 8.8.8.8 (assim como o
8.8.4.4) são servidores DNS do Google. Se fizermos uma consulta de DNS no
domínio `www.google.com` com o servidor de DNS da Net, e depois com o servidor
de DNS do Google, vemos que esses dois resultados são diferentes. Motivo? **A
DROGA DO SERVIDOR DE DNS DA NET FOI HACKEADO!!!**

Notem que o servidor 206.190.150.21 (que o servidor de DNS da Net diz ser o
endereço do Google) é, justamente, o servidor de origem daquele arquivo .zip
malicioso.

## Recomendação

Em primeiro lugar, se você ver a página acima do Flash Player, **feche-a
imediatamente, NÃO CLIQUE EM NADA!!**

Segundo, mude os seus servidores de DNS para os do Google (8.8.4.4) e (8.8.8.8)
o mais rápido possível, e então reinicie o seu computador (reiniciar a rede
basta, mas só para garantir).

### Linux (NetworkManager)

Supondo que você usa NetworkManager (provavelmente, é o default do Ubuntu se não
me engano), crie um arquivo
`/etc/NetworkManager/dispatcher.d/use-my-custom-dns.sh`:

```shell
#!/bin/bash
cp -f /etc/resolv.conf.custom /etc/resolv.conf
```

E depois crie outro arquivo `/etc/resolv.conf.custom`:

```shell
# Google's DNS
nameserver 8.8.8.8
nameserver 8.8.4.4
```

E então reinicie o NetworkManager (se você não sabe como fazer isso, a melhor
forma é reiniciando o computador).

Ao reiniciá-lo, verifique o conteúdo do arquivo `/etc/resolv.conf`. Ele deve ser
exatamente igual ao `/etc/resolv.conf.custom` anterior que criamos.

### Outros sistemas operacionais

Se você for usuário Windows, pesquise como fazer isso.

Se tudo estiver OK, eu recomendaria que vocês deletassem a cache (e tudo o mais)
dos seus navegadores, e então **provavelmente** vocês estarão seguros. Pelo
menos enquanto o DNS do Google não for hackeado também...

**Update**: Se você for usuário do Chromium/Chrome, além de mudar o seu DNS e
deletar a sua sessão (Ctrl + Shift + Delete), assegure-se de que a URL
`chrome://net-internals/#dns` esteja OK. Na dúvida, clique em "Clear host
cache".

