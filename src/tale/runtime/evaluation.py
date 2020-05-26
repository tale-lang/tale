from typing import Any, Iterable, Optional, Tuple

from tale.runtime.objects import (TaleInt, TaleNone, TaleObject, TaleString,
                                  TaleTuple, TaleType)
from tale.syntax.nodes import (Assignment, BinaryExpression, BinaryForm,
                               Expression, Form, IntLiteral, KeywordArgument,
                               KeywordExpression, KeywordForm, Node, Parameter,
                               Parameters, PatternMatchingParameter,
                               PrimitiveExpression, PrimitiveExpressionItem,
                               PrimitiveForm, SimpleParameter, Statement,
                               StringLiteral, UnaryExpression, UnaryForm)


class CapturedArgument:
    """An argument that were captured with an expression.

    Consider looking at the `CapturedExpression` comment for more detailed docs.

    Attributes:
        name: A name of the parameter that captured the argument.
        value: A TaleObject that represents a value of the argument.
    """

    def __init__(self, name: str, value: TaleObject):
        self.name = name
        self.value = value


class CapturedExpression:
    """An expression that was captured by a form."""

    def resolve(self, scope: 'Scope') -> Any:
        """Resolves captured expression into value.

        Args:
            scope: A parent scope that needs to resolve the expression.

        Returns:
            Resolved expression.
        """


class CapturedNode(CapturedExpression):
    """An expression that was captured by a form.

    Represents captured node and arguments.

    For example, the following expression:
        1 squared
    Could be captured by the following form:
        (x) squared = x * x

    Attributes:
        form: A node that represents a form that captured the expression.
        node: A node that rerepsents a value of the form captured the expression.
            For example, `1 squared` could be captured by `(x) squared = x * x`
            form, and the `node` would represent `x * x`.
        arguments: A sequence of arguments that were captured with the
            expression.
            For example, when the `1 squared` expression is captured by
            the `(x) squared = x * x` one, arguments list would contain
            an instance of `CapturedArgument` with `name` equal to `x`, and
            `value` equal to node that represents `1`.
    """

    def __init__(self, form: Form, node: Node, arguments: Iterable[CapturedArgument] = None):
        self.form = form
        self.node = node
        self.arguments = arguments or []

    def resolve(self, scope: 'Scope') -> Any:
        """Resolves current expression in the new scope.

        Args:
            scope: A parent scope that needs to resolve the expression.

        Returns:
            Resolved expression.
        """

        scope = Scope(parent=scope)

        for arg in self.arguments:
            scope.bindings.append(ConstBinding(PrimitiveForm(arg.name), arg.value))

        return scope.resolve(self.node)


class CapturedConst(CapturedExpression):
    """A captured expression that represents an already resolved value.

    Unlike default `CapturedNode`, implements `resolve` that returns
    a predefined value.

    Attributes:
        value: A constant value.
    """

    def __init__(self, instance):
        self._instance = instance

    def resolve(self, scope: 'Scope') -> TaleObject:
        return self._instance


class Binding:
    """A binding between a form and a value."""

    def __init__(self, form: Form, value: Node):
        self.form = form
        self.value = value

    def capture(self, node: Node, scope: 'Scope') -> CapturedExpression:
        """Captures an expression if it's possible.

        Args:
            node: A node that represents an expression.

        Returns:
            An instance of `CapturedExpression` if `expression` matches the
            form of the binding, otherwise `None`.
        """

        def captures_argument(parameter: Parameter, argument: TaleObject):
            def fail():
                return (False, None)
            def ok():
                return (True, None)
            def ok_captured():
                return (True, CapturedArgument(parameter.name, argument))

            if isinstance(parameter, PatternMatchingParameter):
                if parameter.content == str(argument.py_instance):
                    return ok()

            if isinstance(parameter, SimpleParameter):
                if parameter.type_ is not None:
                    if argument.type is None:
                        return fail()
                    if parameter.type_.content != argument.type.name.py_instance:
                        return fail()

                return ok_captured()

            return fail()

        def captures_arguments(parameters: Parameters, argument: TaleObject):
            all = list(parameters.all)

            if len(all) == 1:
                if argument.type is TaleTuple:
                    return None

                captured, arg = captures_argument(all[0], argument)

                if captured:
                    return [arg] if arg is not None else []
                else:
                    return None
            else:
                if argument.type is not TaleTuple:
                    return None

                items = argument.items

                if len(all) != len(items):
                    return None

                args = []

                for parameter, item in zip(all, items):
                    captured, arg = captures_argument(parameter, item)

                    if captured:
                        if arg:
                            args.append(arg)
                    else:
                        return None

                return args

        def captures_simple(form: PrimitiveForm, node: Node):
            if form.content == node.content:
                return CapturedNode(self.form, self.value)

        def captures_unary(form: UnaryForm, node: UnaryExpression):
            if form.identifier == node.identifier:
                arg = scope.resolve(node.argument)
                args = captures_arguments(form.parameter, arg)

                if args is not None:
                    return CapturedNode(self.form, self.value, args) 

        def captures_keyword(form: KeywordForm, node: KeywordExpression):
            form_parts = list(form.parts)
            node_parts = list(node.parts)

            if len(form_parts) != len(node_parts):
                return None

            args = []

            if form.prefix is not None and node.prefix is not None:
                prefix = scope.resolve(node.prefix)
                captured_args = captures_arguments(form.prefix, prefix)

                if captured_args is None:
                    return None
                else:
                    args = args + captured_args
            elif form.prefix is not None or node.prefix is not None:
                return None

            parts = zip(form_parts, node_parts)

            for (form_name, form_arg), (node_name, node_value) in parts:
                if form_name.content != node_name.content:
                    return None

                node_value = scope.resolve(node_value)
                captured_args = captures_arguments(form_arg, node_value)

                if captured_args is not None:
                    args = args + captured_args
                else:
                    return None

            return CapturedNode(self.form, self.value, args)

        def captures_binary(form: BinaryForm, node: BinaryExpression):
            if form.operator.content != node.operator.content:
                return None

            args = []

            first_argument = scope.resolve(node.first_argument)
            second_argument = scope.resolve(node.second_argument)

            captured_args1 = captures_arguments(form.first_parameter,
                                                first_argument)
            captured_args2 = captures_arguments(form.second_parameter,
                                                second_argument)

            if captured_args1 is None or captured_args2 is None:
                return None

            args = captured_args1 + captured_args2

            return CapturedNode(self.form, self.value, args)

        form = self.form

        if isinstance(node, KeywordArgument):
            node = node.children[0]

        if isinstance(form, PrimitiveForm) and \
          (isinstance(node, PrimitiveExpression) or
           isinstance(node, PrimitiveExpressionItem)):
            return captures_simple(form, node)

        if isinstance(form, UnaryForm) and \
           isinstance(node, UnaryExpression):
            return captures_unary(form, node)

        if isinstance(form, KeywordForm) and \
           isinstance(node, KeywordExpression):
            return captures_keyword(form, node)

        if isinstance(form, BinaryForm) and \
           isinstance(node, BinaryExpression):
            return captures_binary(form, node)


class ConstBinding:
    """A binding with the constant value."""

    def __init__(self, form: Form, value: TaleObject):
        self.binding = Binding(form, Node(''))
        self.value = value

    def capture(self, node: Node, scope: 'Scope') -> CapturedExpression:
        captured = self.binding.capture(node, scope)

        if captured:
            return CapturedConst(self.value)


class PredefinedBinding:
    """A binding that is predefined as a part of the Tale's prelude."""

    def __init__(self, form: Form, func):
        self.binding = Binding(form, Node(''))
        self.func = func

    def capture(self, node: Node, scope: 'Scope') -> CapturedExpression:
        captured = self.binding.capture(node, scope)

        if captured:
            return CapturedConst(self.func(captured))


class Scope:
    """A scope of the program execution.

    Attributes:
        parent: A parent scope of the current scope.
            For example, a function scope is a parent for if statement scope.
    """

    def __init__(self, parent: Optional['Scope'] = None):
        self.parent = parent
        self.bindings = []

    def capture(self, node: Node, scope: 'Scope') -> CapturedExpression:
        """Finds a binding that could capture an expression, and captures it.

        Args:
            node: A node that represents an expression.

        Returns:
            An instance of `CapturedExpression`.
        """

        def parent_capture():
            return self.parent.capture(node, scope) if self.parent is not None else None

        captures = (x.capture(node, scope) for x in self.bindings)
        captures = (x for x in captures if x)

        return next(captures, None) or parent_capture()

    def bind(self, form: Node, value: Node):
        """Binds the specified value node to the specified form.

        Args:
            form: A form that holds the binding.
            value: A value that is bound to the form.
        """

        self.bindings.append(Binding(form, value))

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
            print(f'Assigning: {x.form.content}')
            self.bind(x.form, x.value)

        def resolve_expression(x: Expression):
            def resolved(x: Node) -> TaleObject:
                if isinstance(x.children[0], IntLiteral):
                    return TaleObject(TaleInt, int(x.content))

                if isinstance(x.children[0], StringLiteral):
                    return TaleObject(TaleString, x.content)

            def captured(x: Node) -> TaleObject:
                captured = self.capture(x, self)

                if captured:
                    return captured.resolve(scope=self)
                else:
                    return TaleObject(TaleType, x.content)

            def value(x: Node) -> TaleObject:
                return resolved(x) or captured(x)

            print('Resolving: ' + x.content)

            if isinstance(x, PrimitiveExpression):
                items = map(value, x.items)
                items = list(items)

                if len(items) == 1:
                    return items[0]
                else:
                    result = TaleObject(TaleTuple, None)
                    result.items = items
                    
                    return result

            return captured(x)

        def resolve_statement(x: Statement):
            x = x.children[0]

            if isinstance(x, Assignment):
                return resolve_assignment(x)
            if isinstance(x, Expression):
                return resolve_expression(x)

        if isinstance(node, KeywordArgument):
            node = node.children[0]

        if isinstance(node, Expression):
            return resolve_expression(node)
        if isinstance(node, PrimitiveExpressionItem):
            return resolve_expression(node)

        result = None

        for x in node.children:
            if isinstance(x, Statement):
                result = resolve_statement(x)
            if isinstance(x, Expression):
                result = resolve_expression(x)

        return result or TaleNone

def evaluate(node: Node) -> TaleObject:
    """Evaluates the syntax tree node and produces the output.

    Args:
        tree: A root node of the syntax tree that represents the program.

    Returns:
        A an output of the program.
    """

    def identifier(name) -> Node:
        return Node(name, [Node(name)])

    def simple(name: str) -> SimpleParameter:
        return SimpleParameter('', children=[Node('('), Node('x'), Node(')')]),

    def parameters(children) -> Parameters:
        return Parameters('', children)

    def unary(name: str):
        return UnaryForm(name, children=[
            parameters(simple('x')),
            identifier(name)])

    def simple_keyword(name: str):
        return KeywordForm(name, children=[
            identifier(name),
            parameters(simple('x'))])

    def binary(operator: str):
        return BinaryForm(operator, children=[
            parameters(simple('x')),
            identifier(operator),
            parameters(simple('y'))])

    def unary_type() -> PredefinedBinding:
        def execute(x: CapturedExpression):
            arg = x.arguments[0]
            return arg.value.type.name

        return PredefinedBinding(unary('type'), execute)

    def binary_plus() -> PredefinedBinding:
        def execute(x: CapturedExpression):
            a, b = x.arguments

            if a.value.type is TaleInt and a.value.type is TaleInt:
                result = a.value.py_instance + b.value.py_instance

                return TaleObject(TaleInt, result)

        return PredefinedBinding(binary('+'), execute)

    def binary_minus() -> PredefinedBinding:
        def execute(x: CapturedExpression):
            a, b = x.arguments

            if a.value.type is TaleInt and a.value.type is TaleInt:
                result = a.value.py_instance - b.value.py_instance

                return TaleObject(TaleInt, result)

        return PredefinedBinding(binary('-'), execute)

    def print_() -> PredefinedBinding:
        def execute(x: CapturedExpression):
            arg = x.arguments[0]
            print(arg.value.py_instance)

        return PredefinedBinding(simple_keyword('print'), execute)

    prelude = Scope()
    prelude.bindings.append(unary_type())
    prelude.bindings.append(binary_plus())
    prelude.bindings.append(binary_minus())
    prelude.bindings.append(print_())

    scope = Scope(parent=prelude)

    return scope.resolve(node)
