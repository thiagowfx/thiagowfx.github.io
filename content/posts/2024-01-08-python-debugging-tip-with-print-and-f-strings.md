---
title: "Python: debugging tip with print and f-strings"
date: 2024-01-08T18:36:47+01:00
tags:
  - dev
---

It's 2024, [the year of the linux desktop](https://yotld.com/), and the best™
way to debug computer programs is still the good ol' `print` statement.

Since Python 3.6 it is possible to use
[f-strings](https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep498).

One of my favorite ways to use them for debugging is with the [equal
sign](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)
(`=`):

> To display both the expression text and its value after evaluation, (useful
> in debugging), an equal sign `'='` may be added after the expression.

Here is one example:

```python
def is_full_word_match(token, words):
    print(f'  is_full_word_match: {token=} {words=}')
    return token in words
```

If you call it like so:

```python
is_full_word_match("hello", "hello world")
```

Then it will print the following:

```
  is_full_word_match: token='hello' words='hello world'
```

This is a more ergonomic (and quicker) way to write than the classic:

```python
print('  is_full_word_match: token=' + token + ' words=' + words)
```

Or even:

```python
print('  is_full_word_match: token={} words={}'.format(token, words))
```
