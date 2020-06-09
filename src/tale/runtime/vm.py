from typing import Iterable
from abc import ABCMeta, abstractmethod

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
#         Call 'fibonacci()'
#     EndBind
#     StartBind 'b'
#         Call 'n'
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
    """

    def __init__(self, name: str):
        self.name = name


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
        self.value = value


class PushString(Instruction):
    """Push a string onto the stack.

    Attributes:
        value: A string value that would be pushed onto the stack.
    """

    def __init__(self, value: str):
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
        self.bindings = {}

    def body(self, name: str) -> Iterable[Instruction]:
        """Finds a function body for the specified function name.

        Args:
            name: Name of the function whose body is searched for.
        """

        def parent_body():
            return self.parent.body(name) if self.parent is not None else None

        return self.bindings.get(name, None) or parent_body()


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
        current_binding = None

        for i in instructions:

            if isinstance(i, StartBind):
                binding_stack += 1
                if binding_stack == 1:
                    current_binding = i.name
                    self.scope.bindings[i.name] = []
                    continue

            if isinstance(i, EndBind):
                binding_stack -= 1
                if binding_stack == 0:
                    current_binding = None
                    continue

            if binding_stack > 0:
                self.scope.bindings[current_binding].append(i)
                continue

            if isinstance(i, Call):
                body = self.scope.body(i.name)

                if type(body) is list:
                    for x in self.args_stack:
                        self.stack.append(x)

                    self.args_stack.clear()
                    self.scope = Scope(parent=self.scope)
                    self.execute(body)
                    self.scope = self.scope.parent
                else:
                    self.stack.append(body)

            if isinstance(i, Pop):
                self.stack.pop()

            if isinstance(i, PopTo):
                value = self.stack.pop()
                self.scope.bindings[i.name] = value

            if isinstance(i, PushArg):
                self.args_stack.append(self.stack.pop())

            if isinstance(i, PushString) or \
               isinstance(i, PushInt):
                self.stack.append(i.value)
