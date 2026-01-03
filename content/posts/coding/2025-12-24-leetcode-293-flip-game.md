---
title: "LeetCode #293: Flip Game"
date: 2025-12-24T17:02:58-03:00
tags:
  - dev
  - leetcode

categories:
  - coding
---

[LeetCode #293: Flip Game](https://leetcode.com/problems/flip-game):

```python
class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        s = currentState

        ans = []

        for i in range(len(s) - 1):
            j = i + 1

            if s[i] == s[j] == '+':
                ans.append(s[:i] + '--' + s[j + 1:])

        return ans
```
