from tale.core import execute


def test_simple_pattern_matching_common_branch():
    # Arrange.
    program = """
just: (x) = x
just: b = c

just: a
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 'a'


def test_simple_pattern_matching_specific_branch_bottom():
    # Arrange.
    program = """
just: (x) = x
just: b = c

just: b
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 'b'


def test_simple_pattern_matching_specific_branch_top():
    # Arrange.
    program = """
just: b = c
just: (x) = x

just: b
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 'c'
