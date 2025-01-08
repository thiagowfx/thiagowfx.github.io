---
title: "Emissor NFE Sebrae v4.01 para emissão de notas fiscais"
date: 2024-01-19T16:44:46-03:00
tags:
  - portuguese
aliases:
  - nfe
---

_To my English-speaking readers: this post contains Brazilian bureaucracy and
it's in Portuguese, you may want to skip it._

## Instalação

Baixe o arquivo JNLP (cópia): [emissorNfe-4_0_1.jnlp](emissorNfe-4_0_1.jnlp).

Ou direto da fonte: [GCS](https://storage.googleapis.com/nfe-sebrae-prd/nfe/v401/producao/emissorNFe-4_0_1.jnlp)

Execute-o com o Java Web Start (JWS) do Java 8. Não existe mais JWS a partir do
Java 11. Caso não tenha um runtime (JRE), baixe-o diretamente do [site da
Oracle](https://www.java.com/pt-BR/download/manual.jsp).

Caso não funcione, delete e reinstale o applet:

- Abra o Menu Iniciar
- Procure "Configurar Java" no campo de busca
- Clique na Aba "Geral"
- Em "Arquivos Temporários na Internet", clique em "Exibir..."
- Clique no ícone do emissor, e depois no botão 'X' vermelho.
- Execute o arquivo JNLP novamente.

## Notas

- [OpenWebStart](https://openwebstart.com/) não funcionou. Ele lança uma
  exceção.
