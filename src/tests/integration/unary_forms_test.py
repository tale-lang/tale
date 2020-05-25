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
    assert out == 1


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
    assert out == 1


def test_same_unary_form_called_many_times():
    # Arrange.
    program = """
(x) just = x
1 just just
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 1


def test_two_unary_forms_composed():
    # Arrange.
    program = """
(x) a = x
(x) b = x

1 a b a b
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 1
