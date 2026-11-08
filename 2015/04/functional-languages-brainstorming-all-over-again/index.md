---
title: "Functional languages, brainstorming all over again"
url: https://perrotta.dev/2015/04/functional-languages-brainstorming-all-over-again/
last_updated: 2026-11-08
---


## Context

Historically, I love functional languages. The first family I was introduced to
were the lispy ones; more specifically, emacs lisp, then racket, then clojure.

**Emacs Lisp** is very powerful for its purpose, and I believe the only reason
people still use emacs today is because of the power of elisp. Emacs is very
extendable and this is not a coincidence: functional languages are very
expressive.

**Racket** was taught to me in a [coursera
course](https://www.coursera.org/course/programdesign) which intended to teach
functional languages and [how to design programs](http://htdp.org/) with them.
It is very cool and nice for beginners, but after learning the basics of FP I
don't see much space for it.

**Clojure** is lisp for web programming and development. I believe it is the
most suitable and useful functional language to learn today (from the lisp
family, I mean).

Then we go away from the lisp family; the first most notable language out there
that remains now is **Haskell**. Haskell is very peculiar and is what is called
a "pure" functional language, which means that the FP paradigm is forced; there
are no imperative ways to do anything with it (well, except after you learn
about monads).

While I loved to learn Haskell and discovered it has a huge ecosystem, I don't
think it is the most practical functional language to use today. So...what do we
do?

## And now

I then paused my functional programming research/learning for a while, until...
I discovered about [OCaml](http://ocaml.org/). It seems to have a good
compromise between the functional and imperative paradigms, but it is functional
by nature (but not pure). I am now reading [OCaml from the very
beginning](https://www.goodreads.com/book/show/18212242-ocaml-from-the-very-beginning).
It is a very good introdutory book and it is making me like OCaml.

I'll now see if I will like OCaml more than Haskell. And, more important yet: if
it is practical to use in the day to day.

An example – sum of a list:

```ocaml
let rec sum l =
  match l with
    [] -> 0
  | h::t -> h + sum(t)
```

