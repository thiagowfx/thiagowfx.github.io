---
title: "LeetCode #1672: Richest Customer Wealth"
url: https://perrotta.dev/2025/12/leetcode-%231672-richest-customer-wealth/
last_updated: 2026-01-03
---


[LeetCode #1672: Richest Customer Wealth](https://leetcode.com/problems/leetcode-#1672:-richest-customer-wealth):

```python
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(customer_accounts) for customer_accounts in accounts)
```

