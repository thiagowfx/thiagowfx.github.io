---
title: "LeetCode #293: Flip Game"
url: https://perrotta.dev/2025/12/leetcode-%23293-flip-game/
last_updated: 2026-01-03
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

