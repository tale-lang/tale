from tale.core import execute


def test_simple_assignment():
    # Arrange.
    program = """
(x) just = x
1 just
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == '1'


def test_nested_expression():
    # Arrange.
    program = """
(x) just = x
(1 just) just
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == '1'
