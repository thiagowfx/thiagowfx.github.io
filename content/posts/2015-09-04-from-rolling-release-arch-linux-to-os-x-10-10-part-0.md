---
title: "From rolling-release Arch Linux to OS X 10.10+: Part #0"
date: 2015-09-04T01:11:56-03:00
draft: true
tags:
  - dev
  - legacy
  - macos
---

## Prelude and Off-Topic

Hello fellow readers of my not-yet-abandoned-serendipitous blog! Here is the
most awaited post from the century! Before everything else, I want you to
remember this word: **bloat**. There is another one, if you're in the mood:
**temptation**. This will probably be my latest series in this blog; after that,
I feel it simply doesn't make sense existing anymore. While I'm always finding
something new out there in the interwebs, I feel I completed my quest of sharing
my overall thoughts and opinions on technology, privacy, operating systems,
usability, ... and so on. After this blog/series, I should probably inquire the
whereabouts of either (social) psychology or economics/politics/game
theory/rationality or even dive into the unknown world of compilers: this Rust
language is still in my mind for some reason, I feel I'm highly attracted and
being pulled by an unknown force in this domain.

Anyway, let's stop writing flood and go straight to the post: I will probably
write about 3 or 5 posts regarding my transition to OS X. One of those posts
will be a FAQ and a overall/general comparison between OS X and Linux
distributions (remember, I used more than 20 linux distributions (probably), so
I'm the guy who understands this (ok, not really, but mostly).

## Removing OS X Applications

[http://www.cultofmac.com/90060/how-to-completely-uninstall-software-under-mac-os-x-macrx/](http://www.cultofmac.com/90060/how-to-completely-uninstall-software-under-mac-os-x-macrx/): gotta know your system!

**See also**: AppCleaner. Like RevoUninstaller and EasyCleaner from the Windows
World.

This is enough. More than that is manually using find + `rm -rf` on random places
of your system. Also, you'll want to open Activity Monitor to (maybe) find some
traces of old applications. Kill them all.

## Quicklook Plug-ins

<https://github.com/sindresorhus/quick-look-plugins>: makes the finder
previewing experience better overall. Don't install all of those, though! Just
the ones you really think you'd ever use. I'd recommend using brew ask to do
that. Also, do a `qlmanage -r` after installing those plug-ins to force
*quicklookd* to restart. Also, don't trust this repository at all, just use the
information in there to find good plug-ins; the repositories of this guy are
usually way too much *overrated*.

## Resources

Unfortunately, I've already used several resources out there but didn't index
them so they are lost now. However, now that I have a nice control of my
operating system, I could efficiently store a few resources. Here are they:

- [Mac Keyboard Shurtcuts (Apple
  Help)](https://support.apple.com/en-us/HT201236) Comment: as an former emacs
  user, it is really easy to catch new keystrokes and shortcuts. It is a little
  harder to fixate them over time, but nothing that a little practice solves.
  - Cmd-X, Cmd-C, Cmd-V: for simple copy-and-paste operations. They are
    universal.
  - Cmd-Z, Cmd-S-Z: for {un,re}do operations. Universal too.
  - Well, several keys from now on are universal too and I won't keep repeating
    that, so pay attention:
  - Cmd-A: Select All/Everything.
  - Cmd-F: Find.
  - Cmd-G: Find Again. Like F3 in some text editors, like C-n in Emacs, like n
    in vim. If you press Cmd-F again you'll see no effect whatsoever.
  - Cmd-H hide the window from the current front app.
  - Cmd-M minimize the window front the current front app. The difference
    between this and the last action is subtle.
  - Cmd-O open, Cmd-S save, Cmd-P print, Cmd-N new, Cmd-Q quit. It is very nice
    to have those as standard. I miss this on Linux applications.
  - Cmd-Option-Esc: force quit. So I don't need to xkill or to pkill in here. It
    is also possible to find this option in the apple menu.
  - Cmd-Space: spotlight! Like gnome-do, or unity search. You can use it as a
    launcher for apps (like dmenu or rofi) or to quickly open indexed documents
    on the system. Also, quickly list files with a certain extension with
    kind:iso, for example.
  - Spacebar: quick look. Usually available in Finder. Intended as a quick
    preview for some file formats.
  - Cmd-Tab: like alt tab on your favorite desktop environment.
  - Cmd-~: (cmd+shift+`): switch windows of the same app. Like Unity does.
  - Cmd-,: open preferences for the current app. This is a very nice shortcut
    overall.
  - Cmd-S-3: take screenshot of the entire screen, like PrintScreen.
  - Cmd-S-4: take screenshot of a rectangle of the screen.
  - Cmd-S-Power: put the display to sleep. Alternatively, I liked setting up a
    hot corner on bottom left for the same purpose.
  - Cmd-O-Power: put the Mac to sleep.
  - Formatting: Cmd-B, Cmd-I, Cmd-U for bold, italic and underline.
  - *Delete* is actually backspace. To actually delete, use Fn+Delete. Some
    applications also allow you to use C-d.
  - Fn-Up: same as pageup. Fn-Down same as PageDown.
  - Cmd-Up: same as Home. Cmd-Down same as End. You could also use Fn-Left and
    Fn-Right.
  - Cmd-Left: move cursor to the beginning of the line (like C-a for bash). The
    correspondent action for the end of the line is Cmd-Right.
  - Option+{left,right}: move the cursor by word.
  - Some emacs movement keystrokes, but for documents: C-a, C-e, C-f, C-b, C-p,
    C-n.

## Dos and Don'ts

- Wipe the Dashboard. This is useless.
- Don't install Aquamacs. So bad.
- Don't install MacVim. Completely useless. Use vim from within the terminal instead. Also, I'd recommend a brew install vim to get a newer version.
- Install homebrew, and use it for command line applications! I should comment about it in a future post.
- Install homebrew cask, but don't abuse it!
- Cancel all the suggestions from the Spotlight. Otherwise all of your searches will be sent to Apple servers.
- Use Firefox, don't use Google Chrome. Don't infect your OS too soon!
- Safari is okay.
- Remove things you don't use from the dock. Make it like eOS's plank: KISS.
- Learn the hotkeys of your system! They are very handy.
- Put your display to sleep when you leave your computer. Or put the entire system to sleep if you will really leave.
- brew install coreutils (GNU!)
- Grab your dotfiles.
- Configure an Apple ID, but remove your credit card immediately soon. No, you don't want to spend money with useless apps from the app store. There are always better alternatives!
- Install VLC. Don't use quicktime.
- Use quicklook as much as possible! So handy
- Install iterm. Don't use the default terminal app.

## Wrapping up

OK, there is not much information in this post. That's why it is called Part #0.
Actually, there is more information here than I should put in such a post. But
okay; I expect to be slightly more technical in the next post. See ya!
