from typing import Any, Optional

from tale.syntax.nodes import Node, Assignment


class Form:
    """A form of an expression.

    Represents a template that may capture a number of expressions.

    For example, the form `(x) squared` captures `1 squared`, `2 squared`,
    `3 squared`, and so on.

    Attributes:
        node: A syntax node that represents the form.
    """

    def __init__(self, node: Node):
        self.node = node


class Scope:
    """A scope of the program execution.

    Attributes:
        parent: An object that represents parent scope of current.
            For example, an `if` expression inside a function definition
            is considered as a child scope relatively to the function.
    """

    class Binding:
        """A binding between a form and a value."""

        def __init__(self, form: Form, value: Node):
            self.form = form
            self.value = value

    def __init__(self, parent: Optional['Scope'] = None):
        self.parent = parent
        self.bindings = []

    def bind(self, form: Node, value: Node):
        self.bindings.append(Scope.Binding(form ,value))

    def resolve(self, node: Node):
        for child in node.children:
            x = child.name
            print(x)

            if isinstance(child, Assignment):
                print('asdasd')


def evaluate(node: Node) -> Any:
    """Evaluates the syntax tree node and produces the output.

    Args:
        tree: A root node of the syntax tree that represents the program.

    Returns:
        A value that represents the output of the executing program.
    """

    return Scope().resolve(node)
