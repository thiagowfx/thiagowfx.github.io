---
title: "LeetCode #1119: Remove Vowels from a String"
url: https://perrotta.dev/2025/12/leetcode-%231119-remove-vowels-from-a-string/
last_updated: 2026-01-03
---


[LeetCode #1119: Remove Vowels from a String](https://leetcode.com/problems/remove-vowels-from-a-string):

```python
class Solution:
    def removeVowels(self, s: str) -> str:
        return ''.join([c for c in s if c not in 'aeiou'])
```

