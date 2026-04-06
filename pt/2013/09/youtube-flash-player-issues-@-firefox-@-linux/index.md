---
title: "(YouTube) Flash Player Issues @ Firefox @ Linux"
url: https://perrotta.dev/pt/2013/09/youtube-flash-player-issues-@-firefox-@-linux/
last_updated: 2026-03-11
---


O Flash morreu no Linux faz muito tempo (mentira, ainda não). Paramos na
versão 11.2.{alguma coisa = revisões de segurança = "security fixes"}. Esperem
mais alguns anos que ele vai morrer no mundo todo, também.

Mas enquanto ele não morre e o mundo ainda é *parcialmente* dependente dele
para algumas coisas (leia: YouTube), nos contentamos com isso. **OU NÃO.**

Até certo momento era possível assistir (todos os?) vídeos do youtube sem
problema algum no Linux (firefox, opera, chromium, chrome, não importava).
Hoje em dia praticamente todo vídeo que eu assisto dá *crash*. Mais
especificamente, esse *crash* aqui:

Que *workarounds* temos para resolver isso?

## 1. Google Chrome  + Flash Player Integrado

O Google Chrome possui integração nativa (embutida) com PDFs e Flash.  Mas
essa integração é proprietária. O nome desse troço é
[pepper](https://www.google.com.br/search?q=chrome+pepper+engine&ie=utf-8&oe=utf-8&rls=org.mozilla:en-US:official&client=firefox-a&channel=fflb&gws_rd=cr&ei=fhI7Ur2TGJPc8ASb-YBo).
Isso pode resolver todos os seus problemas. Aliás, no início desse ano, eu
tentei migrar do Firefox para o Google Chrome só por causa disso. Achava que o
firefox ia ficar *outdated* no mundo do Linux e que o Chrome era a coisa
moderninha. Bom, isso não é verdade (*ainda*?, não na data desse post). Então
se você usa Chrome ou está disposto a migrar para ele por causa disso, seus
problemas se resolversão *out-of-the-box*.

Note que isso não se aplica ao *Chromium* (versão open source), a menos que
você corra atrás para configurá-lo.

## 2- Firefox +  HTML5

A outra opção é tentar corrigir isso no Firefox. Uma forma de fazer isso é
visitar o link [youtube.com/html5](http://youtube.com/html5) e entrar no
"teste de HTML5" do YouTube. Isso funciona em boa parte dos casos, mas ainda
assim causa erro em alguns vídeos.

Então, a solução que eu achei mais completa até então (apesar de só ter
instalado recentemente, então não posso confirmar que funciona para 100% dos
vídeos) é instalar [esse
add-on](https://addons.mozilla.org/en-US/firefox/addon/youtube-flash-to-HTML5/).
O nome "YouTube Flash to HTML5" é bastante sugestivo por si só.

## Conclusão

Você conhece outra solução para o Flash do YouTube no Linux? Essas soluções
funcionam na sua distro? Compartilhe nos comentários.

Se tudo correr [como previsto](https://www.google.com.br/search?q=flash+will+die&ie=utf-8&oe=utf-8&rls=org.mozilla:en-US:official&client=firefox-a&channel=fflb&gws_rd=cr&ei=aBQ7UsjfLJCY9QTjiYDYDw), TALVEZ o Flash morra logo. Logo = alguns anos, não alguns meses. Talvez ele não morra também. Tecnologia é imprevisível. Mas o HTML5 vem ganhando cada vez mais suporte, integração e espaço na era atual. *Esperemos*.

