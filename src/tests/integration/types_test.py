from tale.core import execute


def test_integer_type():
    # Arrange.
    program = """
x = 1
x type
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 'Int'
