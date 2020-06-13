from typing import Type

from tale.runtime.compiler import compile
from tale.runtime.vm import Call, EndBind, PopTo, PushInt, StartBind
from tale.syntax.nodes import Node
from tale.syntax.parsers.antlr4 import Antlr4Parser


def ast(of: str) -> Node:
    return Antlr4Parser().ast(of)


def types(x) -> [Type]:
    return [type(x) for x in x]


def test_simple_literal_generates_one_instruction():
    # Arrange.
    program = """
1
"""

    # Act.
    i = compile(ast(program))

    # Assert.
    assert len(i) == 1


def test_int_literal_generates_push_int():
    # Arrange.
    program = """
1
"""

    # Act.
    i = compile(ast(program))

    # Assert.
    assert i[0].value.py_instance == 1


def test_string_literal_generates_push_string():
    # Arrange.
    program = """
"1"
"""

    # Act.
    i = compile(ast(program))

    # Assert.
    assert i[0].value.py_instance == '"1"'


def test_simple_assignment():
    # Arrange.
    program = """
x = 1
"""

    # Act.
    i = compile(ast(program))

    # Assert.
    assert types(i) == [
        StartBind,
            PushInt,
        EndBind
    ]


def test_primitive_call():
    # Arrange.
    program = """
x = 1
x
"""

    # Act.
    i = compile(ast(program))

    # Assert.
    assert types(i) == [
        StartBind,
            PushInt,
        EndBind,
        Call
    ]


def test_primitive_call_of_x_actually_calls_x():
    # Arrange.
    program = """
x = 1
x
"""

    # Act.
    i = compile(ast(program))

    # Assert.
    assert i[-1].name == 'x'


def test_unary_form_assignment():
    # Arrange.
    program = """
(x) squared = 1
"""

    # Act.
    i = compile(ast(program))

    # Assert.
    assert types(i) == [
        StartBind,
            PopTo,
            PushInt,
        EndBind
    ]


def test_unary_form_assignment_actually_pops_an_argument():
    # Arrange.
    program = """
(x) squared = 1
"""

    # Act.
    i = compile(ast(program))

    # Assert.
    assert i[1].name == 'x'


def test_unary_form_assignment_binds_with_pattern_matching_value():
    # Arrange.
    program = """
1 squared = 1
"""

    # Act.
    i = compile(ast(program))

    # Assert.
    assert i[0].params == [(1, None)]


def test_unary_form_assignment_binds_with_pattern_matching_type():
    # Arrange.
    program = """
(x: Int) squared = 1
"""

    # Act.
    i = compile(ast(program))

    # Assert.
    assert i[0].params == [(None, 'Int')]


def test_unary_form_call():
    # Arrange.
    program = """
(x) squared = 1
1 squared
"""

    # Act.
    i = compile(ast(program))

    # Assert.
    assert types(i) == [
        StartBind,
            PopTo,
            PushInt,
        EndBind,
        PushInt,
        Call
    ]


def test_unary_form_call_with_correct_function_name():
    # Arrange.
    program = """
(x) squared = 1
1 squared
"""

    # Act.
    i = compile(ast(program))

    # Assert.
    assert i[-1].name == '()squared'
    

def test_prefix_form_assignment():
    # Arrange.
    program = """
!(x) = 1
"""

    # Act.
    i = compile(ast(program))

    # Assert.
    assert types(i) == [
        StartBind,
            PopTo,
            PushInt,
        EndBind
    ]


def test_prefix_form_assignment_actually_pops_an_argument():
    # Arrange.
    program = """
!(x) = 1
"""

    # Act.
    i = compile(ast(program))

    # Assert.
    assert i[1].name == 'x'
    

def test_prefix_form_assignment_binds_with_pattern_matching_value():
    # Arrange.
    program = """
!1 = 1
"""

    # Act.
    i = compile(ast(program))

    # Assert.
    assert i[0].params == [(1, None)]


def test_prefix_form_assignment_binds_with_pattern_matching_type():
    # Arrange.
    program = """
!(x: Int) = 1
"""

    # Act.
    i = compile(ast(program))

    # Assert.
    assert i[0].params == [(None, 'Int')]


def test_prefix_form_call():
    # Arrange.
    program = """
!(x) = 1
!1
"""

    # Act.
    i = compile(ast(program))

    # Assert.
    assert types(i) == [
        StartBind,
            PopTo,
            PushInt,
        EndBind,
        PushInt,
        Call
    ]


def test_prefix_form_call_with_correct_function_name():
    # Arrange.
    program = """
!(x) = 1
!1
"""

    # Act.
    i = compile(ast(program))

    # Assert.
    assert i[-1].name == '!()'
    

def test_binary_form_assignment():
    # Arrange.
    program = """
(x) + (y) = 1
"""

    # Act.
    i = compile(ast(program))

    # Assert.
    assert types(i) == [
        StartBind,
            PopTo,
            PopTo,
            PushInt,
        EndBind
    ]


def test_binary_form_assignment_actually_pops_an_argument():
    # Arrange.
    program = """
(x) + (y) = 1
"""

    # Act.
    i = compile(ast(program))

    # Assert.
    assert i[1].name == 'x'
    assert i[2].name == 'y'


def test_binary_form_assignment_binds_with_pattern_matching_value():
    # Arrange.
    program = """
1 + 2 = 3
"""

    # Act.
    i = compile(ast(program))

    # Assert.
    assert i[0].params == [(1, None), (2, None)]


def test_binary_form_assignment_binds_with_pattern_matching_type_and_value():
    # Arrange.
    program = """
(x: Int) + 1 = 1
"""

    # Act.
    i = compile(ast(program))

    # Assert.
    assert i[0].params == [(None, 'Int'), (1, None)]


def test_binary_form_call():
    # Arrange.
    program = """
(x) + (y) = 1
1 + 1
"""

    # Act.
    i = compile(ast(program))

    # Assert.
    assert types(i) == [
        StartBind,
            PopTo,
            PopTo,
            PushInt,
        EndBind,
        PushInt,
        PushInt,
        Call
    ]


def test_binary_form_call_with_correct_function_name():
    # Arrange.
    program = """
(x) + (y) = 1
1 + 1
"""

    # Act.
    i = compile(ast(program))

    # Assert.
    assert i[-1].name == '()+()'


def test_keyword_form_assignment():
    # Arrange.
    program = """
a: (x) b: (y) c: (z) = 1
"""

    # Act.
    i = compile(ast(program))

    # Assert.
    assert types(i) == [
        StartBind,
            PopTo,
            PopTo,
            PopTo,
            PushInt,
        EndBind
    ]


def test_keyword_form_assignment_actually_pops_an_argument():
    # Arrange.
    program = """
a: (x) b: (y) c: (z) = 1
"""

    # Act.
    i = compile(ast(program))

    # Assert.
    assert i[1].name == 'x'
    assert i[2].name == 'y'
    assert i[3].name == 'z'


def test_keyword_form_assignment_binds_with_pattern_matching_value():
    # Arrange.
    program = """
a: 1 b: 2 c: 3 = 1
"""

    # Act.
    i = compile(ast(program))

    # Assert.
    assert i[0].params == [(1, None), (2, None), (3, None)]


def test_keyword_form_assignment_binds_with_pattern_matching_type_and_value():
    # Arrange.
    program = """
a: (x: Int) b: 2 c: (y: Int) = 1
"""

    # Act.
    i = compile(ast(program))

    # Assert.
    assert i[0].params == [(None, 'Int'), (2, None), (None, 'Int')]


def test_keyword_form_call():
    # Arrange.
    program = """
a: (x) b: (y) c: (z) = 1
a: 1 b: 2 c: 3
"""

    # Act.
    i = compile(ast(program))

    # Assert.
    assert types(i) == [
        StartBind,
            PopTo,
            PopTo,
            PopTo,
            PushInt,
        EndBind,
        PushInt,
        PushInt,
        PushInt,
        Call
    ]


def test_keyword_form_call_with_correct_function_name():
    # Arrange.
    program = """
a: (x) b: (y) c: (z) = 1
a: 1 b: 2 c: 3
"""

    # Act.
    i = compile(ast(program))

    # Assert.
    assert i[-1].name == 'a()b()c()'
