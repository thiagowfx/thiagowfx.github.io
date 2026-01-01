---
title: "LeetCode #344: Reverse String"
date: 2025-12-26T16:55:43-03:00
rss: false
categories:
  - coding
---

[LeetCode #344: Reverse String](https://leetcode.com/problems/reverse-string):

It needs to be done in-place.

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = reversed(s)
```

Or swap characters one by one:

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]
```

Recursively:

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverseString(s, a, b):
            if b - a >= 1:
                s[a], s[b] = s[b], s[a]
                reverseString(s, a  + 1, b - 1)

        return reverseString(s, 0, len(s) - 1)
```
