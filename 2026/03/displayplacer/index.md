
[displayplacer](https://github.com/jakehilborn/displayplacer):

> macOS command line utility to configure multi-display resolutions and
> arrangements. Essentially XRandR for macOS.

Install it via homebrew:

```shell
% brew install displayplacer
```

The typical workflow is: configure displays manually first (System Settings >
Displays), then run displayplacer list to capture the current layout as a
scriptable command.

```shell
% displayplacer list
[...]
Execute the command below to set your screens to the current arrangement. If screen ids are switching, please run `displayplacer --help` for info on using contextual or serial ids instead of persistent ids.

displayplacer "id:37D8832A-2D66-02CA-B9F7-8F30A301B230 res:1728x1117 hz:120 color_depth:8 enabled:true scaling:on origin:(0,0) degree:0" "id:35EC1457-B8EA-4B42-9141-B76922632C43 res:1920x1080 hz:60 color_depth:8 enabled:true scaling:on origin:(-62,-1080) degree:0"
```

I do not have an existing use case for this but it's good to know, it could be
handy for the future.

It could be paired up with Automator.app or
[Hammerspoon](https://www.hammerspoon.org/) for automated scripting.

