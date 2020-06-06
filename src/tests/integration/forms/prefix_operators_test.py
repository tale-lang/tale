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
