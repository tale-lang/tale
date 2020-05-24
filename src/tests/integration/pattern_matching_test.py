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
