from typing import Sequence, Optional

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

    def __init__(self, content: str, children = None):
        super().__init__(content, children)

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

    def __init__(self, content: str, children = None):
        super().__init__(content, children)

    @property
    def argument(self) -> 'Node':
        return self.children[0]

    @property
    def identifier(self) -> str:
        return self.children[1].content


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


class UnaryForm(Form):
    """An unary form.

    An unary form consists of an argument and an identifier.

    For example, a following is an unary form:
        (x) squared
    where:
        `(x)` is a variable argument of a form;
        `squared` is a simple identifier.
    """

    def __init__(self, content: str, children = None):
        super().__init__(content, children)

    @property
    def argument(self) -> 'Argument':
        return self.children[0]

    @property
    def identifier(self) -> str:
        return self.children[1].content


class Argument(Node):
    """An argument node.

    Arguments are variable parts of forms.

    For example, in the following form:
        (x) squared
    `(x)` is an argument with name `x`.
    """

    def __init__(self, content: str, children = None):
        super().__init__(content, children)

    @property
    def name(self) -> str:
        return self.children[1].content
