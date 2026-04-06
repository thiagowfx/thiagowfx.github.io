---
title: "LeetCode #151: Reverse Words in a String"
url: https://perrotta.dev/2025/09/leetcode-%23151-reverse-words-in-a-string/
last_updated: 2026-01-03
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

