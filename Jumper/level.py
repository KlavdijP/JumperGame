import pygame
from player import Player
from functions import *
from platforms import Platform
from enemies import EnemyAir
from random import randint
from settings import *
from math import pow

class Level:
    def __init__(self, level_data, surface):
        self.player = pygame.sprite.GroupSingle()
        self.display_surface = surface
        self.platforms = pygame.sprite.Group()
        self.enemyAir = pygame.sprite.Group()
        self.score = 0

        self.setup_level()

    def setup_level(self):
        player_sprite = Player(250,250)
        self.player.add(player_sprite)

        #Platform creation
        for i in range(0, HEIGHT, 100):
            platform = Platform(randint(0, WIDTH-100), i)
            if i != 0:
                platform.generated = True
            self.platforms.add(platform)
            self.score += 1
        self.enemyAir.add(EnemyAir(WIDTH/2, 0))

    def horizontal_movement_collision(self):
        player = self.player.sprite
        pass
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
                if sprite.rect.colliderect([player.rect.x, player.rect.y+50, 64, 1]):
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
                if player.direction.y < 0:
                    sprite.speed = player.direction.y * -1 #pow(1.5, 10)

    def run(self, event_list):
        ##level platforms
        self.display_surface.blit(load_image('bck.png', 500,800), (0,0))

        #player
        self.player.update(event_list)
        # self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)

        #platforms
        self.platform_speed()
        #platform generator
        for sprite in self.platforms.sprites():
            if sprite.rect.y > 100 and sprite.generated == False:
                sprite.generated = True
                self.platforms.add(Platform(randint(0, WIDTH-100), 0))
                self.score += 1

        #platform update
        self.platforms.update()
        self.platforms.draw(self.display_surface)

        #enemy update
        self.enemyAir.update(self.player.sprite)
        self.enemyAir.draw(self.display_surface)