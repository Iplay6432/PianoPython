from enum import Enum

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


class Color(Enum):
    RED = "red"
    BLUE = "blue"
    GREEN = "green"
    YELLOW = "yellow"
    PINK = "pink"
    PURPLE = "purple"
    BLACK = "black"
    WHITE = "white"
