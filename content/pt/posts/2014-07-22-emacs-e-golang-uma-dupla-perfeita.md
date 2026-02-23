---
title: "Emacs e golang, uma dupla perfeita"
date: 2014-07-22T22:09:00-03:00
tags:
  - dev
  - legacy
---

(Sim, o título é clichê.)

Dentre todas as linguagens de programação que tive contato até hoje, sem dúvida
Go é a que teve a melhor integração com o Emacs. A integração é tão grande que
eu até dispensei completamente a necessidade de utilizar a
[LiteIDE](https://code.google.com/p/golangide/) (aparentemente a IDE mais
standard para Go).

([Esse](http://geekmonkey.org/articles/20-comparison-of-ides-for-google-go) site
lista mais IDEs ainda. Pessoalmente acho uma lista exagerada, mas o leitor pode
optar pelo que se sentir mais confortável. Adicionalmente, o
[reddit](http://www.reddit.com/r/golang/comments/2739gp/golang_ides/) é sempre
uma boa fonte adicional.)

Então, o que você espera ver nesse post? Certamente como integrar o Emacs com o
Go, certo? A verdade é que já existem duas fontes (em inglês) muito boas sobre o
assunto:

- [https://tleyden.github.io/blog/2014/05/22/configure-emacs-as-a-go-editor-from-scratch/](https://tleyden.github.io/blog/2014/05/22/configure-emacs-as-a-go-editor-from-scratch/)

- [http://dominik.honnef.co/posts/2013/03/writing_go_in_emacs/](http://dominik.honnef.co/posts/2013/03/writing_go_in_emacs/)

Qualquer coisa que eu reproduzisse aqui seria simplesmente uma repetição do que
já está listado nelas. Então, em vez disso, primeiramente listo a minha
configuração atual:

```lisp
(when (locate-library "go-mode")
  ;; golang -- you should go get external tools by yourself!
  (add-hook 'before-save-hook #'gofmt-before-save)
  (when (locate-library "go-autocomplete")
    (require 'go-autocomplete))
  (when (locate-library "go-eldoc")
    (add-hook 'go-mode-hook 'go-eldoc-setup))
  (when (locate-library "go-projectile")
    (require 'go-projectile))
  (when (locate-library "golint")
    (require 'golint))
  (setq gofmt-command "goimports")
  (add-hook 'go-mode-hook (lambda () (if (not (string-match "go" compile-command))
                     (set (make-local-variable 'compile-command)
                          "go build -v && go test -v && go vet"))))
  (add-hook 'go-mode-hook (lambda () (local-set-key (kbd "M-.") #'godef-jump))))
```

Depois, dou uma demonstração da introspecção que podemos alcançar com isso,
através de uma ferramenta que divulguei aqui uns dias atrás…asciinema! Só existe
uma pequena limitação, eu só posso usar o asciinema com o emacs no modo
terminal, então ele não fica completamente funcional; mas, mesmo assim, isso já
é suficiente para que vocês possam perceber o poder e a flexibilidade dessa
integração.

Note, no vídeo, que criei um arquivo em [orgmode](http://orgmode.org/) (quantas
vezes nesse blog já indiquei a homepage desse maravilhoso projeto?) e o usei
como base para gravar o asciicast. Aproveitem!

Link: [http://asciinema.org/a/10965](http://asciinema.org/a/10965)

OBS.: Note que a gravação do asciinema é ligeiramente mais lenta do que o tempo
real. É claro que eu escrevi mais rápido do que parece no vídeo.
