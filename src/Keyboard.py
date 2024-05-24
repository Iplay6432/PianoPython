import pygame
from backend import Color, Note, enums
from key import Key
import serial
import time
import threading
class Keyboard:
    def __init__(self, width, height, screen, notes, scalew, scaleh, location):
        self.RASPBERRY = (227,27,93)
        self.GREY = (200,200,200)
        self.height = height/scaleh
        self.width = width/scalew
        self.scaleh = scaleh
        self.screen = screen
        self.notes = notes
        self.values = []
        self.location = location
        self.keys = []

    def place_keyboard(self):
        key_count = len(self.notes)
        self.keys = []
        count = 0
        self.screen.fill(self.GREY)
        noteobj = list(Note)+[Note.C]
        for val in range(0,int(self.width), 1+(int(self.width)//key_count)): # Need to add function to move certain keys up and down(black keys)
            self.values.append(val)
            self.keys.append(
                Key(
                    Color.WHITE if count in {0,2,4,5,7,9,11,12} else Color.BLACK,
                    noteobj[count],
                    val,
                    self.location,
                    (int(self.width)//key_count),
                    int(self.height) if count in {0,2,4,5,7,9,11,12} else (int(self.height - self.location)//2)+75)
            )
            count+=1
        for key in self.keys:
            pygame.draw.rect(self.screen, key.current_color, key)
        for val in range(0,int(self.width), 1+(int(self.width)//key_count)):
            pygame.draw.line(self.screen,Color.BLACK,(val,self.location),(val,int(self.height)))

        return self.values
    def change_color(self, plays):
        self.plays = plays
        for key in self.keys:
            print(key.note.value)
            if key.note.value in plays:
                key.press(True, True)
            else:
                key.press(True, False)