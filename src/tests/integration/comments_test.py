import pytest

from tale.core import execute


def test_one_comment():
    # Arrange.
    program = """
-- A.
1
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 1


def test_two_comments():
    # Arrange.
    program = """
-- A.
-- B.
1
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 1


def test_comments_after_code():
    # Arrange.
    program = """
-- A.
1
-- B.
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 1


def test_invalid_comment():
    # Arrange.
    program = """
- A.
1
"""

    # Act & Assert.
    with pytest.raises(Exception):
        out = execute(program)
