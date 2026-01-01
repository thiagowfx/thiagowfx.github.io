---
title: "LeetCode #28: Find the Index of the First Occurrence in a String"
date: 2025-09-17T00:00:28+02:00
categories:
  - coding
---

[LeetCode #28: Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/):

Surely this feels like cheating:

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
```

...so long as you remember that `.find()` exists on `str`.

Hence let's also do it "the hard way" for the sake of completeness:

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i+len(needle)] == needle:
                return i

        return -1
```

It also works with `range(len(haystack))`, the form above is optimized.

We could also check for `haystack[i:].startswith(needle):` in the `if`.
