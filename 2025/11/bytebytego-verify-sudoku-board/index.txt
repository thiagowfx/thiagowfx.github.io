
[ByteByteGo: Verify Sudoku Board](https://bytebytego.com/exercises/coding-patterns/hash-maps-and-sets/verify-sudoku-board):

```python
from typing import List

def verify_sudoku_board(board: List[List[int]]) -> bool:
    row_sets = [set() for _ in range(9)]
    col_sets = [set() for _ in range(9)]
    grid_sets = [[set() for _ in range(3)] for _ in range(3)]

    for x in range(len(board)):
        for y in range(len(board[0])):
            c = board[x][y]
            if c == 0:
                continue

            if c in row_sets[x]:
                return False
            else:
                row_sets[x].add(c)

            if c in col_sets[y]:
                return False
            else:
                col_sets[y].add(c)

            if c in grid_sets[x // 3][y // 3]:
                return False
            else:
                grid_sets[x // 3][y // 3].add(c)

    return True
```

