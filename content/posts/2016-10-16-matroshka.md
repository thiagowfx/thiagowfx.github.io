---
title: Matroshka
date: 2016-10-16T15:49:01-02:00
tags:
  - dev
  - pt
---

Recentemente participei de uma
[CTF](https://ctf.tecland.com.br/Pwn2Win/game/scoreboard/) promovida pelo
[ELT](https://ctf-br.org/elt) (Epic Leet Team). Uma das *challs* que consegui
resolver completamente foi a **matroshka**, e aqui está um breve *write-up*
sobre a mesma.

Dado um arquivo `matroshka.tar.gz`, precisávamos encontrar a *flag*.

Não era difícil desconfiar do que esse arquivo / *chall* se tratava: matroshkas
são aquelas bonecas russas que se encaixam umas dentro das outras. Então...de
cara, logo já desconfiei: provavelmente existe um arquivo compactado dentro de
outro, dentro de outro, dentro de outro, e assim por diante...

Por experiência, não valeria a pena tentar descompactar tudo manualmente, pois
sabe-se lá quantos níveis de compactação esse negócio iria ter (provavelmente
mais do que 100).

De cara logo pensei em usar o [dtrx](https://brettcsmith.org/2007/dtrx/), que é
um excelente programa (não perco tempo e sempre rodo um `port install dtrx`)
para extrair arquivos sem ter que ficar se lembrando das sintaxes individuais de
cada programa. Nesse caso, não iria rolar: os arquivos eram renomeados de forma
a *trickear* o dtrx, que funciona através de heurísticas, uma delas é a
'extensão' do nome do arquivo. Por exemplo, vários arquivos (após
descompactados) eram renomeados na forma `*.elt`.

A segunda alternativa foi (**serendipidade**, não conhecia essa ferramenta
antes) tentar utilizar o [atool](http://www.nongnu.org/atool/). Por motivos
similares ao `dtrx`, não rolou.

Pois bem, então o jeito ia ser descompactar tudo na marra. Pensei em escrever um
programa que faria o seguinte:

```cpp
try {
	unzip <file>
}
catch {
	try {
		tar xf <file>
	}
	catch {
		// ...e assim por diante
	}
}
```

Obviamente eu utilizaria os programas diretamente, então a coisa poderia ficar
um pouco mais simples, utilizando os return codes dos mesmos para detectar se
descompactaram o arquivo com sucesso. Por exemplo, `tar xf <file>` retorna `0`
se rodou corretamente, do contrário ele retorna algo diferente de zero. Isso se
mostrou válido para todos os programas de descompactação que utilizei, exceto o
lha, que insistia em retornar `0` de qualquer jeito, mesmo quando falhava.

Para automatizar essa tarefa, resolvi utilizar `python2`. `C/C++` provavelmente
também seriam bons candidatos, mas eu queria praticar o meu `python`.

Após algumas inspeções, notei que cada arquivo continha um e somente um arquivo
dentro dele, então a ideia base seria:

* mantenha uma lista com todos os arquivos conhecidos até então (no começo, só
  haveria um);
* descompacte esse arquivo;
* detecte qual arquivo acabou de ser descompactado
* continue fazendo isso até encontrar a `flag`

Meu código ficou assim:

```python
#!/usr/bin/env python

import os
import subprocess

TARGET_DIR = 'mat'

def uncompress_kgb(file):
    return subprocess.call(["kgb", file])

def uncompress_gzip(file):
    return subprocess.call(["gunzip", "-S", '.' + file.split('.')[-1], file])

def uncompress_tar(file):
    return subprocess.call(["tar", "xvf", file])

def uncompress_rar(file):
    return subprocess.call(["unrar", "x", file])

def uncompress_lha(file):
    return subprocess.call(["lha", "e", file])

def uncompress_zip(file):
    return subprocess.call(["unzip", file])

def uncompress_arj(file):
    subprocess.call(["cp", file, file + ".arj"])
    err = subprocess.call(["arj", "x", file])
    subprocess.call(["rm", file + ".arj"])
    return err

def uncompress_7z(file):
    subprocess.call(["7z", "x", file])

def colorprint(s):
    print '\033[93m' + repr(s) + '\033[0m'

os.chdir(TARGET_DIR)

base = set()

while True:
    newbase = set(os.listdir('.'))

    diff = newbase - base
    colorprint(diff)

    if len(diff) > 1:
        raise Exception("len(diff) > 1")
    elif len(diff) == 0:
        print "len(diff) == 0"
        break

    for file in diff:
        err = uncompress_kgb(file)
        if err != 0:
            err = uncompress_gzip(file)
            if err != 0:
                err = uncompress_tar(file)
                if err != 0:
                    err = uncompress_rar(file)
                    if err != 0:
                        err = uncompress_zip(file)
                        if err != 0:
                            err = uncompress_arj(file)
                            if err != 0:
                                err = uncompress_7z(file)
                                if err != 0:
                                    err = uncompress_lha(file)
                                    if err != 0:
                                        print "lha fail"

    base = newbase
```

Essa ideia funcionou bastante bem. A única coisa *overkill* foi que eu não
deletei arquivos anteriores; isso poderia ter simplificado significativamente o
problema (e os *sets* no python).

Ademais, uma das coisas chatas do `arj` é que ele só é capaz de extrair arquivos
que terminam em `*.arj`, então fui obrigado a renomear/copiar um arquivo antes
de tentar utilizá-lo para extrair seu conteúdo.
