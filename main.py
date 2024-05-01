import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
from backend import SONGS


class PianoGame:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.clock = pygame.time.Clock()
        self.running = True

    def loop(self):
        while self.running:
            for event in pygame.event.get():
                self.process_events(event)
            self.render_frame()

    def process_events(self, event: pygame.event.Event):
        if event.type == pygame.QUIT:
            self.running = False

    def render_frame(self):
        pass


def main():
    PianoGame()


if __name__ == "__main__":
    main()
