from enum import Enum, EnumMeta
from typing import Self

__all__ = ("Note", "Color")

class Note(Enum):
    C = "C"
    Db = "Db"
    D = "D"
    Eb = "Eb"
    E = "E"
    F = "F"
    Gb = "Gb"
    G = "G"
    Ab = "Ab"
    A = "A"
    Bb = "Bb"
    B = "B"


class SimpleEnum(EnumMeta):
    def __getattribute__(self, name: str, /) -> Self:
        attr = super().__getattribute__(name)
        if isinstance(attr, type(self)):
            return attr.value
        return attr

class Color(Enum):
    RED = "red"
    BLUE = "blue"
    GREEN = "green"
    YELLOW = "yellow"
    PINK = "pink"
    PURPLE = "purple"
    BLACK = "black"
    WHITE = "white"
