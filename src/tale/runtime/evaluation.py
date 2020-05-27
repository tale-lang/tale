from typing import Any, Iterable, Optional, Tuple
from abc import ABCMeta, abstractmethod

from tale.runtime.objects import (TaleInt, TaleNone, TaleObject, TaleString,
                                  TaleTuple, TaleType)
from tale.syntax.nodes import (Assignment, BinaryExpression, BinaryForm,
                               Expression, Form, IntLiteral, KeywordArgument,
                               KeywordExpression, KeywordForm, Node, Parameter,
                               PatternMatchingParameter, PrimitiveExpression,
                               PrimitiveExpressionItem, PrimitiveForm,
                               SimpleParameter, Statement, StringLiteral,
                               TupleParameter, UnaryExpression, UnaryForm)


class Captured(metaclass=ABCMeta):
    """An expression that was captured by a form."""

    @abstractmethod
    def resolve(self, scope: 'Scope') -> TaleObject:
        """Resolves captured expression into value.

        Args:
            scope: A parent scope that needs to resolve the expression.

        Returns:
            Resolved expression.
        """


class CapturedNode(Captured):
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

    def __init__(self, form: Form, node: Node, arguments: Iterable['CapturedArgument'] = None):
        self.form = form
        self.node = node
        self.arguments = arguments or []

    def resolve(self, scope: 'Scope') -> TaleObject:
        """Resolves current expression in the new scope.

        Args:
            scope: A parent scope that needs to resolve the expression.

        Returns:
            Resolved expression.
        """

        scope = Scope(parent=scope)

        for arg in self.arguments:
            arg.bind(scope)

        return scope.resolve(self.node)


class CapturedConst(Captured):
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


class CapturedArgument(metaclass=ABCMeta):
    """An argument that were captured within an expression.

    Attributes:
        name: A name of the parameter that captured the argument.
        value: A TaleObject that represents a value of the argument.
    """

    @abstractmethod
    def bind(self, scope: 'Scope'):
        """Binds a captured argument into the scope."""


class CapturedSingle(CapturedArgument):
    """A captured single argument."""

    def __init__(self, name: str, value: TaleObject):
        self.name = name
        self.value = value

    def bind(self, scope: 'Scope'):
        form = PrimitiveForm(self.name)
        value = self.value

        scope.bindings.append(ConstBinding(form, value))


class CapturedTuple(CapturedArgument):
    """A captured argument that represents a tuple."""

    def __init__(self, args: CapturedArgument):
        self.args = args

    def bind(self, scope: 'Scope'):
        for arg in self.args:
            arg.bind(scope)


class BoundParameter(metaclass=ABCMeta):
    """A parameter that is a part of a bound form."""

    @staticmethod
    def of(parameter: Parameter) -> 'BoundParameter':
        if isinstance(parameter, SimpleParameter):
            return SimpleBoundParameter(parameter)
        if isinstance(parameter, PatternMatchingParameter):
            return PatternMatchingBoundParameter(parameter)
        if isinstance(parameter, TupleParameter):
            return TupleBoundParameter(parameter)

    @abstractmethod
    def capture(self, argument: TaleObject) -> CapturedArgument:
        ...


class SimpleBoundParameter(BoundParameter):
    def __init__(self, node: SimpleParameter):
        self.node = node

    def capture(self, argument: TaleObject) -> CapturedArgument:
        if self.node.type_ is not None:
            if argument.type is None:
                return None
            if self.node.type_.content != argument.type.name.py_instance:
                return None

        return CapturedSingle(self.node.name, argument)


class PatternMatchingBoundParameter(BoundParameter):
    def __init__(self, node: PatternMatchingParameter):
        self.node = node

    def capture(self, argument: TaleObject) -> CapturedArgument:
        if self.node.content != str(argument.py_instance):
            return None

        return CapturedSingle(None, argument)


class TupleBoundParameter(BoundParameter):
    def __init__(self, node: TupleParameter):
        self.node = node

    def capture(self, argument: TaleObject) -> CapturedArgument:
        if argument.type is not TaleTuple:
            return None

        parameters = list(self.node.items)
        arguments = argument.items

        if len(parameters) != len(arguments):
            return None

        args = []

        for parameter, argument in zip(parameters, arguments):
            parameter = BoundParameter.of(parameter)
            arg = parameter.capture(argument)

            if arg is None:
                return None
            else:
                args.append(arg)

        return CapturedTuple(args)


class Binding(metaclass=ABCMeta):
    """A binding between a form and a value."""

    @staticmethod
    def of(form: Form, value: Node) -> 'Binding':
        if isinstance(form, UnaryForm):
            return UnaryBinding(form, value)
        if isinstance(form, BinaryForm):
            return BinaryBinding(form, value)
        if isinstance(form, KeywordForm):
            return KeywordBinding(form, value)
        if isinstance(form, PrimitiveForm):
            return PrimitiveBinding(form, value)

        raise ValueError(f"Couldn't create a new binding for {type(form)}.")

    def __init__(self, form: Form, value: Node):
        self.form = form
        self.value = value

    @abstractmethod
    def capture(self, node: Node, scope: 'Scope') -> Captured:
        """Captures an expression if it's possible.

        Args:
            node: A node that represents an expression.

        Returns:
            An instance of `CapturedExpression` if `expression` matches the
            form of the binding, otherwise `None`.
        """


class UnaryBinding(Binding):
    """An unary form binding.

    For example, the following statement:
        (x) squared = ...
    produces an unary binding of unary form `(x) squared` to `...`.
    """

    def __init__(self, form: UnaryForm, value: Node):
        self.form = form
        self.value = value
        self.parameter = BoundParameter.of(form.parameter)

    def capture(self, expression: UnaryExpression, scope: 'Scope') -> Captured:
        if not isinstance(expression, UnaryExpression):
            return None
        if self.form.identifier != expression.identifier:
            return None

        arg = scope.resolve(expression.argument)
        arg = self.parameter.capture(arg)

        if arg is not None:
            return CapturedNode(self.form, self.value, [arg]) 


class BinaryBinding(Binding):
    """A binary form binding.

    For example, the following statement:
        (x) + (y) = ...
    produces a binary binding of binary form `(x) + (y)`  to `...`.
    """

    def __init__(self, form: BinaryForm, value: Node):
        self.form = form
        self.value = value
        self.first_parameter = BoundParameter.of(form.first_parameter)
        self.second_parameter = BoundParameter.of(form.second_parameter)

    def capture(self, expression: BinaryExpression, scope: 'Scope') -> Captured:
        if not isinstance(expression, BinaryExpression):
            return None
        if self.form.operator.content != expression.operator.content:
            return None

        args = []

        first_argument = scope.resolve(expression.first_argument)
        first_argument = self.first_parameter.capture(first_argument)

        second_argument = scope.resolve(expression.second_argument)
        second_argument = self.second_parameter.capture(second_argument)

        if first_argument is None or second_argument is None:
            return None

        args.append(first_argument)
        args.append(second_argument)

        return CapturedNode(self.form, self.value, args)


class KeywordBinding(Binding):
    """A keyword form binding.

    For example, the following statement:
        just: (x) = ...
    produces a keyword binding of keyword form `just: (x)`  to `...`.
    """

    def __init__(self, form: KeywordForm, value: Node):
        self.form = form
        self.value = value

    def capture(self, expression: 'KeywordBinding', scope: 'Scope') -> Captured:
        if not isinstance(expression, KeywordExpression):
            return None

        form = self.form

        form_parts = list(form.parts)
        node_parts = list(expression.parts)

        if len(form_parts) != len(node_parts):
            return None

        args = []

        if form.prefix is not None and expression.prefix is not None:
            prefix = scope.resolve(expression.prefix)
            prefix_parameter = BoundParameter.of(form.prefix)
            arg = prefix_parameter.capture(prefix)

            if arg is None:
                return None
            else:
                args.append(arg)
        elif form.prefix is not None or expression.prefix is not None:
            return None

        parts = zip(form_parts, node_parts)

        for (form_name, form_parameter), (node_name, node_value) in parts:
            if form_name.content != node_name.content:
                return None

            node_value = scope.resolve(node_value)
            form_parameter = BoundParameter.of(form_parameter)
            arg = form_parameter.capture(node_value)

            if arg is None:
                return None
            else:
                args.append(arg)

        return CapturedNode(self.form, self.value, args)


class PrimitiveBinding(Binding):
    """A primitive form binding.

    For example, the following statement:
        x = 1
    produces a primitive binding of primitive form `x` to `1`.
    """

    def __init__(self, form: PrimitiveForm, value: Node):
        self.form = form
        self.value = value

    def capture(self, expression: PrimitiveExpression, scope: 'Scope') -> Captured:
        if not isinstance(expression, PrimitiveExpression) and \
           not isinstance(expression, PrimitiveExpressionItem):
            return None
        if self.form.content != expression.content:
            return None

        return CapturedNode(self.form, self.value)


class ConstBinding:
    """A binding with the constant value."""

    def __init__(self, form: Form, value: TaleObject):
        self.binding = Binding.of(form, value)
        self.value = value

    def capture(self, node: Node, scope: 'Scope') -> Captured:
        captured = self.binding.capture(node, scope)

        if captured:
            return CapturedConst(self.value)


class PredefinedBinding:
    """A binding that is predefined as a part of the Tale's prelude."""

    def __init__(self, form: Form, func):
        self.binding = Binding.of(form, Node(''))
        self.func = func

    def capture(self, node: Node, scope: 'Scope') -> Captured:
        captured = self.binding.capture(node, scope)

        if captured:
            return CapturedConst(self.func(captured))


class PyBinding:
    """A binding that is used to capture native Python calls."""

    def capture(self, node: Node, scope: 'Scope') -> Captured:
        if not isinstance(node, KeywordExpression):
            return None

        if node.prefix is not None:
            return None

        parts = list(node.parts)

        if len(parts) != 1:
            return None

        name, value = parts[0]
        
        if name.content != 'py':
            return None

        value = scope.resolve(value)

        if value.type is not TaleTuple:
            return None

        items = value.items

        if items[0].type is not TaleString:
            return None

        code = items[0].py_instance.strip('"')
        args = map(lambda x: str(x.py_instance), items[1:])
        args = ', '.join(args)
        code = code + '(' + args + ')'

        locals_ = {}
        exec(code, {}, locals_)

        result = locals_['result']

        if isinstance(result, int):
            return CapturedConst(TaleObject(TaleInt, result))

        if isinstance(result, str):
            return CapturedConst(TaleObject(TaleString, result))


class Scope:
    """A scope of the program execution.

    Attributes:
        parent: A parent scope of the current scope.
            For example, a function scope is a parent for if statement scope.
    """

    def __init__(self, parent: Optional['Scope'] = None):
        self.parent = parent
        self.bindings = []

    def capture(self, node: Node, scope: 'Scope') -> Captured:
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

        self.bindings.append(Binding.of(form, value))

    def resolve(self, node: Node) -> TaleObject:
        """Processes a syntax node.

        If node is an assignment, then the new binding will be created in the
        scope.
        If node is an expression, then it will be converted to the value.

        Args:
            node: A node to resolve.

        Returns:
            An instance of `TaleObject` that represents a resolved node.
        """

        def resolve_primitive(x: PrimitiveExpression) -> TaleObject:
            if isinstance(x.children[0], IntLiteral):
                return TaleObject(TaleInt, int(x.content))

            if isinstance(x.children[0], StringLiteral):
                return TaleObject(TaleString, x.content)

        def resolve_assignment(x: Assignment):
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
        return SimpleParameter('', children=[Node('('), Node('x'), Node(')')])

    def unary(name: str):
        return UnaryForm(name, children=[
            simple('x'),
            identifier(name)])

    def simple_keyword(name: str):
        return KeywordForm(name, children=[
            identifier(name),
            simple('x')])

    def binary(operator: str):
        return BinaryForm(operator, children=[
            simple('x'),
            identifier(operator),
            simple('y')])

    def unary_type() -> PredefinedBinding:
        def execute(x: Captured):
            arg = x.arguments[0]
            return arg.value.type.name

        return PredefinedBinding(unary('type'), execute)

    def binary_plus() -> PredefinedBinding:
        def execute(x: Captured):
            a, b = x.arguments

            if a.value.type is TaleInt and a.value.type is TaleInt:
                result = a.value.py_instance + b.value.py_instance

                return TaleObject(TaleInt, result)

        return PredefinedBinding(binary('+'), execute)

    def binary_minus() -> PredefinedBinding:
        def execute(x: Captured):
            a, b = x.arguments

            if a.value.type is TaleInt and a.value.type is TaleInt:
                result = a.value.py_instance - b.value.py_instance

                return TaleObject(TaleInt, result)

        return PredefinedBinding(binary('-'), execute)

    def print_() -> PredefinedBinding:
        def execute(x: Captured):
            arg = x.arguments[0]
            print(arg.value.py_instance)

        return PredefinedBinding(simple_keyword('print'), execute)


    prelude = Scope()
    prelude.bindings.append(unary_type())
    prelude.bindings.append(binary_plus())
    prelude.bindings.append(binary_minus())
    prelude.bindings.append(print_())
    prelude.bindings.append(PyBinding())

    scope = Scope(parent=prelude)

    return scope.resolve(node)
