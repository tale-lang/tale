from tale.core import execute


def test_one_indentation_level():
    # Arrange.
    program = """
x =
    1
    2
    3
x
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == '3'


def test_double_indentation_level():
    # Arrange.
    program = """
x =
    y =
        1
        2
        3
    y
x
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == '3'


def test_wrong_indentation():
    # Arrange.
    program = """
x =
    1
   2
x
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out is None
