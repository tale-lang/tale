from typing import Any, Optional

from tale.syntax.nodes import Assignment, Expression, Form, Node, Statement


class Binding:
    """A binding between a form and a value."""

    def __init__(self, form: Form, value: Node):
        self.form = form
        self.value = value

    def captures(self, expression: str) -> bool:
        """Checks whether the form of the binding could capture an expression.

        Args:
            expression: A string that represents a piece of code.

        Returns:
            `True` if `expression` could be catured by `form`, otherwise `False`.
        """

        return self.form.content == expression


class Scope:
    """A scope of the program execution.

    Attributes:
        parent: A parent scope of the current scope.
            For example, a function scope is a parent for if statement scope.
    """


    def __init__(self, parent: Optional['Scope'] = None):
        self.parent = parent
        self.bindings = []

    def binding(self, expression: str):
        """Finds a binding that could capture an expression.

        Args:
            expression: An expression to capture.

        Returns:
            An instance of `Binding`.
        """

        for binding in self.bindings:
            if binding.captures(expression):
                return binding

    def bind(self, form: Node, value: Node):
        """Binds the specified value node to the specified form.

        Args:
            form: A form that holds the binding.
            value: A value that is bound to the form.
        """

        self.bindings.append(Binding(form ,value))

    def resolve(self, node: Node) -> Any:
        """Processes a syntax node.

        If node is an assignment, then the new binding will be created in the
        scope.
        If node is an expression, then it will be resolved.

        Args:
            node: A node to resolve.

        Returns:
            An output of the last expression or None.
        """

        def resolve_assignment(x: Assignment):
            self.bind(x.form, x.value)

        def resolve_expression(x: Expression):
            binding = self.binding(x.content)

            if binding is None:
                return x.content
            else:
                return resolve_expression(binding.value)

        def resolve_statement(x: Statement):
            x = x.children[0]

            if isinstance(x, Assignment):
                return resolve_assignment(x)
            if isinstance(x, Expression):
                return resolve_expression(x)

        result = None

        for child in node.children:
            if isinstance(child, Statement):
                result = resolve_statement(child)

        return result

def evaluate(node: Node) -> Any:
    """Evaluates the syntax tree node and produces the output.

    Args:
        tree: A root node of the syntax tree that represents the program.

    Returns:
        A an output of the program.
    """

    return Scope().resolve(node)
