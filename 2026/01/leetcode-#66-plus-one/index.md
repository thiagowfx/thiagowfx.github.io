
[LeetCode #66: Plus One](https://leetcode.com/problems/plus-one):

One-liner:

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(d) for d in str(int(''.join([str(d) for d in digits])) + 1)]
```

Keep the list structure:

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ## return [int(d) for d in str(int(''.join([str(d) for d in digits])) + 1)]

        inc = 1
        for i, digit in list(enumerate(digits))[::-1]:
            # [4, 2, 9]
            # [4, 2, 1]

            digits[i] += inc
            if digits[i] == 10:
                digits[i] = 0
                ## inc = 1
            else:
                inc = 0
                break

        if inc == 1:
            digits = [1] + digits

        return digits
```

