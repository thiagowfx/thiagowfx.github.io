---
title: "From Emacs to Vim – Chapter #2 – Philosophy"
date: 2014-10-18T23:47:21-03:00
tags:
  - dev
  - legacy
  - vim
---

Previous post. Oh man, up to this point I am slightly disoriented about emacs shortcuts. It has been probably one month since I am using vim almost exclusively. I just use emacs to blog here and to use orgmode. Yes, I still know so many of Emacs shortcuts and keybindings that I can even recite them to you while I am dream. However, I am not practicing them so much as before, so they will probably fade away some time.

But I have used emacs for two years, so I won't forget the basic commands, terminologies, functions and shortcuts, so no problem at all. Okay, so I've just finished reading Practical Vim. I super encourage you to buy the book and support its author, because this was (is!) a fantastic book! I also thanks Jason Ryan, forums and wiki admin from the Arch Linux community, for recommending the book. It is one of the reasons that made me commit myself to learn (and stick to) vim.

Now, in this post I'll talk a little about the differences between emacs and vim. This is supposed to be an informal post, with information coming out of my head on-the-fly, so don't expect much consistency or formality here. I'll list a couple of topics/categories and tell you what text editor I most like in each of them.

## IDE vs text editor

Vim is not an IDE. I'll repeat that. **Vim is not an IDE**. Vim is just a text editor. Don't even try to make it a IDE. If you want a solid text editor to behave like an IDE, use and stick to Emacs. Emacs is not **just** a text editor; it is a **full-featured** text editor. Theoretically, it might be anything you want. There are no limits about the customizations you can do to extend emacs. The limit is the sky (actually, the memory of your current hardware).

I prefer **vim** here. For two years I tried to make emacs the perfect IDE. You can achieve good results with it (yeah, **good** ones!), however, it is best when you keep it simple. I like this aspect in vim, and now I understand why almost everyone of the Arch Linux community that I know prefer vim rather than emacs.

Vim is KISS. It is kiss in text editing. For example, vim defaults are very good; I can survive without a .vimrc. However, emacs defaults are terrible (from my point of view, and considering that I know it can be better). I simply cannot use emacs for much time without my .emacs file.

## Shortcuts / keystrokes / chords / modal text editor

Emacs shortcuts mostly involve pressing `<Control>` or `<Meta>`, plus a letter or number key. Sometimes you have to do this (which I'll call a **chord**) two or three times. For example, to quit emacs you press `<C-x C-c>`. Vim shortcuts usually involve only a few chars, but you have to switch to normal mode to activate them (most of the time, at least).

Now, which is better? That depends. From my point of view, emacs win in respect to speed. I usually issue a command faster in emacs than in vim. However, vim commands are better to navigate through text than emacs ones, because they are well integrated.

Furthermore, an extensive use of Emacs can lead to RSI (repetitive strain injury). Even Richard Stallman had it once. Vim commands are slightly less aggressive (in respect to the keyboard), so the health of your hands and fingers will benefit from them.

Some people also recommend the mapping of the caps lock key to `<Esc>` in vim, or to `<Control>` in Emacs. They claim that the caps lock key is not much used, so it is more useful when mapped to `<Esc>`/`<Ctrl>`. Well, I personally never accustomed myself to this convention. It has a natural problem of compatibility: every new computer you use won't be configured this way. So I don't find this very portable, and I don't want to bring a .Xmodmap file everywhere.

So, who wins here? **Emacs**. However, remember what I've said: Emacs is faster, but it will hurt your fingers if you use it for prolonged hours.

## Command-line

**Emacs** command line wins. Sorry vim, that's it. Short and clear. It is even more powerful with smex, ido and icomplete. At this point I don't know any enhancement for the vim command line, but I have to say it is pretty good also. For now, I'm only using `wildmenu`. But emacs wins, period.

## Movement of the cursor through a buffer

**Vim** is better. Period. Like I've said before, it is very well integrated in this respect. You can switch your cursor to almost anywhere in your buffer with just a couple of keystrokes.

Now, in Emacs I am usually mechanical, and keep repeating myself. For example, if I want to go a few lines above, I'll probably hit `<C-u C-p>` a couple of times. In vim, currently I press `k` a few times too, but this is due to lack of practice. There are faster ways of moving in vim than I am used to.

## Buffer management

The two editors are very decent in this regard. Since I am more used to Emacs, nowadays I find easier to manage emacs buffers; however, the vim way of navigating through them is pretty decent, so I won't declare a winner in this category.

## GUI (graphical user interface)

It is almost impossible to use emacs for a couple of minutes if you are not using its X version. Its console version is just awful. In contrast, vim is perfect on the console, but I find gvim pretty bad (well, at least, I feel like I am editing the console when I used it: no relevant differences).

So the **emacs** GUI is better. It is probably even better on OS X, however I cannot confirm that right now.

## Books

Emacs books will usually teach you emacs lisp. It is very hard to learn about emacs without learning what is actually happening under its hood. When you realize that everything you do in emacs is just Emacs Lisp, you really find that very beautiful. A functional language being used for the greater good.

But this is also a problem: if you don't care about elisp, you will probably get bored. Fast. Very fast.

Now, vim books usually teach you how vim commands are integrated with themselves and with vim itself. At least the books I've read up to today. This is better on a practical basis, when you want to quickly become good with it (you see, I already feel fluent in vim with just one month usage – I felt fluent in emacs only about a couple of months, and part of this reason was bad out-of-the-box defaults).

The point is: you don't need to know about vimscript to actually get work done on vim. Therefore, **vim** books are better in respect to being pragmatic; buuuuut **emacs** books are better regarding teaching the inner workings of the editor, and how to program and extend it.

## Out-of-the-box, better defaults

**Vim. vim. vim.**

## Ubiquity

**Vim. vim. vim.** And vi. However, "micro emacses" such as mg (the program that Linus Torvalds uses) and zile are very good. But they are very basic, they are just micro text editors with emacs keystrokes; not much features.

## One-line answers

### Color themes / colorschemes

Emacs!

### Plug-ins and extensibility

Emacs is more extensible, but vim plug-ins give you less headache.

### Communities

There are more people using vim than emacs, but the emacs community is still good today. …and my creativity ran away now. Which additional topics do you believe that vim or emacs is better than its counterpart in? Comment.
