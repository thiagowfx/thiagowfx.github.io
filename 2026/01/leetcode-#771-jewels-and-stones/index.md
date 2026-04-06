---
title: "LeetCode #771: Jewels and Stones"
url: https://perrotta.dev/2026/01/leetcode-%23771-jewels-and-stones/
last_updated: 2026-01-07
---


[LeetCode #771: Jewels and Stones](https://leetcode.com/problems/jewels-and-stones):

Cozy:

```python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set(jewels)

        ans = 0

        for stone in stones:
            if stone in s:
                ans += 1

        return ans
```

One-liner:

```python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set(jewels)
        return sum(stone in s for stone in stones)
```

