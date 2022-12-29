import pygame
from settings import *

class PauseMenu:
    def __init__(self, surface):
        self.display_surface = surface

        # self.image = pygame.Surface((WIDTH/3,HEIGHT/3))
        # self.image.fill('blue')
        # self.rect = self.image.get_rect(center )

        self.font = pygame.font.Font("./fonts/rexlia_rg.otf", 30)

    def show_pause_menu(self):
        self.display_surface.fill('black')
        