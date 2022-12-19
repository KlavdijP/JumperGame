import pygame
from functions import *
from settings import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, clickPos):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill('red')
        self.rect = self.image.get_rect(center = pos)
        self.clickPos = clickPos
        self.speed = 10
        self.direction = pygame.math.Vector2(0,0)
        self.setDirection()

    def setDirection(self):
        v = pygame.math.Vector2(self.clickPos[0] - self.rect.x, self.clickPos[1] - self.rect.y)
        length = v.length()
        if length != 0:
            v /= length
            self.direction.x, self.direction.y = v

    def update(self):
        # self.getDirection()
        self.rect.x += self.direction.x * self.speed 
        self.rect.y += self.direction.y * self.speed 

        if self.rect.x < 0 or self.rect.x > WIDTH or self.rect.y < 0 or self.rect.y > HEIGHT:
            self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        super().__init__()
        self.image = pygame.Surface((64, 64))
        self.image = load_image('lik-left.png', 75, 50)
        # self.image.fill('red')
        self.rect = self.image.get_rect(center = (posx,posy))

        #player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.4
        self.jump_speed = -30
        self.top_reached = False

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.jump()
        else:
            self.direction.x = 0
        
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        if self.direction.y >= 0:
            self.direction.y = self.jump_speed

    def position(self):
        return (self.rect.x, self.rect.y)

    def update(self, event_list):
        self.get_input()
        self.apply_gravity()

        #movement
        self.rect.x += self.direction.x * self.speed 

        if self.rect.y < HEIGHT/2 - 10:
            self.rect.y = HEIGHT/2 - 10
            self.top_reached = True
        else:
            self.top_reached = False

        #offscreen
        if self.rect.x < 0-self.rect.w:
            self.rect.x = WIDTH - 30
        elif self.rect.x > WIDTH:
            self.rect.x = -self.rect.w

        #on moouse click
        # for event in event_list:
        #     if event.type == pygame.MOUSEBUTTONUP:
        #         pos = pygame.mouse.get_pos()
        #         self.rect.x = pos[0]
        #         self.rect.y = pos[1]
        #         self.direction.y = 0