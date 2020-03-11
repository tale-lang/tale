import antlr4
from tree_format import format_tree

from grammar.TaleLexer import TaleLexer
from grammar.TaleParser import TaleParser


class Node:
    def __init__(self, instance):
        self.name = type(instance).__name__
        self.value = instance.getText()
        if isinstance(instance, antlr4.tree.Tree.TerminalNode):
            self.children = []
        else:
            self.children = [Node(x) for x in instance.getChildren()]

    def __str__(self):
        return format_tree(self,
                           format_node=lambda x: f'{x.name} "{x.value}"',
                           get_children=lambda x: x.children)


def parse(code: str):
    """Parses provided code string."""

    code = antlr4.InputStream(code)

    lexer = TaleLexer(code)
    stream = antlr4.CommonTokenStream(lexer)
    parser = TaleParser(stream)
    tree = parser.program()

    return Node(tree)
