from tale.core import execute


def test_simple_assignment():
    # Arrange.
    program = """
x = y
x
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 'y'
