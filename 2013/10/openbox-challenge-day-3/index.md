
[Previously]({{< ref "2013-10-28-openbox-challenge-day-2" >}}).

So, it's the third day, let's go.

## Setting up my config repo

First things first: I've created a github repo with my config files. I chose not
to use my dotfiles repo, because this repo is usually changing. My primary way
to add files to it will be using symbolic links. But git doesn't really follow
symbolic links. I had to handle this with some workarounds, which you could read
about in this [Stack Overflow thread about
symlinks](http://stackoverflow.com/questions/954560/how-do-i-add-files-without-committing-them)
and in [this one about git and symbolic
links](http://stackoverflow.com/questions/954560/how-do-i-add-files-without-committing-them).
The `mount --bind` way sounds intelligent, I haven't thought of this before. But
I don't want to mess with my `/etc/fstab` with several entries, it would look a
bit dirty. So I've created a symbolic link from my openbox config dir to my
github repo.

If you are reading to try to learn about openbox, I would recommend you to check
out my autostart file. I usually use `#cst` to identify parts of the code that
I've edited (cst = custom). Today I've modified the environment config file,
just to add one language to it. I won't set up a cron job anymore, I've noticed
this is unnecessary in this case. Actually, this may be a good idea to apply to
the dotfiles repo; but not to the openbox one.

## Shortcuts and tricks

A shortcut I discovered today: scroll the mouse while focusing the desktop and
you'll switch around desktops. Another good trick which I'm used to in Fluxbox
(and works in openbox also) is to hold the Alt key while right clicking in a
window. This will resize the window.

The first shortcut would soon prove very annoying in the 1px left margin space I configured yesterday. I was accidentally switching desktops all the time because of that. So I removed the margin space.

## Menu configuration

Changing subjects: the **obmenu** tool is amazing (it is in the official Arch
repos) to configure the menu. It is a GUI, so I won't talk about its details,
it's really simple to use it. I've created a "Firefox" entry to test, and it
works like a charm. But what if I run mmaker again? Yeah, the firefox entry
disappears (like you should expect). What if I want to integrate my custom
obmenu entries with the mmaker (generation)? I searched a little and found out
that this can be easily achieved by editing the menu.xml file by hand. First,
create a custom_menu.xml file. Then run mmaker again. Now, add the contents of
custom_menu.xml to menu.xml -- in the right place! My right place is under the
root menu. To update the menu, run `openbox --reconfigure`. This is not a fully
automated manner, but works and it's simple. Actually it's pretty easy to write
a script to automate this, but I find it unnecessary. Let's (be) KISS here.

## Off-topic reflection

So, I'll end here for today. Truth is I spend more time editing these posts than
learning openbox itself. This is because I wanna make decent posts, right? I
wouldn't mind this, I really enjoy writing these posts, but I have college
homework to do and tests to study to. I'm not sure what I'll do about this. I
don't want to pass a day without posting (this would break the challenge), but I
can't lose so much time with this either. I want to learn emacs `org2blog` to
optimize my time, but not now. I think the practice is essential! It helps me
endorsing more firmly the _know-how_ and the concepts of these activities.

## Screenshot

Bonus: here is a screenshot of my menu:

![Openbox menu screenshot](http://farm3.staticflickr.com/2847/10564931235_b12d28a1f1_o.png)

I encourage you to make any comments about what you think of this challenge.

## Tomorrow plans

- Icons in the menu? (Fluxbox easily supports that)
- Read more about menu.xml (I only skimmed it today)
- Etc (can't think of anything now)

---

## Today interesting pages

- http://ubuntuforums.org/showthread.php?t=192106
- http://crunchbanglinux.org/wiki/configuring_the_openbox_menu
- http://obmenu.sourceforge.net/index.html
- http://menumaker.sourceforge.net/
- https://github.com/thiagowfx/openbox

Thank you for reading.

