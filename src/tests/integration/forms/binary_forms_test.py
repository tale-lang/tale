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
    assert out == 1


def test_second_argument():
    # Arrange.
    program = """
(x) + (y) = y

1 + 2
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 2


def test_binary_form_as_result():
    # Arrange.
    program = """
x = 1
y = 2

x + y
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 'x+y'
