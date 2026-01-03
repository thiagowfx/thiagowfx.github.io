---
title: "LeetCode #121: Best Time To Buy And Sell Stock"
date: 2025-09-07T02:06:22+02:00
tags:
  - dev
  - leetcode

categories:
  - coding
---

[LeetCode #121: Best Time To Buy And Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/):

Initially I would think that we should start with the lowest element of the
list, and then find the maximum profit from it.

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float('inf')
        i_lowest = None
        for i, p in enumerate(prices):
            if p < lowest:
                lowest = p
                i_lowest = i

        profit = 0
        for p in prices[i_lowest + 1:]:
            profit = max(profit, p - lowest)

        return profit

        # 6 4 2 1 4 3
```

The problem with this approach is evident with an input such as `[2, 4, 1]`.
This initial solution returns `0`, whereas it should return `2`.

We need to employ **two pointers**. The first pointer (`i`) tracks the lowest
element (so far), the second pointer (`j`) scans for the maximum profit. We
should update `i` only if it would result in a better profit; this helps
avoiding failing on the above scenario.

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1  # i + 1
        profit = 0

        while True:
            assert j > i  # sanity check
            if j >= len(prices):
                break

            profit = max(profit, prices[j] - prices[i])

            if prices[j] < prices[i]:
                i = j

            j += 1

        return profit
```
