---
title: "Recording screencasts on Linux"
date: 2015-03-21T18:03:48+00:00
tags:
  - dev
  - legacy
---

One-line self-documenting functions, put this into your shell init file:

```shell
# ffmpeg x11 screencasting
# it will just record video: no audio
# dimensions of your screen are automatically calculated
_ffmpeg-screencast() {
 ffmpeg -f x11grab -s $(xdpyinfo | awk '/dimensions:/ {print $2}') -r 25 -i :0.0 -qscale 0 $HOME/ffmpeg-out-$(date '+%Y-%m-%d-%H-%M-%S').mkv
}

# ffmpeg x11 screencasting with audio
# it supersedes the previous function
# source of the audio is determined with `pavucontrol`: open it then go to the "recording" tab. You can select between the microphone or your computer as audio sources
_ffmpeg-screencast-audio() {
 ffmpeg -f alsa -i pulse -acodec pcm_s16le -f x11grab -s $(xdpyinfo | awk '/dimensions:/ {print $2}') -r 25 -i :0.0 -qscale 0 $HOME/ffmpeg-out-$(date '+%Y-%m-%d-%H-%M-%S').mkv
}
```

## Observations

1. If you want to get this automatically, you might be interested in my
dotfiles repo. In particular, inspect the .alias file, where those functions
are located (at least at the time of this post; things change).
2. Audio recording works best with Pulse Audio (citation needed). I haven't
tested with alsa only.
3. Pavucontrol is just a fancy interface for configuring pulseaudio, but there
are others.
4. Tweak those parameters...ffmpeg is a really powerful tool.
5. I tested this on the i3 window manager, and it works beautifully. I tested
some GUI screencasting programs on it before and the results were poor.
6. Source of this script: a merge of several ones on the web.

Oh yes, and you can stop the screen capturing with the 'q' key or with a
classical Control-C.

**Edit:** thanks Victor for a small improvement with `awk` in the above
functions.
