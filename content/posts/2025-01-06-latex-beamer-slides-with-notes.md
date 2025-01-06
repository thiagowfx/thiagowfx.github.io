---
title: "LaTeX beamer slides with notes"
date: 2025-01-06T01:02:56-03:00
tags:
  - dev
---

([via Andrej Bauer](https://gist.github.com/andrejbauer/ac361549ac2186be0cdb) from University of Ljubljana, adapted):

```tex
\documentclass[12pt]{beamer}

\usepackage{pgfpages}

%\setbeameroption{hide notes} % Only slides
%\setbeameroption{show only notes} % Only notes
\setbeameroption{show notes on second screen=right} % Both

% Give a slight yellow tint to the notes page
\setbeamertemplate{note page}{\pagecolor{yellow!5}\insertnote}\usepackage{palatino}

\title{How to make Beamer slides with notes}
\author{Thiago Perrotta\\Universidade Federal do Rio de Janeiro}
\date{\small \today}

\begin{document}

\begin{frame}
  \titlepage

  \note[item]{Thank the audience for being awake.}
\end{frame}

\begin{frame}
  \begin{itemize}
  \item Here are
  \item some very boring bullets
  \item about nothing.
  \end{itemize}

  \note[item]{Note that this slide is boring.}

  \note[item]{Observe that there are no actual bullets here.}

  \note[item]{Future work: add another bullet.}
\end{frame}

\end{document}
```

I created a sample LaTeX project on [Overleaf](https://www.overleaf.com/)
because I did not want to install the full [texlive](https://tug.org/texlive/)
suite on my Mac.

It compiled successfully and worked beautifully.

The workflow is: 1) Generate the notes:

```
\setbeameroption{hide notes} % Only slides
%\setbeameroption{show only notes} % Only notes
%\setbeameroption{show notes on second screen=right} % Both
```

2) Generate the slides:

```
%\setbeameroption{hide notes} % Only slides
\setbeameroption{show only notes} % Only notes
%\setbeameroption{show notes on second screen=right} % Both
```

Then present the slides in the projector whilst keeping the notes open in your
laptop.

The author suggests to use [Skim.app](https://skim-app.sourceforge.io/) to sync
both documents. It's a good idea, I had used it at the time when I wrote my
undergrad thesis.

Overleaf is quite different today than from 8 years ago:

- There is a visual editor (ala [LyX](https://www.lyx.org/)[^1])
- There's first-class integration with Academia (Zotero, Mendeley)
- There's an [AI-based language feedback
  feature](https://www.overleaf.com/learn/how-to/Writefull_integration) (is this
  surprising in 2025?)
- There's first-class git integration / github sync

Very cool!

[^1]: I used to love LyX. It used to be my favorite way to create slides /
    presentations for university. I am happy to see it's still under active
    development.
