import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
from backend import SONGS, Note, Color


class PianoGame:
    def __init__(self) -> None:
        pygame.init()
        self.height, self.width = (800, 600)
        self.screen = pygame.display.set_mode(self.shape)
        self.clock = pygame.time.Clock()
        self.running = True

        self.time = 0
        self.dt = 0

        self.notes = Note

    @property
    def shape(self) -> tuple[int, int]:
        return (self.height, self.width)

    def loop(self):
        while self.running:
            for event in pygame.event.get():
                self.process_events(event)
            self.screen.fill(Color.BLACK.value)

            self.render_frame()

            pygame.display.flip()

            self.dt = self.clock.tick(60) / 1000
            self.time += self.dt

        pygame.quit()

    def process_events(self, event: pygame.event.Event):
        if event.type == pygame.QUIT:
            self.running = False

    def render_frame(self):
        height = 70
        width = self.width // len(self.notes)
        x = 0
        buff = 0
        for note in self.notes:
            pygame.draw.rect(self.screen, Color.BLUE, pygame.Rect(x, height, x+width, height))
            x += width + buff


def main():
    piano = PianoGame()
    piano.loop()


if __name__ == "__main__":
    main()
