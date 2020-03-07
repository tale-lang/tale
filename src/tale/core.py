import antlr4

from grammar.TaleLexer import TaleLexer
from grammar.TaleParser import TaleParser


def execute(code):
    code = antlr4.InputStream(code)

    lexer = TaleLexer(code)
    stream = antlr4.CommonTokenStream(lexer)
    parser = TaleParser(stream)
    tree = parser.program()

    print(tree)
