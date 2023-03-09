# `Caller(fn, /, *args, **kwargs)`

A class that can be used to call `fn` with other functions, registered using
the `.caller` method, as arguments. When a caller is created, the `args` and
`kwargs` are saved in the object.

```py
cal = Caller(print, "Function:", MISSING, "Output:", MISSING, sep="\n")

@cal.register(1)
def plus_two(a):
    return a + 2

cal.register(3, plus_two(1))
cal()
```

## `Caller.call()`<br>`Caller.exec()`<br>`Caller()`

Executes the caller with the registered arguments.

## `@Caller.register(idx: str | int | tuple[()], /) -> Callable`<br>`Caller.register(idx: str | int | tuple[()], item, /) -> None`

Registers `item` as an argument `idx`.

If `idx` is a string, registers it in the caller's `kwargs`. If it's an integer,
it's registered in the `args` instead.

If `idx` is an empty tuple or a number equal to `len(args)`, the item
is appended to `args`.

If it's neither of these three types, a `TypeError` is raised.

### As a decorator

Registers the decoratee as an argument `idx`, and returns it.
