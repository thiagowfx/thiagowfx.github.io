---
title: "LeetCode #58: Length of Last Word"
date: 2025-09-17T00:19:08+02:00
tags:
  - coding
---

[LeetCode #58: Length of Last Word](https://leetcode.com/problems/length-of-last-word/):

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
```

`.split()` acts on whitespace by default. It is equivalent to `.split(' ')`.

Previously:

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])
```

It turns out `.strip()` is not really necessary.
