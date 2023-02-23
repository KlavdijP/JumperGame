import pygame
from settings import *
from functions import *

class Button(pygame.sprite.Sprite):
    def __init__(self, pos, surface, type, displayed="", metrics = (300,80), fontsize=30, image = ""):
        super().__init__()
        if displayed == "":
            self.displayed = type
        else:
            self.displayed = displayed
        self.metrics = metrics
        self.type = type
        self.surface = surface
        self.pos = pos
        if image != "":
            self.image = load_image(image,self.metrics[0], self.metrics[1])
        else:
            self.image = pygame.Surface(self.metrics)
            self.image.fill('red')
        self.rect = self.image.get_rect(center = pos)

    def draw(self):
        self.surface.blit(self.image, self.rect)