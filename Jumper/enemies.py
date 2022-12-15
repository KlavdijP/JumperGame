import pygame
from functions import *
from settings import *
from math import sqrt

class EnemyAir(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image = load_image('enemy-fly.png', 150, 100)
        self.rect = self.image.get_rect(topleft = (posx,posy))
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 1

    def distance(self, player):
        return sqrt(pow(self.rect.x - player.rect.x,2) + pow(self.rect.y - player.rect.y,2))

    def update(self, player):
        print(self.distance(player))
        self.rect.y = self.direction.y