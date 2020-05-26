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
