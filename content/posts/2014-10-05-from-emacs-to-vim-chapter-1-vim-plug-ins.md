---
title: "From Emacs to Vim - Chapter #1 - Vim plug-ins"
date: 2014-10-06T01:50:00-03:00
tags:
  - dev
  - legacy
  - vim
---

This is the continuation of the first post. As you get the feeling and overview
of **vim**, the first thing you'll probably miss as a
probable-soon-to-be-emacs-orphan (actually, not really, I've already told you
I'm not going to abandon emacs – for example, this post is being written within
it, with org2blog – (too many level of parenthesis, please help me!!)) are your
customizations and custom plug-ins and extensions. A couple of google searches
would bring me to projects like janus and vim bootstrap. Those look nice and I
would probably appreciate them if I were a beginner. However, as a super user –
if you read this statement as bragging, then you are probably not understanding
    the purpose of this mini series –, I like to be in control of the
    personalization and settings of my text editor. Right? So, I've chosen to
    control my own plug-ins. In other words: bottom-up instead of top-down. Now,
    the two state-of-the-art plug-in managers you'll find out there to manage
    your vimscripts are vundle and pathogen. I began using Vundle, but after a
    few hours I realized that pathogen was KISS and superior. Period. Not that
    Vundle is bad. It looks (works) okay too; in this case it was simply a
    matter of personal choice. The way Vundle works is as follows: your `.vimrc`
    will be populated with several lines such as:

```vim
Plugin 'tpope/vim-surround'
Plugin 'username-from-github/repository-name'
Plugin 'matchit'
Plugin 'vimscript-name-from-vim-dot-org'
Plugin 'git://www.absolute-path-to-my-site-here.com/repository-name.git'
```

Then, you just have to install those plug-ins with a simple command:

```vim
:Plugin Install
```

Done. It is simple, yes, but I liked more the approach of **pathogen**: you maintain a git repository with your plug-ins. Each new plug-in is a git submodule within your repository. Yay, this means it is super-easy to set up and share your plug-ins with other people. This is exactly what I've done: you can peek out my vim repository here. Now, there is one super good advantage here over emacs. The cost of adding a new plug-in is practically zero. This has two meanings, actually:

1. vim start-up time is ridiculously fast. Even with a dozen plug-ins, I still
   don't notice it. With emacs, if I don't run it as a daemon, it is a
   nightmare: a couple of seconds (yeah, a couple of seconds is really a
   nightmare, not kidding) of start-up time.
2. I don't even have to touch my `.vimrc` to add a new plug-in. I just have to
   clone a new repository into my `$HOME/.vim/bundle` folder. Period. With
   emacs, I have to continuously poke my `.emacs` file to add, remove and
   constantly tweak my extensions. Yeah, I've been doing that for a while, and
   it **does** provoke a lot of stress and anxiety. You already have to tolerate
   a little bit of RSI with emacs, so you don't need more problems.

Now, don't undermine my (our) dear Emacs! Emacs Lisp will (and will always be)
superior to vimscript. I have no doubt of this fact and therefore I won't even
discuss it here. Emacs is much more extensible than vim. Okay, then what? You
have to find a few plug-ins, right? In Emacs, most plug-ins with decent quality
you might find will be available either on MELPA or Marmalade and, of course, on
GitHub too. In vim, it looks like the home of scripts is the vim website itself
((1) and (2)) **and** GitHub. I couldn't find a central repo or website hosting
the majority of its plug-ins, as with emacs. However, there is vim-awesome,
which indexes existing ones (this concept is like the ruby toolbox, godoc.org
and Emacs paradox extension by Bruce Connor. I won't discuss the plug-ins I'm
using right now, however here is a snapshot of my `$HOME/.vim/bundle` directory
at the time of this post (19 plug-ins, yay):

- You Complete Me
- ack.vim
- ag.vim
- ctrlp.vim
- delimit Mate
- nerdtree
- syntastic
- tagbar
- vim-airline
- vim-bufferline
- vim-commentary
- vim-easytags
- vim-fugitive
- vim-gitgutter
- vim-markdown
- vim-misc
- vim-repeat
- vim-sensible
- vim-surround

Most of those have an emacs equivalent. Okay, I'm stopping here for now, until the next post :) Update: next post.
