from typing import Any, Callable, List
from functools import reduce


def pipe(*funcs: List[Callable]) -> Any:
    """Composes a sequence of functions into single pipe.

    For example, a following code:

        pipe(f, g)(x)

    Is similar to:

        g(f(x))

    Args:
        funcs: A sequence of functions. 

    Returns:
        A function that pipes an input value into the first function of the sequence,
        whose result is piped into the second function, etc.
    """

    def pipe_(f: Callable, g: Callable):
        return lambda x: g(f(x))

    return reduce(pipe_, funcs, lambda x: x)
