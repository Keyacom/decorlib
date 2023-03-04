from src.decorlib import *

if __name__ == "__main__":
    class A: pass
    @setattr(A)
    def __repr__(self):
        return "<instance of A>"
    print(A())

    d = {}
    @setitem(d, 'func')
    def func():
        return 1
    print(d['func'])

    @call(print, MISSING)
    def empty(): pass

    cal = Caller(print, "Function:", MISSING, "Output:", MISSING, sep="\n")

    @cal.register(1)
    def plus_two(a):
        return a + 2

    cal.register(3, plus_two(1))
    cal()
