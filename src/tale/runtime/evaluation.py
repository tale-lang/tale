from typing import Any, Iterable, Optional

from tale.syntax.nodes import (Assignment, Expression, Form, Node,
                               PrimitiveExpression, PrimitiveForm, Statement,
                               UnaryExpression, UnaryForm)


class CapturedArgument:
    def __init__(self, name: str, value: Node):
        self.name = name
        self.value = value


class CapturedExpression:
    def __init__(self, node: Node, arguments: Iterable[CapturedArgument] = None):
        self.node = node
        self.arguments = arguments or []


class Binding:
    """A binding between a form and a value."""

    def __init__(self, form: Form, value: Node):
        self.form = form
        self.value = value

    def capture(self, node: Node) -> CapturedExpression:
        """Captures an expression if it's possible.

        Args:
            node: A node that represents an expression.

        Returns:
            An instance of `CapturedExpression` if `expression` matches the
            form of the binding, otherwise `None`.
        """

        def captures_simple(form: PrimitiveForm, node: PrimitiveExpression):
            if form.content == node.content:
                return CapturedExpression(self.value)

        def captures_unary(form: UnaryForm, node: UnaryExpression):
            if form.identifier == node.identifier:
                return CapturedExpression(
                        self.value,
                        [CapturedArgument(form.argument.name, node.argument)])

        form = self.form

        if isinstance(form, PrimitiveForm) and \
           isinstance(node, PrimitiveExpression):
            return captures_simple(form, node)
        if isinstance(form, UnaryForm) and \
           isinstance(node, UnaryExpression):
            return captures_unary(form, node)


class Scope:
    """A scope of the program execution.

    Attributes:
        parent: A parent scope of the current scope.
            For example, a function scope is a parent for if statement scope.
    """

    def __init__(self, parent: Optional['Scope'] = None):
        self.parent = parent
        self.bindings = []

    def capture(self, node: Node) -> CapturedExpression:
        """Finds a binding that could capture an expression, and captures it.

        Args:
            node: A node that represents an expression.

        Returns:
            An instance of `CapturedExpression`.
        """

        captures = (x.capture(node) for x in self.bindings)
        captures = (x for x in captures if x)

        return next(captures, None)

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
        If node is an expression, then it will be converted to the value.

        Args:
            node: A node to resolve.

        Returns:
            An output of the last expression or None.
        """

        def resolve_assignment(x: Assignment):
            print('Resolving: ' + x.content)
            self.bind(x.form, x.value)

        def resolve_expression(x: Expression):
            print('Resolving: ' + x.content)
            captured = self.capture(x)

            if captured is None:
                return x.content
            else:
                scope = Scope(parent=self)

                for arg in captured.arguments:
                    scope.bind(PrimitiveForm(arg.name), arg.value)

                return scope.resolve(captured.node)

        def resolve_statement(x: Statement):
            x = x.children[0]

            if isinstance(x, Assignment):
                return resolve_assignment(x)
            if isinstance(x, Expression):
                return resolve_expression(x)

        if isinstance(node, Expression):
            return resolve_expression(node)

        result = None

        for x in node.children:
            if isinstance(x, Statement):
                result = resolve_statement(x)

        return result

def evaluate(node: Node) -> Any:
    """Evaluates the syntax tree node and produces the output.

    Args:
        tree: A root node of the syntax tree that represents the program.

    Returns:
        A an output of the program.
    """

    return Scope().resolve(node)
