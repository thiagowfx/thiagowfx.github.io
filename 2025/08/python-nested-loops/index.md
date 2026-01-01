
Given a list `v = [1, 2, 3, 4]`, use a double nested[^1] loop to iterate over
every pair of its elements, in order.

[^1]: Doubly-nested?

In other words, the iteration must yield the following deterministic order:

- 1, 2
- 1, 3
- 1, 4
- 2, 3
- 2, 4
- 3, 4

## C/C++ style

Use indexes + `range`:

```python
for i in range(len(v)):
    for j in range(i + 1, len(v)):
        print(v[i], v[j])

1 2
1 3
1 4
2 3
2 4
3 4
```

## C/C++ style, but iterating directly

We could use `enumerate`:

```python
for i, a in enumerate(v):
    for b in v[i + 1:]:
        print(a,b)
```

It is not an objectively superior improvement to the previous form, but at least
we avoid `range` and `len`.

## `itertools`

```python
for a, b in itertools.combinations(v, 2):
  print(a,b)
```

Discrete Mathematics `combinations` provides an elegant one-liner for this
situation. The second argument controls how many elements to include per tuple,
for comparison:

```python
>>> list(itertools.combinations(v, 3))
[(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
```

