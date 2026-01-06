
[LeetCode #54: Spiral Matrix](https://leetcode.com/problems/spiral-matrix):

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        dirs = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]
        idir = 0

        m = len(matrix)
        n = len(matrix[0])

        def within_bounds(x, y, m, n):
            return 0 <= x < m and 0 <= y < n

        ans = []
        pos = [0, 0]
        new_pos = [None, None]

        ## while True
        while len(ans) < m * n:
            ans.append(matrix[pos[0]][pos[1]])
            matrix[pos[0]][pos[1]] = None

            new_pos[0] = pos[0] + dirs[idir][0]
            new_pos[1] = pos[1] + dirs[idir][1]

            if within_bounds(new_pos[0], new_pos[1], m, n) and matrix[new_pos[0]][new_pos[1]] is not None:
                pos[0] = new_pos[0]
                pos[1] = new_pos[1]
            else:
                idir = (idir + 1) % len(dirs)

                new_pos[0] = pos[0] + dirs[idir][0]
                new_pos[1] = pos[1] + dirs[idir][1]

                if within_bounds(new_pos[0], new_pos[1], m, n) and matrix[new_pos[0]][new_pos[1]] is not None:
                    pos[0] = new_pos[0]
                    pos[1] = new_pos[1]
                else:
                    return ans

        return ans
```

