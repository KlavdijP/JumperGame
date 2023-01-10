import pygame
from settings import *
from button import Button
from functions import write_file, read_file


class PauseMenu:
    def __init__(self, surface, change_status):
        self.display_surface = surface
        self.change_status = change_status
        self.buttons = pygame.sprite.Group()

        self.buttons.add(Button((WIDTH/2, HEIGHT/10 * 2), self.display_surface, "play", "RESUME")) #Add unpause button
        self.buttons.add(Button((WIDTH/2, HEIGHT/10 * 4), self.display_surface, "start_menu", "MAIN MENU")) #Add unpause button
        self.buttons.add(Button((WIDTH/2, HEIGHT/10 * 6), self.display_surface, "settings_pause", "SETTINGS")) #Add unpause button
        self.buttons.add(Button((WIDTH/2, HEIGHT/10 * 8), self.display_surface, "exit", "EXIT")) #Add unpause button
        
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

class StartMenu:
    def __init__(self, surface, change_status):
        self.display_surface = surface
        self.change_status = change_status
        self.buttons = pygame.sprite.Group()
        self.buttons.add(Button((WIDTH/2, HEIGHT/10 * 4), self.display_surface, "newgame", "PLAY"))
        self.buttons.add(Button((WIDTH/2, HEIGHT/10 * 6), self.display_surface, "settings_menu", "SETTINGS"))
        self.buttons.add(Button((WIDTH/2, HEIGHT/10 * 8), self.display_surface, "exit", "EXIT"))

        self.score = read_file("high_score.txt")

        self.font = pygame.font.Font("./fonts/rexlia_rg.otf", 30)

    def update_score(self):
        self.score = read_file("high_score.txt")

    def show_menu(self, event_list):
        self.display_surface.fill('black')
        # self.buttons.draw(self.display_surface)
        for button in self.buttons.sprites():
            button.draw()

        sfx_label = self.font.render("High score: " + str(self.score), False, "#53f53f")
        sfx_rect = sfx_label.get_rect(center = (WIDTH/2, HEIGHT/10 * 2))
        self.display_surface.blit(sfx_label, sfx_rect)

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
                for x in self.buttons:
                    if x.rect.collidepoint(pos):
                        print("Clicked %s", x.type)
                        self.change_status(x.type)

class SettingsMenuMenu:
    def __init__(self, surface, change_status, settings):
        self.settings = settings
        self.display_surface = surface
        self.change_status = change_status
        self.buttons = pygame.sprite.Group()
        self.buttons.add(Button((WIDTH/2, HEIGHT/2), self.display_surface, "start_menu", "BACK"))
        self.buttons.add(Button((WIDTH/14 * 5, HEIGHT/10 * 4), self.display_surface, "volume", "-", (50, 50)))
        self.buttons.add(Button((WIDTH/14 * 9, HEIGHT/10 * 4), self.display_surface, "volume", "+", (50, 50)))
        
        self.font = pygame.font.Font("./fonts/rexlia_rg.otf", 30)

    def show_menu(self, event_list):
        self.display_surface.fill('black')
        # self.buttons.draw(self.display_surface)
        for button in self.buttons.sprites():
            button.draw()

        sfx_label = self.font.render(str(self.settings.sfx), False, "#53f53f")
        sfx_rect = sfx_label.get_rect(center = (WIDTH/14*7, HEIGHT/10 * 4))
        self.display_surface.blit(sfx_label, sfx_rect)


        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
                for x in self.buttons:
                    if x.rect.collidepoint(pos):
                        print("Clicked %s", x.type)
                        if x.type != "volume":
                            self.change_status(x.type)
                        else:
                            if x.displayed == "+":
                                self.settings.set_sfx(10)
                            elif x.displayed == "-":
                                self.settings.set_sfx(-10)
     
class SettingsMenuPause:
    def __init__(self, surface, change_status, settings):
        self.settings = settings
        self.display_surface = surface
        self.change_status = change_status
        self.buttons = pygame.sprite.Group()
        self.buttons.add(Button((WIDTH/2, HEIGHT/2), self.display_surface, "pause", "BACK"))
        self.buttons.add(Button((WIDTH/14 * 5, HEIGHT/10 * 4), self.display_surface, "volume", "-", (50, 50)))
        self.buttons.add(Button((WIDTH/14 * 9, HEIGHT/10 * 4), self.display_surface, "volume", "+", (50, 50)))
        
        self.font = pygame.font.Font("./fonts/rexlia_rg.otf", 30)

    def show_menu(self, event_list):
        self.display_surface.fill('black')
        # self.buttons.draw(self.display_surface)
        for button in self.buttons.sprites():
            button.draw()

        sfx_label = self.font.render(str(self.settings.sfx), False, "#53f53f")
        sfx_rect = sfx_label.get_rect(center = (WIDTH/14*7, HEIGHT/10 * 4))
        self.display_surface.blit(sfx_label, sfx_rect)

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
                for x in self.buttons:
                    if x.rect.collidepoint(pos):
                        print("Clicked %s", x.type)
                        if x.type != "volume":
                            self.change_status(x.type)
                        else:
                            if x.displayed == "+":
                                self.settings.set_sfx(10)
                            elif x.displayed == "-":
                                self.settings.set_sfx(-10)