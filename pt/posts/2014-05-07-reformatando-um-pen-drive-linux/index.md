
**Motivação:** toda vez que insiro um pen-drive em um computador com Windows da
faculdade, pego um vírus. **SEMPRE**. Incrível. Naturalmente, a opção mais óbvia
para se livrar disso é inserindo o pen-drive em um outro Windows e ativando a
opção para formatar o pen-drive.

Só existem dois probleminhas com essa "solução". A primeira é que, ao inserir o
pen-drive nesse outro computador, você estará automaticamente infectando esse
computador. Na verdade, a coisa toda se parece com um vírus não-virtual mesmo:
bastou entrar em contato, infectou o novo organismo. Os seus únicos potenciais
anticorpos são: a) utilizar um outro sistema não compatível com o Windows ou b)
desativar a opção de *autorun* de novas mídias no Windows em que o pen-drive for
inserido. O problema é que essa opção está quase sempre ativada, e ninguém se
lembra de desativá-la (ou não se importa, porque não é algo muito prático para
quem quer fazer uma simples apresentação de apenas alguns minutos!).

O segundo é que, mesmo que você formate o pen-drive, alguns instantes depois o
vírus se recopiará para o mesmo. Ou seja, você só teria formatado por meros
instantes...

Claro, a melhor forma de atacar isso é começando por rodar um anti-vírus no
Windows originalmente infectado, mas isso foge do escopo desse post.

Vou expor aqui uma forma de recuperar o pen-drive a partir do Linux. Recuperar,
nesse contexto, significa simplesmente formatá-lo: recriar o sistema de
arquivos. Só isso.

Gostaria de destacar que existem boas chances de existir uma forma de fazer o
que eu vou listar a seguir através de um programa com interface gráfica
(exemplo: **gparted**). No entanto, vou me ater à linha de comando, porque é uma
forma que vai sempre funcionar, e que é confiável (talvez não seja
necessariamente fácil, mas isso é outra história).

**Etapas -- atenção! Recomendo que leia tudo antes de testar em seu próprio
dispositivo. Se você utilizar esses documentos no disco errado, vai perder os
arquivos desse disco. Apenas atenção!:**

1 - Obtenha uma máquina com Linux, abra um emulador de terminal, e insira o
pen-drive.

2 - Certifique-se que o Pen-drive foi reconhecido pelo sistema. Para isso, você
deverá checar os discos da forma /dev/sdX, onde X é uma única letra, como por
exemplo /dev/sda, /dev/sdb/, /dev/sdc. Usualmente o primeiro disco da máquina (o
/dev/sda) é o que está rodando o sistema. Então, atenção: **praticamente nunca o
pen-drive vai ser o /dev/sda.**Note que a palavra **disco**, nesse contexto,
significa (em geral): Disco Rígido (HD), SSD, Pen-Drive, Cartão SD, ... ou seja,
praticamente qualquer dispositivo moderno de armazenamento de dados.

2.1 - Como checar os discos? Rode o comando

```shell
sudo fdisk -l
```

É necessário um pouco de bom-senso. Geralmente você sabe a capacidade do seu
pen-drive (digamos, 4GB); portanto, procure o dispositivo que indicar 4GB. Se
você estiver na dúvida, retire o pen-drive, rode esse comando novamente, então
recoloque o pen-drive e rode esse comando mais uma vez: agora compare qual disco
apareceu dessa vez.

3 - Vou supor que o pen-drive é o /dev/sdX. **Atenção! Utilize essa linha de
comando para a letra que é correta para você.**Agora, rode

```shell
sudo cfdisk /dev/sdX
```

Provavelmente você só possui uma partição alocada, do tipo FAT32. Eu recomendo
deletar essa partição e criar uma nova. Isso deve ser intuitivo, apenas siga a
interface. Depois de criar a nova partição, usualmente ela vai ter algum sistema
de arquivos que tem a ver com o Linux. Nesse caso, é necessário mudar o tipo do
sistema de arquivos (procure a opção "type", ou similar) para FAT32. NTFS também
é uma opção, mas eu realmente recomendo colocar FAT32: é o que o próprio windows
seleciona (geralmente)!

Se você fez isso direitinho, agora procure a opção "write" para gravar as
mudanças realizadas. Se você NÃO FEZ isso direito e, por algum motivo, se
enrolou ou não encontrou dada opção, então procure "cancel". Se você cancelar,
nada do que você fez foi gravado em disco, então é como se você nunca tivesse
rodado o comando **cfdisk**, pode ficar tranquilo.

4 - Agora que recriamos o nosso sistema de arquivos FAT32, devemos criá-lo
efetivamente! OK, perdão pela minha terminologia. É o seguinte: na etapa
anterior, **indicamos** que o sistema de arquivos é FAT32 (ou NTFS, depende de
você). Agora vamos **alocar** esse sistema de arquivos **efetivamente**. O
comando típico é o seguinte:

```shell
sudo mkfs.ntfs -L "MEULABEL" /deb/sdX1
```

```shell
sudo mkfs.vfat /dev/sdX1
```

Qual você vai usar? Depende se você escolheu FAT32 ou NTFS. Para especificar um
label no caso de ter escolhido FAT32, utilize o comando

```shell
sudo fatlabel /dev/sdX1 "MEULABEL"
```

Sobre a numeração, /dev/sdX1, /dev/sdX2, etc, se referem às partições do disco
/dev/sdX. No caso, eu assumi que você só criou uma única partição (o que é o
comum em pen-drives), então você vai utilizar /dev/sdX1 mesmo.

Bom, é isso! Se você seguiu as etapas corretamente, o seu pen-drive estará
formatado, livre do vírus. Não o insira na mesma máquina que o infectou, senão
você vai ter que formatá-lo novamente.

