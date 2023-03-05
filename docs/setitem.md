
# `@setitem(obj, idx, /)`

Set the `idx` item of `obj` to the decorated function or class, and returns
that function or class. Raises `TypeError` if `obj` does not support subscript
assignment.

```py
d = {}
@setitem(d, 'func')
def func():
    return 1
assert d['func']() == 1
```
