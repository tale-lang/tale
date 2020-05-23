from tale.core import execute


def test_simple_unary_form():
    # Arrange.
    program = """
just: (x) = x
just: 1
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == '1'


def test_unary_form_with_two_parts_first_arg():
    # Arrange.
    program = """
add: (x) to: (y) = x
add: 1 to: 2
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == '1'


def test_unary_form_with_two_parts_second_arg():
    # Arrange.
    program = """
add: (x) to: (y) = y
add: 1 to: 2
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == '2'


def test_unary_form_with_prefix_first_arg():
    # Arrange.
    program = """
(x) just: (y) = x
1 just: 2
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == '1'


def test_unary_form_with_prefix_second_arg():
    # Arrange.
    program = """
(x) just: (y) = y
1 just: 2
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == '2'
