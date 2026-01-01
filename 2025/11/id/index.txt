
Identity function:

```python
>>> help(id)
Help on built-in function id in module builtins:

id(obj, /)
    Return the identity of an object.

    This is guaranteed to be unique among simultaneously existing objects.
    (CPython uses the object's memory address.)
```

Different values have distinct IDs:

```python
>>> id(1)
4314997520
>>> id(2)
4314997552
```

Beware of mutable objects:

```python
>>> id(set())
4318516320
>>> id(set())
4318519232
```

Same ID in this case:

```python
>>> a = set()
>>> b = a
>>> assert id(a) == id(b)
```

Do not confound `id()` with `lambda x: x`. This is also an identity function,
but in the mathematical sense in that `f(x) = x`.

