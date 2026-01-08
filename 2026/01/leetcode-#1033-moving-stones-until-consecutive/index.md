
[LeetCode #1033: Moving Stones Until Consecutive](https://leetcode.com/problems/moving-stones-until-consecutive):

Convoluted:

```python
class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        (a, b, c) = sorted([a, b, c])

        ans_max = ((c - b) - 1) + ((b - a) - 1)

        ans_min = 0
        while not ((b - a) == 1 and (c - b) == 1): ## 3 4 5
            ## 3 10 50

            if (b - a) == 1 or (c - b) == 1:
                ans_min += 1
                break

            # find smallest interval with a gap
            ## (3, 10)
            if (c - b == 1) or (b - a) <= (c - b): # left
                e1 = a
                e2 = b
                ms  = c
            else: ## right
                e1 = b
                e2 = c
                ms = a

            # move the other stone (ms) to the middle of (e1, e2)
            ms = (e1 + e2) // 2

            # update a, b, c; then keep going
            a, b, c = e1, ms, e2
            assert a < b
            assert b < c

            ans_min += 1
            if ans_min == 2:
                break

        return [ans_min, ans_max]
```

`min_ans` will be up to 2. That will significantly simplify everything!

```python
class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        (a, b, c) = sorted([a, b, c])

        ans_max = ((c - b) - 1) + ((b - a) - 1)

        ans_min = 0
        if ((b - a) == 1 and (c - b) == 1): ## 3 4 5
            ans_min = 0
        elif (b - a) in [1, 2] or (c - b) in [1, 2]: ## 3 4 6
            ans_min = 1
        else:
            ans_min = 2

        return [ans_min, ans_max]
```

