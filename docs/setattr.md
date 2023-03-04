# `setattr`

Set the `name` attribute of `obj` to the decorated function or class, and
returns that function or class.

```py
class A: pass
@setattr(A)
def __repr__(self):
    return "<instance of A>"
assert repr(A()) == "<instance of A>"
```

## Parameters

- `obj`: The object to set the attribute of.
- `name`: The name of the attribute. Defaults to `None`, allowing to fall back
to the decorated function or class's `__name__`.

## Exceptions

- `AttributeError`: `name` not in `type(obj).__slots__`, or the object is
immutable.
- `TypeError`: The decorated object has no `__name__` and `name` is not a
string.
