import pygame
from player import Player
from functions import *
from platforms import Platform
from random import randint
from settings import *
from math import pow

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
        self.platforms.add(Platform(randint(0, WIDTH-100), 0))

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed                

        # for sprite in self.platforms.sprites():
        #     if sprite.rect.colliderect(player.rect):
        #         if player.direction.x < 0: #moving left and colliding left
        #             player.rect.left = sprite.rect.right
        #         elif player.direction.x > 0: #moving right and colliding right
        #             player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        if player.direction.y >= 0:
            for sprite in self.platforms.sprites():
                if sprite.rect.colliderect(player.rect):
                    if sprite.type == 3:
                        sprite.kill()
                    elif sprite.type == 2:
                        player.jump()
                        sprite.kill()
                    else:
                        player.jump()

    def platform_speed(self):
        player = self.player.sprite
        if player.rect.y > HEIGHT/2:
            for sprite in self.platforms.sprites():
                sprite.speed = 0
        else:
            for sprite in self.platforms.sprites():
                sprite.speed = pow(1.2, 10)

    def run(self, event_list):
        ##level platforms
        self.display_surface.blit(load_image('bck.png', 500,800), (0,0))

        #player
        self.player.update(event_list)
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)

        #platforms
        self.platform_speed()
        #platform generator
        for sprite in self.platforms.sprites():
            if sprite.rect.y > 100 and sprite.rect.y <= 100+sprite.speed:
                self.platforms.add(Platform(randint(0, WIDTH-100), 0))

        #platform update
        self.platforms.update(0)
        self.platforms.draw(self.display_surface)