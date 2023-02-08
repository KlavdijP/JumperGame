import pygame
from settings import *
from button import Button
from functions import *

prices = {
    "gpu": 10,
    "microchip": 1,
    "mb": 10,
    "psu": 10,
    "fan": 1,
    "cpu": 10,
    "frame": 10,
}

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

class ShopMenu:
    def __init__(self, surface, change_status):
        self.display_surface = surface
        self.change_status = change_status
        self.buttons = pygame.sprite.Group()
        self.microchips = 0
        self.money = 0
        self.gpus = 0
        self.psus = 0
        self.mbs = 0
        self.fans = 0
        self.cpus = 0
        self.frames = 0
        self.buttons.add(Button((WIDTH/2, HEIGHT/10 * 7), self.display_surface, "start_menu", "BACK")) #Add unpause button
        self.buttons.add(Button((WIDTH/8 * 1, HEIGHT/10 * 3), self.display_surface, "gpu", "BUY", metrics=(60, 60), fontsize=15)) #Add unpause button
        self.buttons.add(Button((WIDTH/8 * 2, HEIGHT/10 * 3), self.display_surface, "microchip", "BUY", metrics=(60, 60), fontsize=15)) #Add unpause button
        self.buttons.add(Button((WIDTH/8 * 3, HEIGHT/10 * 3), self.display_surface, "mb", "BUY", metrics=(60, 60), fontsize=15)) #Add unpause button
        self.buttons.add(Button((WIDTH/8 * 4, HEIGHT/10 * 3), self.display_surface, "psu", "BUY", metrics=(60, 60), fontsize=15)) #Add unpause button
        self.buttons.add(Button((WIDTH/8 * 5, HEIGHT/10 * 3), self.display_surface, "fan", "BUY", metrics=(60, 60), fontsize=15)) #Add unpause button
        self.buttons.add(Button((WIDTH/8 * 6, HEIGHT/10 * 3), self.display_surface, "cpu", "BUY", metrics=(60, 60), fontsize=15)) #Add unpause button
        self.buttons.add(Button((WIDTH/8 * 7, HEIGHT/10 * 3), self.display_surface, "frame", "BUY", metrics=(60, 60), fontsize=15)) #Add unpause button
        self.font1 = pygame.font.Font("./fonts/rexlia_rg.otf", 30)
        self.font2= pygame.font.Font("./fonts/rexlia_rg.otf", 15)
        self.update()

    def update(self):
        data = return_json_data()
        self.microchips = data["microchips"]
        self.gpus = data["gpus"]
        self.money = data["money"]
        self.gpus = data["gpus"]
        self.psus = data["psus"]
        self.mbs = data["mbs"]
        self.fans = data["fans"]
        self.cpus = data["cpus"]
        self.frames = data["frames"]

    def buy(self, item):
        if item == "gpu":
            if self.microchips - prices["gpu"] >= 0:
                update_stock("gpus", 1)
                update_stock("microchips", -1 * prices["gpu"])
        
        elif item == "microchip":
            if self.money - prices["microchip"] >= 0:
                update_stock("microchips", 1)
                update_stock("money", -1 * prices["microchip"])
        
        elif item == "mb":
            if self.microchips - prices["mb"] >= 0:
                update_stock("mbs", 1)
                update_stock("microchips", -1 * prices["mb"])
        
        elif item == "psu":
            if self.microchips - prices["psu"] >= 0:
                update_stock("psus", 1)
                update_stock("microchips", -1 * prices["psu"])
        
        elif item == "fan":
            if self.microchips - prices["fan"] >= 0:
                update_stock("fans", 1)
                update_stock("microchips", -1 * prices["fan"])
        
        elif item == "cpu":
            if self.microchips - prices["cpu"] >= 0:
                update_stock("cpus", 1)
                update_stock("microchips", -1 * prices["cpu"])
        
        elif item == "frame":
            if self.microchips - prices["frame"] >= 0:
                update_stock("frames", 1)
                update_stock("microchips", -1 * prices["frame"])
        
        self.update()

    def show_menu(self, event_list):
        self.display_surface.fill('black')
        # self.buttons.draw(self.display_surface)
        for button in self.buttons.sprites():
            button.draw()

        sfx_label = self.font1.render("Money: " + str("%.2f" % round(self.money,2)), False, "#53f53f")
        sfx_rect = sfx_label.get_rect(center = (WIDTH/2, HEIGHT/10 * 1))
        self.display_surface.blit(sfx_label, sfx_rect)

        sfx_label = self.font1.render("Microchips: " + str(self.microchips), False, "#53f53f")
        sfx_rect = sfx_label.get_rect(center = (WIDTH/2, HEIGHT/10 * 2))
        self.display_surface.blit(sfx_label, sfx_rect)

        sfx_label = self.font2.render("GPU", False, "#53f53f")
        sfx_rect = sfx_label.get_rect(center = (WIDTH/8 * 1, HEIGHT/10 * 4))
        self.display_surface.blit(sfx_label, sfx_rect)
        sfx_label = self.font2.render(str(self.gpus), False, "#53f53f")
        sfx_rect = sfx_label.get_rect(center = (WIDTH/8 * 1, HEIGHT/10 * 4.25))
        self.display_surface.blit(sfx_label, sfx_rect)

        sfx_label = self.font2.render("MC", False, "#53f53f")
        sfx_rect = sfx_label.get_rect(center = (WIDTH/8 * 2, HEIGHT/10 * 4))
        self.display_surface.blit(sfx_label, sfx_rect)
        sfx_label = self.font2.render(str(self.microchips), False, "#53f53f")
        sfx_rect = sfx_label.get_rect(center = (WIDTH/8 * 2, HEIGHT/10 * 4.25))
        self.display_surface.blit(sfx_label, sfx_rect)

        sfx_label = self.font2.render("MB", False, "#53f53f")
        sfx_rect = sfx_label.get_rect(center = (WIDTH/8 * 3, HEIGHT/10 * 4))
        self.display_surface.blit(sfx_label, sfx_rect)
        sfx_label = self.font2.render(str(self.mbs), False, "#53f53f")
        sfx_rect = sfx_label.get_rect(center = (WIDTH/8 * 3, HEIGHT/10 * 4.25))
        self.display_surface.blit(sfx_label, sfx_rect)

        sfx_label = self.font2.render("PSU", False, "#53f53f")
        sfx_rect = sfx_label.get_rect(center = (WIDTH/8 * 4, HEIGHT/10 * 4))
        self.display_surface.blit(sfx_label, sfx_rect)
        sfx_label = self.font2.render(str(self.psus), False, "#53f53f")
        sfx_rect = sfx_label.get_rect(center = (WIDTH/8 * 4, HEIGHT/10 * 4.25))
        self.display_surface.blit(sfx_label, sfx_rect)

        sfx_label = self.font2.render("FAN", False, "#53f53f")
        sfx_rect = sfx_label.get_rect(center = (WIDTH/8 * 5, HEIGHT/10 * 4))
        self.display_surface.blit(sfx_label, sfx_rect)
        sfx_label = self.font2.render(str(self.fans), False, "#53f53f")
        sfx_rect = sfx_label.get_rect(center = (WIDTH/8 * 5, HEIGHT/10 * 4.25))
        self.display_surface.blit(sfx_label, sfx_rect)

        sfx_label = self.font2.render("CPU", False, "#53f53f")
        sfx_rect = sfx_label.get_rect(center = (WIDTH/8 * 6, HEIGHT/10 * 4))
        self.display_surface.blit(sfx_label, sfx_rect)
        sfx_label = self.font2.render(str(self.cpus), False, "#53f53f")
        sfx_rect = sfx_label.get_rect(center = (WIDTH/8 * 6, HEIGHT/10 * 4.25))
        self.display_surface.blit(sfx_label, sfx_rect)

        sfx_label = self.font2.render("FRAME", False, "#53f53f")
        sfx_rect = sfx_label.get_rect(center = (WIDTH/8 * 7, HEIGHT/10 * 4))
        self.display_surface.blit(sfx_label, sfx_rect)
        sfx_label = self.font2.render(str(self.frames), False, "#53f53f")
        sfx_rect = sfx_label.get_rect(center = (WIDTH/8 * 7, HEIGHT/10 * 4.25))
        self.display_surface.blit(sfx_label, sfx_rect)

        

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
                for x in self.buttons:
                    if x.rect.collidepoint(pos):
                        print("Clicked %s", x.type)
                        if x.type == "gpu":
                            self.buy("gpu")
                        elif x.type == "microchip":
                            self.buy("microchip")
                        elif x.type == "mb":
                            self.buy("mb")
                        elif x.type == "psu":
                            self.buy("psu")
                        elif x.type == "fan":
                            self.buy("fan")
                        elif x.type == "cpu":
                            self.buy("cpu")
                        elif x.type == "frame":
                            self.buy("frame")
                        else:
                            self.change_status(x.type)

class StartMenu:
    def __init__(self, surface, change_status):
        self.display_surface = surface
        self.change_status = change_status
        self.buttons = pygame.sprite.Group()
        self.buttons.add(Button((WIDTH/2, HEIGHT/10 * 4), self.display_surface, "newgame", "PLAY"))
        self.buttons.add(Button((WIDTH/2, HEIGHT/10 * 5), self.display_surface, "shop_menu", "SHOP"))
        self.buttons.add(Button((WIDTH/2, HEIGHT/10 * 6), self.display_surface, "settings_menu", "SETTINGS"))
        self.buttons.add(Button((WIDTH/2, HEIGHT/10 * 7), self.display_surface, "exit", "EXIT"))
        self.score = 0
        self.player_name = return_json_data()["player_name"]
        self.font = pygame.font.Font("./fonts/rexlia_rg.otf", 30)

        self.update_score()

    def update_score(self):
        self.score = return_json_data()["high_score"]

    def show_menu(self, event_list):
        self.display_surface.fill('black')
        # self.buttons.draw(self.display_surface)
        for button in self.buttons.sprites():
            button.draw()

        sfx_label = self.font.render("High score: " + str(self.score), False, "#53f53f")
        sfx_rect = sfx_label.get_rect(center = (WIDTH/2, HEIGHT/10 * 2))
        self.display_surface.blit(sfx_label, sfx_rect)

        sfx_label = self.font.render("Player: " + str(self.player_name), False, "#53f53f")
        sfx_rect = sfx_label.get_rect(center = (WIDTH/2, HEIGHT/10 * 1))
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
        # self.buttons.add(Button((WIDTH/2, HEIGHT/10 * 6), self.display_surface, "start_menu", "CHANGE NAME"))
        self.buttons.add(Button((WIDTH/2, HEIGHT/10 * 7), self.display_surface, "start_menu", "BACK"))
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