from typing import Any


class TaleObject:
    """A basic block of the Tale's object model.

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


TaleType = TaleObject(None, None)
TaleType.type = TaleType

TaleString = TaleObject(TaleType, str)
TaleString.name = TaleObject(TaleString, 'String')

TaleType.name = TaleObject(TaleString, 'Type')

TaleNone = TaleObject(None, None, TaleObject(TaleString, 'None'))
TaleInt = TaleObject(TaleType, int, TaleObject(TaleString, 'Int'))
TaleTuple = TaleObject(TaleType, None, TaleObject(TaleString, 'Tuple'))
