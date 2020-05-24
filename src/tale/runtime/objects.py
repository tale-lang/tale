from typing import Any


class TaleObject:
    """A basic block of Tale's object model.

    All values in Tale exist only as instances of this class.

    For example, in the following expression:
        x = 1
    `1` is an instance of `TaleObject`.

    Attributes:
        type: An instance of `TaleObject` that represents the type of the
            object.
        name: A name of the object.
        py_instance: An instance of the object in Python memory.
    """

    def __init__(self, type: 'TaleObject', py_instance: Any, name = None):
        self.type = type
        self.py_instance = py_instance
        self.name = name

TaleNone = TaleObject(None, None)

TaleType = TaleObject(type(TaleObject), None)
TaleType.type = TaleType

TaleInt = TaleObject(TaleType, int, TaleObject(TaleType, 'Int'))
