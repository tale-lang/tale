from abc import ABCMeta, abstractproperty
from typing import Iterable


class Node(metaclass=ABCMeta):
    """A node of the abstract syntax tree."""

    @abstractproperty
    def children(self) -> Iterable['Node']:
        """List that represents child nodes."""
