from tale.core import execute


def test_common_branch():
    # Arrange.
    program = """
just: (x) = x
just: b = c

just: a
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 'a'


def test_specific_branch_bottom():
    # Arrange.
    program = """
just: (x) = x
just: b = c

just: b
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 'b'


def test_specific_branch_top():
    # Arrange.
    program = """
just: b = c
just: (x) = x

just: b
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 'c'


def test_common_branch_with_three_branches():
    # Arrange.
    program = """
just: a = b
just: b = c
just: (x) = x

just: c
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 'c'


def test_first_specific_branch_with_three_branches():
    # Arrange.
    program = """
just: a = b
just: b = c
just: (x) = x

just: a
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 'b'


def test_second_specific_branch_with_three_branches():
    # Arrange.
    program = """
just: a = b
just: b = c
just: (x) = x

just: b
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 'c'


def test_unary_form_common_branch():
    # Arrange.
    program = """
a just = b
b just = c
(x) just = x

c just
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 'c'


def test_unary_form_specific_branch():
    # Arrange.
    program = """
a just = b
b just = c
(x) just = x

a just
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 'b'


def test_binary_form_common_branch():
    # Arrange.
    program = """
a + b = c
(x) + (y) = x

a + c
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 'a'


def test_binary_form_specific_branch():
    # Arrange.
    program = """
a + b = c
(x) + (y) = x

a + b
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 'c'


def test_pattern_matching_without_common_branch():
    # Arrange.
    program = """
a + b = c
a + c = d

a + c
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 'd'


def test_pattern_matching_of_keyword_form_with_prefix():
    # Arrange.
    program = """
1 plus: 2 = 3
1 plus: 2
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 3


def test_pattern_matching_with_tuple_argument_common_branch():
    # Arrange.
    program = """
1, 2 just = 3
(x), (y) just = x

1, 1 just
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 1


def test_pattern_matching_with_tuple_argument_specific_branch():
    # Arrange.
    program = """
1, 2 just = 3
(x), (y) just = x

1, 2 just
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 3


def test_pattern_matching_with_half_of_tuple_argument():
    # Arrange.
    program = """
1, 2 just = 3
(x), 2 just = 4
(x),(y) just = x

2, 2 just
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 4


def test_pattern_matching_with_prefix_operator_specific_branch():
    # Arrange.
    program = """
-1 = 2
-(x) = x

-1
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 2


def test_pattern_matching_with_prefix_operator_common_branch():
    # Arrange.
    program = """
-1 = 2
-(x) = x

-3
"""

    # Act.
    out = execute(program)

    # Assert.
    assert out == 3
