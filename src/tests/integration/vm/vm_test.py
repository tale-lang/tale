from tale.runtime.vm import (Call, EndBind, PopTo, PushArg, PushInt, StartBind,
                             Vm)


def test_simple_literal():
    # Arrange.
    vm = Vm()
    instructions = [
        PushInt(1),
    ]

    # Act.
    vm.execute(instructions)

    # Assert.
    assert len(vm.stack) == 1
    assert vm.stack[0].py_instance == 1


def test_simple_assignment():
    # Arrange.
    vm = Vm()
    instructions = [
        StartBind('x'),
            PushInt(1),
        EndBind(),

        Call('x')
    ]

    # Act.
    vm.execute(instructions)

    # Assert.
    assert len(vm.stack) == 1
    assert vm.stack[0].py_instance == 1


def test_nested_assignment():
    # Arrange.
    vm = Vm()
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
    vm.execute(instructions)

    # Assert.
    assert len(vm.stack) == 1
    assert vm.stack[0].py_instance == 1


def test_function_call():
    # Arrange.
    vm = Vm()
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
    vm.execute(instructions)

    # Assert.
    assert len(vm.stack) == 1
    assert vm.stack[0].py_instance == 1


def test_function_call_with_value_pattern_matching():
    # Arrange.
    vm = Vm()
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
    vm.execute(instructions)

    # Assert.
    assert len(vm.stack) == 1
    assert vm.stack[0].py_instance == 2


def test_function_call_with_value_pattern_matching_that_failed_to_match():
    # Arrange.
    vm = Vm()
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
    vm.execute(instructions)

    # Assert.
    assert vm.stack == []


def test_function_call_with_type_pattern_matching():
    # Arrange.
    vm = Vm()
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
    vm.execute(instructions)

    # Assert.
    assert len(vm.stack) == 1
    assert vm.stack[0].py_instance == 2


def test_function_call_with_type_pattern_matching_that_failed_to_match():
    # Arrange.
    vm = Vm()
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
    vm.execute(instructions)

    # Assert.
    assert vm.stack == []
