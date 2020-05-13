from typing import Any, Iterable
import os

import antlr4

from grammar.TaleLexer import TaleLexer
from grammar.TaleParser import TaleParser
from tale.syntax.nodes import Node, Assignment, Statement, Form
from tale.syntax.parsers.parser import Parser
from tale.common import pipe


class Antlr4Parser(Parser):
    """A parser that uses ANTLR4 under the hood.

    Uses `grammar.TaleLexer` and `grammar.TaleParser` to tokenize the input,
    and to produce an abstract syntax tree.
    """

    def ast(self, code: str) -> Node:
        def kind(x):
            result = type(x).__name__

            # ANTLR4 appends `Context` at the end of the compound node.
            # For example, if an expression `Program` had parsed,
            # it'd have a `ProgramContext` name.
            if result.endswith('Context'):
                return result[:-len('Context')]
            
            # ANTLR4 uses `TerminalNodeImpl` as a name of the terminal node.
            if result == 'TerminalNodeImpl':
                return 'Terminal'

            return result

        def content(x):
            result = x.getText()
            return result if result != os.linesep else '<CR>'

        def children(x):
            if isinstance(x, antlr4.tree.Tree.TerminalNode):
                return []
            else:
                return list(map(node, x.getChildren()))

        def node(x):
            def new_(node: Any, as_: type) -> Node:
                return as_(kind(node), content(node), children(node))

            if isinstance(x, TaleParser.StatementContext):
                return new_(x, as_=Statement)
            if isinstance(x, TaleParser.AssignmentContext):
                return new_(x, as_=Assignment)
            if isinstance(x, TaleParser.AssignmentFormContext):
                return new_(x, as_=Form)

            return new_(x, as_=Node)

        parser = pipe(
                antlr4.InputStream,
                TaleLexer,
                antlr4.CommonTokenStream,
                TaleParser)
        program = parser(code).program()

        return node(program)
