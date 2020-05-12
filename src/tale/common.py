from typing import Any, Callable, List
from functools import reduce


def compose(*funcs: List[Callable]) -> Any:
    def compose_(f: Callable, g: Callable):
        return lambda x: g(f(x))

    return reduce(compose_, funcs, lambda x: x)
