import pygame
from functions import *

class Platform(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.image = load_image('./assets/normal-block.png', 100,20)
        self.rect = self.image.get_rect(topleft = (posx, posy))

        self.speed = 2
    
    def update(self, height):
        self.rect.y += self.speed