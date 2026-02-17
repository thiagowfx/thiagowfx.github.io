---
title: "Mail from Emacs - Part #1"
date: 2014-08-23T18:13:37-03:00
tags:
  - dev
  - legacy
---

**Whisper** : Yeah, this is probably the most crazy thing I've ever done (with
emacs, sure).

## Overview

I have a couple of e-mail accounts out there; this is inevitable nowadays. I
usually manage them all from a single Gmail account, with a little help of POP3
**or** automatic e-mail forwarding (that depends on the relevance of the other
mail accounts). The point is, while I don't have to manually check every account
– just the main one –, I still depend on the web interface of Gmail. In a
scenario like this, two-step verification with [Google
Authenticator](<https://code.google.com/p/google-authenticator/>) is a must. No
problem, but what about mail clients? Currently I'm very happy with [Claws
Mail](<http://www.claws-mail.org/>); it is simple and gets the job done.
Thunderbird is not a software that I personally enjoy, but I find it great to
set up (for example) for my family, since it is GUI friendly. Now, while Claws
Mail is reasonably elegant, it is not something that I use in a daily basis. Not
even in a weekly one. I only open it up sometimes, usually when I need
(correction: **want**) to send a PGP signed message. Another thing is this year
I became a reasonably active user of mailing lists: there are a couple of them
that I read weekly. Reading them from gmail is a slow process (web or android,
this doesn't matter here).

## Now, let's get Gnus

The previous section was intended to point out to you my motivation do to this.
There is one more: curiosity. The hacker spirit of Linux/Emacs/(whatever) users
is really special: sometimes we try out things just for the sake of trying them
out. No strings attached, not a single reason to do them. This is divided in (at
least, I hope) two parts. This one is only a 'Hello World' kind of setup. I
don't know yet how to operate Gnus properly (beyond its basics), so if you only
want the technical details, go away – nah, just wait for the next post.
[EmacsWiki](<http://www.emacswiki.org/emacs/GnusGmail>) had all the information
I needed to setup Gnus from Gmail. Seriously, I don't need to duplicate
everything here, just follow it. Briefly, you just have to create a
`$HOME/.gnus` file for the configuration of Gnus (the mail client (embedded)
inside emacs we are using here) and a `$HOME/.authinfo` for your Gmail password.
I really hope you are using two-step auth here, otherwise you'll be storing your
default Gmail passwrod as plain-text in your filesystem. Please **don't do
that**. As an additional layer of security in the case your *nix box is shared
with another user, it won't hurt if you do

    chmod 700 $HOME/.gnus
    chmod 700 $HOME/.authinfo

to keep those files only available to you. Next, to make sure your e-mail is
working, do a `M-x gnus`. You should see there your labels from gmail. Yay! Now,
do a `C-x m` to send a new e-mail. By doing this, you'll be creating a new
    buffer with the following contents:

    To:
    Subject:
    From: (myawesomefullnamehere) <(myawesomeemailhere)@gmail.com>
    --text follows this line--

    --

    — Thiago

Pretty neat, huh? It even took my signature from `$HOME/.signature`, that I use
for Claws Mail. However, about the 'From' line, I suspect it parsed the contents
    of the two `user-full-name` and `user-mail-address` variables that I have
    set on my `$HOME/.emacs` file. I just sent a sample e-mail and saw it
    worked. Cool, dude!

Now, there are so many things to do / discover here. Here is a mini org list to
remind myself later:

    * Sending mails
    — [ ] attachments
    — [ ] PGP signing
    — [ ] PGP encryption
    — [ ] multiple e-mails
    — [ ] CCo
    — [ ] Integration with other emacs features: spell-checking, auto-fill,
      etc.
    — [ ] Plain text only?? What if I want to send a org or markdown mail?
      This would be super cool.
    * Managing mails
    — [ ] Delete one mail
    — [ ] Delete several e-mails
    — [ ] Searching for old e-mails (this is probably better with the gmail
      interface...)
    — [ ] Change a label
    — [ ] Mark mails as {un,}read
    — [ ] Sync mails periodically
    — [ ] Sync mails manually

For starters, this is okay. Until later.
