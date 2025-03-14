import os
import sys
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
from backend import Note, Color #,SONGS
from backend.NotesByKeyStrokes import NotesByKeyStrokes
from backend.Button import Button
from key import Key
from Falling import Falling
from communication import read_arduino
import queue
import threading
import platform
from Keyboard import Keyboard

RASPBERRY = (227,27,93)
GREY = (200,200,200)

class PianoGame:
    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()
        self.gamestate = 0
        #Gamestate vals:
            #   0 = Main screen
            #   1 = Autoplay keyboard
            #   2 = Freeplay keyboard

        self.height, self.width = (480, 800)
        self.vals = []
        if platform.machine() == "aarch64":
            self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.running = True

        self.time = 0
        self.dt = 0
        self.plays =[]
        self.notes = Note
        self.ranonce = False
        self.queue = queue.Queue()
        self.playing: dict[Note, threading.Thread] = {}

    @property
    def shape(self) -> tuple[int, int]:
        return (self.width, self.height)

    def loop(self):
        if "--pi" in sys.argv:
            left_arduino_process = threading.Thread(target=read_arduino, args=(self.queue, True))
            left_arduino_process.start()
            # right_arduino_process = threading.Thread(target=read_arduino, args=(self.queue, False))
            # right_arduino_process.start()

        while self.running:
            for event in pygame.event.get():
                self.process_events(event)
            # self.screen.fill(Color.BLACK)

            if "--pi" in sys.argv:
                self.process_arduino_events()
            else:
                self.process_keyboard_events()

            self.render_frame()

            pygame.display.flip()

            self.dt = self.clock.tick(60) / 1000
            self.time += self.dt

        pygame.quit()
    def process_keyboard_events(self) -> None:
        k = NotesByKeyStrokes()
        on = k.playing()
        i=0
        notes = tuple(Note)
        for keyOn,note in zip(on,notes):
            if keyOn == 1:
                self.play_note(note)
            else:
                self.stop_note(note)
            i+=1
    def process_events(self, event: pygame.event.Event):
        if event.type == pygame.QUIT:
            self.running = False

    def process_arduino_events(self) -> None:
        for _ in range(2):
            self.process_keypress()

    def process_keypress(self) -> None:
        try:
            keypress_dict: dict[bool, str] = self.queue.get_nowait()
        except queue.Empty:
            return

        if True in keypress_dict:  # right side of keyboard
            keypress = keypress_dict[True]
            notes = tuple(Note)[6:-1]
        else:  # left side of keyboard
            keypress = keypress_dict[False]
            notes = tuple(Note)[:6]

        for key, note in zip(keypress, notes):
            if key == "1":
                self.play_note(note)
            else:
                self.stop_note(note)

    def play_note(self, note: Note):
        # Create a new thread that will play the sound
        thread = threading.Thread(target=self._play_note, args=(note,))
        # Start the new thread
        thread.start()

        self.playing[note] = thread

        # Play audio file
    def _play_note(self, note: Note) -> None:
        if note.value not in self.plays:
            sound = pygame.mixer.Sound(f"notes/{note.value}5.wav")
            while note.value not in self.plays:
                self.plays.append(note.value)
            sound.play()

    def stop_note(self, note: Note):
        playing = self.playing.get(note)
        if playing is not None and note.value in self.plays:
            playing.join(timeout=.2)
            self.plays.remove(note.value)

    def render_frame(self):
        if self.gamestate==2: #FREEPLAY
            keyboard= Keyboard(self.width, self.height, self.screen, self.notes, 1, 1, 0)
            keyboard.place_keyboard(self.plays)

        elif self.gamestate == 1:
            self.Learning()
        elif self.gamestate == 0: #MAIN START SCREEN
            self.screen.fill(RASPBERRY)
            # Initialize font
            font_large = pygame.font.Font('freesansbold.ttf', 60)
            font_small = pygame.font.Font('freesansbold.ttf', 25)

            # Render "Raspberry Pi-ano" text
            title_screen = font_large.render("Raspberry Pi-ano", True, Color.WHITE)
            text_rect_1 = title_screen.get_rect(center=(int(self.width / 2), 200))
            self.screen.blit(title_screen, text_rect_1)

            # Create buttons
            buttons = [
                Button("Twinkle", font_small, Color.BLACK, int(self.width / 2) - 75, 100, 150, 50, "under"),
                Button("Vivaldi", font_small, Color.BLACK, int(self.width / 2) + 75, 100, 150, 50, "give"),
                Button("Fur elise", font_small, Color.BLACK, int(self.width / 2) + 225, 100, 150, 50, "doom"),
                Button("Birthday", font_small, Color.BLACK, int(self.width / 2) - 225, 100, 150, 50,"Lamb"),
                Button("Ode Joy", font_small, Color.BLACK, int(self.width / 2) - 375, 100, 150, 50, "rushe"),
                Button("FreePlay", font_small, Color.BLACK, self.width - 165, self.height - 65, 150, 50, None)
            ]

            # Draw buttons
            for button in buttons:
                button.draw(self.screen)

            # Handle button clicks
            for event in pygame.event.get():
                for button in buttons:
                    if button.is_clicked(event):
                        # print(f"{button.text} button clicked")
                        if button.midi != None:
                            self.gamestate = 1
                            self.Learning(str(button.midi))
                        else:
                            self.gamestate = 2
            img = pygame.image.load("piano.png")
            size = 200
            img = pygame.transform.scale(img, (size, size))
            self.screen.blit(img,((self.width//2)-(size//2),(self.height//2)))
    def Learning(self, song = "give"):
        key_count = len(self.notes)
        self.keys = []
        valss = []
        count = 0
        self.screen.fill(GREY)
        key_height = int(self.height/2)

        keyboard= Keyboard(self.width, self.height, self.screen, self.notes, 1.2, 1, self.height - key_height)
        keyboard.place_keyboard(self.plays)

        for val in range(0,int(self.width/1.2), 1+(int(self.width/1.2)//key_count)):
            valss.append(val)
            count += 1
        if not self.ranonce:
            for idx, arg in enumerate(sys.argv):
                if "--song" in arg:
                    if "=" not in arg:
                        song = sys.argv[idx+1]
                    else:
                        song = arg.removeprefix("--song=")
            self.falling = Falling(1,self.clock, self.screen,self.height,self.width, 0,100, self.notes, song, valss, self.plays)
            self.falling.place_key()
            self.ranonce = True
        else:
            keyboard.place_keyboard(self.plays)
            self.falling.update(self.clock)
            self.falling.update_text()


        count = 0


def main():
    try:
        piano = PianoGame()
        piano.loop()
    except KeyboardInterrupt:
        os._exit(0)


if __name__ == "__main__":
    main()
