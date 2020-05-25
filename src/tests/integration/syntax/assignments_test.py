from tale.core import execute


def test_simple_assignment():
    # Arrange.
    program = """
x = 1
x
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 1
