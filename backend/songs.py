from dataclasses import dataclass
from .enums import Note

__all__ = ("SONGS",)

SONGS = []

@dataclass
class OdeToJoy:
    notes: dict[str, int] = {
        Note.E: 700,
        Note.E: 700,
        Note.F: 700,
        Note.G: 700
    }


SONGS.append(OdeToJoy)