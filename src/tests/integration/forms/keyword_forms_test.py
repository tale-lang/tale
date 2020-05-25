from tale.core import execute


def test_simple_keyword_form():
    # Arrange.
    program = """
just: (x) = 1
just: 2
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 1


def test_simple_keyword_form_returns_arg():
    # Arrange.
    program = """
just: (x) = x
just: 1
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 1


def test_keyword_form_with_two_parts_first_arg():
    # Arrange.
    program = """
add: (x) to: (y) = x
add: 1 to: 2
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 1


def test_keyword_form_with_two_parts_second_arg():
    # Arrange.
    program = """
add: (x) to: (y) = y
add: 1 to: 2
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 2


def test_keyword_form_with_prefix_first_arg():
    # Arrange.
    program = """
(x) just: (y) = x
1 just: 2
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 1


def test_keyword_form_combined_with_unary_form():
    # Arrange.
    program = """
(x) squared = x
just: (x) = x
just: 1 squared
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 1


def test_keyword_form_has_less_priority_than_binary():
    # Arrange.
    program = """
just: (x) = x
just: 1 + 2
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 3
