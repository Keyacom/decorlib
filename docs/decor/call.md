# `@call(fn: Callable[..., Any], /, *args: object, **kwargs: object)`

Call `fn` with `args` and `kwargs`, substituting each `MISSING` definition with
the decorated function or class, and returns that function or class.

Raises `TypeError` if `fn` is not callable.
Raises `likepep403.MissingRequired` if there is no `MISSING` definition in
either `args` or `kwargs`.

```py
@call(print, MISSING)
def empty():
    pass
```
