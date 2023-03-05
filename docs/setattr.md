# `@setattr(obj, name=None, /)`

Set the `name` attribute of `obj` to the decorated function or class, and
returns that function or class.

`name` defaults to `None`, allowing to fall back to the decorated function or
class's `__name__`.

Raises `AttributeError` if `name` not in `type(obj).__slots__`, or the object is
immutable.
Raises `TypeError` if the decorated object has no `__name__` and `name` is not a
string.

```py
class A: pass
@setattr(A)
def __repr__(self):
    return "<instance of A>"
assert repr(A()) == "<instance of A>"
```