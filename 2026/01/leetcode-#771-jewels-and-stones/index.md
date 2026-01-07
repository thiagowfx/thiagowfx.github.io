
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

