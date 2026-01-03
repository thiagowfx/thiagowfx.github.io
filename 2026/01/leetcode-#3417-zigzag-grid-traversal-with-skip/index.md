
[LeetCode #3417: Zigzag Grid Traversal With Skip](https://leetcode.com/problems/zigzag-grid-traversal-with-skip):

Initial:

```python
class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        x = 0
        y = 0

        m = len(grid)
        n = len(grid[0])

        direction = +1

        ans = []
        include = False

        while x < m:
            include = not include
            if include:
                ans.append(grid[x][y])

            next_y = y + direction

            if next_y >= n:
                x += 1
                y = n - 1
                direction = -1
            elif next_y < 0:
                x += 1
                y = 0
                direction = +1
            else:
                ## x += 0
                y += direction

        return ans
```

Simplified:

```python
class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        x = 0
        y = 0

        m = len(grid)
        n = len(grid[0])

        direction = +1

        ans = []
        include = False

        while x < m:
            include = not include
            if include:
                ans.append(grid[x][y])

            ## x += 0
            y += direction

            if y >= n:
                x += 1
                y = n - 1
                direction = -1
            elif y < 0:
                x += 1
                y = 0
                direction = +1

        return ans
```

