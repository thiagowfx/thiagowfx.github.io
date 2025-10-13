---
title: "LeetCode #151: Reverse Words in a String"
date: 2025-09-10T00:22:18+02:00
tags:
  - coding
rss: false
---

[LeetCode #151: Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/):

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])
```

Note the following property of `split()`:

```python
>>> ' blue  sky '.split()
['blue', 'sky']
```

It strips leading and trailing whitespace. Furthermore, it collates multiple
whitespace characters in the middle. `.split(' ')` works as well. There's no
need to call `s.strip()`.
