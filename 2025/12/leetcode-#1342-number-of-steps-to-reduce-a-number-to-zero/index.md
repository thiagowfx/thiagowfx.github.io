
[LeetCode #1342: Number of Steps to Reduce a Number to Zero](https://leetcode.com/problems/leetcode-#1342:-number-of-steps-to-reduce-a-number-to-zero):

```python
class Solution:
    def numberOfSteps(self, num: int) -> int:
        ans = 0

        while num != 0:
            ## if num & 1 == 0:
            if num % 2 == 0:
                ## num >>= 1
                num //= 2
            else:
                num -= 1
            ans += 1

        return ans
```

