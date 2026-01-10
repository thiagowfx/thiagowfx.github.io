
[LeetCode #286: Walls and Gates](https://leetcode.com/problems/walls-and-gates):

Level order traversal:

```python
from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])

        INF = 2 ** 31 - 1

        def bfs(x, y):
            queue = deque([(x, y)])

            dirs = [
                (0, 1),
                (1, 0),
                (0, -1),
                (-1, 0),
            ]

            def within_bounds(a, b):
                return 0 <= a < m and 0 <= b < n

            level = 0
            while queue:
                level += 1
                num_elements = len(queue)

                for _ in range(num_elements):
                    (x, y) = queue.popleft()

                    for dir in dirs:
                        neighbor = (
                            x + dir[0],
                            y + dir[1],
                        )

                        if within_bounds(neighbor[0], neighbor[1]):
                            value = rooms[neighbor[0]][neighbor[1]]

                            if value == 0 or value == -1:
                                continue

                            if level < value:
                                rooms[neighbor[0]][neighbor[1]] = level
                                queue.append((neighbor[0], neighbor[1]))



        for x, row in enumerate(rooms):
            for y, cell in enumerate(row):
                if cell == 0:
                    bfs(x, y)
```

