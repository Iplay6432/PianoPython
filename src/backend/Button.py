import pygame
from backend import Color


class Button:
    def __init__(self, text, font, color, x, y, width, height, midi):
        self.text = text
        self.font = font
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.text_surface = self.font.render(self.text, True, self.color)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)
        self.midi = midi

    def draw(self, screen):
        pygame.draw.rect(screen, Color.WHITE, self.rect)
        screen.blit(self.text_surface, self.text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False