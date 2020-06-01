from tale.core import execute


def test_simple_form():
    # Arrange.
    program = """
-(x) = x
-1
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 1
