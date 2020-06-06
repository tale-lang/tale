from tale.core import execute


def test_first_argument():
    # Arrange.
    program = """
(x) + (y) = x

a + b
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 'a'


def test_second_argument():
    # Arrange.
    program = """
(x) + (y) = y

a + b
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 'b'


def test_calling_keyword_form():
    # Arrange.
    program = """
(x) and: (y) = x
(x) + (y) = x and: y

a + b
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 'a'
