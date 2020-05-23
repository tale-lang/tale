from typing import Any

from tale.runtime.evaluation import evaluate
from tale.syntax.parsers.antlr4 import Antlr4Parser


def execute(code: str) -> Any:
    """Executes a code string.

    Args:
        code: Code as a string.

    Returns:
        A result of the code execution.

    Examples:
        >>> execute('2 + 2')
        4
        >>> execute('x = 1')
        None
    """

    print('--------------------------------------------------------------')
    print('ANTLR4 Output:')
    tree = Antlr4Parser().ast(code)
    print('--------------------------------------------------------------')
    print('Syntax tree:')
    print(str(tree).rstrip())
    print('--------------------------------------------------------------')
    output = evaluate(tree)
    print('Output:')
    print(output or '<empty>')
    print('--------------------------------------------------------------')

    return output
