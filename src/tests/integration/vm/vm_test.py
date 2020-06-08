from tale.runtime.vm import Call, EndBind, PushInt, StartBind, Vm


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
