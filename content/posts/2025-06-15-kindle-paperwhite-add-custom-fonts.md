---
title: "Kindle Paperwhite: add custom fonts"
date: 2025-06-15T02:14:41+02:00
tags:
  - dev
  - serenity
---

First step, download the font you're interested in. In this example, I used
[Literata](https://fonts.google.com/specimen/Literata)[^1].

The download will be a `.zip` file. Extract it.

You're looking for `.ttf` or `.otf` files. I take note of the following font
files in the archive:

```
Literata-Italic-VariableFont_opsz,wght.ttf
Literata-VariableFont_opsz,wght.ttf
Literata-Black.ttf
Literata-BlackItalic.ttf
Literata-Bold.ttf
Literata-BoldItalic.ttf
Literata-ExtraBold.ttf
Literata-ExtraBoldItalic.ttf
Literata-ExtraLight.ttf
Literata-ExtraLightItalic.ttf
Literata-Italic.ttf
Literata-Light.ttf
Literata-LightItalic.ttf
Literata-Medium.ttf
Literata-MediumItalic.ttf
Literata-Regular.ttf
Literata-SemiBold.ttf
Literata-SemiBoldItalic.ttf
```

Second, connect the Kindle to your laptop with a USB cable[^2].

When using a macbook, you'll need a USB <-> USB-C adapter / dongle.

Open the mounted directory. There should be a top-level `fonts/` directory
within it. Dump all the aforementioned font files there.

Eject the device.

Open a book. Select the added font. ~~Profit!~~ Enjoy your pleasant read!

An interesting note: the added font has properly showed up in
[KOReader](http://koreader.rocks/), but not in the native Kindle Paperwhite
reader. Another reason [to jailbreak]({{< ref
"2025-05-17-winterbreak-hello-world" >}})?

## Appendix

A verbatim[^3] excerpt from the stock `Readme.txt` within `fonts/`:

```
You can now install your favorite fonts on your Kindle and choose one of them to read your eBooks.

Any font you install must be either an OpenType (OTF) or a TrueType (TTF) font. All other font formats are unsupported. Also, fonts are usually available as a font family and may consist of several files for different font styles - one each for Regular, Italic, Bold, BoldItalic, etc.  For the best reading experience, we recommend you install all the files in the font family. Supported font files will have .ttf, .otf, or .ttc file extensions.

How to install fonts on your Kindle:

1. If the font is packaged into a compressed file (such as a ZIP file), uncompress the files using your favorite file extracting program

2. Copy the font files into the "fonts" folder on your Kindle

3. Disconnect your Kindle from the computer

4. You can now choose a custom font in addition to the Kindle fonts from the Display Settings (Aa) menu

Once you choose a custom font from the Display Settings (Aa) menu, your Kindle will render the book content using that font for most books. If the font is not able to be used for rendering the book's content, your Kindle will use the default system font instead. This can happen if the font does not support the characters in the book or if the font is damaged.

Amazon respects the intellectual property of others. You are responsible for ensuring you have obtained the necessary rights and permissions to use any fonts you upload to your Kindle. By using the font upload functionality on Kindle, you agree that your use of the fonts you upload will not infringe or violate the rights of any third party, and that you will indemnify Amazon for all claims resulting from your use of the fonts you upload.

For further help, please visit: http://amzn.to/2F2DhMK
```

[^1]: Got this suggestion via [Reddit](https://www.reddit.com/r/kobo/comments/1ijpu75/whats_your_favorite_font/).

[^2]: The first two cables I connected did not work. Only the third one did.
    Aren't all USB cables supposed to be fungible and equivalent? Huh.

[^3]: Some blank lines were deleted, the rest is exactly as is.
