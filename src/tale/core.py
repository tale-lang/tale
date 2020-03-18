from tale.syntax import parse
from tale.runtime import evaluate


def execute(code: str):
    """Executes code represented by string.

    This function meant to act as an interpreter entry point:
    here provided code is parsed to syntax tree, analyzed and
    executed line by line.

    Args:
        code: Code as a string.
    """

    print('--------------------------------------------------------------')
    print('ANTLR4 Output:')
    tree = parse(code)
    print('--------------------------------------------------------------')
    print('Syntax tree:')
    print(str(tree).rstrip())
    print('--------------------------------------------------------------')

    output = evaluate(tree)
    print('Output:')
    print(output or '<empty>')
    print('--------------------------------------------------------------')
