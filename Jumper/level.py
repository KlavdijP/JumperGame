import pygame
from player import Player, Bullet, Shield
from pickups import Pickups
from functions import *
from platforms import Platform
from enemies import EnemyAir, PCFan, Bouncer
from random import randint
from settings import *
from math import pow
from ui import UI

background = load_image('bck2', WIDTH,HEIGHT)

class Level:
    def __init__(self, surface, settings, change_status, display):
        self.settings = settings
        self.change_status = change_status
        self.player = pygame.sprite.GroupSingle()
        self.display_surface = surface
        self.platforms = pygame.sprite.Group()
        self.enemyAir = pygame.sprite.GroupSingle()
        self.enemyFan = pygame.sprite.GroupSingle()
        self.enemyBouncer = pygame.sprite.GroupSingle()
        self.lastenemy = 0
        self.bullets = pygame.sprite.Group()
        self.score = 140
        self.microchips = 0
        self.cash = 0
        self.difficulty = "easy"
        self.ui = UI(self.display_surface)
        self.shield = pygame.sprite.GroupSingle()
        self.pickups = pygame.sprite.Group()
        self.display = display
        self.font = pygame.font.Font("./fonts/rexlia_rg.otf", 15)


        #Background
        self.bck_scroll = 0
        #Platform
        self.last_type = 4 ##Last generated platform type

        self.setup_level()

    def update_score(self, amount):
        self.score += amount
        if self.score < 162:
            self.set_difficulty()
            #print(self.score, self.difficulty)
        self.enemy_generate()

    def setup_level(self):
        player_sprite = Player(250,250, self.settings)
        self.player.add(player_sprite)

        #Platform creation
        for i in range(0, HEIGHT, 100):
            platform = Platform(randint(0, WIDTH-100), i, self.settings, self.difficulty)
            while(platform.returnType() == 3):
                platform = Platform(randint(0, WIDTH-100), i, self.settings, self.difficulty)
            if i != 0:
                platform.generated = True
            self.platforms.add(platform)
            self.last_type = platform.returnType()

    def move_platforms(self):
        for platform in self.platforms:
            platform.move_it()

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
                        self.move_platforms()
                        self.update_score(1)
                        sprite.kill()
                    else:
                        player.jump(sprite.rect.top)
                        self.move_platforms()

    def stop_object(self, object):
        for sprite in object.sprites():
            sprite.speed = 0

    def move_object(self, object, speed):
        for sprite in object.sprites():
            sprite.speed = speed

    def objects_speed(self):
        player = self.player.sprite
        if player.rect.y > HEIGHT/2:
            self.stop_object(self.platforms)
            self.stop_object(self.pickups)
            self.stop_object(self.enemyFan)
        else:
            if player.direction.y < 0:
                speed = player.direction.y * -1
                self.move_object(self.platforms, speed)
                self.move_object(self.pickups, speed)
                self.move_object(self.enemyFan, speed)

                self.bck_scroll += speed

    def platform_generate(self):
        for sprite in self.platforms.sprites():
            if sprite.rect.y > 100 and sprite.generated == False:
                sprite.generated = True
                platform = Platform(randint(0, WIDTH-100), 0, self.settings, self.difficulty)
                while(platform.returnType() == 3 and self.last_type == 3):
                    platform = Platform(randint(0, WIDTH-100), 0, self.settings, self.difficulty)
                
                #Shield generate
                spawn_shield = randint(0, 1000)
                if spawn_shield < 50:
                    self.pickups.add(Pickups(platform.rect.x, platform.rect.y-75, "shield"))
                
                #Microchip generate
                spawn_microchip = randint(0,1000)
                if spawn_microchip < 50:
                    self.pickups.add(Pickups(randint(0 + 20, WIDTH - 20), platform.rect.y-20, "microchip"))
                
                #Cash generate
                spawn_cash = randint(0,1000)
                if spawn_cash < 50:
                    self.pickups.add(Pickups(randint(0 + 20, WIDTH - 20), platform.rect.y-20, "cash"))
                self.platforms.add(platform)
                self.last_type = platform.returnType()
                self.update_score(1)

    def playerShootBullet(self, clickPos):
        playerPos = self.player.sprite.position()
        playerPos = ((playerPos[0]+25), (playerPos[1]+25))

        if len(self.bullets) < 2:
            self.bullets.add(Bullet(playerPos,clickPos, self.settings))

    def collision_bullet_enemy(self):
        for bullet in self.bullets.sprites():
            for air in self.enemyAir.sprites():
                if bullet.rect.colliderect(air.rect):
                    bullet.kill()
                    air.die()
                    air.kill()
                    print("Enemy air je ubit")
            for bouncer in self.enemyBouncer.sprites():
                if bullet.rect.colliderect(bouncer.rect):
                    bullet.kill()
                    bouncer.kill()
                    print("Enemy bouncer je ubit")

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

        #Player touches enemy bouncer
        for bouncer in self.enemyBouncer.sprites():
            if pygame.sprite.collide_mask(bouncer, self.player.sprite): #air.rect.colliderect(self.player.sprite.rect):
                if len(self.shield.sprites()) == 0:
                    self.end()
        
        #Player touches pickup
        for pickup in self.pickups.sprites():
            if pickup.rect.colliderect(self.player.sprite.rect):
                type = pickup.return_type() 
                if type == "shield":
                    self.shield.add(Shield(self.player.sprite.position()))
                elif type == "microchip":
                    self.microchips += 1                
                elif type == "cash":
                    self.cash += 10
                
                pickup.kill()

    def end(self):
        # high_score = read_file("high_score.txt")
        # if self.score > int(high_score):
        #     write_file("high_score.txt", self.score)
        update_high_score(self.score)
        update_stock("microchips", self.microchips)
        update_stock("money", self.cash)
        post_request(return_json_data())

        self.microchips = 0
        self.cash = 0
        self.change_status("start_menu")

    def spawn_air(self):
        if len(self.enemyAir) == 0 and (self.score - self.lastenemy) > 15:
            self.enemyAir.add(EnemyAir(randint(0+100, WIDTH-100), -50, self.settings))
            self.lastenemy = self.score

    def spawn_fan(self):
        if len(self.enemyFan) == 0 and (self.score - self.lastenemy) > 15:
            coord_x = randint(0+100, WIDTH-100)
            last_x = self.platforms.sprites()[-1].rect.x
            while abs(coord_x - last_x) < 100:
                coord_x = randint(0+100, WIDTH-100)
            self.enemyFan.add(PCFan(coord_x, -50, self.settings))
            self.lastenemy = self.score
    
    def spawn_bouncer(self):
        if len(self.enemyBouncer) == 0 and (self.score - self.lastenemy) > 15:
            self.enemyBouncer.add(Bouncer(randint(0+100, WIDTH-100), -50, self.settings))
            self.lastenemy = self.score

    def enemy_generate(self):
        arr = [] # [n, step1, step2, step3]
        if self.difficulty == "intermediate":
            arr = [1000, 700]
        elif self.difficulty == "very_hard":
            arr = [1000, 800]
        elif self.difficulty == "hard":
            arr = [1000, 900]
        elif self.difficulty == "medium":
            arr = [1000, 950]
        elif self.difficulty == "easy":
            arr = [1, 2]
        
        randType = randint(0, arr[0])
        if randType < arr[1]:
            return
        elif randType >= arr[1]:
            tmp = randint(0, 3)
            if tmp == 0:
                self.spawn_bouncer()
            elif tmp == 1:
                self.spawn_air()
            elif tmp == 2:
                self.spawn_fan()

            # if (arr[0] - randType) > (arr[0] - arr[1])/2:
            #     self.spawn_air()
            # else:
            #     self.spawn_fan()

    def set_difficulty(self):
        if self.score <= 20:
            self.difficulty = "easy"
        elif self.score >= 20 and self.score < 40:
            self.difficulty = "medium"
        elif self.score >= 40 and self.score < 80:
            self.difficulty = "hard"
        elif self.score >= 80 and self.score < 160:
            self.difficulty = "very_hard"
        elif self.score > 160:
            self.difficulty = "intermediate"

    def draw_background(self, scroll):
        self.display_surface.blit(background, (0, 0 + scroll))
        self.display_surface.blit(background, (0, -1*HEIGHT + scroll))

    def run(self, event_list):
        if self.bck_scroll >= HEIGHT:
            self.bck_scroll = 0
        self.draw_background(self.bck_scroll)

        #tutorial
        if self.score < 20:
            sfx_label = self.font.render("press A and D to move", False, "black")
            sfx_rect = sfx_label.get_rect(center = (WIDTH/2, HEIGHT/10 * 6))
            self.display_surface.blit(sfx_label, sfx_rect)
            sfx_label = self.font.render("avoid enemies or shoot them down", False, "black")
            sfx_rect = sfx_label.get_rect(center = (WIDTH/2, HEIGHT/10 * 6.5))
            self.display_surface.blit(sfx_label, sfx_rect)
            sfx_label = self.font.render("pick up microchips and cash", False, "black")
            sfx_rect = sfx_label.get_rect(center = (WIDTH/2, HEIGHT/10 * 7))
            self.display_surface.blit(sfx_label, sfx_rect)

        #player
        self.player.update(event_list)
        if self.player.sprite.rect.y > HEIGHT:
            self.end()
        # self.horizontal_movement_collision()
        self.collision_player_platform()

        #platform generator
        self.platform_generate()
        #platforms
        self.objects_speed()
        #platform update
        self.platforms.update()
        self.platforms.draw(self.display_surface)

        #enemy update
        ## EnemyAir
        self.enemyAir.update(self.player.sprite)
        self.enemyAir.draw(self.display_surface)
        ## EnemyFan
        self.enemyFan.update()
        self.enemyFan.draw(self.display_surface)
        ## EnemyBouncer
        self.enemyBouncer.update()
        self.enemyBouncer.draw(self.display_surface)

        #PICKUPS
        ## Shield
        self.shield.update(self.player.sprite.position())
        self.shield.draw(self.display_surface)

        self.pickups.update()
        self.pickups.draw(self.display_surface)

        #player collision objects
        self.collision_player_objects()

        #bullet

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                ##pos = pygame.mouse.get_pos()
                pos = get_mouse_pos(self.display)
                print(pos, self.player.sprite.position()[0]+25, self.player.sprite.position()[1]+25)
                self.playerShootBullet(pos)
                # self.shield.add(Shield(self.player.sprite.position()))
        self.bullets.update()

        #bullet collision enemy
        self.collision_bullet_enemy()

        #player draw
        self.bullets.draw(self.display_surface)
        self.player.draw(self.display_surface)

        #UI
        self.ui.show_score(self.score)

# self.enemyAir.add(EnemyAir(WIDTH/2, randint(0+100, WIDTH-100), self.settings))
# self.enemyFan.add(PCFan(100,0, self.settings))