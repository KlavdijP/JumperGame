import pygame
from settings import *

class UI:
    def __init__(self, surface):
        self.display_surface = surface
        self.font = pygame.font.Font("./fonts/rexlia_rg.otf", 30)

    def show_score(self, score):
        score_surf = self.font.render(str(score), False, "white")
        score_rect = score_surf.get_rect(center = (WIDTH/2, 60))
        self.display_surface.blit(score_surf, score_rect)