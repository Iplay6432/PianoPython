import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
from backend import Note, Color #,SONGS
import serial


class PianoGame:
    def __init__(self) -> None:
        pygame.init()
        self.gamestate = 0 
        #Gamestate vals:
            #   0 = Main screen
            #   1 = Autoplay keyboard
            #   2 = Freeplay keyboard

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
        if self.gamestate==2:
            key_count = len(self.notes)
            self.keys = []
            for x in range(0,self.width, 1+(self.width//key_count)): # Need to add function to move certain keys up and down(black keys) 
                self.keys.append(
                    pygame.Rect(x, 0, self.width//key_count, self.height)  # Can we make them shorter?
                )

            for key in self.keys:
                pygame.draw.rect(self.screen, Color.WHITE, key) # Need to add function to change color of certain keys(black keys)
        elif self.gamestate == 0:
            self.screen.fill(Color.BLACK)

            #Render "Raspberry Pi-ano" text
            font = pygame.font.Font('freesansbold.ttf', 60)
            title_screen = font.render("Raspberry Pi-ano",True,Color.WHITE)
            text_rect_1 = title_screen.get_rect(center=(int(self.width/2), 200))
            self.screen.blit(title_screen,text_rect_1)


            #Buttons
            font = pygame.font.Font('freesansbold.ttf', 25)

            twinkle = font.render(" Twinkle ",True,Color.BLACK)
            text_rect_2 = twinkle.get_rect(center=(int(self.width/2), 100))
            pygame.draw.rect(self.screen,Color.WHITE,text_rect_2)
            self.screen.blit(twinkle,text_rect_2)
            
            vivaldi = font.render(" Vivaldi ",True,Color.BLACK)
            text_rect_3 = vivaldi.get_rect(center=(int(self.width/2)+150, 100))
            pygame.draw.rect(self.screen,Color.WHITE,text_rect_3)
            self.screen.blit(vivaldi,text_rect_3)

            fur = font.render(" Fur elise ",True,Color.BLACK)
            text_rect_4 = fur.get_rect(center=(int(self.width/2)+300, 100))
            pygame.draw.rect(self.screen,Color.WHITE,text_rect_4)
            self.screen.blit(fur,text_rect_4)

            birthday = font.render(" Birthday ",True,Color.BLACK)
            text_rect_5 = fur.get_rect(center=(int(self.width/2)-150, 100))
            pygame.draw.rect(self.screen,Color.WHITE,text_rect_5)
            self.screen.blit(birthday,text_rect_5)

            ode = font.render(" Ode Joy ",True,Color.BLACK)
            text_rect_6 = fur.get_rect(center=(int(self.width/2)-300, 100))
            pygame.draw.rect(self.screen,Color.WHITE,text_rect_6)
            self.screen.blit(ode,text_rect_6)











def main():
    piano = PianoGame()
    piano.loop()


if __name__ == "__main__":
    main()
