import pygame

class Player:
    def __init__(self, posx, posy):
        self.x = posx
        self.y = posy
        self.image = pygame.transform.scale(pygame.image.load('./assets/lik-left.png'), (150,100))