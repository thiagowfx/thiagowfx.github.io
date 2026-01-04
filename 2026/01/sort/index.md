
```python
a = [2, 3, 1]

assert sorted(a) == [1, 2, 3]
assert a == [2, 3, 1]

a.sort()
assert a == [1, 2, 3]

a = [2, 3, 1]
assert list(sorted(a)) == [1, 2, 3]

a = ["1", 2]
try:
    a.sort()
    assert False
except Exception:
    ...

# lexicographic
a = ["21", "3"]
assert sorted(a) == ["21", "3"]
assert(sorted(["21", "1"])) == ["1", "21"]

assert sorted([1, 2, 3], reverse=True) == [3, 2, 1]
assert sorted([1, 2, 3][::-1], reverse=True) == [3, 2, 1]
assert sorted([1, 2, 3][slice(None, None, -1)], reverse=True) == [3, 2, 1]

assert sorted([1, 2, 3], key=lambda x: -x) == [3, 2, 1]

a = [2, 3, 1]
assert a.sort(key=lambda x: -x) is None
assert a == [3, 2, 1]

def neg(x):
    return -x

assert sorted([1, 2, 3], key=neg) == [3, 2, 1]

a = ["21", "3"]
assert sorted(a, key=lambda s: len(s)) == ["3", "21"]
```

