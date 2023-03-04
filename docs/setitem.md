
# `setitem`

Set the `idx` item of `obj` to the decorated function or class, and returns
that function or class.

```py
d = {}
@setitem(d, 'func')
def func():
    return 1
assert d['func']() == 1
```

## Parameters

- `obj`: The object to set the attribute of.
- `idx`: The item index to be set.

## Exceptions

- `TypeError`: The object does not support subscript assignment.
