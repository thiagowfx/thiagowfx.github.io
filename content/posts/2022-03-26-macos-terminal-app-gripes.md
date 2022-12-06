---
title: "macOS terminal app gripes"
date: 2022-03-26T02:28:15-03:00
tags:
  - dev
  - macos
---

`Terminal.app` is a pretty decent terminal emulator for macOS, with sensible defaults. There's absolutely no need to install [`iTerm2`](https://iterm2.com/). I see many people doing it right away when getting a Macbook, but in my opinion it is unnecessarily bloated.

That said, I have my own gripes for `Terminal.app`, but the list is surprisingly small.

<!--more-->

## 1. No OSC-52 support

https://github.com/roy2220/osc52pty:

> OSC 52 is one of Xterm Control Sequences, which is designated for clipboard setting. Once a terminal supporting OSC 52 catches a text in the form of OSC 52 from the output, instead of printing the text onto the screen, it decodes the text first and then sends the content to the system clipboard.

> Although `Terminal.app` does NOT support OSC 52, here [osc52pty] is the workaround for it.

I dislike this workaround because it requires an external binary. Even though it is a single binary because it is a Golang executable, I still dislike the external dependency.

## 2. No true color (256 colors)

What is true color? See [stack overflow](https://stackoverflow.com/questions/6403744/are-there-terminals-that-support-true-color) for context.

Run the [following](https://gist.github.com/XVilka/8346728) to print a color band, a smooth (gradient) output indicates true color support:

```shell
awk 'BEGIN{
    s="/\\/\\/\\/\\/\\"; s=s s s s s s s s;
    for (colnum = 0; colnum<77; colnum++) {
        r = 255-(colnum*255/76);
        g = (colnum*510/76);
        b = (colnum*255/76);
        if (g>255) g = 510-g;
        printf "\033[48;2;%d;%d;%dm", r,g,b;
        printf "\033[38;2;%d;%d;%dm", 255-r,255-g,255-b;
        printf "%s\033[0m", substr(s,colnum+1,1);
    }
    printf "\n";
}'
```

`Terminal.app` will not print a gradient.

## 3. No GPU acceleration

https://unix.stackexchange.com/q/658709:

> Q: What are the advantages of hardware-accelerated terminal emulators?

> A: They can potentially be faster at outputting and refreshing vast amounts of information. It could also allow for smooth(er) scrolling. Human beings however are quite slow at reading this information, [...] the average person is unlikely to be able to comprehend it anyways. CPU usage could be lower but it needs to be tested.

`Terminal.app` isn't GPU accelerated.

## Recommendations

Both [alacritty][alacritty] and [kitty][kitty] are decent replacements (or complements) for `Terminal.app` that work out-of-the-box, with sensible defaults including all the aforementioned points.


[alacritty]: https://alacritty.org
[kitty]: https://sw.kovidgoyal.net/kitty/
