import pygame
from functions import *
from random import randint
from settings import *

glass_block = load_image('glass-block', 75,20)
segment_block = load_image('segment-block', 75,20)
cable_block = load_image('cable-block', 75,20)

class Platform(pygame.sprite.Sprite):
    def __init__(self, posx, posy, settings, difficulty, move=False):
        super().__init__()
        self.settings = settings
        self.image = pygame.Surface((50,50))
        self.difficulty = difficulty
        ### TYPES
        #   1- Normal
        #   2- Dissapears after jumped on
        #   3- Breaks after jumped on
        ###
        self.arr = [0,0,0] # [n, step1, step2]
        self.move = move
        self.gen_move = move
        self.type = self.giveType()
        if self.type == 1:
            self.image = cable_block
        elif self.type == 2:
            self.image = segment_block
        else:
            self.image = glass_block
        if posx == WIDTH/2:
            posx += 1
        self.rect = self.image.get_rect(topleft = (posx, posy))

        self.speed = 0
        self.move_speed = 20
        self.generated = False
        self.move_to = 0
        self.get_move_to()


    def get_move_to(self):
        getpos = self.rect.x+WIDTH/2 if self.rect.x < WIDTH/2 else self.rect.x-WIDTH/2
        if getpos > WIDTH-50:
            getpos -= 50
        self.move_to = getpos

        # print(self.rect.x, self.move_to)
    def returnType(self):
        return self.type

    def move_it(self):
        if self.gen_move:
            randMove = randint(0, self.arr[0])
            if randMove > self.arr[1] and randMove < self.arr[2]:
                self.move = True
                # print("self move = true")

    def giveType(self):
        movable = 100
        if self.difficulty == "intermediate":
            self.arr = [1000, 50, 800]
            movable = randint(0,5)

        elif self.difficulty == "very_hard":
            self.arr = [1000, 400, 900]
            movable = randint(0,10)

        elif self.difficulty == "hard":
            self.arr = [1000, 800, 950]
            movable = randint(0,20)

        elif self.difficulty == "medium":
            self.arr = [1000, 950, 1000]

        elif self.difficulty == "easy":
            self.arr = [1, 2, 0]

        if movable < 3:
            self.gen_move = True
            self.move = True

        randType = randint(0, self.arr[0])
        if randType < self.arr[1]:
            # print(randType)
            return 1
        elif randType >= self.arr[1] and randType < self.arr[2]:
            return 2
        else:
            # print(randType)
            return 3

    def update(self):
        self.rect.y += self.speed
        if self.move:
            if self.rect.x < self.move_to:
                self.rect.x += self.move_speed
                if self.rect.x > self.move_to:
                    self.get_move_to()
                    self.move = False
            else:
                self.rect.x -= self.move_speed
                if self.rect.x < self.move_to:
                    self.get_move_to()
                    self.move = False

        if self.rect.y >= HEIGHT+50:
            self.kill()