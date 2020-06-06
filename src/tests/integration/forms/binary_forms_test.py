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


def test_calling_keyword_form_in_body():
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


def test_compound_binary_expression():
    # Arrange.
    program = """
(x) + (y) = y

a + b + c + d
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 'd'
