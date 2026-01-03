---
title: "LeetCode #122: Best Time To Buy And Sell Stock II"
date: 2025-09-07T02:37:02+02:00
tags:
  - dev

categories:
  - coding
---

[LeetCode #122: Best Time To Buy And Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/):

[Previously]({{< ref "2025-09-07-leetcode-121-best-time-to-buy-and-sell-stock" >}}).

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1  # i + 1
        profit = 0
        total_profit = 0

        while True:
            assert j > i  # sanity check
            if j >= len(prices):
                break

            profit = max(profit, prices[j] - prices[i])

            if (prices[j] - prices[i]) > profit:
                profit = prices[j] - prices[i]
            else:
                total_profit += profit
                profit = 0
                i = j

                # 1 3 6 2 4

            j += 1

        total_profit += profit

        return total_profit
```
