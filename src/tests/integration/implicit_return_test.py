from textwrap import dedent

from tale.core import execute


def test_one_expression():
    # Arrange.
    program = """
x
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 'x'
