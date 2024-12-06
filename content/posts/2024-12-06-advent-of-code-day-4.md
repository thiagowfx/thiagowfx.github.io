---
title: "Advent of Code: Day 4"
date: 2024-12-06T11:44:39+01:00
tags:
  - dev
  - devops
---

Link to [Day #4](https://adventofcode.com/2024/day/4) puzzle.

<!--more-->

It's a pretty typical 2D matrix search problem, or a graph search problem, if
you will.

The problem is naturally unraveled into the following searches:

- horizontally
- horizontally, reversed
- vertically
- vertically, reversed
- diagonally, all 4 directions (NW, NE, SW, SE)

It's possible to write a single pair of for loops that addresses the general
case. The (classic) idea is to think of all 8 compass directions to move along
the matrix:

- (1, 0)
- (-1, 0)
- (0, 1)
- (0, -1)
- (1, 1)
- (-1, -1)
- (-1, 1)
- (1, -1)

Within the inner iteration, change `x += dx` and `y += dy` (or `i += di`, `j +=
dj`, naming is hard). I did this many times in C++ though, and I want to write
elegant Python code.

Therefore I came up with the following solution instead, with nested list
comprehensions:

```python
def search_horizontal(matrix, keyword):
    return sum((True for row in matrix for i in range(len(row) - len(keyword) + 1) if "".join(row[i:i + len(keyword)]) in [keyword, keyword[::-1]]))
```

It follows the same principle as the original intent, however it leverages
list slices so that we can omit the `dx/dy` step.

The vertical search is pretty straightforward: it is just a matter of running
the horizontal search in the transposed matrix (`zip(*matrix)`).

I must confess that using `zip` to transpose matrices always felt magical and a
mere coincidence that it just works™. Ruby has a `.transpose` method, which is
more readable.

For the diagonal search, I couldn't think of an elegant list comprehension
manner to address it. Is it even possible to "2D slice" in Python?

After-the-fact I decided to ask ChatGPT, and it is indeed possible, but it
requires NumPy:

> If a is 2-D, returns the diagonal of a with the given offset, i.e., the
> collection of elements of the form a[i, i+offset]. If a has more than two
> dimensions, then the axes specified by axis1 and axis2 are used to determine
> the 2-D sub-array whose diagonal is returned. The shape of the resulting array
> can be determined by removing axis1 and axis2 and appending an index to the
> right equal to the size of the resulting diagonals.

The method call resembles `numpy.array([[1, 2], [3, 4]]).diagonal(offset=1)`,
perhaps with the aid of `.flip()` to account for the other direction.

Anyway, my plain diagonal search is:

```python
def search_diagonal(matrix, keyword):
    rows = len(matrix)
    cols = len(matrix[0])

    count = 0

    for i in range(rows):
        for j in range(cols):
            if i + len(keyword) <= rows and j + len(keyword) <= cols:
                if "".join(matrix[i + k][j + k] for k in range(len(keyword))) in [keyword, keyword[::-1]]:
                    count += 1
            if i + len(keyword) <= rows and j - len(keyword) >= -1:
                if "".join(matrix[i + k][j - k] for k in range(len(keyword))) in [keyword, keyword[::-1]]:
                    count += 1

    return count
```

Part two is fundamentally a different problem.

One way to address it is to search for all `'A'` characters, and then look
around its "edges" to see if they contain exactly two `'M'` and two `'S'`, and
that they are properly arranged:

```python
def search_double_mas(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    count = 0

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if matrix[i][j] != 'A':
                continue

            # look at a QWERTY keyboard to make sense of these variable names
            q = matrix[i - 1][j - 1]
            e = matrix[i - 1][j + 1]
            z = matrix[i + 1][j - 1]
            c = matrix[i + 1][j + 1]
            edges = [q, e, z, c]

            if edges.count('M') != 2 or edges.count('S') != 2:
                continue

            if q == e or q == z:
                count += 1

    return count
```

I couldn't find an opportunity for reuse of the solution from part one.

The full solution:

```python
#!/usr/bin/env python3
import sys

def search_horizontal(matrix, keyword):
    return sum((True for row in matrix for i in range(len(row) - len(keyword) + 1) if "".join(row[i:i + len(keyword)]) in [keyword, keyword[::-1]]))

def search_vertical(matrix, keyword):
    return search_horizontal(zip(*matrix), keyword)

def search_diagonal(matrix, keyword):
    rows = len(matrix)
    cols = len(matrix[0])

    count = 0

    for i in range(rows):
        for j in range(cols):
            if i + len(keyword) <= rows and j + len(keyword) <= cols:
                if "".join(matrix[i + k][j + k] for k in range(len(keyword))) in [keyword, keyword[::-1]]:
                    count += 1
            if i + len(keyword) <= rows and j - len(keyword) >= -1:
                if "".join(matrix[i + k][j - k] for k in range(len(keyword))) in [keyword, keyword[::-1]]:
                    count += 1

    return count


def search_double_mas(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    count = 0

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if matrix[i][j] != 'A':
                continue

            # look at a QWERTY keyboard to make sense of these variable names
            q = matrix[i - 1][j - 1]
            e = matrix[i - 1][j + 1]
            z = matrix[i + 1][j - 1]
            c = matrix[i + 1][j + 1]
            edges = [q, e, z, c]

            if edges.count('M') != 2 or edges.count('S') != 2:
                continue

            if q == e or q == z:
                count += 1

    return count



def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    keyword = "XMAS"

    # ['abcd', 'efgh', 'ijkl'] -> [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l']]
    matrix = [list(line) for line in lines]

    # part one
    print(search_horizontal(matrix, keyword) + search_vertical(matrix, keyword) + search_diagonal(matrix, keyword))

    # part two
    print(search_double_mas(matrix))


if __name__ == '__main__':
    main()
```
