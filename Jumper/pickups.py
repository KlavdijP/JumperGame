import pygame
from functions import *
from random import randint
from settings import *

class Pickups(pygame.sprite.Sprite):
    def __init__(self, posx, posy, type):
        super().__init__()
        self.image = pygame.Surface((75,75))
        if type == "shield":
            self.image = load_image('binary-shield', 75, 75)
        self.rect = self.image.get_rect(topleft = (posx, posy))
        self.speed = 0
    
    def update(self):
        self.rect.y += self.speed

        if self.rect.y >= HEIGHT+50:
            self.kill()