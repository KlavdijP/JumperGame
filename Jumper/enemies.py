import pygame
from functions import *
from settings import *

class EnemyAir(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image = load_image('enemy-fly.png', 150, 100)
        self.rect = self.image.get_rect(topleft = (posx,posy))
        self.direction = pygame.math.Vector2(0,0)
        #player movement
        # self.speed = 8

    def update(self, event_list):
        pass