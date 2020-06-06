from tale.core import execute


def test_simple_prefix_operator():
    # Arrange.
    program = """
-(x) = x

-1
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 1


def test_multiple_prefix_operators_in_expression():
    # Arrange.
    program = """
-(x) = x + 1

-(-1)
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 3
