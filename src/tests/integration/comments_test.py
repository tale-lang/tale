from tale.core import execute


def test_one_comment():
    # Arrange.
    program = """
-- Test.
1
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == '1'
