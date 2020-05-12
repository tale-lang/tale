from abc import ABCMeta, abstractmethod

from tale.syntax.nodes.node import Node


class Parser(metaclass=ABCMeta):
    """A parser for the Tale language."""

    @abstractmethod
    def ast(self, code: str) -> Node:
        """Produces an abstract syntax tree from the string.

        Args:
            code: A string that represents a Tale program.

        Returns:
            An instance of `tale.syntax.nodes.node.Node` that represents
            a root of the abstract syntax tree.

        Raises:
            ValueError: If the specified `code` string is empty or represents
                an invalid Tale program.
        """
