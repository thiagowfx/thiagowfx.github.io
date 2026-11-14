---
title: "OCaml starters"
url: https://perrotta.dev/2015/04/ocaml-starters/
last_updated: 2026-11-14
---


You should read [this]({{< ref
"2015-04-11-functional-languages-brainstorming-all-over-again" >}}) post first.

Last week or so I thought I would start to learn **Perl** or **Lua**, but I
discovered **OCaml**...and then my focus instantly shifted into it. I'm not
really sure what I'll do about the language, but for now I'm studying it a
little bit, so I'll post here a few notes about it.

**Note:** this post is likely to be updated as I progress through the language;
alternatively, a new post might be created, or I can abandon this thing
altogether (yeah, [this]({{< ref "2014-05-18-im-learning-php" >}}) happens).

## So

- To get an interpreter: *ocaml*
  - Now enter valid OCaml expressions, and finish them with ;;
  - You can enter more than one expression at a time, e.g.

  ```ocaml
  let x = 1
  let y = 2
  ;;
  ```

  - Equivalently, you can write a script.ml file and enter these same commands, then enter into the interpreter and type:

    ```ocaml
    #use "script.ml";;
    ```

- Alternatively, you can compile this script with *ocamlc.* This will create three files: an executable (*a.out* by default), *a.cmi* (interface) and *a.cmo* (object file).
- To run an OCaml executable, use *ocamlrun*.
- Up to here, this is very similar to haskell: *ghc*, *ghci*, and *runhaskell*.
- Pattern matching is very easy overall (as with haskell)

- ```ocaml
  let isvowel c =
      match c with
          'a' | 'e' | 'i' | 'o' | 'u' -> true
          | _ -> false;;
  ```

- However, I find P.M. (pattern matching) more explicit with OCaml. Haskell uses function overloading to implement pattern matching (at least in the syntax level), while OCaml uses a switch-like statement to do that. Well, actually haskell desugars function overloading to a 'case' expression behind the scenes, which is very similar to OCaml's match, but hey...it is just slightly easier to read the OCaml syntax.
- You can use _ to match anything.
- You can also use _ to ignore what is not relevant to you in a match, e.g. when matching tuples:

- ```ocaml
  let fst (x, _) = x;;
  let snd (_, y) = y;;
  ```

- You can match character ranges, e.g. *'A'..'Z'.*
- Two bindings are available: *let* and *let rec*. The last one is used to define recursive functions, and they are fundamentally the same; the difference lies in scoping rules (e.g., when using *let ... in)*. Example of *let rec:*

- ```ocaml
  let rec factorial n =
      if (n < 0) then failwith "negative factorial!"
      else if (n = 0) then 1
      else n * factorial (n-1);;
  ```

- [OCaml from the very beginning](https://www.goodreads.com/book/show/18212242-ocaml-from-the-very-beginning) is a super nice intro book to the language. I gave it a 5/5 on Goodreads.
- Examples from the book: in [this](https://github.com/johnwhitington/ocaml-from-very-beginning-exercises) user repository.
- Logical operators are not exactly what you expect regarding equality: = and <>. Yeah, not ==. Annoying, huh?
- true and false are written in lowercase. Different from python, equal to ruby. Why are programming languages so different? At least, if you write it wrong, you are prompted with a nice message:

- ```text
  Error: Unbound constructor True
  Hint: Did you mean true?
  ```

- Speaking of messages, error messages from OCaml are veeeeeery good. It looks like its creators know how to *actually* communicate with other humans (*gcc*, this is a subtle sarcasm directed to you!). Want to see an example? I'll give you one about a warning:

- ```ocaml
  let f l =
      match l with
      [] -> True;;

  (* Response: (yeah, this is a comment!)

  Warning 8: this pattern matching is not exhaustive.
  Here is an example of a value that is not matched:
  _::_
  val f : 'a list -> bool = <fun>

  *)
  ```

- Naming convention when deconstructing lists: *h::t*. This means head and tail. In haskell, we usually use *x:xs*.
- Oh yeah, haskell is : while OCaml is :: while in the lisp family of languages this is *cons*.
- And the append/concatenate operator is @. In haskell it is ++, in python it is +.
- Yeah, I keep comparing OCaml with other languages because I find it easier to understand it this way.
- A list in OCaml is a single linked list behind the scenes. So the :: operator only acts on one side of the list...you're screwed if you want the other one – alternatively, revert the list or use a better data structure.
- Speaking about lists....[1;2;3;4] not [1,2,3,4]. The last style is from Python / Haskell / Ruby.
- Package manager? Yeah! [opam](http://opam.ocaml.org/). This should be analogous to RubyGems and Haskell's Cabal or node's npm. *opam install, opam remove, opam search...*I keep writing it *opan,* for some reason.
- I **love** this feature: every function in OCaml has only one parameter. Native *currying* (aka *partial application*) FTW! Like haskell.
- The compiler is pretty smart about inferring types, but annotations can be made too:

- ```ocaml
  let sum10 (x:int):int = x + 10;;
  ```

- Anonymous functions:

- ```ocaml
  fun x -> 2 * x

  (* example of use with map: *)
  map (fun x -> 2 * x) [1; 2; 3] (* yields [2; 4; 6] *)
  ```

- Just comparing with haskell, which is slightly smaller:

```haskell
map (\x -> 2 * x) [1..3]

-- or, better yet
map (* 2) [1..3]
```

- Actually, it is possible to use something such as (+) or (<=) in OCaml. But...not (\*). This is confused with a comment. Maybe there is a way of escaping this. **Edit:** yeah, we just have to insert spaces: ( \* ).

I guess I'm stopping here for now. This includes up to chapter 6 of the
aforementioned book, plus a few random sources on the web.

