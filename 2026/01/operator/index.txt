
```python
import operator

if __name__ == "__main__":
    assert operator.add(1, 2) == 3
    assert operator.__add__(1, 2) == 3
    assert operator.sub(1, 2) == -1
    assert operator.mul(3, 2) == 6
    assert operator.abs(-3) == 3
    assert operator.concat("a", "b") == "ab"
    assert operator.contains([1, 2], 1)
    assert operator.eq(1, 1)
    assert operator.le(1, 1)
    assert operator.le(1, 2)
    assert operator.lt(1, 2)
    assert operator.truediv(6, 2) == 3
```

