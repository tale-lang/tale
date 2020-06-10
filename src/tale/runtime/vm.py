from abc import ABCMeta, abstractmethod
from typing import Any, Iterable, Tuple

from tale.runtime.ts import TaleInt, TaleObject, TaleString

# Case 1:
# ------
# x = 1
# x
# ------
# StartBind 'x'
#     PushInt 1
# EndBind
# Call 'x'
# ------

# Case 2:
# ------
# x = 1
# 2
# x
# ------
# StartBind 'x'
#     PushInt 1
# EndBind
# Call 'x'
# ------

# Case 3:
# ------
# x = 1
# print: "Hello, world"
# x
# ------
# StartBind 'x'
#     PushInt 1
# EndBind
# PushString "Hello, world"
# PushArg
# Call 'print()'
# Pop
# Call 'x'
# ------

# Case 4:
# ------
# x =
#     y =
#         z = 1
#         z
#     y
# x
# ------
# StartBind 'x'
#   StartBind 'y'
#       StartBind 'z'
#           PushInt 1
#       EndBind
#       Call 'z'
#   Call 'y'
# EndBind
# Call 'x'
# ------

# Case 5:
# ------
# fibonacci: 1 = 0
# fibonacci: 2 = 1
# fibonacci: (n) =
#     a = fibonacci: n - 1
#     b = fibonacci: n - 2
#     a + b
#
# fibonacci: 10
# ------
# StartBind 'fibonacci()' 1
#     PushInt 0
# EndBind
# StartBind 'fibonacci()' 2
#     PushInt 1
# EndBind
# StartBind 'fibonacci()'
#     PopTo 'n'
#     StartBind 'a'
#         Call 'n'
#         PushArg
#         Call 'fibonacci()'
#     EndBind
#     StartBind 'b'
#         Call 'n'
#         PushArg
#         Call 'fibonacci()'
#     EndBind
#     Call 'a'
#     Call 'b'
#     PushArg
#     PushArg
#     Call '()+()'
# EndBind
# PushInt 10
# PushArg
# Call 'fibonacci()'
# ------

# Without arg:
# Call 'x'

# With simple arg:
# PushInt 1
# PushArg
# Call '()x'

# With typed arg:
# PushInt 1
# PushArg
# Call '()x'

# With value arg:
# PushInt 1
# PushArg
# Call '()x'

# With two typed args:
# PushInt 1
# PushInt 2
# PushArg
# PushArg
# Call '()x()'

class Instruction(metaclass=ABCMeta):
    """A Tale Virtual Machine's instruction."""


class StartBind(Instruction):
    """Starts a binding of the function.

    Attributes:
        name: A name of the function.
        params: A list of pairs where each consists of either an expected value
            of an argument or an expected type of an argument.
    """

    def __init__(self, name: str, params: Iterable[Tuple[str, str]] = None):
        self.name = name
        self.params = params


class EndBind(Instruction):
    """End current `Bind` definition."""


class Call(Instruction):
    """Call a function.

    Attributes:
        name: A name of the function to be called.
    """

    def __init__(self, name: str):
        self.name = name


class Pop(Instruction):
    """Pop a value from the stack."""


class PopTo(Instruction):
    """Pops a value from the stack and binds it to the specified name."""

    def __init__(self, name: str):
        self.name = name


class PushArg(Instruction):
    """Pops a value from the stack and pushes it to the args stack."""


class PushInt(Instruction):
    """Push an integer onto the stack.

    Attributes:
        value: An integer value that would be pushed onto the stack.
    """

    def __init__(self, value: int):
        self.value = TaleObject(TaleInt, value)


class PushString(Instruction):
    """Push a string onto the stack.

    Attributes:
        value: A string value that would be pushed onto the stack.
    """

    def __init__(self, value: str):
        self.value = TaleObject(TaleString, value)


class Function:
    """Represents a defined function.

    Attributes:
        name: A name of the function.
        params: A list of parameters of the function that are needed for
            pattern matching.
        body: A list of instructions that represent the body of the function.
    """

    def __init__(self,
                 name: str,
                 params: Iterable[Tuple[str, str]],
                 body: Iterable[Instruction]):
        self.name = name
        self.body = body
        self.params = params

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
    """Represents a function that returns a constant value."""

    def __init__(self, name, value):
        super().__init__(name, None, None)
        self.value = value


class Scope:
    """A scope of the execution.

    For example, when a function is executed, it is executed in the new scope,
    which is destroyed after the function is finished.

    Attributes:
        stack: A stack of the virtual machine. Holds arguments and return values.
        bindings: A dictionary of bindings that are defined in the current block.
    """

    def __init__(self, parent: 'Scope' = None):
        self.parent = parent
        self._functions = []

    def functions(self, name: str) -> Iterable[Function]:
        """Finds all functions with the specified name.

        Args:
            name: Name of a function. For example, 'x' or '()+()', etc.

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
    """A Tale Virtual Machine implementation.

    Attributes:
        stack: A stack of the virtual machine. Holds arguments and return values.
        args_stack: A stack that holds arguments.
        scope: A current scope of the execution. For example, each new function
            call opens a new scope.
    """

    def __init__(self):
        self.stack = []
        self.args_stack = []
        self.scope = Scope()

    def execute(self, instructions: Iterable[Instruction]):
        """Executes a list of instructions in this virtual machine.

        Args:
            instructions: A sequence of instructions to be executed.
        """

        binding_stack = 0
        binding = None
        name = None
        params = None
        body = None

        for i in instructions:

            if isinstance(i, StartBind):
                binding_stack += 1
                if binding_stack == 1:
                    binding = i.name
                    name = i.name
                    params = i.params
                    body = []
                    continue

            if isinstance(i, EndBind):
                binding_stack -= 1
                if binding_stack == 0:
                    self.scope.define(Function(name, params, body))
                        
                    binding = None
                    body = None
                    name = None
                    continue

            if binding_stack > 0:
                body.append(i)
                continue

            if isinstance(i, Call):
                functions = self.scope.functions(i.name)

                for f in functions:
                    if isinstance(f, ConstFunction):
                        self.stack.append(f.value)
                    else:
                        if not f.matches(self.args_stack):
                            continue

                        for x in self.args_stack:
                            self.stack.append(x)

                        self.args_stack.clear()
                        self.scope = Scope(parent=self.scope)
                        self.execute(f.body)
                        self.scope = self.scope.parent

            if isinstance(i, Pop):
                self.stack.pop()

            if isinstance(i, PopTo):
                value = self.stack.pop()
                self.scope.define(ConstFunction(i.name, value))

            if isinstance(i, PushArg):
                self.args_stack.append(self.stack.pop())

            if isinstance(i, PushString) or \
               isinstance(i, PushInt):
                self.stack.append(i.value)
