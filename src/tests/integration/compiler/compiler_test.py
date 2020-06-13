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
