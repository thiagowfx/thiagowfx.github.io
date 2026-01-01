
Suppose you want to take a screenshot from a web page, maybe to add to a [pull
request](https://github.com/miniflux/v2/pull/1341) of a project you're working
on.

(i) The straightforward way to do so is to use your OS tool:

- **Windows**: [Snipping
  tool](https://support.microsoft.com/en-us/windows/use-snipping-tool-to-capture-screenshots-00246869-1843-655f-f220-97299b865f6b)
  or hit the _PrintScreen_ key
- **Linux**: [`scrot`](https://github.com/resurrecting-open-source-projects/scrot) or something from your Desktop Environment (DE) such as
  `xfce4-screenshooter`. For a full-featured one, I'd recommend
  [`flameshot`](https://flameshot.org/) (first) or
  [`shutter`](https://shutter-project.org/) (second). For Wayland people seem
  to like [`grim`](https://wayland.emersion.fr/grim/).
- **macOS**: Hit `Cmd + Shift + 4` or one of its
  [variations](https://support.apple.com/en-ca/HT201361).

Even [Chromebooks](https://support.google.com/chromebook/answer/10474268?hl=en)
have a way to do so these days.

However, maybe you didn't know you can also use [Google Chrome](https://www.google.com/intl/en_ca/chrome/) to take screenshots! Here's how:

- Go to the page you want to screenshot.
- Open DevTools (`Ctrl + Shift + J` on Linux).
- Hit `Ctrl + Shift + P` à la VSCode to pop up a command bar, type 'screenshot'.
- Choose one option. I like the 'Capture area screenshot' one which allows me to drag a square for the area I want to capture.
- Hit `Enter`.

You will then be prompted where you want to save your screenshot. Profit!

