import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
from backend import SONGS, Note, Color


class PianoGame:
    def __init__(self) -> None:
        pygame.init()
        self.height, self.width = (600, 800)
        self.screen = pygame.display.set_mode(self.shape)
        self.clock = pygame.time.Clock()
        self.running = True

        self.time = 0
        self.dt = 0

        self.notes = Note

    @property
    def shape(self) -> tuple[int, int]:
        return (self.width, self.height)

    def loop(self):
        while self.running:
            for event in pygame.event.get():
                self.process_events(event)
            self.screen.fill(Color.BLACK)

            self.render_frame()

            pygame.display.flip()

            self.dt = self.clock.tick(60) / 1000
            self.time += self.dt

        pygame.quit()

    def process_events(self, event: pygame.event.Event):
        if event.type == pygame.QUIT:
            self.running = False

    def render_frame(self):
        self.key_count = 6
        self.keys = []
        print(self.width,self.height)
        for x in range(0,self.width, 1+(self.width//self.key_count)):
            self.keys.append(pygame.Rect(x,0,self.width//self.key_count,self.height))

        for key in self.keys:
            pygame.draw.rect(self.screen, Color.WHITE, key)
        


def main():
    piano = PianoGame()
    piano.loop()


if __name__ == "__main__":
    main()
