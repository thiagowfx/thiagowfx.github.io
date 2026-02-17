
_Ideally_ one who wants to be _super_ keyboard centric should try a window
manager like awesome, i3 or xmonad, but I don't want to do this now. Here is a
list of keyboard shortcuts I like. It's really easy to configure these in XFCE,
openbox, fluxbox, KDE, (Ubuntu) unity, and so on... you only have to find the
right option (or the right config file).

In XFCE, there are at least two relevant sections on its settings manager:

- Keyboard --> Application Shortcuts
- Window Manager --> Keyboard

In fluxbox, look for `~/.fluxbox/keys`. In openbox, `~/.config/openbox/rc.xml`.

---

You should know shortcuts are a personal thing. Customize them as _you_ like.

## Window Manager Shortcuts

- Super + D = show desktop
- Alt + Tab = cycle through windows
  - Alt + Shift + Tab = (backwards)
- Alt + F4 = close current window
- Super + Up = maximize (and unmaximize) window

## Application / Misc Shortcuts

- Super + s = search (currently I launch **catfish**)
- Super + w = web browser (currently I launch **firefox**)
- Super + f = file manager (**Thunar**)
- Alt + F2 and Super + r = program launcher (could be fbrun. I use XFCE's one)
- Alt + F3 = application finder (XFCE's one)
- Print Screen = scrot or **xfce4-screenshooter -r**
- Super + c = configuration center (xfce4-settings-manager)
- Control + Alt + Del = lock screen (xflock4 or slock)
- Control + Esc = kill a window (**xkill**) - this is useful, I've learnt that
  from KDE
- Control + Alt + Esc = task manager (lxtask or **xfce4-taskmanager**)
  (inherited from KDE too)
- Super + Space = application launcher (**synapse** or gnome do or launchy)
- F12 = drop-down terminal (**tilda** or guake or yakuake (for KDE))

---

The super key is usually the windows key. Also, I like a feature called
**tiling**. You probably know this one. Move the window to the left (or right)
side in Windows 7/8 and it will resize and snap itself to the corresponding
side. XFCE doesn't support this out-of-the-box, but I've found a python script
which accomplish this. Search for stiler (if you download the AUR package,
notice you should run the script with python **2**). Then, try `stiler left` and
`stiler right`. I've assigned them to Super + Left and Super + Right,
respectively.

I only posted here the shortcuts I commonly use. There are (usually) many more,
but not every one are relevant.

