import pygame
from settings import *

class Button(pygame.sprite.Sprite):
    def __init__(self, pos, surface, type, displayed="", metrics = (300,80), fontsize=30):
        super().__init__()
        if displayed == "":
            self.displayed = type
        else:
            self.displayed = displayed
        self.metrics = metrics
        self.type = type
        self.surface = surface
        self.image = pygame.Surface(self.metrics)
        self.image.fill('red')
        self.rect = self.image.get_rect(center = pos)

        self.font = pygame.font.Font("./fonts/rexlia_rg.otf", fontsize)
        self.text = self.font.render(str(self.displayed), False, "#53f53f")
        self.text_rect = self.text.get_rect(center = self.rect.center)

    def draw(self):
        self.surface.blit(self.image, self.rect)
        self.surface.blit(self.text, self.text_rect)

    # def type(self):
    #     return self.type