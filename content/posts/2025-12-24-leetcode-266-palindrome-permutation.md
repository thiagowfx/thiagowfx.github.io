---
title: "LeetCode #266: Palindrome Permutation"
date: 2025-12-24T17:22:36-03:00
tags:
  - coding
rss: false
---

[LeetCode #266: Palindrome Permutation](https://leetcode.com/problems/palindrome-permutation):

```python
from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        c = Counter(s)

        # only up to one odd count
        return len([v for v in c.values() if v & 1]) <= 1
```
