import os
from typing import Any, Iterable

import antlr4

from tale.common import pipe
from tale.syntax.grammar.TaleLexer import TaleLexer
from tale.syntax.grammar.TaleParser import TaleParser
from tale.syntax.nodes import (Argument, Assignment, Expression,
                               KeywordExpression, KeywordForm,
                               KeywordNameExpression, KeywordPrefixExpression,
                               KeywordValueExpression, Node,
                               PrimitiveExpression, PrimitiveForm, Statement,
                               UnaryExpression, UnaryForm)
from tale.syntax.parsers.parser import Parser


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

            if isinstance(x, TaleParser.StatementContext):
                return new_(x, as_=Statement)

            if isinstance(x, TaleParser.AssignmentContext):
                return new_(x, as_=Assignment)

            if isinstance(x, TaleParser.AssignmentFormContext):
                x = list(x.getChildren())[0]

                if isinstance(x, TaleParser.SimpleFormContext):
                    return new_(x, as_=PrimitiveForm)
                if isinstance(x, TaleParser.UnaryFormContext):
                    return new_(x, as_=UnaryForm)
                if isinstance(x, TaleParser.KeywordFormContext):
                    return new_(x, as_=KeywordForm)

            if isinstance(x, TaleParser.ExpressionContext):
                x = list(x.getChildren())[0]

                if isinstance(x, TaleParser.PrimitiveContext):
                    return new_(x, as_=PrimitiveExpression)
                if isinstance(x, TaleParser.UnaryContext):
                    return new_(x, as_=UnaryExpression)
                if isinstance(x, TaleParser.KeywordContext):
                    return new_(x, as_=KeywordExpression)

                return new_(x, as_=Expression)

            if isinstance(x, TaleParser.PrimitiveContext):
                return new_(x, as_=PrimitiveExpression)
            if isinstance(x, TaleParser.UnaryContext):
                return new_(x, as_=UnaryExpression)

            if isinstance(x, TaleParser.KeywordPrefixContext):
                return new_(x, as_=KeywordPrefixExpression)
            if isinstance(x, TaleParser.KeywordNameContext):
                return new_(x, as_=KeywordNameExpression)
            if isinstance(x, TaleParser.KeywordValueContext):
                return new_(x, as_=KeywordValueExpression)

            if isinstance(x, TaleParser.ArgumentContext):
                return new_(x, as_=Argument)

            return new_(x, as_=Node)

        parser = pipe(
                antlr4.InputStream,
                TaleLexer,
                antlr4.CommonTokenStream,
                TaleParser)
        program = parser(code).program()

        return node(program)
