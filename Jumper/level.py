import pygame
from player import Player, Bullet
from functions import *
from platforms import Platform
from enemies import EnemyAir
from random import randint
from settings import *
from math import pow

class Level:
    def __init__(self, level_data, surface, update_score):
        self.player = pygame.sprite.GroupSingle()
        self.display_surface = surface
        self.platforms = pygame.sprite.Group()
        self.enemyAir = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        #Audio
        self.enemy_dies = pygame.mixer.Sound("./audio/enemy_dies.wav")

        #UI
        self.update_score = update_score

        #Platform
        self.last_type = 4 ##Last generated platform type

        self.setup_level()

    def setup_level(self):
        player_sprite = Player(250,250)
        self.player.add(player_sprite)

        #Platform creation
        for i in range(0, HEIGHT, 100):
            platform = Platform(randint(0, WIDTH-100), i)
            while(platform.returnType() == 3 and self.last_type == 3):
                platform = Platform(randint(0, WIDTH-100), i)
            if i != 0:
                platform.generated = True
            self.platforms.add(platform)
            self.last_type = platform.returnType()
        self.enemyAir.add(EnemyAir(WIDTH/2, randint(0+100, WIDTH-100)))

    def collision_player_platform(self):
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
                    sprite.speed = player.direction.y * -1

    def platform_generate(self):
        for sprite in self.platforms.sprites():
            if sprite.rect.y > 100 and sprite.generated == False:
                sprite.generated = True
                platform = Platform(randint(0, WIDTH-100), 0)
                while(platform.returnType() == 3 and self.last_type == 3):
                    platform = Platform(randint(0, WIDTH-100), 0)
                self.platforms.add(platform)
                self.last_type = platform.returnType()
                self.update_score(1)

    def playerShootBullet(self, clickPos):
        playerPos = self.player.sprite.position()
        self.bullets.add(Bullet(playerPos,clickPos))

    def collision_bullet_enemy(self):
        for bullet in self.bullets.sprites():
            for air in self.enemyAir.sprites():
                if bullet.rect.colliderect(air.rect):
                    bullet.kill()
                    self.enemy_dies.play()
                    air.kill()
                    print("Enemy je ubit")

    def run(self, event_list):
        ##level platforms
        self.display_surface.blit(load_image('bck', WIDTH,HEIGHT), (0,0))

        #player
        self.player.update(event_list)
        # self.horizontal_movement_collision()
        self.collision_player_platform()

        #bullet
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                self.playerShootBullet(pos)
        self.bullets.update()
        self.bullets.draw(self.display_surface)

        #platform generator
        self.platform_generate()
        #platforms
        self.platform_speed()
        #platform update
        self.platforms.update()
        self.platforms.draw(self.display_surface)
        
        #bullet collision enemy
        self.collision_bullet_enemy()

        #enemy update
        self.enemyAir.update(self.player.sprite)
        self.enemyAir.draw(self.display_surface)


        #player draw
        self.player.draw(self.display_surface)