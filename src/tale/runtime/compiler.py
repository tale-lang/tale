from typing import Iterable

from tale.runtime.vm import Instruction
from tale.syntax.nodes import Node


def compile(node: Node) -> Iterable[Instruction]:
    """Converts a syntax tree to the list of virtual machine instructions."""

    # foreach child in node.children:
    #     is last = child == node.children[-1]
    #
    #     if it's a statement:
    #         child = child.children[0]
    #
    #     if it's an expression:
    #         generate code for expression
    #
    #         if is not last:
    #             generate Pop
    #
    #     if it's an assignment:
    #         generate code for assignment

    # when generating code for a statement:
    #     if it's an assignment: generate code for assignment
    #     if it's an expression: generate code for expression

    # when generating code for an assignment:
    #     name = name of the form   (overloaded) (1)
    #     value = value of the form
    #     args = args of the form   (overloaded)
    #
    #     generate StartBind for name and args
    #     generate body of the value
    #     generate EndBind

    # when generating body of the assignment:
    #     if it's a compound expression:
    #         generate as node with child
    #     if it's a expression:
    #         generate for expression

    # when generating code for an expression:
    #     value = value of the expression
    #
    #     if it's an int literal:
    #         generate PushInt value
    #     if it's an string literal:
    #         generate PushString value
    #     if it's a primitive expression:
    #         generate Call with value
    #     if it's an expression with arguments:
    #         foreach argument:
    #             generate argument
    #         generate Call with value

    # when generating an argument:
    #     if it's an int literal:
    #         generate PushInt value
    #     if it's an string literal:
    #         generate PushString value
    #     if it's an expression:
    #         generate expression
