from tale.core import execute


def test_type():
    # Arrange.
    program = """
x = "a"
x type
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 'String'
