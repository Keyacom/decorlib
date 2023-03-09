from likepep403 import *
from collections.abc import Callable

if __name__ == "__main__":

    class A:
        pass

    @setattr(A)
    def __repr__(self):
        return "<instance of A>"

    print(A())

    d: dict[str, Callable] = {}

    @setitem(d, "func")
    def func():
        return 1

    print(d["func"]())

    @call(print, MISSING)
    def empty():
        pass

    cal = Caller(print, "Function:", MISSING, "Output:", MISSING, sep="\n")

    @cal.register(1) # type: ignore
    def plus_two(a):
        return a + 2

    cal.register(3, plus_two(1))
    cal()

    assert MISSING == MISSING

    assert isinstance([], SupportsSetitem)
    assert isinstance({}, SupportsSetitem)
