from abc import ABCMeta, abstractmethod
from typing import Any, Iterable, Sequence, Tuple

from tale.runtime.ts import TaleInt, TaleObject, TaleString


class Instruction(metaclass=ABCMeta):
    """A Tale Virtual Machine's instruction."""
    
    @abstractmethod
    def execute(self, vm: 'Vm'):
        """Changes the state of the virtual machine.

        Args:
            vm: An instance of the Tale Virtual Machine.
        """


class StartBind(Instruction):
    """Start a binding of the function.

    Attributes:
        name: A name of the function that is represented by the binding.
        params: A list of pairs where each consists of either an expected value
            of a parameter or an expected type of a parameter.
    """

    def __init__(self, name: str, params: Iterable[Tuple[str, str]] = None):
        self.name = name
        self.params = params

    def execute(self, vm: 'Vm'):
        """Defines a function in the VM within the current scope.

        Args:
            vm: An instance of the Tale Virtual Machine.
        """

        address = vm.instruction_index + 1
        stack = 1

        while stack != 0:
            vm.move_next()

            if isinstance(vm.current_instruction, EndBind):
                stack -= 1
            if isinstance(vm.current_instruction, StartBind):
                stack += 1

        vm.scope.define(Function(self.name, self.params, address))
        vm.move_next()


class EndBind(Instruction):
    """End current `StartBind` definition."""

    def execute(self, vm: 'Vm'):
        """Moves VM to the previous `Call` location."""

        vm.scope = vm.scope.parent
        vm.jump_to(vm.return_stack.pop())


class Call(Instruction):
    """Call a function.

    Attributes:
        name: A name of the function to be called.
    """

    def __init__(self, name: str):
        self.name = name

    def execute(self, vm: 'Vm'):
        """Moves VM to the location of the function that matches the specified
           name and arguments.
        """

        functions = vm.scope.functions(self.name)

        for f in functions:
            if isinstance(f, ConstFunction):
                vm.values_stack.append(f.value)
                vm.move_next()
                return
            else:
                if not f.matches(vm.args_stack):
                    continue

                # TODO: Rethink this.
                for x in vm.args_stack:
                    vm.values_stack.append(x)
                vm.args_stack.clear()

                vm.scope = Scope(parent=vm.scope)
                vm.return_stack.append(vm.instruction_index + 1)
                vm.jump_to(f.address)
                return

        vm.move_next()


class Pop(Instruction):
    """Pop a value from the stack."""

    def execute(self, vm: 'Vm'):
        vm.values_stack.pop()
        vm.move_next()


class PopTo(Instruction):
    """Pop a value from the stack and bind it to the specified name."""

    def __init__(self, name: str):
        self.name = name

    def execute(self, vm: 'Vm'):
        value = vm.values_stack.pop()
        vm.scope.define(ConstFunction(self.name, value))
        vm.move_next()


class PushArg(Instruction):
    """Pop a value from the stack and pushe it to the args stack."""

    def execute(self, vm: 'Vm'):
        vm.args_stack.append(vm.values_stack.pop())
        vm.move_next()


class PushInt(Instruction):
    """Push an integer onto the stack.

    Attributes:
        value: An integer value that would be pushed onto the stack.
    """

    def __init__(self, value: int):
        self.value = TaleObject(TaleInt, value)

    def execute(self, vm: 'Vm'):
        vm.values_stack.append(self.value)
        vm.move_next()


class PushString(Instruction):
    """Push a string onto the stack.

    Attributes:
        value: A string value that would be pushed onto the stack.
    """

    def __init__(self, value: str):
        self.value = TaleObject(TaleString, value)

    def execute(self, vm: 'Vm'):
        vm.values_stack.append(self.value)
        vm.move_next()


class Function:
    """A function that is defined within a virtual machine.

    Attributes:
        name: A name of the function.
        params: A list of parameters of the function that are needed for
            pattern matching.
        address: An address of the function body.
    """

    def __init__(self,
                 name: str,
                 params: Iterable[Tuple[str, str]],
                 address: int):
        self.name = name
        self.params = params
        self.address = address

    def matches(self, args: Iterable[Any]) -> bool:
        if self.params is None:
            return True

        if len(self.params) != len(args):
            return False

        for param, arg in zip(self.params, args):
            # Means that we need to pattern match on value.
            if len(param) == 1:
                if param[0] != arg.py_instance:
                    return False

            # Means that we need to pattern match on type.
            if len(param) == 2:
                # TODO: Implement more accurate checking.
                if param[1] != arg.type.name.py_instance:
                    return False

        return True


# TODO: Refactor `Function` to abstract class.
class ConstFunction(Function):
    """A function that returns a constant value."""

    def __init__(self, name, value):
        super().__init__(name, None, None)
        self.value = value


class Scope:
    """A scope of the execution.

    For example, when a function is executed, it is executed in the new scope,
    which is destroyed after the function is finished.

    Attributes:
        parent: A scope that is responsible for the creation of this one.
    """

    def __init__(self, parent: 'Scope' = None):
        self.parent = parent
        self._functions = []

    def functions(self, name: str) -> Iterable[Function]:
        """Finds all functions with the specified name.

        Args:
            name: A function name. For example, 'x' or '()+()', etc.

        Returns:
            A sequence of functions that match the specified name.
            They could be either from the current scope or from any parent one.
        """

        def parent_functions() -> Iterable['Function']:
            return self.parent._functions if self.parent is not None else []

        for f in self._functions:
            if f.name == name:
                yield f

        for f in parent_functions():
            if f.name == name:
                yield f

    def define(self, f: Function):
        """Defines a function in the scope.

        Args:
            f: A function to be defined.
        """

        self._functions.append(f)


class Vm:
    """An implementation of the Tale Virtual Machine.

    Attributes:
        instructions: A sequence of instructions this virtual machine should
            execute with.
        instruction_index: An index of the currently executing instruction.
        values_stack: A stack that holds values.
        args_stack: A stack that holds arguments.
        return_stack: A stack that holds return addresses.
        scope: A scope of the execution. For example, each new function
            call opens a new scope.
    """

    def __init__(self, instructions: Sequence[Instruction]):
        self.instructions = instructions
        self.instruction_index = 0

        self.values_stack = []
        self.args_stack = []
        self.return_stack = []
        self.scope = Scope()

    @property
    def current_instruction(self) -> Instruction:
        """Returns the current instruction of the VM."""

        return self.instructions[self.instruction_index]

    @property
    def at_the_end(self) -> bool:
        """Checks whether the VM is reached its end."""

        return self.instruction_index >= len(self.instructions) 

    def move_next(self):
        """Advances the current instruction index by 1."""

        self.instruction_index += 1

    def jump_to(self, address: int):
        """Sets the current instruction index to the specified address.

        Args:
            address: An address the VM should jump to.
        """

        self.instruction_index = address

    def execute(self):
        """Executes a list of instructions in this virtual machine.

        Args:
            instructions: A sequence of instructions to be executed.
        """

        while not self.at_the_end:
            self.current_instruction.execute(self)
