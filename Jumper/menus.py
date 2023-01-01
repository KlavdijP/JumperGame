import pygame
from settings import *
from button import Button

class PauseMenu:
    def __init__(self, surface, change_status):
        self.display_surface = surface
        self.change_status = change_status
        self.buttons = pygame.sprite.Group()

        self.buttons.add(Button((WIDTH/2, HEIGHT/10 * 8), self.display_surface, "play")) #Add unpause button
        self.buttons.add(Button((WIDTH/2, HEIGHT/10 * 7), self.display_surface, "settings_pause")) #Add unpause button
        self.buttons.add(Button((WIDTH/2, HEIGHT/10 * 9), self.display_surface, "start_menu")) #Add unpause button
        
        self.font = pygame.font.Font("./fonts/rexlia_rg.otf", 30)

    def show_menu(self, event_list):
        self.display_surface.fill('black')
        # self.buttons.draw(self.display_surface)
        for button in self.buttons.sprites():
            button.draw()

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

class StartMenu:
    def __init__(self, surface, change_status):
        self.display_surface = surface
        self.change_status = change_status
        self.buttons = pygame.sprite.Group()
        self.buttons.add(Button((WIDTH/2, HEIGHT/10 * 2), self.display_surface, "newgame"))
        self.buttons.add(Button((WIDTH/2, HEIGHT/10 * 4), self.display_surface, "settings_menu"))

        self.font = pygame.font.Font("./fonts/rexlia_rg.otf", 30)

    def show_menu(self, event_list):
        self.display_surface.fill('black')
        # self.buttons.draw(self.display_surface)
        for button in self.buttons.sprites():
            button.draw()

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
                for x in self.buttons:
                    if x.rect.collidepoint(pos):
                        print("Clicked %s", x.type)
                        self.change_status(x.type)

class SettingsMenuMenu:
    def __init__(self, surface, change_status):
        self.display_surface = surface
        self.change_status = change_status
        self.buttons = pygame.sprite.Group()
        self.buttons.add(Button((WIDTH/2, HEIGHT/2), self.display_surface, "start_menu"))

        self.font = pygame.font.Font("./fonts/rexlia_rg.otf", 30)

    def show_menu(self, event_list):
        self.display_surface.fill('black')
        # self.buttons.draw(self.display_surface)
        for button in self.buttons.sprites():
            button.draw()


        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
                for x in self.buttons:
                    if x.rect.collidepoint(pos):
                        print("Clicked %s", x.type)
                        self.change_status(x.type)

class SettingsMenuPause:
    def __init__(self, surface, change_status):
        self.display_surface = surface
        self.change_status = change_status
        self.buttons = pygame.sprite.Group()
        self.buttons.add(Button((WIDTH/2, HEIGHT/2), self.display_surface, "pause"))

        self.font = pygame.font.Font("./fonts/rexlia_rg.otf", 30)

    def show_menu(self, event_list):
        self.display_surface.fill('black')
        # self.buttons.draw(self.display_surface)
        for button in self.buttons.sprites():
            button.draw()

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
                for x in self.buttons:
                    if x.rect.collidepoint(pos):
                        print("Clicked %s", x.type)
                        self.change_status(x.type)