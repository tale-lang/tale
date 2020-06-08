# x = 1     -> Bind 'x'
#              PushInt 1
#              Return
#              EndBind 'x'

# 1         -> Nop
# 1         -> PushInt 1      (if last expression in the block)
# "1" last  -> PushString "1" (if last expression in the block)

# x         -> Call 'x'       (if has return value)
#              Pop

# x         -> Call 'x'       (if last expression in the block)

# !x        -> Call 'x'
#              Call '!()'

# x squared -> Call 'x'
#              Call '()squared'

# x + y     -> Call 'x'
#              Call 'y'
#              Call '()+()'

# squared: x -> Call 'x'
#               Call 'squared()'

# Case 1:
# ------
# x = 1
# x
# -----
# Bind 'x'
#     PushInt 1
#     Return
# EndBind
# Call 'x'
# Return
# -----

# Case 2:
# ------
# x = 1
# 2
# x
# -----
# Bind 'x'
#     PushInt 1
#     Return
# EndBind
# Call 'x'
# Return
# -----

# Case 3:
# ------
# x = 1
# print: "Hello, world"
# x
# -----
# Bind 'x'
#     PushInt 1
#     Return
# EndBind
# PushString "Hello, world"
# Call 'print()'
# Pop
# Call 'x'
# Return
# -----

# Case 4:
# ------
# x =
#     y =
#         z = 1
#         z
#     y
# x
# -----
# Bind 'x'
#   Bind 'y'
#       Bind 'z'
#           PushInt 1
#           Return
#       EndBind
#       Call 'z'
#       Return
#   Call 'y'
#   Return
# EndBind
# Call 'x'
# Return
# -----

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
# -----
# Bind 'fibonacci()' 1
#     PushInt 0
#     Return
# EndBind
# Bind 'fibonacci()' 2
#     PushInt 1
#     Return
# EndBind
# Bind 'fibonacci()'
#     Bind 'a'
#         Load 0
#         Call 'fibonacci()'
#         Return
#     EndBind
#     Bind 'b'
#         Load 0
#         Call 'fibonacci()'
#         Return
#     EndBind
#     StoreArg 0
#     Call 'a'
#     Call 'b'
#     Call '()+()'
#     Return
# EndBind
# PushInt 10
# Call 'fibonacci()'
# Return
# -----


class Instruction:
    pass


class Vm:
    def execute(self, instructions: Iterable[Instruction]):
        pass
