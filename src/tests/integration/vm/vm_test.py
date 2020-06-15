from typing import Sequence

from tale.runtime.vm import (Call, EndBind, Instruction, PopTo, PushArg,
                             PushInt, StartBind, Vm)


def execute(instructions: Sequence[Instruction]) -> Vm:
    vm = Vm(instructions)
    vm.execute()

    return vm


def test_simple_literal():
    # Arrange.
    instructions = [
        PushInt(1),
    ]

    # Act.
    vm = execute(instructions)

    # Assert.
    assert len(vm.values_stack) == 1
    assert vm.values_stack[0].py_instance == 1


def test_simple_assignment():
    # Arrange.
    instructions = [
        StartBind('x'),
            PushInt(1),
        EndBind(),

        Call('x')
    ]

    # Act.
    vm = execute(instructions)

    # Assert.
    assert len(vm.values_stack) == 1
    assert vm.values_stack[0].py_instance == 1


def test_nested_assignment():
    # Arrange.
    instructions = [
        StartBind('x'),
            StartBind('y'),
                PushInt(1),
            EndBind(),
            Call('y'),
        EndBind(),
        Call('x')
    ]

    # Act.
    vm = execute(instructions)

    # Assert.
    assert len(vm.values_stack) == 1
    assert vm.values_stack[0].py_instance == 1


def test_function_call():
    # Arrange.
    instructions = [
        StartBind('()x'),
            PopTo('a'),
            Call('a'),
        EndBind(),
        PushInt(1),
        PushArg(),
        Call('()x')
    ]

    # Act.
    vm = execute(instructions)

    # Assert.
    assert len(vm.values_stack) == 1
    assert vm.values_stack[0].py_instance == 1


def test_function_call_with_value_pattern_matching():
    # Arrange.
    instructions = [
        StartBind('()x', [(1,)]),
            PopTo('a'),
            PushInt(2),
        EndBind(),
        PushInt(1),
        PushArg(),
        Call('()x')
    ]

    # Act.
    vm = execute(instructions)

    # Assert.
    assert len(vm.values_stack) == 1
    assert vm.values_stack[0].py_instance == 2


def test_function_call_with_value_pattern_matching_that_failed_to_match():
    # Arrange.
    instructions = [
        StartBind('()x', [(1,)]),
            PopTo('a'),
            PushInt(2),
        EndBind(),
        PushInt(2),
        PushArg(),
        Call('()x')
    ]

    # Act.
    vm = execute(instructions)

    # Assert.
    assert vm.values_stack == []


def test_function_call_with_type_pattern_matching():
    # Arrange.
    instructions = [
        StartBind('()x', [(None, 'Int')]),
            PopTo('a'),
            PushInt(2),
        EndBind(),
        PushInt(2),
        PushArg(),
        Call('()x')
    ]

    # Act.
    vm = execute(instructions)

    # Assert.
    assert len(vm.values_stack) == 1
    assert vm.values_stack[0].py_instance == 2


def test_function_call_with_type_pattern_matching_that_failed_to_match():
    # Arrange.
    instructions = [
        StartBind('()x', [(None, 'String')]),
            PopTo('a'),
            PushInt(2),
        EndBind(),
        PushInt(1),
        PushArg(),
        Call('()x')
    ]

    # Act.
    vm = execute(instructions)

    # Assert.
    assert vm.values_stack == []
