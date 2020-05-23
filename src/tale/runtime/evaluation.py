from typing import Any, Iterable, Optional

from tale.syntax.nodes import (Assignment, Expression, Form, KeywordExpression,
                               KeywordForm, Node, PrimitiveExpression,
                               PrimitiveForm, Statement, UnaryExpression,
                               UnaryForm)


class CapturedArgument:
    """An argument that were captured with an expression.

    Consider looking at the `CapturedExpression` comment for more detailed docs.

    Attributes:
        name: A name of the argument.
        value: A node that represents an actual value of the argument.
    """

    def __init__(self, name: str, value: Node):
        self.name = name
        self.value = value


class CapturedExpression:
    """An expression that was captured by a form.

    Represents captured node and arguments.

    For example, the following expression:
        1 squared
    Could be captured by the following form:
        (x) squared = x * x

    Attributes:
        node: A node that rerepsents a value of the form captured the initial
            expression.
            For example, `1 squared` could be captured by `(x) squared = x * x`
            form, and the `node` would represent `x * x`.
        arguments: A sequence of arguments that were captured with the
            expression.
            For example, when the `1 squared` expression is captured by
            the `(x) squared = x * x` one, arguments list would contain
            an instance of `CapturedArgument` with `name` equal to `x`, and
            `value` equal to node that represents `1`.
    """

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

        def captures_keyword(form: KeywordForm, node: KeywordExpression):
            form_parts = list(form.parts)
            node_parts = list(node.parts)

            captured = []

            if len(form_parts) != len(node_parts):
                return None
            if form.prefix is not None and node.prefix is None:
                return None
            if form.prefix is None and node.prefix is not None:
                return None
            if form.prefix is not None and node.prefix is not None:
                captured.append(CapturedArgument(
                    form.prefix.name,
                    node.prefix))

            parts = iter(node_parts)

            for name, arg in form_parts:
                node_name, node_arg = next(parts)

                if name.content != node_name.content:
                    return None

                captured.append(CapturedArgument(arg.name, node_arg))

            return CapturedExpression(self.value, captured)

        form = self.form

        if isinstance(form, PrimitiveForm) and \
           isinstance(node, PrimitiveExpression):
            return captures_simple(form, node)

        if isinstance(form, UnaryForm) and \
           isinstance(node, UnaryExpression):
            return captures_unary(form, node)

        if isinstance(form, KeywordForm) and \
           isinstance(node, KeywordExpression):
            return captures_keyword(form, node)


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
