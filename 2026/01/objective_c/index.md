
```python
def mysum(a, b):
    return a + b
assert mysum(1, 2) == 3

try:
    assert mysum(1, 2, 3) == 3
    assert False
except Exception:
    ...

def mysum(a, b, *args):
    return a + b
assert mysum(1, 2) == 3
assert mysum(1, 2, 3) == 3

def mysum(a, b, *args):
    return a + b + sum(args)
assert mysum(1, 2) == 3
assert mysum(1, 2, 3) == 6

def mysum(*args):
    return sum(args)
assert mysum(1, 2) == 3
assert mysum(1, 2, 3) == 6
assert mysum() == 0

# all arguments that follow are keyword arguments
def mysum(*, a, b):
    return a + b
assert mysum(a=1, b=2) == 3
try:
    assert mysum(1, 2) == 3
except Exception:
    ...
```

