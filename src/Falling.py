import pygame
from backend import Note, Color
from key import Key
import json
from pysine import sine
import time
from gensound import Sine
from mido import MidiFile
from concurrent.futures import ThreadPoolExecutor
import soundfile as sf
import sounddevice as sd
import time
class Falling(pygame.Rect):
    def __init__(self, note, screen, height, width, location, len, notes):  # note is the index
        # super.__init__(args)
        self.note = note
        self.screen = screen
        self.height = height
        self.width = width / 1.2
        self.location = location
        self.len = len
        self.notes = notes
        self.speed = 1
        self.start_time = 0
        self.lengths =  []
        self.executor = ThreadPoolExecutor(max_workers=5)
        with open("jsons/Lamb.json") as f:
            self.song = json.load(f)
 

    def play_wav(self, wav_file, duration):
        # Read file
        data, fs = sf.read(wav_file, dtype='float32')  

        # Start playback
        sd.play(data, fs)

        # Sleep for duration
        time.sleep(duration)

        # Stop playback
        sd.stop()
    def place_key(self): 
        key_count = len(self.notes)
        self.keys = []
        vals = [0, 56, 112, 168, 224, 280, 336, 392, 448, 504, 560, 616]
        note_names = list(Note.__members__.keys())
    
        for note in self.song:
            duration_seconds = note[1] / 1000.0
            lens = duration_seconds * (self.speed * 60)
        
            self.lengths.append(lens)
            no = ''.join([i for i in note[0] if not i.isdigit()])
         
            no = note_names.index(no)
            no = vals[no]

            self.keys.append(
                Key(
                    Color.GREEN,
                    Note.A,
                    no,
                    -1*lens,
                    (int(self.width) // key_count),
                    int(lens),
                )
            )

        for key in self.keys:
            pygame.draw.rect(self.screen, key.current_color, key)
        self.play_wav("notes/A3.wav", 1)
        self.start_time = time.time()
    def update(self):
        i = 0
        for key in self.keys.copy():  # iterate over a copy of the list
            timefrom = self.song[i][2]/1000
            if time.time() - self.start_time > timefrom:
                # update y-coordinate
                key.y += self.speed  # adjust this value to change the speed of falling

                # redraw key
                pygame.draw.rect(self.screen, key.current_color, key)

                # remove key if it's off the screen
                if key.y > self.height / 2:
                    self.keys.remove(key)
                elif self.height /2 > key.y > self.height/2 - self.lengths[i]:
                    print("About to crash")
                    key.current_color = Color.RED
                    if not hasattr(key, 'sine_called') or not key.sine_called:
                        key.sine_called = True
                        self.executor.submit(self.play_wav, f"notes/{self.song[i][0]}.wav", self.song[i][1]/1000)
                        print("Playing sound")
                    
                
                        
            i +=1

        # pygame.draw.rect(self.screen, Color.GREEN, pygame.Rect((self.note*((self.width/1.2)/13)*2),self.location,((self.width/1.2)/13)*2,self.len))