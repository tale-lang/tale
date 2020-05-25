import io
import os
from contextlib import redirect_stderr
from typing import Any, Iterable

import antlr4
from tree_format import format_tree

from tale.common import pipe
from tale.syntax.grammar.TaleLexer import TaleLexer
from tale.syntax.grammar.TaleParser import TaleParser
from tale.syntax.nodes import (Assignment, AssignmentBody, BinaryExpression,
                               BinaryForm, Expression, KeywordArgument,
                               KeywordExpression, KeywordForm, KeywordName,
                               KeywordPrefix, Node, PatternMatchingParameter,
                               PrimitiveExpression, PrimitiveForm, Program,
                               SimpleParameter, Statement, Token,
                               UnaryExpression, UnaryForm)
from tale.syntax.parsers.parser import Parser


class Antlr4DebugNode:
    """An ANTLR4 syntax node that is used for debugging purposes.

    It's mainly needed for checking the raw syntax tree created by ANTLR4.
    The raw syntax tree is a bit longer than the one created for Tale.
    """

    def __init__(self, node):
        def content(x):
            result = x.getText()
            return result if result != os.linesep else '<CR>'

        def children(x):
            if isinstance(x, antlr4.tree.Tree.TerminalNode):
                return []
            else:
                return list(map(Antlr4DebugNode, x.getChildren()))

        self.node = node
        self.content = content(node)
        self.children = children(node)

    def __str__(self):
        return format_tree(self,
                           format_node=lambda x: f'{type(x.node).__name__} "{x.content}"',
                           get_children=lambda x: x.children)


class Antlr4Parser(Parser):
    """A parser that uses ANTLR4 under the hood.

    Uses `grammar.TaleLexer` and `grammar.TaleParser` to tokenize the input,
    and to produce an abstract syntax tree.
    """

    def ast(self, code: str) -> Node:
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
                return as_(content(node), children(node))

            def new_child(node: Any, as_: type) -> Node:
                return new_(next(node.getChildren()), as_)

            if isinstance(x, TaleParser.ProgramContext):
                return new_(x, as_=Program)

            if isinstance(x, TaleParser.StatementContext):
                return new_(x, as_=Statement)

            if isinstance(x, TaleParser.AssignmentContext):
                return new_(x, as_=Assignment)

            if isinstance(x, TaleParser.AssignmentBodyContext):
                return new_child(x, as_=AssignmentBody)
            
            if isinstance(x, TaleParser.SimpleAssignmentBodyContext):
                return node(next(x.getChildren()))

            if isinstance(x, TaleParser.AssignmentFormContext):
                x = next(x.getChildren())

                if isinstance(x, TaleParser.SimpleFormContext):
                    return new_(x, as_=PrimitiveForm)

                if isinstance(x, TaleParser.UnaryFormContext):
                    return new_(x, as_=UnaryForm)

                if isinstance(x, TaleParser.KeywordFormContext):
                    return new_(x, as_=KeywordForm)

                if isinstance(x, TaleParser.BinaryFormContext):
                    return new_(x, as_=BinaryForm)

            if isinstance(x, TaleParser.ExpressionContext):
                x = next(x.getChildren())

                if isinstance(x, TaleParser.PrimitiveContext):
                    return new_(x, as_=PrimitiveExpression)

                if isinstance(x, TaleParser.UnaryContext):
                    return new_(x, as_=UnaryExpression)

                if isinstance(x, TaleParser.KeywordContext):
                    return new_(x, as_=KeywordExpression)

                if isinstance(x, TaleParser.BinaryContext):
                    return new_(x, as_=BinaryExpression)

                return new_(x, as_=Expression)

            if isinstance(x, TaleParser.PrimitiveContext):
                return new_(x, as_=PrimitiveExpression)

            if isinstance(x, TaleParser.UnaryContext):
                return new_(x, as_=UnaryExpression)

            if isinstance(x, TaleParser.KeywordPrefixContext):
                return new_(x, as_=KeywordPrefix)

            if isinstance(x, TaleParser.KeywordNameContext):
                return new_(x, as_=KeywordName)

            if isinstance(x, TaleParser.KeywordValueContext):
                return new_(x, as_=KeywordArgument)

            if isinstance(x, TaleParser.BinaryContext):
                return new_(x, as_=BinaryExpression)

            if isinstance(x, TaleParser.ParameterContext):
                x = next(x.getChildren())

                if isinstance(x, TaleParser.SimpleParameterContext):
                    return new_(x, as_=SimpleParameter)

                if isinstance(x, TaleParser.PatternMatchingParameterContext):
                    return new_(x, as_=PatternMatchingParameter)

            if (x.getText() == 'indent'):
                return Token('<INDENT>')

            if (x.getText() == 'dedent'):
                return Token('<DEDENT>')

            if (x.getText() == 'newLine'):
                return Token('<NL>')

            if isinstance(x, antlr4.TerminalNode):
                return new_(x, as_=Token)

            return new_(x, as_=Node)

        err = io.StringIO()

        with redirect_stderr(err):
            parser = pipe(
                    antlr4.InputStream,
                    TaleLexer,
                    antlr4.CommonTokenStream,
                    TaleParser)
            program = parser(code).program()

        print(Antlr4DebugNode(program))

        err = err.getvalue()

        if len(err) > 0:
            raise Exception(err)

        return node(program)
