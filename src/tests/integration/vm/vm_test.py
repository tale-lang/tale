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
    assert vm.stack == [1]


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
    assert vm.stack == [1]


class test_nested_assignment():
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
    assert vm.stack == [1]


class test_function_call():
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
    assert vm.stack == [1]
