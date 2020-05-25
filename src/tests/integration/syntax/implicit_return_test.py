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


def test_two_expressions():
    # Arrange.
    program = """
x
y
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 'y'
