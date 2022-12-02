import pygame
from functions import *
from random import randint
from settings import *

class Platform(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.rect = self.image.get_rect(topleft = (posx, posy))

        ### TYPES
        #   1- Normal
        #   2- Dissapears after jumped on
        #   3- Breaks after jumped on
        ###
        self.type = self.returnType()
        if self.type == 1:
            self.image = load_image('normal-block.png', 100,20)
        elif self.type == 2:
            self.image = load_image('cloud-block.png', 100,20)
        else:
            self.image = load_image('break-block.png', 100,20)
        
        self.speed = 4
    
    def returnType(self):
        n = 1000
        randType = randint(0, 1000)
        if randType < 750:
            return 1
        elif randType >= 750 and randType < 900:
            return 2
        else:
            return 3

    def update(self, height):
        self.rect.y += self.speed

        if self.rect.y >= HEIGHT+50:
            self.kill()