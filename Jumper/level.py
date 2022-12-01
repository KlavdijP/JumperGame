import pygame
from player import Player
from functions import *
from platforms import Platform
from random import randint
from settings import *

class Level:
    def __init__(self, level_data, surface):
        self.player = pygame.sprite.GroupSingle()
        self.display_surface = surface
        self.platforms = pygame.sprite.Group()

        self.setup_level()

    def setup_level(self):
        player_sprite = Player(250,250)
        self.player.add(player_sprite)

        #Platform creation
        self.platforms.add(Platform(randint(0, WIDTH), 0))

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        # for sprite in self.

    def run(self, event_list):
        ##level platforms
        self.display_surface.blit(load_image('bck.png', 500,800), (0,0))

        #player
        self.player.update(event_list)
        self.horizontal_movement_collision()
        self.player.draw(self.display_surface)

        #platforms
        #platform generator
        if self.platforms.sprites()[-1].rect.y == 100:
            self.platforms.add(Platform(randint(0, WIDTH), 0))

        ##TODO check if there can be error in [0]
        elif self.platforms.sprites()[0].rect.y >= HEIGHT/2:
            self.platforms.sprites()[0].kill()
        #platform update
        self.platforms.update(0)
        self.platforms.draw(self.display_surface)