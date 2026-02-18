
There are plenty of tutorials and insights about tmux on the web. This post
isn't another tutorial. Instead, I'm listing four purposes of why you should use
tmux. I'm not here to convince you to use any tool; just read and create your
own judgment about it.

## Okay, tmux

> **Observation:** You should probably install and open `tmux` to follow this
> mini tutorial. After executing `tmux`, you'll probably notice nothing fancy
> happens—it just feels like opening a new terminal.

### Purpose #1: Terminal multiplexing

Tmux is a terminal multiplexer. If you are used to opening several windows of
your favorite terminal emulator (terminator, gnome-terminal, xfce4-terminal,
konsole), you should probably stop that now.

> **Observation:** `<prefix>` denotes your tmux prefix key. The default is
> `C-b`, but it can be changed—for example, vim users tend to dislike this
> setting because `C-b` is frequent in vim (it scrolls one page up, like Page
> Up). `C-a` is a common alternative.

Here's how you open a new tab (window in tmux terminology) on tmux: `<prefix>
c`. No mouse; no need to play with two windows. To switch between windows:
`<prefix> n` for next and `<prefix> p` for previous.

Now for multiplexing: to create a new horizontal split, use `<prefix> "`. To
create a new vertical split, use `<prefix> %`. To switch between splits:
`<prefix> o`. This subset of keystrokes is sufficient to boost your terminal
productivity.

### Purpose #2: Pair programming

Suppose you want to share a terminal session with a friend. What is a terminal
session? Think of it as an analog to desktop sharing in the GUI world. However,
it is more than simple sharing—the observer has full control over the terminal,
just like you.

Therefore, a terminal session is suitable for:

- Pair programming
- Remote support (from a technical person)

What do you do? Open `tmux`. Tell your friend to SSH into your machine. They run
`tmux attach-session`. This assumes you only have one active session. That's it.
To quit, execute `exit` or type `Ctrl+D`.

### Purpose #3: Highly configurable

Tmux is very configurable and can be scripted to do almost anything concerning
shell organization. Look at other people's `.tmux.conf` files, merge them, and
create your own reasonable configuration.

### Purpose #4: IDE/programming workspace

Tmux can be used as an "IDE" or programming workspace. This becomes really easy
with `tmuxinator`. The idea is to center all your workflow into one place: tmux.
No need to swap windows.

## Conclusion

Stop hitting alt-tab and using the mouse. Use tmux—but only if it would boost
your productivity. Otherwise, stick to your habits.

> **Observation**: What about GNU screen? I haven't tried it. Most sources I
> read and most people I know prefer tmux, finding it more modern and powerful.

**Bonus**: Detaching from a terminal, then re-attaching to it later is useful
for monitoring servers, though there are better solutions for that.

