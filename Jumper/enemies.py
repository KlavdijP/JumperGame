import pygame
from functions import *
from settings import *
from math import sqrt, dist, atan2, sin, cos, pi
from random import randint


class EnemyAir(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image = load_image('enemy-fly.png', 150, 100)
        self.rect = self.image.get_rect(topleft = (posx,posy-200)) ##Enemy spawns 200pixels before reaching top
        self.direction = pygame.math.Vector2(0,0)
        self.rest_direction = self.get_direction()

        self.speed = 4
        
        self.detect = False
        self.returnBack = False
        self.returnPos = [0, 0]
        self.playerPos = [0, 0]

    def get_direction(self):
        rand = randint(0, 1)
        if rand == 0:
            return -1
        else:
            return 1
        
    def pointTo(self, destination):
        v = pygame.math.Vector2(destination[0] - self.rect.x, destination[1] - self.rect.y)
        length = v.length()
        if length != 0:
            v /= length
            self.direction.x, self.direction.y = v
        else:
            self.direction.x, self.direction.y = [0, 0]

        # print(self.direction.x, self.direction.y)

    def move_left_right(self):
        self.rect.x += self.speed * self.rest_direction
        if self.rect.x < 0:
            self.rest_direction = 1
        elif self.rect.x > WIDTH:
            self.rest_direction = -1

    def move(self):
        # angle = atan2(self.direction.x, self.direction.y)
        # x = cos(angle)
        # y = sin(angle)
        # print(angle*180/pi, x, y)
        if self.detect == False and self.returnBack == False:
            self.rect.y += self.speed
            self.move_left_right()
        else:
            self.rect.x += self.direction.x * self.speed
            self.rect.y += self.direction.y * self.speed

        # print(self.rect)

    def update(self, player):        
        if self.detect == False and self.returnBack == False: ##Go to player position
            if player.top_reached:
                self.playerPos = [player.rect.x, player.rect.y]
                self.returnPos = [self.rect.x, self.rect.y]
                self.pointTo(self.playerPos)
                self.detect = True
        # if self.detect == False and self.returnBack == True: ##From player to previous
        #     self.pointTo(self.returnPos)
        if self.detect == True and self.returnBack == False: ##From start to player
            self.pointTo(self.playerPos)
            # print(dist((self.rect.x, self.rect.y), self.playerPos))
            if dist((self.rect.x, self.rect.y), self.playerPos) <= self.speed:
            # if self.direction.x == 0 and self.direction.y == 0:
                self.returnBack = True
                self.detect = False
        if self.detect == False and self.returnBack == True:
            self.pointTo(self.returnPos)
            # print(dist((self.rect.x, self.rect.y), self.returnPos))
            if dist((self.rect.x, self.rect.y), self.returnPos) <= self.speed:
            # if self.direction.x == 0 and self.direction.y == 0:
                self.returnBack = False
                self.detect = False
        self.move()

        if self.rect.y > HEIGHT+10:
            self.kill()