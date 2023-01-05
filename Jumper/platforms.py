import pygame
from functions import *
from random import randint
from settings import *

glass_block = load_image('glass-block', 75,20)
segment_block = load_image('segment-block', 75,20)
cable_block = load_image('cable-block', 75,20)

class Platform(pygame.sprite.Sprite):
    def __init__(self, posx, posy, settings):
        super().__init__()
        self.settings = settings
        self.image = pygame.Surface((50,50))

        ### TYPES
        #   1- Normal
        #   2- Dissapears after jumped on
        #   3- Breaks after jumped on
        ###
        self.type = self.giveType()
        if self.type == 1:
            self.image = cable_block
        elif self.type == 2:
            self.image = segment_block
        else:
            self.image = glass_block
        self.rect = self.image.get_rect(topleft = (posx, posy))

        self.speed = 0
        self.generated = False
    
    def returnType(self):
        return self.type
        
    def giveType(self):
        n = 1000
        randType = randint(0, 1000)
        if randType < 750:
            return 1
        elif randType >= 750 and randType < 900:
            return 2
        else:
            return 3

    def update(self):
        self.rect.y += self.speed

        if self.rect.y >= HEIGHT+50:
            self.kill()