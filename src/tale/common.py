from typing import Any, Callable, List
from functools import reduce


def pipe(*funcs: List[Callable]) -> Any:
    def pipe_(f: Callable, g: Callable):
        return lambda x: g(f(x))

    return reduce(pipe_, funcs, lambda x: x)
