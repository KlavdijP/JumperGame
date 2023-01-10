import pygame
from player import Player, Bullet, Shield
from pickups import Pickups
from functions import *
from platforms import Platform
from enemies import EnemyAir, PCFan
from random import randint
from settings import *
from math import pow
from ui import UI

background = load_image('bck', WIDTH,HEIGHT)

class Level:
    def __init__(self, surface, settings, change_status):
        self.settings = settings
        self.change_status = change_status
        self.player = pygame.sprite.GroupSingle()
        self.display_surface = surface
        self.platforms = pygame.sprite.Group()
        self.enemyAir = pygame.sprite.Group()
        self.enemyFan = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.score = 0
        self.ui = UI(self.display_surface)
        self.shield = pygame.sprite.GroupSingle()
        self.pickups = pygame.sprite.Group()
        #Platform
        self.last_type = 4 ##Last generated platform type

        self.setup_level()

    def update_score(self, amount):
        self.score += amount

    def setup_level(self):
        player_sprite = Player(250,250, self.settings)
        self.player.add(player_sprite)

        #Platform creation
        for i in range(0, HEIGHT, 100):
            platform = Platform(randint(0, WIDTH-100), i, self.settings)
            while(platform.returnType() == 3):
                platform = Platform(randint(0, WIDTH-100), i, self.settings)
            if i != 0:
                platform.generated = True
            self.platforms.add(platform)
            self.last_type = platform.returnType()
        self.enemyAir.add(EnemyAir(WIDTH/2, randint(0+100, WIDTH-100), self.settings))
        self.enemyFan.add(PCFan(100,0, self.settings))

    def collision_player_platform(self):
        player = self.player.sprite
        if player.direction.y >= 0:
            for sprite in self.platforms.sprites():
                if sprite.rect.colliderect([player.rect.x, player.rect.y+50, 64, 1]):
                    if sprite.type == 3:
                        self.settings.glass_break()
                        self.update_score(1)
                        sprite.kill()
                    elif sprite.type == 2:
                        player.jump(sprite.rect.top)
                        self.update_score(1)
                        sprite.kill()
                    else:
                        player.jump(sprite.rect.top)
    
    def stop_object(self, object):
        for sprite in object.sprites():
            sprite.speed = 0

    def move_object(self, object, player):
        for sprite in object.sprites():
            if player.direction.y < 0:
                sprite.speed = player.direction.y * -1

    def objects_speed(self):
        player = self.player.sprite
        if player.rect.y > HEIGHT/2:
            self.stop_object(self.platforms)
            self.stop_object(self.pickups)
            self.stop_object(self.enemyFan)
        else:
            self.move_object(self.platforms, player)
            self.move_object(self.pickups, player)
            self.move_object(self.enemyFan, player)

    def platform_generate(self):
        for sprite in self.platforms.sprites():
            if sprite.rect.y > 100 and sprite.generated == False:
                sprite.generated = True
                platform = Platform(randint(0, WIDTH-100), 0, self.settings)
                while(platform.returnType() == 3 and self.last_type == 3):
                    platform = Platform(randint(0, WIDTH-100), 0, self.settings)
                spawn_shield = randint(0, 1000)
                if spawn_shield < 50:
                    self.pickups.add(Pickups(platform.rect.x, platform.rect.y-75))
                self.platforms.add(platform)
                self.last_type = platform.returnType()
                self.update_score(1)

    def playerShootBullet(self, clickPos):
        playerPos = self.player.sprite.position()
        playerPos = (playerPos[0]+25, playerPos[1]+25)
        self.bullets.add(Bullet(playerPos,clickPos, self.settings))

    def collision_bullet_enemy(self):
        for bullet in self.bullets.sprites():
            for air in self.enemyAir.sprites():
                if bullet.rect.colliderect(air.rect):
                    bullet.kill()
                    air.die()
                    air.kill()
                    print("Enemy je ubit")

    def collision_player_objects(self):
        #Player touches enemy air
        for air in self.enemyAir.sprites():
            if pygame.sprite.collide_mask(air, self.player.sprite): #air.rect.colliderect(self.player.sprite.rect):
                if len(self.shield.sprites()) == 0:
                    self.end()
        #Player touches enemy fan
        for fan in self.enemyFan.sprites():
            if pygame.sprite.collide_mask(fan, self.player.sprite): #air.rect.colliderect(self.player.sprite.rect):
                if len(self.shield.sprites()) == 0:
                    self.end()
        
        #Player touches pickup
        for pickup in self.pickups.sprites():
            if pickup.rect.colliderect(self.player.sprite.rect):
                pickup.kill()
                self.shield.add(Shield(self.player.sprite.position()))

    def end(self):
        high_score = read_file("high_score.txt")
        if self.score > int(high_score):
            write_file("high_score.txt", self.score)
        self.change_status("start_menu")

    def run(self, event_list):
        ##level platforms
        self.display_surface.blit(background, (0,0))

        #player
        self.player.update(event_list)
        if self.player.sprite.rect.y > HEIGHT:
            self.end()
        # self.horizontal_movement_collision()
        self.collision_player_platform()

        #bullet
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                self.playerShootBullet(pos)
                # self.shield.add(Shield(self.player.sprite.position()))
        self.bullets.update()

        #platform generator
        self.platform_generate()
        #platforms
        self.objects_speed()
        #platform update
        self.platforms.update()
        self.platforms.draw(self.display_surface)

        #UI
        self.ui.show_score(self.score)

        #bullet collision enemy
        self.collision_bullet_enemy()

        #player collision objects
        self.collision_player_objects()

        #enemy update
        ## EnemyAir
        self.enemyAir.update(self.player.sprite)
        self.enemyAir.draw(self.display_surface)
        ## EnemyFan
        self.enemyFan.update()
        self.enemyFan.draw(self.display_surface)


        self.shield.update(self.player.sprite.position())
        self.shield.draw(self.display_surface)

        self.pickups.update()
        self.pickups.draw(self.display_surface)
        #player draw
        self.bullets.draw(self.display_surface)
        self.player.draw(self.display_surface)

