
[LeetCode #200: Number of Islands](https://leetcode.com/problems/number-of-islands):

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def within_bounds(a, b):
            return 0 <= a < m and 0 <= b < n

        def dfs(x, y):
            if not within_bounds(x, y):
                return

            if grid[x][y] in ["-1", "0"]:
                return

            grid[x][y] = "-1"

            for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                neighbor = (
                    x + dir[0],
                    y + dir[1],
                )
                dfs(neighbor[0], neighbor[1])

        ans = 0

        for x, row in enumerate(grid):
            for y, cell in enumerate(row):
                if grid[x][y] == "1":
                    dfs(x, y)
                    ans += 1

        return ans
```

