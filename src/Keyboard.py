import pygame
from backend import Color, Note, enums
from key import Key
import serial
import time
import threading
class Keyboard:
    def __init__(self, width, height, screen, notes, scalew, scaleh):
        self.RASPBERRY = (227,27,93)
        self.GREY = (200,200,200)
        self.height = height/scaleh
        self.width = width/scalew
        self.screen = screen
        self.notes = notes
        self.values = []
        self.set = serial.Serial("COM4", 9600)

    def place_keyboard(self):
        key_count = len(self.notes)
        self.keys = []
        count = 0
        self.screen.fill(self.GREY)
        noteobj = [Note.C, Note.Db, Note.D, Note.Eb, Note.E, Note.F, Note.Gb, Note.G, Note.Ab, Note.A, Note.Bb, Note.B, Note.C]
        for val in range(0,int(self.width), 1+(int(self.width)//key_count)): # Need to add function to move certain keys up and down(black keys)
            self.values.append(val)
            self.keys.append(
                Key(
                    Color.WHITE if count in {0,2,4,5,7,9,11,12} else Color.BLACK,
                    noteobj[count],
                    val,
                    0,
                    (int(self.width)//key_count),
                    int(self.height) if count in {0,2,4,5,7,9,11,12} else (int(self.height)//2)+75)
            )
            # threading.Thread(target= self.play_note, args=(key)).start()
            count+=1

        for key in self.keys:
            pygame.draw.rect(self.screen, key.current_color, key)
        for val in range(0,int(self.width), 1+(int(self.width)//key_count)):
            pygame.draw.line(self.screen,Color.BLACK,(val,0),(val,int(self.height)))

        return self.values
    # def _play_wav(self, wav_file, times):
    #     # Load audio file
    #     sound = pygame.mixer.Sound(wav_file)
    #     sound.set_volume(2.0)
    #     if times < 1000:
    #         sound.play()
    #         time.sleep(times/1000)
    #         sound.fadeout(100)
    #     else:
    #         sound.play()
    #     # Play audio file
    # def play_note(self, key):
    #     first = False
    #     while key.active:
    #         if first == False:
    #             sound.set_volume(2.0)
    #             sound = pygame.mixer.Sound(key.note + "4.wav")
    #     sound.stop



    # def get_played(self):
    #     x = 0
    #     bs = []
    #     ds = []
    #     for key in self.keys:
    #         while x < 14:
    #             bs.append(self.set.readline())
    #         if (key.note+"1") in bs and key.active == False:
    #             ds.append(key.note)
    #             key.press(True, True)
    #         elif (key.note+"0") in bs and key.active == True:
    #             key.press(True, False)
    #         else:
    #             key.press(False, False)
    #     return ds