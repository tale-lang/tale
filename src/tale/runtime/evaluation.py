from typing import Any, Optional

from tale.syntax.nodes import Assignment, Form, Node, Statement


class Binding:
    """A binding between a form and a value."""

    def __init__(self, form: Form, value: Node):
        self.form = form
        self.value = value


class Scope:
    """A scope of the program execution.

    Attributes:
        parent: A parent scope of the current scope.
            For example, a function scope is a parent for if statement scope.
    """


    def __init__(self, parent: Optional['Scope'] = None):
        self.parent = parent
        self.bindings = []

    def bind(self, form: Node, value: Node):
        """Binds the specified value node to the specified form.

        Args:
            form: A form that holds the binding.
            value: A value that is bound to the form.
        """

        self.bindings.append(Binding(form ,value))

    def resolve(self, node: Node):
        def resolve_assignment(x: Assignment):
            self.bind(x.form, x.value)

        def resolve_statement(x: Statement):
            child = x.children[0]

            if isinstance(child, Assignment):
                resolve_assignment(child)

        for child in node.children:
            if isinstance(child, Statement):
                resolve_statement(child)

def evaluate(node: Node) -> Any:
    """Evaluates the syntax tree node and produces the output.

    Args:
        tree: A root node of the syntax tree that represents the program.

    Returns:
        A value that represents the output of the executing program.
    """

    return Scope().resolve(node)
