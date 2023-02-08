import pygame
from functions import *
from settings import *
from math import sqrt, dist, atan2, sin, cos, pi
from random import randint

fanimages = [
    load_image('./Fan/fan01', 100, 100),
    load_image('./Fan/fan02', 100, 100),
    load_image('./Fan/fan03', 100, 100),
    load_image('./Fan/fan04', 100, 100),
    load_image('./Fan/fan05', 100, 100)
]

airimages = [
    load_image('./EnemyAir/enemy01', 100, 100),
    load_image('./EnemyAir/enemy02', 100, 100),
    load_image('./EnemyAir/enemy03', 100, 100),
    load_image('./EnemyAir/enemy04', 100, 100)
]

bouncerimages = [
    load_image('./Bouncer/bouncer01', 100, 100),
]


class EnemyAir(pygame.sprite.Sprite):
    def __init__(self, posx, posy, settings):
        super().__init__()
        self.settings = settings
        self.image = pygame.Surface((50, 50))
        self.counter = 0
        self.image = airimages[self.counter]
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
        
    def animate(self):
        if self.counter > len(airimages)-1:
            self.counter = 0
        self.image = airimages[int(self.counter)]
        self.counter += 0.1
    
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

        self.animate()

    def die(self):
        self.settings.enemy_air_die()

class PCFan(pygame.sprite.Sprite):
    def __init__(self, posx, posy, settings):
        super().__init__()
        self.settings = settings
        self.counter = 0
        self.image = pygame.Surface((50, 50))
        self.image = fanimages[self.counter]
        self.rect = self.image.get_rect(topleft = (posx,posy-200)) ##Enemy spawns 200pixels before reaching top
        self.speed = 4
        
        #Audio
        self.settings.enemy_fan()

    def move(self):
        self.rect.y += self.speed
        # print(self.rect)

    def animate(self):
        if self.counter > len(fanimages)-1:
            self.counter = 0
        self.image = fanimages[self.counter]
        self.counter += 1

    def update(self):
        self.move()

        if self.rect.y > HEIGHT+10:
            self.settings.enemy_fan_stop()
            self.kill()
        
        #Animation
        self.animate()

class Bouncer(pygame.sprite.Sprite):
    def __init__(self, posx, posy, settings):
        super().__init__()
        self.settings = settings
        self.image = pygame.Surface((50, 50))
        self.counter = 0
        self.image = bouncerimages[self.counter]
        self.rect = self.image.get_rect(topleft = (posx,posy-200)) ##Enemy spawns 200pixels before reaching top
        self.direction = pygame.math.Vector2(0,1)
        self.rest_direction = self.get_direction()

        self.speed = 4
    def get_direction(self):
        rand = randint(0, 1)
        if rand == 0:
            return -1
        else:
            return 1
        
    def animate(self):
        if self.counter > len(bouncerimages)-1:
            self.counter = 0
        self.image = bouncerimages[int(self.counter)]
        self.counter += 0.1
    
    def move(self):
        self.rect.x += self.speed * self.rest_direction
        self.rect.y += self.direction.y * self.speed
        if self.rect.x < 0:
            self.rest_direction = 1
        elif self.rect.x > WIDTH:
            self.rest_direction = -1


    def update(self):
        self.move()
        if self.rect.y > HEIGHT+10:
            self.kill()
        self.animate()