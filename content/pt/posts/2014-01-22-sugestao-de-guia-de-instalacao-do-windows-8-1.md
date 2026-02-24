---
title: "Sugestão de guia de instalação do Windows 8[.1]"
date: 2014-01-22T16:11:11-03:00
tags:
  - dev
  - legacy
---

## Overview

A versão developer preview do Windows 8.1 expirou em 16 de janeiro. Isso implica
que o computador ficava reiniciando de duas em duas horas. A opção mais imediata
poderia ser procurar algo que parasse esse comportamento, mas...vamos fazer as
coisas direitinho. Decidi instalar o Windows 8 (sim, do 8.1 pro 8. Não faz tanta
diferença assim, apesar do 8.1 ser ligeiramente melhor) no computador dos meus
pais.

Em geral eu utilizo um processo bastante similar durante cada instalação, então
vou aproveitar que terei que realizá-lo mais uma vez para documentá-lo aqui.
Ademais, o objetivo é ter um Windows o mais clean e KISS possível (isso não é
100% verdadeiro. Na verdade, o objetivo é não introduzir *bloat* na história).
Então, vamos lá:

## Instalação

- Grave a .iso do Windows 8 no seu USB Flash Drive (aka Pendrive). Se você ainda
  utiliza CDs ou DVDs, diga-me: qual é o seu problema?? Procurar "Windows 7 USB
  DVD Download Tool"

- Boote pelo seu pendrive. Se a sua placa-mãe tem um bom design, você faz isso
  através de uma simples tecla (geralmente F2 ou F12, mas isso sempre varia.
  Padrões, para quê?). Procure algo como "boot menu". Caso contrário, altere a
  ordem de Boot manualmente, através das configurações do chipset (BIOS).

- Particione o HD. Eu gosto de deixar um espaço de 30 GB no final, caso eu
  resolva fazer um dual boot mais tarde. A seu gosto.

- Durante a tela de instalação: não saia avançando que nem um louco. Procure por
  "personalizar", evitando "configurações expressas" sempre que possível.

- Modifique as suas configurações a gosto. Em particular, pode ser que convenha
  mudar as definições do Windows Update. No mínimo, deixe "atualizações mais
  importantes".

- (Opcional) Ative o Do Not Track do IE caso ele não esteja ativado por default.
  Na verdade, se você for desinstalar o IE mais tarde, essa etapa não é
  necessária.

- Enviar informações à Microsoft: configure a seu gosto.

- "Compartilhar informações com aplicativos": desative TUDO. Principalmente a
  plataforma de localização.

- Usar uma conta do Microsoft? Olha, eu sempre fiz isso. Mas eu nunca utilizei
  nenhum aplicativo da Modern UI. Então, sinceramente? Escolhi criar uma conta
  local. Note que se você decidir baixar algum aplicativo mais tarde, precisará
  de uma conta da Microsoft de qualquer modo. Pense nisso.

## Pós-instalação

Nesse ponto o Windows está instalado. Agora vamos aos *tweaks*.

- Remova TODOS os aplicativos da Modern UI. Todos. Exceto: música, fotos, vídeo
  e leitor. Nesse ponto só deve sobrar, além deles, a Loja e o Internet Explorer
  (bom, a área de trabalho também).

- Abra o Internet Explorer e baixe ou o Chrome ou o Firefox. A gosto. Pode
  utilizar o IE da Modern UI mesmo. Pronto? Agora mude o seu navegador padrão.

- Agora, eu gosto de me livrar (pelo menos ocultar) da Modern UI. Utilize um
  desses dois programas, ou outro que preferir: Classic Shell ou Start Menu 8.

- Se durante qualquer wizard / setup a janela se mover para fora do display
  visível, você pode apertar Alt + Space e depois selecionar a opção de movê-la
  \+ as teclas direcionais para resolver o seu problema.

- Depois, vamos baixar alguns softwares para uso genérico. Nesse ponto, pode ser
  interessante instalar o AdBlock plus e/ou os seus complementos favoritos para
  seu browser para evitar algumas inconveniências. Eis a minha lista de
  software:

- Avast (anti-vírus) (opcional). A menos que você seja um usuário experiente e
  saiba o que está acessando.

- CCleaner (registro, startup, etc). Alternativamente, você pode querer utilizar
  o **msconfig**.

- Drivers! Impressora, placa de vídeo, etc

- Flash (opcional)

- GIMP (edição de imagens)

- IrFanView + plug-ins + idioma (imagens)

- Java (opcional)

- LibreOffice (pacote office)

- Notepad 2

- Notepad++

- PDF X-Change Viewer (PDF)

- PeaZip (ZIP/RAR/etc) - melhor integrado ao Windows do que o 7-Zip

- VLC (vídeos, música). Alternativa: BSPlayer

- qBitTorrent (cliente de torrent)

Isso é o básico. Mais do que isso depende das necessidades de uso de cada um. No
entanto, eis uma lista que pode ser útil:

- Chocolatey / Npackd (espécie de gerenciador de pacotes para o Windows)

- Clementine (biblioteca de músicas)

- Comodo Firewall

- Cygwin (ambiente UNIX no Windows)

- DirectX

- Dropbox ou [Copy](https://copy.com) (cloud syncing service)

- PowerISO / Daemon Tools (CD/DVD virtual)

- Sandboxie (chroot like)

- Skype / Raidcall

- Thunderbird (cliente de e-mail)

- VirtualBox (máquinas virtuais)

É provável que, nesse ponto, você não tenha prestado muita atenção e (por isso)
tenha instalado alguma barra ou *crapware* durante a instalação dos outros
programas. Agora vai lá e remove tudo o que não presta.

## Pós-Pós-Instalação

- Remova o Internet Explorer.

- Desinstale componentes do Windows não necessários ("ativar ou desativar
  recursos do Windows")

- Desative os efeitos desnecessários da área de trabalho.

- Instalar add-ons para o seu web browser.

- Checar a lista de programas que iniciam com o Windows (pode ter um monte
  agora) ==> CCleaner ou msconfig

Pronto, isso resume o básico. Se você tiver um HD Externo, convém copiar os
setups utilizados agora para poupar algum trabalho da próxima vez. Esse não é um
guia de **manutenção**, então vou parar por aqui. *Happy hacking!*
