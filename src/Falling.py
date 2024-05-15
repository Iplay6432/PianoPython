import pygame
from backend import Note, Color
from key import Key

class Falling(pygame.Rect):
    def __init__ (self, note, screen, height, width,location, len,notes): #note is the index
        # super.__init__(args)
        self.note = note
        self.screen = screen
        self.height = height
        self.width = width/1.2
        self.location = location
        self.len = len
        self.notes= notes

    def place_key(self):
        key_count = len(self.notes)
        self.keys = []
        count = 0
        key_height = int(self.height/2)
        for val in range(0,int(self.width/1.2), 1+(int(self.width/1.2)//key_count)): # Need to add function to move certain keys up and down(black keys) 
            self.keys.append(
                Key(
                    Color.WHITE if count in {0,2,4,5,7,9,11,12} else Color.BLACK,
                    Note.A,
                    val,
                    0,
                    ((int(self.width/1.2))//key_count),
                    (int(self.height - key_height) if count in {0,2,4,5,7,9,11,12} else (int(self.height - key_height)//2.5)+75) )
            )
            
            count+=1
        for key in self.keys:
            pygame.draw.rect(self.screen, key.current_color, key)

        # pygame.draw.rect(self.screen, Color.GREEN, pygame.Rect((self.note*((self.width/1.2)/13)*2),self.location,((self.width/1.2)/13)*2,self.len))