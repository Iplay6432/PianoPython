from backend import Note, Color
from key import Key
import json
import time
from concurrent.futures import ThreadPoolExecutor
import threading
import time
import pygame.mixer

class Falling(pygame.Rect):
    def __init__(self, note, screen, height, width, location, len, notes, songname):  # note is the index
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
        self.executor = ThreadPoolExecutor(max_workers=10)
        with open(f"jsons/{songname}.json") as f:
            self.song = json.load(f)
 
    def play_wav(self, wav_file, times):
        # Create a new thread that will play the sound
        thread = threading.Thread(target=self._play_wav, args=(wav_file, times))
        # Start the new thread
        thread.start()
    def _play_wav(self, wav_file, times):
        # Load audio file
        sound = pygame.mixer.Sound(wav_file)
        sound.set_volume(2.0)
        if times < 1000:
            sound.play()
            time.sleep(times/1000)
            sound.stop()
        else:
            sound.play()
        # Play audio file
        
    def place_key(self): 
        key_count = len(self.notes)
        self.keys = []
        vals = [0, 52, 104, 156, 208, 260, 312, 364, 416, 468, 520, 572, 624]
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
                    Note.Empty,
                    no,
                    -1*lens,
                    (int(self.width) // key_count),
                    int(lens),
                )
            )

        for key in self.keys:
            pygame.draw.rect(self.screen, key.current_color, key)
            pygame.draw.rect(self.screen, Color.BLUE, key, 1)
            key.played = False
        self.play_wav("notes/A3.wav", 2)
        self.start_time = time.time()
    def update(self):
        for i in range(len(self.keys)):  # iterate over the indices of the list
            key = self.keys[i]  # get the key at the current index
            timefrom = self.song[i][2]/1000
            if time.time() - self.start_time > timefrom:
                # update y-coordinate
                key.y += self.speed  # adjust this value to change the speed of falling

                # redraw key
                pygame.draw.rect(self.screen, key.current_color, key)
                pygame.draw.rect(self.screen, Color.BLUE, key, 1)
                
                if self.height /2 > key.y > self.height/2 - self.lengths[i]:
                    key.current_color = Color.RED
                    pygame.draw.rect(self.screen, Color.YELLOW, key, 1)
                    if not hasattr(key, 'played') or not key.played:
                        key.played = True
                        self.play_wav(f"notes/{self.song[i][0]}.wav", self.song[i][1])
        d = 0
        for key in self.keys:
            key = self.keys[i - d]
            if key.played:
                self.keys.remove(key)
                d +=1 
                
