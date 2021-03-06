from typing import Any, Iterable, Optional, Sequence, Tuple

from tree_format import format_tree

from tale.common import group


class Node:
    """A node of the abstract syntax tree.

    Attributes:
        kind: A string that represents the node kind. For example, `Statement`,
            `Assignment`, `Form`, etc.
        children: A sequence of child nodes.
    """

    def __init__(self, content: str, children: Optional[Sequence['Node']] = None):
        self.content = content
        self.children = children or []

    def __str__(self):
        def name(x) -> str:
            if isinstance(x, Token):
                return ' "' + x.content + '"'
            else:
                return ''

        return format_tree(self,
                           format_node=lambda x: f'{type(x).__name__}{name(x)}',
                           get_children=lambda x: x.children)


class Program(Node):
    """A main program."""


class Statement(Node):
    """A statement.

    Statement is either an expression or an assignment.
    """


class Identifier(Node):
    """An identifier.

    For example, in the expression:
        x = 1
    `x` is an identifier.
    """


class Assignment(Statement):
    """An assignment.

    The following is an example of the assignment:
        y = x
    where:
        `y` is a form (the `form` property of the node);
        `x` is a value (the `value` property of the node).
    """

    @property
    def form(self) -> 'Form':
        return self.children[0]

    @property
    def value(self) -> Node:
        return self.children[2]


class Form(Node):
    """A form of an expression.

    Represents a template that may capture a number of expressions.

    For example, the form `(x) squared` captures `1 squared`, `2 squared`,
    `3 squared`, and so on.

    Attributes:
        node: A syntax node that represents the form.
    """


class UnaryForm(Form):
    """An unary form.

    An unary form consists of an argument and an identifier.

    For example, the following is an unary form:
        (x) squared
    where:
        `(x)` is a variable argument of a form;
        `squared` is a simple identifier.
    """

    @property
    def parameter(self) -> 'Parameter':
        return self.children[0]

    @property
    def identifier(self) -> str:
        return self.children[1].content


class PrefixOperatorForm(Form):
    """A prefix operator form.

    An prefix operator form consists of operator followed by a parameter.

    For example, the following is a prefix operator form:
        -(x)
    where:
        `-` is an operator;
        `(x)` is a parameter.

    Prefix operators have higher precedence than unary forms.
    For example, the following:
        -1 asString
    Is equal to:
        (-1) asString
    """

    @property
    def operator(self) -> str:
        return self.children[0].content

    @property
    def parameter(self) -> 'Parameter':
        if isinstance(self.children[1], Parameter):
            return self.children[1]
        else:
            return self.children[1]


class BinaryForm(Form):
    """A binary form.

    A binary form consists of two parameters that are separated by some special
    character.
    For example, the following is a binary form:
        (x) + (y)
    where:
        `(x)` is a first parameter;
        `+` is an operator;
        `(y)` is a second parameter.
    """

    @property
    def first_parameter(self) -> 'Parameter':
        return self.children[0]

    @property
    def operator(self) -> Node:
        return self.children[1]

    @property
    def second_parameter(self) -> 'Parameter':
        return self.children[2]


class KeywordForm(Form):
    """A keyword form.

    A keyword form consists of parameters and identifiers.
    Unlike unary form, parameters and identifiers could be placed anywhere.
    The only rule here is that an parameter couldn't be followed by an parameter,
    or an identifier couldn't be followed by an identifier.

    For example, the following is a keyword form:
        just: (x)
    where:
        `just` is an identifier;
        `(x)` is an parameter.

    Consider a more complex example:
        add: (x) to: (y)
    where:
        `add` and `to` are identifiers;
        `(x)` and `(y)` are parameters.
    """

    @property
    def prefix(self) -> 'Parameter':
        if isinstance(self.children[0], Parameter):
            return self.children[0]

    @property
    def parts(self) -> Iterable[Tuple[Node, Node]]:
        def is_not_prefix_and_colon(x: Node):
            return x is not self.prefix and x.content != ':'

        children = filter(is_not_prefix_and_colon, self.children)
        children = group(children, by=2)

        return children


class PrimitiveForm(Form):
    """A primitive form.

    Primitive form captures only plain values.
    """


class Parameter(Node):
    """A parameter.

    An parameter is either a single or a tuple one.

    For example, in the following form:
        (x) squared = x * x
    `(x)` is a single parameter.

    On the other hand, in the form:
        first: (x), (y) = x
    `(x), (y)` is a tuple parameter: it consists of two single ones.
    """


class TupleParameter(Parameter):
    """A comma separated sequence of sigle parameters."""

    @property
    def items(self) -> Iterable['Parameter']:
        return (x for x in self.children if isinstance(x, Parameter))


class SingleParameter(Parameter):
    """A single parameter.

    A single parameter is either a simple or a pattern matching one.

    For example, in the following form:
        (x) squared = x * x
    `(x)` is a simple parameter.

    On the other hand, in the form:
        2 squared = 4
    `2` is a pattern matching parameter.
    """

    @property
    def type_(self) -> str:
        return self.children[3] if len(self.children) > 3 else None


class SimpleParameter(SingleParameter):
    """A single parameter.

    A single parameter is either a simple or a pattern matching one.

    For example, in the following form:
        (x) squared = x * x
    `(x)` is a simple parameter.

    On the other hand, in the form:
        2 squared = 4
    `2` is a pattern matching parameter.
    """

    @property
    def type_(self) -> str:
        return self.children[3] if len(self.children) > 3 else None

    @property
    def name(self) -> str:
        return self.children[1].content


class PatternMatchingParameter(SingleParameter):
    """A pattern matching parameter.

    Represents a plain value.

    For example, in the following form:
        2 squared = 4
    `2` is a pattern matching parameter.
    """


class AssignmentBody(Node):
    """An assignment body.

    Can be either a simple expression:
        x = 1
    Or a sequence of statements:
        x =
            y = 1
            y
    """


class Expression(Statement):
    """An expression.

    Represents a value that could be captured by form.

    For example, the following is an expression:
        1 squared
    It could be captured by the form:
        (x) squared
    """


class UnaryExpression(Expression):
    """An unary expression.

    An unary expression consist of two parts: an argument and the identifier.
    """

    @property
    def argument(self) -> 'Node':
        return self.children[0]

    @property
    def identifier(self) -> str:
        return self.children[1].content


class PrefixOperatorExpression(Expression):
    """A prefix operator expression.

    A prefix operator consist of two parts: an operator and the value.
    """

    @property
    def operator(self) -> str:
        return self.children[0].content

    @property
    def argument(self) -> 'Node':
        if self.children[1].content == '(':
            return self.children[2]
        else:
            return self.children[1]


class BinaryExpression(Expression):
    """A binary expression.

    Consists of two arguments and an operator.

    For example, the following is an example of binary expression:
        1 + 1
    where:
        `1` is a first argument;
        `+` is an operator;
        `2` is a second argument.
    """

    @property
    def first_argument(self) -> Expression:
        return self.children[0]

    @property
    def operator(self) -> Node:
        return self.children[1]

    @property
    def second_argument(self) -> Expression:
        return self.children[2]


class KeywordExpression(Expression):
    """A keyword expression.

    Unlike unary expression, a keyword expression consists of pairs
    of arguments and identifiers.

    For example, the following is a keyword expression:
        add: 1 to: list
    """

    @property
    def prefix(self) -> 'KeywordArgument':
        """Returns a prefix of the keyword expression.

        Usually, a keyword expression consists of sequence of pairs where each pair
        represents an identifier and a value.
        For example, the `add: 1 to: list` expression consists of two pairs:
        `(add, 1)` and `(to, 1)`.

        However, sometimes the first node of a keyword expression is an argument node.
        For example, the `1 added_to: list` expression consists of `1` and a pair
        `(added_to, list)`. Here the `1` expression is a prefix.
        """

        if isinstance(self.children[0], KeywordArgument):
            return self.children[0]

    @property
    def parts(self) -> Iterable[Tuple['KeywordName', 'KeywordArgument']]:
        def is_not_prefix_and_colon(x: Node):
            return x is not self.prefix and x.content != ':'

        children = filter(is_not_prefix_and_colon, self.children)
        children = group(children, by=2)

        return children


class KeywordArgument(Expression):
    """An argument of the keyword expression.

    For example, the `add: 1 to: list` expression consists of two arguments:
    `1` and `list`.
    """


class KeywordName(Node):
    """A name of the keyword expression part.

    For example, the `add: 1 to: list` expression consists of two names:
    `add` and `to`.
    """


class PrimitiveExpression(Expression):
    """A primitive expression.

    Primitive expression is just a plain value.
    """

    @property
    def items(self) -> Iterable['PrimitiveExpressionItem']:
        return (x for x in self.children if isinstance(x, PrimitiveExpressionItem))


class PrimitiveExpressionItem(Node):
    """An item of the primitive expression.

    For example, the following expression:
        just: 1, 2
    Contains `1, 2` as primitive expression with two items: `1` and `2`.
    """


class IntLiteral(Node):
    """An integer literal.

    Represents a positive integer number.
    """


class StringLiteral(Node):
    """A string literal."""


class Token(Node):
    """A plain text.

    For example, in the expression:
        x = 1
    `=` is a token.
    """
