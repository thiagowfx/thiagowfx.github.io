
**Problem statement**: Given a `.png` image suitable to be used as a profile
picture (an avatar in a forum, for example), convert it to 80x80, ensure its
file size is under 10KiB and keep its transparency when existing. The extension
should remain `.png`.

This kind of task is perfect for the LLM™. It took me a few round-trip prompts
to achieve the desired outcome:

```shell
% magick image.png -resize 80x80 -fuzz 10% -transparent white
% pngquant --quality=70-85 --force --output image.png
```

`magick` comes from [ImageMagick](https://imagemagick.org/index.php). Most
likely you already have it installed if you're in Linux or macOS.

**Fun fact**: the command used to be called `convert` (it is still in my muscle
memory!) but not in newer versions of ImageMagick:

```shell
% convert
WARNING: The convert command is deprecated in IMv7, use "magick" instead of "convert" or "magick convert"
[...]
```

[`pngquant`](https://pngquant.org/) is new to me:

> pngquant is a command-line utility and a library for lossy compression of PNG
> images.
>
> The conversion reduces file sizes significantly (often as much as 70%) and
> preserves full alpha transparency. Generated images are compatible with all
> web browsers and operating systems.

In my little experiment:

* input: 52KB, 256 x 256 pixels
* [output](https://bbs.archlinux.org/img/avatars/73061.png?m=1750766467): 4.1KB, 80 x 80 pixels, with transparent background

