from typing import Any


class TaleObject:
    """A basic block of Tale's object model.

    All values in Tale exist only as instances of this class.

    For example, in the following expression:
        x = 1
    `1` is an instance of `TaleObject`.

    Attributes:
        type_: An instance of `TaleObject` that represents the type of the
            object.
        name: A name of the object.
        py_instance: An instance of the object in Python memory.
    """

    def __init__(self, type_: 'TaleObject', py_instance: Any):
        self.type_ = type_
        self.py_instance = py_instance


NoneObject = TaleObject(None, None)
