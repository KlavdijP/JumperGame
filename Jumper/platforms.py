import pygame
from functions import *
from random import randint
from settings import *

glass_block = load_image('glass-block', 75,20)
segment_block = load_image('segment-block', 75,20)
cable_block = load_image('cable-block', 75,20)

class Platform(pygame.sprite.Sprite):
    def __init__(self, posx, posy, settings, difficulty):
        super().__init__()
        self.settings = settings
        self.image = pygame.Surface((50,50))
        self.difficulty = difficulty
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
        arr = [] # [n, step1, step2]
        if self.difficulty == "intermediate":
            arr = [1000, 50, 800]

        elif self.difficulty == "very_hard":
            arr = [1000, 400, 900]

        elif self.difficulty == "hard":
            arr = [1000, 800, 950]

        elif self.difficulty == "medium":
            arr = [1000, 950, 1000]

        elif self.difficulty == "easy":
            arr = [1, 2, 0]
        
        randType = randint(0, arr[0])
        if randType < arr[1]:
            print(randType)
            return 1
        elif randType >= arr[1] and randType < arr[2]:
            return 2
        else:
            print(randType)
            return 3

    def update(self):
        self.rect.y += self.speed

        if self.rect.y >= HEIGHT+50:
            self.kill()