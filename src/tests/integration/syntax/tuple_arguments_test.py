from tale.core import execute


def test_unary():
    # Arrange.
    program = """
(x), (y) first = x

1, 2 first
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 1


def test_keyword():
    # Arrange.
    program = """
second: (x), (y) = y

second: 1, 2
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 2
