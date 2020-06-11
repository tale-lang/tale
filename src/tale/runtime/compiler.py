from typing import Iterable, Tuple

from tale.runtime.vm import (Call, EndBind, Instruction, Pop, PopTo, PushInt,
                             PushString, StartBind)
from tale.syntax.nodes import (Assignment, BinaryExpression, BinaryForm,
                               Expression, Form, IntLiteral, KeywordArgument,
                               KeywordExpression, KeywordForm, Node, Parameter,
                               PatternMatchingParameter,
                               PrefixOperatorExpression, PrefixOperatorForm,
                               PrimitiveExpression, PrimitiveExpressionItem,
                               PrimitiveForm, SimpleParameter, SingleParameter,
                               Statement, StringLiteral, Token, TupleParameter,
                               UnaryExpression, UnaryForm)

# TODO: Fix names. They are bad.
Name = str
Type = str
Value = str
Param = Iterable[Tuple[Name, Type, Value]]
Params = Iterable[Param]
PatternMatchingParam = Iterable[Tuple[Value, Type]]


def compile(node: Node) -> Iterable[Instruction]:
    """Converts a syntax tree to the list of virtual machine instructions."""

    instructions = []

    def generate_pop():
        instructions.append(Pop())

    def generate_for_assignment(x: Assignment):
        def name_of_param(x: Parameter):
            if isinstance(x, TupleParameter):
                return f'({"," * len([x.items])})'
            else:
                return '()'

        def name_of_form(x: Form) -> str:
            def unary(x: UnaryForm) -> str:
                return f'{name_of_param(x.parameter)}{x.identifier}'
            def prefix(x: PrefixOperatorForm) -> str:
                return f'{x.operator}{name_of_param(x.parameter)}'
            def binary(x: BinaryForm) -> str:
                return f'{name_of_param(x.first_parameter)}{x.operator}' \
                       f'{name_of_param(x.second_parameter)}'
            def keyword(x: KeywordForm) -> str:
                prefix = name_of_param(x.prefix) if x.prefix is not None else ''
                parts = [f'{id.content}{name_of_param(param)}' for id, param in x.parts]
                parts = ''.join(parts)
                return f'{prefix}{parts}'
            def primitive(x: PrimitiveForm) -> str:
                return f'{x.content}'

            if isinstance(x, UnaryForm):
                return unary(x)
            if isinstance(x, PrefixOperatorForm):
                return prefix(x)
            if isinstance(x, BinaryForm):
                return binary(x)
            if isinstance(x, KeywordForm):
                return keyword(x)
            if isinstance(x, PrimitiveForm):
                return primitive(x)

        def params_of_form(x: Form) -> Params:
            def param_of(x: Parameter) -> Param:
                if isinstance(x, TupleParameter):
                    return [param_of(x) for x in x.items]

                if isinstance(x, SingleParameter):
                    if isinstance(x, PatternMatchingParameter):
                        return [(None, None, x.content)]
                    if isinstance(x, SimpleParameter):
                        return [(x.name, x.type_, None)]

            def unary(x: UnaryForm) -> Params:
                return param_of(x.parameter)
            def prefix(x: PrefixOperatorForm) -> Params:
                return param_of(x.parameter)
            def binary(x: BinaryForm) -> Params:
                return param_of(x.first_parameter) + param_of(x.second_parameter)
            def keyword(x: KeywordForm) -> Params:
                params = []

                if x.prefix is not None:
                    params = params + param_of(x.prefix)

                for id, param in x.parts:
                    params = params + param_of(param)

                return params

            def primitive(x: PrimitiveForm) -> Params:
                return []

            if isinstance(x, UnaryForm):
                return unary(x)
            if isinstance(x, PrefixOperatorForm):
                return prefix(x)
            if isinstance(x, BinaryForm):
                return binary(x)
            if isinstance(x, KeywordForm):
                return keyword(x)
            if isinstance(x, PrimitiveForm):
                return primitive(x)

        def generate_start_bind(name: str, params: Params):
            def converted(x: Param) -> PatternMatchingParam:
                [(value, type) for _, type, value in x]

            params = [converted(x) for x in params]
            instructions.append(StartBind(name, params))

        def generate_body(x: Node, params: Params):
            def generate_params():
                for name, _, _ in params:
                    if name is not None:
                        instructions.append(PopTo(name))

            if isinstance(x, Expression) or \
               isinstance(x, PrimitiveExpressionItem):
                generate_params()
                generate_for_expression(x)
            else:
                generate_params()
                generate(x)

        def generate_end_bind():
            instructions.append(EndBind())

        name = name_of_form(x.form)
        value = x.value.children[0]
        params = params_of_form(x.form)

        generate_start_bind(name, params)
        generate_body(value, params)
        generate_end_bind()

    def generate_for_expression(x: Expression):
        def arguments(x: Expression) -> Iterable[Node]:
            # TODO: Move the code to the nodes.
            def unary(x: UnaryExpression) -> Iterable[Node]:
                return [x.argument]
            def prefix(x: PrefixOperatorExpression) -> Iterable[Node]:
                return [x.argument]
            def binary(x: BinaryExpression) -> Iterable[Node]:
                return [x.first_argument, x.second_argument]
            def keyword(x: KeywordExpression) -> Iterable[Node]:
                args = []

                if x.prefix is not None:
                    args.append(x.prefix)
                for name, arg in x.parts:
                    args.append(arg)

                return args

            if isinstance(x, UnaryExpression):
                return unary(x)
            if isinstance(x, PrefixOperatorExpression):
                return prefix(x)
            if isinstance(x, BinaryExpression):
                return binary(x)
            if isinstance(x, KeywordExpression):
                return keyword(x)

        def name_of_expression(x: Expression) -> str:
            def unary(x: UnaryExpression) -> str:
                return f'(){x.identifier}'
            def prefix(x: PrefixOperatorExpression) -> str:
                return f'{x.operator}()'
            def binary(x: BinaryExpression) -> str:
                return f'(){x.operator}()'
            def keyword(x: KeywordExpression) -> str:
                prefix = '()' if x.prefix is not None else ''
                parts = [f'{id.content}()' for id, _ in x.parts]
                parts = ''.join(parts)
                return f'{prefix}{parts}'

            if isinstance(x, UnaryForm):
                return unary(x)
            if isinstance(x, PrefixOperatorForm):
                return prefix(x)
            if isinstance(x, BinaryForm):
                return binary(x)
            if isinstance(x, KeywordForm):
                return keyword(x)

        if isinstance(x.children[0], IntLiteral):
            instructions.append(PushInt(int(x.content)))
            return
        if isinstance(x.children[0], StringLiteral):
            instructions.append(PushString(x.content))
            return
        if isinstance(x.children[0], Token):
            instructions.append(Call(x.content))
            return
        if isinstance(x, PrimitiveExpression):
            for x in x.items:
                generate_for_expression(x)
            return

        for arg in arguments(x):
            if isinstance(x, KeywordArgument):
                arg = x.children[0]

            if isinstance(arg, IntLiteral):
                instructions.append(PushInt(int(x.content)))
            if isinstance(arg, StringLiteral):
                instructions.append(PushString(x.content))
            if isinstance(arg, Expression):
                generate_for_expression(arg)

        name = name_of_expression(x)
        instructions.append(Call(name))

    def generate(x: Node):
        last = node.children[-1]

        # Get rid of `<NL>` and other empty nodes.
        children = [x for x in node.children if isinstance(x, Expression) or \
                                                isinstance(x, Statement)] 

        for child in children:
            is_last = child == children[-1]

            if isinstance(child, Statement):
                child = child.children[0]

            if isinstance(child, Assignment):
                generate_for_assignment(child)

            if isinstance(child, Expression):
                generate_for_expression(child)

                if not is_last:
                    generate_pop()

    generate(node)

    return instructions
