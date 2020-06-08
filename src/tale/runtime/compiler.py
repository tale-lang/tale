from typing import Iterable

from tale.runtime.vm import Instruction
from tale.syntax.nodes import Node


def compile(node: Node) -> Iterable[Instruction]:
    """Converts a syntax tree to the list of virtual machine instructions."""
