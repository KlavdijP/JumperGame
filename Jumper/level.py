import pygame
from player import Player
from functions import *

class Level:
    def __init__(self, level_data, surface):
        self.player = pygame.sprite.GroupSingle()
        self.display_surface = surface

        self.setup_level()

    def setup_level(self):
        # self.display_surface.blit(load_image('./assets/bck.png', 500,800), (0,0))
        # self.display_surface.fill((0,0,0))
        player_sprite = Player(250,250)
        self.player.add(player_sprite)

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed


    def run(self):
        ##level platforms
        self.display_surface.blit(load_image('./assets/bck.png', 500,800), (0,0))
        #player
        self.player.update()
        self.horizontal_movement_collision()
        self.player.draw(self.display_surface)