import pygame
from functions import *
from random import randint
from settings import *

class Platform(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        super().__init__()
        self.image = pygame.Surface((50,50))

        ### TYPES
        #   1- Normal
        #   2- Dissapears after jumped on
        #   3- Breaks after jumped on
        ###
        self.type = self.giveType()
        if self.type == 1:
            self.image = load_image('normal-block.png', 75,20)
        elif self.type == 2:
            self.image = load_image('cloud-block.png', 75,20)
        else:
            self.image = load_image('break-block.png', 75,20)
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