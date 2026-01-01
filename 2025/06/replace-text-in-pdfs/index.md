
**Problem statement**: Given an existing PDF file, replace text in it.

`Preview.app` on macOS cannot replace text; it can only add annotations. It is
possible to use it in a hacky way: add a white square on top of the text you
want to replace, then add another piece of text atop.

I found that [PDFGear](https://www.pdfgear.com/) does the job well. It is not
open source, but it is free. On macOS it needs to be manually downloaded and
installed from the [Mac App
Store](https://apps.apple.com/us/app/pdfgear-pdf-editor-reader/id6469021132?mt=12&os=mac&lang=en),
as it's not in Homebrew. It's also available on Windows. It is quite well-rated
in [Trustpilot](https://www.trustpilot.com/review/pdfgear.com) (4.9 stars, 6500+
reviews).

On Linux I would probably try [Xournal++](https://xournalpp.github.io/), however
it is really a PDF _annotation_ tool. It is also available on macOS: `brew
install xournal++`.

