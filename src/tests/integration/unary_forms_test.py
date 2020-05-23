from tale.core import execute


def test_simple_assignment():
    # Arrange.
    program = """
(x) just = x
1 just
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == '1'


def test_nested_expression():
    # Arrange.
    program = """
(x) just = x
(1 just) just
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == '1'


def test_not_matched_expression():
    # Arrange.
    program = """
(x) just = x
1 jusx
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == '1jusx'


def test_unary_form_span_on_multiple_lines():
    # Arrange.
    program = """
(x) just =
    y = x
    y

1 just
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == '1'
