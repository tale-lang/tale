from functools import reduce
from itertools import zip_longest
from typing import Any, Callable, Iterable, List


def group(iterable: Iterable[Any], by: int) -> Iterable[Iterable[Any]]:
    """Groups an iterable into chunks of the specified size.

    Args:
        iterable: An iterable that will be grouped.
        by: A size of each chunk.

    Returns:
        A sequence of tuples of the constant size with `None` representing an
        empty element.

    Examples:
        >>> list(group([1, 2, 3, 4], by=1))
        [(1,), (2,), (3,), (4,)]
        >>> list(group([1, 2, 3, 4], by=2))
        [(1, 2), (3, 4)]
        >>> list(group([1, 2, 3, 4], by=3))
        [(1, 2, 3), (4, None, None)]
    """

    args = [iter(iterable)] * by
    return zip_longest(*args)


def pipe(*funcs: List[Callable]) -> Any:
    """Composes a sequence of functions into a single pipe.

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
