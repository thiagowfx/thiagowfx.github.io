
```python
assert ... == ...
assert ... == Ellipsis

a = [1, 2, 3]

# RHS: iterable unpacking
b = [1, *a]
assert b == [1, 1, 2, 3]

# LHS: starred unpacking
b, *rest = a
assert b == 1

# LHS: starred unpacking
b, *_ = a
assert b == 1

(a, _, _, b) = [1, 2, 3, 4]
assert a == 1
assert b == 4

# does not work
# (a, *_, b, *_) = [1, 2, 3, 4, 5]

(a, *_, b) = [1, 2, 3, 4, 5]
assert a == 1
assert b == 5
```

