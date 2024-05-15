import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
from backend import Note, Color #,SONGS
import serial
from key import Key
from Falling import Falling

RASPBERRY = (227,27,93)
GREY = (200,200,200)

class PianoGame:
    def __init__(self) -> None:
        pygame.init()
        self.gamestate = 1
        #Gamestate vals:
            #   0 = Main screen
            #   1 = Autoplay keyboard
            #   2 = Freeplay keyboard

        self.height, self.width = (480.0, 800.0)
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
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
        if self.gamestate==2: #FREEPLAY
            key_count = len(self.notes)
            self.keys = []
            count = 0
            self.screen.fill(GREY)
            for val in range(0,self.width, 1+(self.width//key_count)): # Need to add function to move certain keys up and down(black keys) 
                self.keys.append(
                    Key(
                        Color.WHITE if count in {0,2,4,5,7,9,11,12} else Color.BLACK,
                        Note.A,
                        val,
                        0,
                        (self.width//key_count),
                        self.height if count in {0,2,4,5,7,9,11,12} else (self.height//2)+75)
                )
                
                count+=1
            
            for key in self.keys:
                pygame.draw.rect(self.screen, key.current_color, key)
            for val in range(0,self.width, 1+(self.width//key_count)):
                pygame.draw.line(self.screen,Color.BLACK,(val,0),(val,self.height))
        elif self.gamestate == 1:
            self.Learning()
        elif self.gamestate == 0: #MAIN START SCREEN
            self.screen.fill(RASPBERRY)

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

            fp = font.render(" FreePlay ",True,Color.BLACK)
            text_rect_7 = fur.get_rect(bottom=self.height-15,right=self.width-15)
            pygame.draw.rect(self.screen,Color.WHITE,text_rect_7)
            self.screen.blit(fp,text_rect_7)

            img = pygame.image.load("piano.png")
            size =200
            img = pygame.transform.scale(img, (size,size))
            self.screen.blit(img,((self.width//2)-(size//2),(self.height//2)))
    def Learning(self):
        key_count = len(self.notes)
        self.keys = []
        count = 0
        self.screen.fill(GREY)
        key_height = int(self.height/2)
        
        for val in range(0,int(self.width/1.2), 1+(int(self.width/1.2)//key_count)): # Need to add function to move certain keys up and down(black keys) 
            self.keys.append(
                Key(
                    Color.WHITE if count in {0,2,4,5,7,9,11,12} else Color.BLACK,
                    Note.A,
                    val,
                    self.height - key_height,
                    ((int(self.width/1.2))//key_count),
                    (int(self.height - key_height) if count in {0,2,4,5,7,9,11,12} else (int(self.height - key_height)//2.5)+75) )
            )
            
            count+=1
        for key in self.keys:
            pygame.draw.rect(self.screen, key.current_color, key)
        for val in range(0,int(self.width/1.2), 1+(int(int(self.width/1.2)/key_count))):
            pygame.draw.line(self.screen,Color.BLACK,(val,self.height - key_height),(val,int(self.height)))
        Falling(1,self.screen,self.height,self.width, 0,100, self.notes).place_key()














def main():
    piano = PianoGame()
    piano.loop()


if __name__ == "__main__":
    main()
