---
title: "LeetCode #243: Shortest Word Distance"
date: 2025-12-25T05:17:07-03:00
tags:
  - dev
  - leetcode

categories:
  - coding
---

[LeetCode #243: Shortest Word Distance](https://leetcode.com/problems/shortest-word-distance):

```python
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        p1 = []  # [3]
        p2 = []  # [1, 4]

        for i , word in enumerate(wordsDict):
            if word == word1:
                p1.append(i)

            elif word == word2:
                p2.append(i)

        ans = float('inf')

        for a in p1:
            for b in p2:
                ans = min(ans, abs(a - b))

        return ans
```

Better:

```python
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        i1 = i2 = None
        ans = len(wordsDict) - 1

        for i, word in enumerate(wordsDict):
            if word == word1:
                i1 = i
            elif word == word2:
                i2 = i

            if i1 is not None and i2 is not None:
                ans = min(ans, abs(i1 - i2))

        return ans
```
