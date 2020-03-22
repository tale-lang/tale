from typing import Any

from tale.syntax import Node

class Evaluation:
    """An evaluation of a syntax tree node.

    This object handles a context and a scope of an evaluation: it knows,
    what variables are defined and where they're defined.
    It's also responsible for evaluating syntax tree nodes.
    """

    def __init__(self, node: Node):
        self.node = node

    def resolve(self, expression: Node) -> Any:
        pass

    def bind(self, assignment: Node) -> None:
        pass

    def result(self) -> Any:
        value = None

        for child in self.node.children:
            child = child.children[0]  # First `child` is always `Statement`.

            if child.name == 'Expression':
                value = self.resolve(child)
            if child.name == 'Assignment':
                value = self.bind(child)

        return value

def evaluate(tree: Node) -> Any:
    """Evaluates the syntax tree node and returns a result.

    This method is used by the `core` module after successful parsing of the syntax tree.

    Args:
        tree: A root node of the syntax tree that represents the program.
    """

    return Evaluation(tree).result()
