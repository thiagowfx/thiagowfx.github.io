
[LeetCode #1672: Richest Customer Wealth](https://leetcode.com/problems/leetcode-#1672:-richest-customer-wealth):

```python
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(customer_accounts) for customer_accounts in accounts)
```

