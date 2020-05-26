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
                               BinaryForm, Expression, IntLiteral,
                               KeywordArgument, KeywordExpression, KeywordForm,
                               KeywordName, KeywordPrefix, Node, Parameters,
                               PatternMatchingParameter, PrimitiveExpression,
                               PrimitiveExpressionItem, PrimitiveForm, Program,
                               SimpleParameter, Statement, StringLiteral,
                               Token, UnaryExpression, UnaryForm)
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
            def new(node: Any, as_: type) -> Node:
                return as_(content(node), children(node))

            def newchild(node: Any, as_: type) -> Node:
                return new(next(node.getChildren()), as_)

            if isinstance(x, TaleParser.ProgramContext):
                return new(x, as_=Program)

            if isinstance(x, TaleParser.StatementContext):
                return new(x, as_=Statement)

            if isinstance(x, TaleParser.AssignmentContext):
                return new(x, as_=Assignment)

            if isinstance(x, TaleParser.AssignmentBodyContext):
                return newchild(x, as_=AssignmentBody)
            
            if isinstance(x, TaleParser.SimpleAssignmentBodyContext):
                return node(next(x.getChildren()))

            if isinstance(x, TaleParser.AssignmentFormContext):
                x = next(x.getChildren())

                if isinstance(x, TaleParser.SimpleFormContext):
                    return new(x, as_=PrimitiveForm)

                if isinstance(x, TaleParser.UnaryFormContext):
                    return new(x, as_=UnaryForm)

                if isinstance(x, TaleParser.KeywordFormContext):
                    return new(x, as_=KeywordForm)

                if isinstance(x, TaleParser.BinaryFormContext):
                    return new(x, as_=BinaryForm)

            if isinstance(x, TaleParser.ExpressionContext):
                x = next(x.getChildren())

                if isinstance(x, TaleParser.PrimitiveContext):
                    x = next(x.getChildren())
                    return new(x, as_=PrimitiveExpression)

                if isinstance(x, TaleParser.UnaryContext):
                    return new(x, as_=UnaryExpression)

                if isinstance(x, TaleParser.KeywordContext):
                    return new(x, as_=KeywordExpression)

                if isinstance(x, TaleParser.BinaryContext):
                    return new(x, as_=BinaryExpression)

                return new(x, as_=Expression)

            if isinstance(x, TaleParser.PrimitiveContext):
                return new(x, as_=PrimitiveExpression)

            if isinstance(x, TaleParser.PrimitiveItemContext):
                return new(x, as_=PrimitiveExpressionItem)

            if isinstance(x, TaleParser.UnaryContext):
                return new(x, as_=UnaryExpression)

            if isinstance(x, TaleParser.KeywordPrefixContext):
                return new(x, as_=KeywordPrefix)

            if isinstance(x, TaleParser.KeywordNameContext):
                return new(x, as_=KeywordName)

            if isinstance(x, TaleParser.KeywordValueContext):
                return new(x, as_=KeywordArgument)

            if isinstance(x, TaleParser.BinaryContext):
                return new(x, as_=BinaryExpression)

            if isinstance(x, TaleParser.ParametersContext):
                return new(x, as_=Parameters)

            if isinstance(x, TaleParser.ParameterContext):
                x = next(x.getChildren())

                if isinstance(x, TaleParser.SimpleParameterContext):
                    return new(x, as_=SimpleParameter)

                if isinstance(x, TaleParser.PatternMatchingParameterContext):
                    return new(x, as_=PatternMatchingParameter)

            if isinstance(x, TaleParser.LiteralContext):
                x = next(x.getChildren())

                if isinstance(x, TaleParser.IntLiteralContext):
                    return new(x, as_=IntLiteral)

                if isinstance(x, TaleParser.StringLiteralContext):
                    return new(x, as_=StringLiteral)

            if (x.getText() == 'indent'):
                return Token('<INDENT>')

            if (x.getText() == 'dedent'):
                return Token('<DEDENT>')

            if (x.getText() == 'newLine'):
                return Token('<NL>')

            if isinstance(x, antlr4.TerminalNode):
                return new(x, as_=Token)

            return new(x, as_=Node)

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
