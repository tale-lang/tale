from tale.core import execute


def test_type():
    # Arrange.
    program = """
x = 1
x type
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 'Int'


def test_pattern_matching_integer_branch():
    # Arrange.
    program = """
just: (x: Int) = x
just: (x)      = Error

just: 1
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 1


def test_pattern_matching_common_branch():
    # Arrange.
    program = """
just: (x: Int) = x
just: (x)      = Error

just: a
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 'Error'
