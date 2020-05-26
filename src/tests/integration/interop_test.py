from tale.core import execute


def test_random():
    # Arrange.
    program = """
x = py: "import random; result = random.randint", 1, 1
x
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 1


def test_invalid_first_arg():
    # Arrange.
    program = """
x = py: 1
x
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 'py:1'


def test_overriden():
    # Arrange.
    program = """
py: (x) = x
py: 1
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 1
