import pygame
from backend import Note, Color

RASPBERRY = (227,27,93)

class Key(pygame.Rect):
    def __init__(self, default_color, note: Note, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.active = False
        self.default_color = default_color
        self.current_color = self.default_color
        self.note: Note = note if isinstance(note, Note) else Note(note)
    
    def press(self, change, on):
        if change:
            if on:
                self.active = True
                self.current_color = (RASPBERRY)
            else:
                self.active = False
                self.current_color = (self.default_color)
        

    
        
    