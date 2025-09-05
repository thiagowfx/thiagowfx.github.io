---
title: "The fundamental right to paste"
date: 2024-01-22T18:55:13-03:00
tags:
  - dev
---

Some websites attempt to prevent users from pasting text (i.e. `Ctrl+V` /
`Cmd+V`) in web browsers.

It serves no purpose in most cases other than hindering accessibility and
increasing annoyance for users.

It is relatively easy to bypass most trivial blocks with plain JavaScript. Open a DevTools console (`Option + Cmd + I` in Google Chrome on macOS), then paste in the following snippet:

```javascript
function () {
  const forceEnableCopyPaste = (e) => {
    e.stopImmediatePropagation();
    return true;
  };

  ['paste', 'copy'].forEach(event => {
    document.addEventListener(event, forceEnableCopyPaste, true);
  });
})();
```

**Bonus points**: it also works for copying text.

I can see the point of trying to attempt to block copying (e.g. copyright,
online exams), but there's little reason to prevent pasting.

The only _arguably valid_ use case I've seen to date for blocking pasting is
in some sign-up forms wherein you need to type in some piece of user ID (e.g.
your email, or your telephone number) twice. The second text field is
sometimes blocked, as to _encourage_ you to double check it is absolutely
correct™, by the means of carefully typing it out.

The snippet above could also be easily converted to a bookmarklet.

Search for "bookmarklet builder" in your favorite search engine, go to a website such as https://caiorss.github.io/bookmarklet-maker/, paste the above snippet therein, then get a compressed version such as:

```javascript
javascript:(function()%7Bjavascript%3A%20(function%20()%20%7B%0A%20%20const%20forceEnableCopyPaste%20%3D%20(e)%20%3D%3E%20%7B%0A%20%20%20%20e.stopImmediatePropagation()%3B%0A%20%20%20%20return%20true%3B%0A%20%20%7D%3B%0A%0A%20%20%5B'paste'%2C%20'copy'%5D.forEach(event%20%3D%3E%20%7B%0A%20%20%20%20document.addEventListener(event%2C%20forceEnableCopyPaste%2C%20true)%3B%0A%20%20%7D)%3B%0A%7D)()%3B%7D)()%3B
```

Now just create a web browser favorite with that resource. Clicking the
bookmark will yield the same effect as pasting the snippet into devtools.
