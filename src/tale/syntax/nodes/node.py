from abc import ABCMeta, abstractproperty
from typing import Iterable


class Node(metaclass=ABCMeta):
    """A node of the abstract syntax tree."""

    @abstractproperty
    def children(self) -> Iterable['Node']:
        """Child nodes of the current.

        Returns:
            An iterable where each element represents a child node of the
            current.
        """
