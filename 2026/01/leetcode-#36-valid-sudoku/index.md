
[LeetCode #36: Valid Sudoku](https://leetcode.com/problems/valid-sudoku):

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = len(board)
        n = len(board[0])

        def is_valid(a):
            a = [el for el in a if el != "."]
            ## [1, 2, 2] -> 3
            ## {1, 2}    -> 2
            ##
            ## [1, 2]
            ## {1, 2}
            return len(a) - len(set(a)) == 0

        for row in board:
            if not is_valid(row):
                return False

        for col in zip(*board):
            if not is_valid(col):
                return False

        subgrids_i = [
            [0, 0],
            [0, 3],
            [0, 6],
            [3, 0],
            [3, 3],
            [3, 6],
            [6, 0],
            [6, 3],
            [6, 6],
        ]

        for subgrid_i in subgrids_i:
            subgrid = []

            for x in range(3):
                for y in range(3):
                    ix = subgrid_i[0] + x
                    iy = subgrid_i[1] + y
                    subgrid.append(board[ix][iy])

            if not is_valid(subgrid):
                return False

        return True
```

