---
title: Scilab Notes (HOWTO)
date: 2014-03-07T17:09:30-03:00
tags:
  - dev
  - legacy
---

Resumo sobre como utilizar o Scilab. Objetivo: matrizes, equações lineares e,
mais geralmente, álgebra linear (computacional, ou não). A motivação para essas
notas são basicamente a) resumo pessoal e b) estudar para uma prova.

Essas notas não tendem a ser extensivas. Na verdade, estou colocando aqui
apenas as coisas que parecem ser mais importantes / úteis, e que eu
provavelmente possa precisar uma vez ou outra. O Scilab é um ambiente
full-featured, bem mais rico e complexo do que esse resumo pareça demonstrar
(por exemplo, não estou cobrindo nada de programação, nem de Cálculo, aqui). É
realmente impressionante. Eu já o tinha usado uma vez mas, agora que passo
novamente por ele, percebo o quão completo ele é.

Essas notas estão licenciadas sob a Creative Commons BY-NC-SA (assim como todo
o conteúdo desse blog, até hoje), o que significa que você pode compartilhá-las
à vontade, desde que não faça uso comercial das mesmas; além disso, você pode
criar derivados a partir delas, desde que os distribuam sob a mesma licença.
OK, agora vamos ao trabalho.

**Se você quiser aprimorar esse trabalho (por exemplo, indicando algum erro, ou
acrescentando mais alguma coisa), por favor deixe um comentário ou me mande uma
mensagem para que eu inclua mais itens aqui. Obrigado.** No entanto, lembre-se
que essa lista não pretende ser exaustiva.

## Geral

- Definindo um vetor / matriz linha: `a = [1, 2, 3]` ou `b = [1 2 3]`.

- Soma, subtração: `a + b`, `a — b`.

- Obtendo ajuda (interativa) sobre uma função: `help`, exemplo `help help`.

- Atribuição: `c = a + b`

- Definindo constantes: `k = 5.23`

- Ele suporta as keybindings do Emacs (parcialmente...)! Que alegria ao descobrir isso:

- C-a: início da linha

- C-e: fim da linha

- C-k: matar a linha

- C-b: volta um caractere

- C-f: ops, em vez de avançar um caractere ele entra no search...

- Up/down: navegar no histórico de comandos

- $ scilab -nw: modo console

- Listas: declarar como `l = list(1,2,3,4)`. Existem várias formas de manipulá-las. Não achei uma função super útil a princípio, manipular vetores parece mais útil na maior parte das aplicações.

- `clc()`: clear no console

- `%eps`, sim, isso mesmo.

- `%T`, `%F`: true, false.

- `%inf`, infinito.

- `rand()` gera número aleatório (sempre de 0 a 1), `rand(5,4)` gera uma matriz com elementos aleatórios.

- Funções / variáveis matemáticas: `exp` (e^), `log`, `log10`, `ceil`, `floor`, `abs(-10)`, `max`, `min`, `sum`, `prod`, `sqrt(10)`, `%pi`, `%e`, trigonométricas `cos`, `sin`, `tan`, `sec`, `csc`, `cotg`, inversas `atan`,`acos`, `asin`, hiperbólicas, `sinh`, `cosh`, ... tudo o que você imaginar.

- Funções matemáticas: `factor`, `factorial`.

- Operações típicas com números complexos:

- `z=complex(1,2)`: define a partir da parte real, e depois da parte imaginária

- Alternativamente: `1 + 2 * %i`

- real(z)

- imag(z)

- Conjugado `z'` ou `conj(z)`

- `ans` retorna a última resposta que você não atribuiu (útil!)

- `:` forma vetores (implícitos). Python-like. Exemplo: `1:5` retorna `[1,2,3,4,5]` e `1:2:5:` retorna `[1,3,5]`.

## Álgebra linear

- Multiplicação por escalar: `k * a`, `5 * a`.

- Comprimento de um vetor/matriz (= número de elementos): `length(l)` ou `size(l)`

- Declarando uma matriz: `m = [ [1,2]; [3,4] ]` ou `m = [1,2; 3,4]`, isto é, o ponto-e-vírgula separa as linhas. Convém declarar todos os elementos dela!

- Multiplicação de matrizes: `m * n`.

- Multiplicação de uma matriz por ela mesmo == potenciação: `m^2`, `m^5`, `m**5`, etc.

- Inversa de uma matriz: `m^-1` ou `inv(m)`. Lembrando que `m * m^-1` = matriz identidade.* Falando em identidade, para declarar uma matriz identidade com n linhas e m colunas:`eye(n, m)`. Note que `eye(k)` (onde k é uma constante) é igual a 1 (constante). A matriz não precisa ser quadrada, porém note que apenas a diagonal principal é preenchida. Você também pode fazer `eye(m)` (de uma matriz).

- `zeros(3,4)`, `ones(5,2)`: matriz com apenas zeros, ou apenas uns, com a dimensão especificada.

- `diag(m)` retorna a diagonal principal de m.

- Matriz transposta: `m'`.

- Norma (quadrada) da matriz: `norm(a)`. Você pode calcular a norma p especificando um segundo argumento: norm(a,1) retorna a norma de Manhattan / Táxi.

- `triu(m)` ou `tril(m)`: retorna a matriz triangular superior e inferior, respectivamente. Basicamente, a mesma matriz de entrada, só que as posições adequadas são preenchidas com zero.

- Essa achei super útil: `clean(m)`. Arredonda para zero os elementos muito pequenos (algo como `1e-10`, por exemplo).

- Extrair elemento de matriz: `m(1,2)` (da linha 1, coluna 2) (1-based index).

- Extrair uma linha ou uma coluna (respec.): `m(1,:)`, `m(:,1)`.

- Slices de uma matriz: `m(2,2:3)`.

- A\B e A/B: divisão de matriz, pela esquerda e pela direita, respectivamente. Isso é super útil, especialmente a do backslash.

- `clear a, m, k, b`: mata as variáveis/matrizes/etc especificadas. Como se nunca tivessem existido.

- `kernel(m)` - nullspace

- `[L,U] = lu(m)` - retorna a fatoração LU de m. Também existe uma versão alternativa, com uma matriz de permutação, `[L,U,E] = lu(m)`.

- `det(m)` --> determinante

- `rank(m)`--> posto de m = número de vetores linearmente independentes

- `trace(m)` --> traço da matriz (=soma dos elementos da diagonal). O mesmo que `sum(diag(m))`. Faz sentido, né?

- autovetores, autovalores = spec(A) ==> só podem ser calculados todos de uma vez.

Acho que estou satisfeito. A única coisa que falta para completar essa lista é
como definir funções. Isso inevitavelmente nos fará entrar na parte de
programação do Scilab...if, for e amigos. Provavelmente não postarei aqui como
definir funções. Existe uma pequena chance de eu incluir aqui uma função como
exemplo, mas só.
