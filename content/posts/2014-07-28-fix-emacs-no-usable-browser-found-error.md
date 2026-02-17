---
title: 'emacs: "No Usable Browser Found" error'
date: 2014-07-28T20:20:00-03:00
tags:
  - dev
  - legacy
---

Recently I've moved from Chromium to Google Chrome on Linux. But the problem is
that emacs does not recognize it out-of-the-box. To fix this problem, you can
add the following snippet to your `.emacs:`

    (setq browse-url-generic-program (executable-find (getenv "BROWSER")) browse-url-browser-function 'browse-url-generic)

This assumes you have a defined `BROWSER` environment variable (usually auto set by your system OR somewhere in your shell startup file). This way you might change your browser later and emacs will still find the correct one. If you prefer to set your browser manually instead, you can do this:

    (setq browse-url-generic-program (executable-find "google-chrome-stable") browse-url-browser-function 'browse-url-generic)

Always evaluate `(executable-find "google-chrome-stable")` to make sure the
browser path was correctly found. Adapted from
http://www.fettesps.com/emacs-resolving-the-no-usable-browser-found-error/.
