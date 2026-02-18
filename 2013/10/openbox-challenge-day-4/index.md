
I've been loving doing this. It's really a nice way to maintain an intensive
practice. But today was a very limited day for me. I had only half an hour to
make any further progress. But even a little progress is better than nothing,
right? [Previously]({{< ref "2013-10-29-openbox-challenge-day-3" >}}).

## Compositing and visual effects

I've installed **xcompmgr** from the official repos to enable a few compositing
effects on my desktop. I don't care much for that, though, but it's a simple way
to enable some transparency and fading. Guake and Plank are the most noticing
applications from xcompmgr effects. I've added this line to my autostart file:
`xcompmgr -cf CF -t-5 -l-5 -r4.2 -o.55 &`

## Logout menu and screen lock

I've also checked out a program called **oblogout**. This does what you think it
does... it's a logout menu, with several options nicely displayed in a GUI:
shutdown, lock, hibernate etc. The default "lock" behavior was to call
**xtrlock**. But I don't have this program. I already use **slock**. So, I went
to `/etc/oblogout.conf` and replaced the appropriate line. This would be a good
program to assign to a custom hotkey (later).

## Menu icons and utilities

I've also tried to add icons to the openbox menu. It seems that **menumaker**
doesn't support this feature. So I should've searched for a menu generation tool
with icons, but I didn't, not today. I've found another menu generation utility
called **obmenu-generator** (in the AUR). With the command `obmenu-generator -p
-i`, I've added the pipe menu entry to my original menu.xml.

One good program is **lxappearance-obconf**. I've talked about lxappearance
before. But this -obconf suffix adds more functionality to it, exposing some of
the openbox configs. It is simple but nice.

That's it for today. I feel I need hotkeys now. Git repo updated again. Thank
you for reading.

