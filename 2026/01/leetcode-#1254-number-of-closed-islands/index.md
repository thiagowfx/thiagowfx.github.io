
[LeetCode #1254: Number of Closed Islands](https://leetcode.com/problems/number-of-closed-islands):

```python
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def within_bounds(a, b):
            return 0 <= a < m and 0 <= b < n

        def dfs(x, y, poisoned=False):
            if not within_bounds(x, y):
                return True

            if grid[x][y] in [-1, 1]:
                return False

            grid[x][y] = -1

            for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                neighbor = (
                    x + dir[0],
                    y + dir[1],
                )
                if dfs(neighbor[0], neighbor[1]):
                    poisoned = True

            return poisoned

        ans = 0

        for x, row in enumerate(grid):
            for y, cell in enumerate(row):
                if grid[x][y] == 0:
                    if not dfs(x, y):
                        ans += 1

        return ans
```

