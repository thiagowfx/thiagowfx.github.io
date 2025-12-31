---
title: "LeetCode #1119: Remove Vowels from a String"
date: 2025-12-31T02:10:14-03:00
tags:
  - coding
rss: false
---

[LeetCode #1119: Remove Vowels from a String](https://leetcode.com/problems/remove-vowels-from-a-string):

```python
class Solution:
    def removeVowels(self, s: str) -> str:
        return ''.join([c for c in s if c not in 'aeiou'])
```
