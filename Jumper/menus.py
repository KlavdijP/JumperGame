import pygame
from settings import *
from button import Button

class PauseMenu:
    def __init__(self, surface, change_status):
        self.display_surface = surface
        self.change_status = change_status
        self.buttons = pygame.sprite.Group()
        self.buttons.add(Button((WIDTH/2, HEIGHT/2), self.display_surface, "ingame"))

        self.font = pygame.font.Font("./fonts/rexlia_rg.otf", 30)


    def show_pause_menu(self, event_list):
        self.display_surface.fill('black')
        self.buttons.draw(self.display_surface)

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
                for x in self.buttons:
                    if x.rect.collidepoint(pos):
                        print("Clicked %s", x.type)
                        self.change_status(x.type)
        # for x in self.buttons:
        #     x.rect.collidepoint()