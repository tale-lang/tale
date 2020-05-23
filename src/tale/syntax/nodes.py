from typing import Iterable, Optional, Sequence, Tuple

from tree_format import format_tree


class Node:
    """A node of the abstract syntax tree.

    Attributes:
        kind: A string that represents the node kind. For example, `Statement`,
            `Assignment`, `Form`, etc.
        children: A sequence of child nodes.
    """

    def __init__(self, content: str, children: Optional[Sequence['Node']] = None):
        self.content = content
        self.children = children

    def __str__(self):
        return format_tree(self,
                           format_node=lambda x: f'{type(x).__name__} "{x.content}"',
                           get_children=lambda x: x.children)


class Statement(Node):
    """A statement node.

    Statement is either an expression or an assignment.
    """


class Assignment(Statement):
    """An assignment node.

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


class Expression(Statement):
    """An expression node.

    Represents a value that could be captured by form.

    For example, the following is an expression:
        1 squared
    It could be captured by the form:
        (x) squared
    """


class PrimitiveExpression(Expression):
    """A primitive expression.

    Primitive expression is just a plain value.
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


class KeywordPrefixExpression(Expression):
    """A prefix of a keyword expression.

    Usually, a keyword expression consists of sequence of pairs where each pair
    represents an identifier and a value.
    For example, the `add: 1 to: list` expression consists of two pairs:
    `(add, 1)` and `(to, 1)`.

    However, sometimes a keyword expression first node is an argument node.
    For example, the `1 added_to: list` expression consists of `1` and a pair
    `(added_to, list)`. Here the `1` expression is a prefix.
    """


class KeywordNameExpression(Expression):
    """A name of the keyword expression part.

    For example, the `add: 1 to: list` expression consists of two names:
    `add` and `to`.
    """


class KeywordValueExpression(Expression):
    """A value of the keyword expression part.

    For example, the `add: 1 to: list` expression consists of two values:
    `1` and `list`.
    """


class KeywordExpression(Expression):
    """A keyword expression.

    Unlike unary expression, a keyword expression consists of pairs
    of arguments and identifiers.
    """

    @property
    def prefix(self) -> KeywordPrefixExpression:
        if isinstance(self.children[0], KeywordPrefixExpression):
            return self.children[0]

    @property
    def parts(self) -> Iterable[Tuple[KeywordNameExpression, KeywordValueExpression]]:
        name = None

        for x in self.children:
            if isinstance(x, KeywordNameExpression):
                name = x
            if isinstance(x, KeywordValueExpression):
                yield (name, x)


class Form(Node):
    """A form of an expression.

    Represents a template that may capture a number of expressions.

    For example, the form `(x) squared` captures `1 squared`, `2 squared`,
    `3 squared`, and so on.

    Attributes:
        node: A syntax node that represents the form.
    """


class PrimitiveForm(Form):
    """A primitive form.

    Primitive form captures only plain values.
    """


class Argument(Node):
    """An argument node.

    Arguments are variable parts of forms.

    For example, in the following form:
        (x) squared
    `(x)` is an argument with name `x`.
    """

    @property
    def name(self) -> str:
        return self.children[1].content


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
    def argument(self) -> Argument:
        return self.children[0]

    @property
    def identifier(self) -> str:
        return self.children[1].content


class KeywordForm(Form):
    """A keyword form.

    A keyword form consists of arguments and identifiers.
    Unlike unary form, arguments and identifiers could be placed anywhere.
    The only rule here is that an argument couldn't be followed by an argument,
    or an identifier couldn't be followed by an identifier.

    For example, the following is a keyword form:
        just: (x)
    where:
        `just` is an identifier;
        `(x)` is an argument.

    Consider a more complex example:
        add: (x) to: (y)
    where:
        `add` and `to` are identifiers;
        `(x)` and `(y)` are arguments.
    """

    @property
    def prefix(self) -> KeywordPrefixExpression:
        if isinstance(self.children[0], Argument):
            return self.children[0]

    @property
    def parts(self) -> Iterable[Tuple[Node, Node]]:
        name = None
        children = self.children

        if self.prefix is not None:
            children = children[1:]

        for x in children:
            if x.content == ':':
                continue

            if isinstance(x, Argument):
                yield (name, x)
            else:
                name = x
