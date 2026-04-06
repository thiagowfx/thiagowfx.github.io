---
title: "Emacs *must have* libraries/packages"
url: https://perrotta.dev/2014/03/emacs-must-have-libraries/packages/
last_updated: 2026-03-03
---


So, recently I've been heavily playing with Emacs (24, please) – at least at
the customization level –, tayloring and customizing it to my needs. You can
find my .emacs startup file
[on GitHub](https://github.com/thiagowfx/dotfiles/blob/master/.emacs). **Nowadays**
it is well documented – it used to be so messy.

Here is a list of packages you might find useful. Please notice I won't be
posting any individual links, because you can easily find them with a simple
search, or a reference about them on the [EmacsWiki,](http://www.emacswiki.org)
or even their source code on [Github](http://www.github.com/). Also, do not
forget to get them through [MELPA](http://melpa.milkbox.net/#/)/ package.el.

PS.: This is not sorted either by relevance or by my personal usage, it's just
random.

- Ace-jump-mode: quickly navigate through a buffer, at the char, word or line
  level. Your choice. With only 3 ~ 4 keystrokes, you can go anywhere (on the
  visible part of the current buffer).

- recentf: tracks your most recent (visited) files, so that you can quickly open
  them later.

- ido: quickly (do you notice the **quickly** everywhere? That's the
  intention!) find-file and switch-to-buffer. This is much more comfortable than
  the default switching.

- smex: similar to IDO, but for M-x commands (it depends on IDO).

- uniquify: if you ever open two files with the same name which are located on
  different places, this will make easier to identify what file is which.

- eldoc-mode: lisp functions get their signatures on the minibuffer – for the
  sake of the documentation.

- winner-mode: undo (and redo too!) window layouts. Super useful after creating
  (or switching to) new buffers.

- windmove: quickly move through your buffers located in the same window (~
  directions)

- saveplace: remembers your last position on a file (after you reopen it, the
  point will get to the last place you've been to)

- auto-complete: essential for C/C++ (and other languages too) development. It
  gets out of your way (what a relief!)

- company-mode: more autocompletion, looks more modern than auto-complete

- linum-mode: displays line numbers of a buffer (file)

