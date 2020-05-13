from typing import Iterable

import antlr4
from tree_format import format_tree

from grammar.TaleLexer import TaleLexer
from grammar.TaleParser import TaleParser
from tale.syntax.nodes.node import Node
from tale.syntax.parsers.parser import Parser
from tale.common import pipe


class Antlr4Node(Node):
    """A node of the syntax tree.

    Wraps an ANTLR4 syntax tree for more convenient usage.
    Knows how to print itself to the console.

    Attributes:
        instance: An instance of ANTLR4 node.
    """

    def __init__(self, instance):
        def beautify(name: str):
            # ANTLR4 appends `Context` at the end of the compound node.
            # For example, if an expression `Program` had parsed,
            # it'd have a `ProgramContext` name.
            if name.endswith('Context'):
                return name[:-len('Context')]
            
            # ANTLR4 uses `TerminalNodeImpl` as a name of the terminal node.
            if name == 'TerminalNodeImpl':
                return 'Terminal'

            return name

        self.name = type(instance).__name__
        self.name = beautify(self.name)
        self.value = instance.getText()

        if isinstance(instance, antlr4.tree.Tree.TerminalNode):
            self._children = []
        else:
            self._children = [Antlr4Node(x) for x in instance.getChildren()]

    @property
    def children(self) -> Iterable[Node]: 
        return self._children

    def __str__(self):
        return format_tree(self,
                           format_node=lambda x: f'{x.name} "{x.value}"',
                           get_children=lambda x: x.children)


class Antlr4Parser(Parser):
    """A parser that uses ANTLR4 under the hood.

    Uses `grammar.TaleLexer` and `grammar.TaleParser` to tokenize the input,
    and to produce an abstract syntax tree.
    """

    def ast(self, code: str) -> Node:
        parser = pipe(
                antlr4.InputStream,
                TaleLexer,
                antlr4.CommonTokenStream,
                TaleParser)
        tree = parser(code).program()

        return Antlr4Node(tree)
