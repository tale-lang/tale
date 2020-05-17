from typing import Sequence, Optional

from tree_format import format_tree


class Node:
    """A node of the abstract syntax tree.

    Attributes:
        kind: A string that represents the node kind. For example, `Statement`,
            `Assignment`, `Form`, etc.
        children: A sequence of child nodes.
    """

    def __init__(self, kind: str, content: str, children: Optional[Sequence['Node']] = None):
        self.kind = kind
        self.content = content
        self.children = children

    def __str__(self):
        return format_tree(self,
                           format_node=lambda x: f'{x.kind} "{x.content}"',
                           get_children=lambda x: x.children)


class Statement(Node):
    """A node that represents either an assignment or an expression."""


class Assignment(Statement):
    """A node that represents an assignment.

    For example, the following is the example of an assignment:
        y = x
    where:
        y is a form (the `form` property of the node);
        x is a value (the `value` property of the node).
    """

    def __init__(self, kind: str, content: str, children = None):
        super().__init__(kind, content, children)

    @property
    def form(self) -> 'Form':
        return self.children[0]

    @property
    def value(self) -> Node:
        return self.children[2]


class Expression(Statement):
    ...


class Form(Node):
    """A form of an expression.

    Represents a template that may capture a number of expressions.

    For example, the form `(x) squared` captures `1 squared`, `2 squared`,
    `3 squared`, and so on.

    Attributes:
        node: A syntax node that represents the form.
    """
