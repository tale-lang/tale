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
