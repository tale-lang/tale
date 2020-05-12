from typing import Any

from tale import syntax, runtime
from tale.syntax.parsers.antlr4 import Antlr4Parser


def execute(code: str) -> Any:
    """Executes the provided code string.

    This function is meant to be an interpreter entry point:
    here the code is parsed, analyzed and evaluated to produce an output.

    Args:
        code: Code as a string.
    """

    print('--------------------------------------------------------------')
    print('ANTLR4 Output:')
    tree = Antlr4Parser().ast(code)
    print('--------------------------------------------------------------')
    print('Syntax tree:')
    print(str(tree).rstrip())
    print('--------------------------------------------------------------')
    output = runtime.evaluate(tree)
    print('Output:')
    print(output or '<empty>')
    print('--------------------------------------------------------------')
