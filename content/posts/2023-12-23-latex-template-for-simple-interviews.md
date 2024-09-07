---
title: "LaTeX template for simple interviews"
date: 2023-12-23T21:49:15+01:00
tags:
  - dev
---

Whenever I need to write out a simple document wherein content is more important than form, **LaTeX** is my preferred choice. It beats Google Docs, Microsoft Word, LibreOffice, or any other text processor for that matter.

<!--more-->

[Overleaf](https://www.overleaf.com/) is a solid cloud editor choice these days but I tend to prefer to have full control over my programming environment, thus for a local solution [TeXShop](https://pages.uoregon.edu/koch/texshop/) is my favorite on macOS:

```shell
$ brew install texshop
```

The following template worked well for me to answer interview questions:

```latex
% The next lines tell TeXShop to typeset with xelatex, and to open and save the source with Unicode encoding.
%!TEX TS-program = xelatex
%!TEX encoding = UTF-8 Unicode
\documentclass[12pt, oneside]{article}

\usepackage{geometry}
\geometry{letterpaper}
\usepackage{amssymb}

\usepackage{fontspec,xltxtra,xunicode}
\defaultfontfeatures{Mapping=tex-text}
\setromanfont[Mapping=tex-text]{Hoefler Text}
\setsansfont[Scale=MatchLowercase,Mapping=tex-text]{Gill Sans}
\setmonofont[Scale=MatchLowercase]{Andale Mono}

\title{My document title}
% \author{Thiago Perrotta}  % uncomment if applicable
\date{\today}

\begin{document}

\maketitle

\tableofcontents

\pagebreak

\section{Preliminaries}

\paragraph{Foo bar?}

Lorem ipsum.

\paragraph{What is the answer for life, universe and everything?}

42.
```
