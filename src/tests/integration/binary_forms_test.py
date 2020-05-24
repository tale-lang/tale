from tale.core import execute


def test_first_argument():
    # Arrange.
    program = """
(x) + (y) = x

1 + 2
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == '1'


def test_second_argument():
    # Arrange.
    program = """
(x) + (y) = y

1 + 2
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == '2'
