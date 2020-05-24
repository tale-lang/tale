from tale.core import execute


def test_common_branch():
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


def test_specific_branch_bottom():
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


def test_specific_branch_top():
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


def test_common_branch_with_three_branches():
    # Arrange.
    program = """
just: a = b
just: b = c
just: (x) = x

just: c
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 'c'


def test_first_specific_branch_with_three_branches():
    # Arrange.
    program = """
just: a = b
just: b = c
just: (x) = x

just: a
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 'b'


def test_second_specific_branch_with_three_branches():
    # Arrange.
    program = """
just: a = b
just: b = c
just: (x) = x

just: b
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 'c'
