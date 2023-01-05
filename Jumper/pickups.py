import pygame
from functions import *
from random import randint
from settings import *

class Pickups(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        super().__init__()
        self.image = pygame.Surface((75,75))
        self.image = load_image('binary-shield', 75, 75)
        self.rect = self.image.get_rect(topleft = (posx, posy))
        self.speed = 0
    
    def update(self):
        self.rect.y += self.speed

        if self.rect.y >= HEIGHT+50:
            self.kill()