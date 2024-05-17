import pygame
from backend import Note, Color
from key import Key
import json
import re

class Falling(pygame.Rect):
    def __init__(
        self, note, screen, height, width, location, len, notes
    ):  # note is the index
        # super.__init__(args)
        self.note = note
        self.screen = screen
        self.height = height
        self.width = width / 1.2
        self.location = location
        self.len = len
        self.notes = notes
        self.speed = 5
        with open("jsons/Give.json") as f:
            self.song = json.load(f)
    
    
    def place_key(self):
        def is_float(value):
            return isinstance(value, float)
    
        key_count = len(self.notes)
        self.keys = []
        vals = [0, 56, 112, 168, 224, 280, 336, 392, 448, 504, 560, 616]
        note_names = list(Note.__members__.keys())
        for note in self.song:
            
            no = ''.join([i for i in note[0] if not i.isdigit()])
         
            no = note_names.index(no)
            no = vals[no]

            self.keys.append(
                Key(
                    Color.GREEN,
                    Note.A,
                    no,
                    0,
                    (int(self.width) // key_count),
                    int(self.len),
                )
            )

        for key in self.keys:
            pygame.draw.rect(self.screen, key.current_color, key)

    def update(self):
        for key in self.keys.copy():  # iterate over a copy of the list
            # update y-coordinate
            key.y += self.speed  # adjust this value to change the speed of falling

            # redraw key
            pygame.draw.rect(self.screen, key.current_color, key)

            # remove key if it's off the screen
            if key.y > self.height / 2:
                self.keys.remove(key)

        # pygame.draw.rect(self.screen, Color.GREEN, pygame.Rect((self.note*((self.width/1.2)/13)*2),self.location,((self.width/1.2)/13)*2,self.len))
