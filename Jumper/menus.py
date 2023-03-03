import pygame
from settings import *
from button import Button
from functions import *

prices = {
    "gpu": (120, 0),
    "microchip": (0, 100),
    "mb": (80, 0),
    "psu": (5, 10),
    "fan": (2, 10),
    "cpu": (100, 0),
    "frame": (0, 100),
}

background = load_image('menu', WIDTH,HEIGHT)

class PauseMenu:
    def __init__(self, surface, change_status, display):
        self.display_surface = surface
        self.display = display
        self.change_status = change_status
        self.buttons = pygame.sprite.Group()

        self.buttons.add(Button((WIDTH/2, HEIGHT/10 * 4), self.display_surface, "play", metrics=(150,50), image="/buttons/resume"))
        self.buttons.add(Button((WIDTH/2, HEIGHT/10 * 5), self.display_surface, "start_menu", metrics=(150,50), image="/buttons/menu"))
        self.buttons.add(Button((WIDTH/2, HEIGHT/10 * 6), self.display_surface, "settings_pause", metrics=(150,50), image="/buttons/settings"))
        self.buttons.add(Button((WIDTH/2, HEIGHT/10 * 7), self.display_surface, "exit", metrics=(150,50), image="/buttons/exit"))
        
    def show_menu(self, event_list):
        self.display_surface.fill((18,32,45))
        # self.buttons.draw(self.display_surface)
        for button in self.buttons.sprites():
            button.draw()

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = get_mouse_pos(self.display)
                # print(pos)
                for x in self.buttons:
                    # print("\t%s %s" % (x.pos, x.type))
                    if x.rect.collidepoint(pos):
                        # print("Clicked %s", x.type)
                        self.change_status(x.type)

class ShopMenu:
    def __init__(self, surface, change_status, display):
        self.display_surface = surface
        self.display = display
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
        self.buttons.add(Button((WIDTH/2, HEIGHT/10 * 9), self.display_surface, "start_menu", metrics=(150,50), image="/buttons/menu")) #Add unpause button
        self.buttons.add(Button((WIDTH/8 * 2, HEIGHT/10 * 3), self.display_surface, "microchip", metrics=(40,40), image="/shop/microchip", fontsize=15)) #Add unpause button
        self.buttons.add(Button((WIDTH/8 * 6, HEIGHT/10 * 3), self.display_surface, "build", metrics=(80,80), image="/shop/build", fontsize=15)) #Add unpause button
        self.buttons.add(Button((WIDTH/8 * 2, HEIGHT/10 * 5), self.display_surface, "mb", metrics=(50,50), image="/shop/mb", fontsize=15)) #Add unpause button
        self.buttons.add(Button((WIDTH/8 * 4, HEIGHT/10 * 5), self.display_surface, "gpu", metrics=(50,50), image="/shop/gpu", fontsize=15)) #Add unpause button
        self.buttons.add(Button((WIDTH/8 * 6, HEIGHT/10 * 5), self.display_surface, "cpu", metrics=(50,50), image="/shop/cpu", fontsize=15)) #Add unpause button
        self.buttons.add(Button((WIDTH/8 * 2, HEIGHT/10 * 7), self.display_surface, "fan", metrics=(50,50), image="/shop/fan", fontsize=15)) #Add unpause button
        self.buttons.add(Button((WIDTH/8 * 4, HEIGHT/10 * 7), self.display_surface, "frame", metrics=(50,50), image="/shop/case", fontsize=15)) #Add unpause button
        self.buttons.add(Button((WIDTH/8 * 6, HEIGHT/10 * 7), self.display_surface, "psu", metrics=(50,50), image="/shop/psu", fontsize=15)) #Add unpause button
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
        self.builds = data["builds"]

    def buy(self, item):
        if item == "gpu":
            if self.microchips - prices["gpu"][0] >= 0:
                update_stock("gpus", 1)
                update_stock("microchips", -1 * prices["gpu"][0])
        
        elif item == "microchip":
            if self.money - prices["microchip"][1] >= 0:
                update_stock("microchips", 10)
                update_stock("money", -1 * prices["microchip"][1])
        
        elif item == "mb":
            if self.microchips - prices["mb"][0] >= 0:
                update_stock("mbs", 1)
                update_stock("microchips", -1 * prices["mb"][0])
        
        elif item == "psu":
            if self.microchips - prices["psu"][0] >= 0:
                if self.money - prices["psu"][1] >= 0:
                    update_stock("psus", 1)
                    update_stock("money", -1 * prices["psu"][1])
                    update_stock("microchips", -1 * prices["psu"][0])
        
        elif item == "fan":
            if self.microchips - prices["fan"][0] >= 0:
                if self.money - prices["psu"][1] >= 0:
                    update_stock("fans", 1)
                    update_stock("microchips", -1 * prices["fan"][0])
                    update_stock("money", -1 * prices["fan"][1])
        
        elif item == "cpu":
            if self.microchips - prices["cpu"][0] >= 0:
                update_stock("cpus", 1)
                update_stock("microchips", -1 * prices["cpu"][0])
        
        elif item == "frame":
            if self.money - prices["frame"][0] >= 0:
                update_stock("frames", 1)
                update_stock("money", -1 * prices["frame"][0])

        elif item == "build":
            if (self.mbs - 1 >= 0 and
                self.gpus -1 >= 0 and
                self.cpus -1 >= 0 and
                self.fans -3 >= 0 and
                self.frames -1 >= 0 and
                self.psus -1 >= 0 ):

                update_stock("builds", 1)
                update_stock("mbs", -1)
                update_stock("gpus", -1)
                update_stock("cpus", -1)
                update_stock("fans", -3)
                update_stock("frames", -1)
                update_stock("psus", -1)     
        self.update()

    def draw_text(self, part, amount, pos1, pos2):
        sfx_label = self.font2.render(part, False, "white")
        sfx_rect = sfx_label.get_rect(center = (pos1, pos2 * 0.95))
        self.display_surface.blit(sfx_label, sfx_rect)
        sfx_label = self.font2.render(str(amount), False, "white")
        sfx_rect = sfx_label.get_rect(center = (pos1, pos2 * 0.95 + 15))
        self.display_surface.blit(sfx_label, sfx_rect)

    def show_menu(self, event_list):
        self.display_surface.fill((18,32,45))
        # self.buttons.draw(self.display_surface)
        for button in self.buttons.sprites():
            button.draw()

        sfx_label = self.font1.render("Money: " + str("%.2f" % round(self.money,2)), False, "white")
        sfx_rect = sfx_label.get_rect(center = (WIDTH/2, HEIGHT/10 * 1))
        self.display_surface.blit(sfx_label, sfx_rect)

        sfx_label = self.font1.render("Microchips: " + str(self.microchips), False, "white")
        sfx_rect = sfx_label.get_rect(center = (WIDTH/2, HEIGHT/10 * 2))
        self.display_surface.blit(sfx_label, sfx_rect)

        self.draw_text("MC", self.microchips, WIDTH/8 *2, HEIGHT/10 *4)
        self.draw_text("BUILD", self.builds, WIDTH/8 *6, HEIGHT/10 *4)
        self.draw_text("MB", self.mbs, WIDTH/8 *2, HEIGHT/10 *6)
        self.draw_text("GPU", self.gpus, WIDTH/8 *4, HEIGHT/10 *6)
        self.draw_text("CPU", self.cpus, WIDTH/8 *6, HEIGHT/10 *6)
        self.draw_text("FAN", self.fans, WIDTH/8 *2, HEIGHT/10 *8)
        self.draw_text("FRAME", self.frames, WIDTH/8 *4, HEIGHT/10 *8)       
        self.draw_text("PSU", self.psus, WIDTH/8 *6, HEIGHT/10 *8)

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = get_mouse_pos(self.display)
                # print(pos)
                for x in self.buttons:
                    if x.rect.collidepoint(pos):
                        # print("Clicked %s", x.type)
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
                        elif x.type == "build":
                            self.buy("build")
                        else:
                            self.change_status(x.type)

class StartMenu:
    def __init__(self, surface, change_status, display):
        self.display_surface = surface
        self.display = display
        self.change_status = change_status
        self.buttons = pygame.sprite.Group()
        self.buttons.add(Button((WIDTH/2, HEIGHT/10 * 4), self.display_surface, "newgame", metrics=(150,50), image="/buttons/play"))
        self.buttons.add(Button((WIDTH/2, HEIGHT/10 * 5), self.display_surface, "shop_menu", metrics=(150,50), image="/buttons/shop"))
        self.buttons.add(Button((WIDTH/2, HEIGHT/10 * 6), self.display_surface, "settings_menu", metrics=(150,50), image="/buttons/settings"))
        self.buttons.add(Button((WIDTH/2, HEIGHT/10 * 7), self.display_surface, "start_about", metrics=(150,50), image="/buttons/about"))
        self.buttons.add(Button((WIDTH/2, HEIGHT/10 * 8), self.display_surface, "exit", metrics=(150,50), image="/buttons/exit"))
        self.score = 0
        self.player_name = return_json_data()["player_name"]
        self.font = pygame.font.Font("./fonts/rexlia_rg.otf", 30)
        self.input_rect = pygame.Rect(WIDTH/10*2, HEIGHT/10 * 1, WIDTH/10*6, 40)

        self.active = False 
        self.update_score()

    def update_score(self):
        self.score = return_json_data()["high_score"]

    def show_menu(self, event_list):
        #self.display_surface.fill((18,32,45))
        self.display_surface.blit(background, (0,0))
        # self.buttons.draw(self.display_surface)
        for button in self.buttons.sprites():
            button.draw()

        sfx_label = self.font.render("High score: " + str(self.score), False, "white")
        sfx_rect = sfx_label.get_rect(center = (WIDTH/2, HEIGHT/10 * 2))
        self.display_surface.blit(sfx_label, sfx_rect)

        sfx_label = self.font.render(str(self.player_name), False, "white")
        if self.active == True:
            pygame.draw.rect(self.display_surface, "white", self.input_rect, 2)
        else:
            pygame.draw.rect(self.display_surface, (18,32,45), self.input_rect, 2)
        # sfx_rect = sfx_label.get_rect(center = (WIDTH/2, HEIGHT/10 * 1))
        self.display_surface.blit(sfx_label, (self.input_rect.x + 5, self.input_rect.y + 5))

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = get_mouse_pos(self.display)
                # print(pos)
                for x in self.buttons:
                    if x.rect.collidepoint(pos):
                        # print("Clicked %s", x.type)
                        self.change_status(x.type)
                if self.input_rect.collidepoint(pos):
                    self.active = True
                else:
                    if self.active == True:
                        change_name(self.player_name)
                    self.active = False

            if event.type == pygame.KEYDOWN:
                if self.active == True:
                    if event.key == pygame.K_BACKSPACE:
                        self.player_name = self.player_name[:-1]
                    else:
                        if len(self.player_name) < 12:
                            self.player_name += event.unicode

class SettingsMenuMenu:
    def __init__(self, surface, change_status, settings, display):
        self.settings = settings
        self.display_surface = surface
        self.display = display
        self.change_status = change_status
        self.buttons = pygame.sprite.Group()
        # self.buttons.add(Button((WIDTH/2, HEIGHT/10 * 6), self.display_surface, "start_menu", "CHANGE NAME"))
        self.buttons.add(Button((WIDTH/2, HEIGHT/10 * 7), self.display_surface, "start_menu", metrics=(150,50), image="/buttons/menu"))
        self.buttons.add(Button((WIDTH/14 * 5, HEIGHT/10 * 3), self.display_surface, "volume", "s-", metrics=(50,50), image="/buttons/minus"))
        self.buttons.add(Button((WIDTH/14 * 9, HEIGHT/10 * 3), self.display_surface, "volume", "s+", metrics=(50,50), image="/buttons/plus"))
        self.buttons.add(Button((WIDTH/14 * 5, HEIGHT/10 * 5), self.display_surface, "volume", "m-", metrics=(50,50), image="/buttons/minus"))
        self.buttons.add(Button((WIDTH/14 * 9, HEIGHT/10 * 5), self.display_surface, "volume", "m+", metrics=(50,50), image="/buttons/plus"))
        
        self.font = pygame.font.Font("./fonts/rexlia_rg.otf", 30)

    def show_menu(self, event_list):
        self.display_surface.fill((18,32,45))
        # self.buttons.draw(self.display_surface)
        for button in self.buttons.sprites():
            button.draw()

        sfx_label = self.font.render("SFX", False, "white")
        sfx_rect = sfx_label.get_rect(center = (WIDTH/14*7, HEIGHT/10 * 2.4))
        self.display_surface.blit(sfx_label, sfx_rect)

        sfx_label = self.font.render(str(self.settings.sfx), False, "white")
        sfx_rect = sfx_label.get_rect(center = (WIDTH/14*7, HEIGHT/10 * 3))
        self.display_surface.blit(sfx_label, sfx_rect)

        sfx_label = self.font.render("MUSIC", False, "white")
        sfx_rect = sfx_label.get_rect(center = (WIDTH/14*7, HEIGHT/10 * 4.4))
        self.display_surface.blit(sfx_label, sfx_rect)
        sfx_label = self.font.render(str(self.settings.music), False, "white")
        sfx_rect = sfx_label.get_rect(center = (WIDTH/14*7, HEIGHT/10 * 5))
        self.display_surface.blit(sfx_label, sfx_rect)

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = get_mouse_pos(self.display)
                # print(pos)
                for x in self.buttons:
                    if x.rect.collidepoint(pos):
                        # print("Clicked %s", x.type)
                        if x.type != "volume":
                            self.change_status(x.type)
                        else:
                            if x.displayed == "s+":
                                self.settings.set_sfx(10)
                            elif x.displayed == "s-":
                                self.settings.set_sfx(-10)
                            elif x.displayed == "m+":
                                self.settings.set_song(10)
                            elif x.displayed == "m-":
                                self.settings.set_song(-10)
     
class SettingsMenuPause:
    def __init__(self, surface, change_status, settings, display):
        self.settings = settings
        self.display = display
        self.display_surface = surface
        self.change_status = change_status
        self.buttons = pygame.sprite.Group()
        self.buttons.add(Button((WIDTH/2, HEIGHT/10 * 7), self.display_surface, "pause", metrics=(150,50), image="/buttons/back"))
        self.buttons.add(Button((WIDTH/14 * 5, HEIGHT/10 * 3), self.display_surface, "volume", "-", metrics=(50,50), image="/buttons/minus"))
        self.buttons.add(Button((WIDTH/14 * 9, HEIGHT/10 * 3), self.display_surface, "volume", "+", metrics=(50,50), image="/buttons/plus"))
        self.buttons.add(Button((WIDTH/14 * 5, HEIGHT/10 * 5), self.display_surface, "volume", "m-", metrics=(50,50), image="/buttons/minus"))
        self.buttons.add(Button((WIDTH/14 * 9, HEIGHT/10 * 5), self.display_surface, "volume", "m+", metrics=(50,50), image="/buttons/plus"))
        self.font = pygame.font.Font("./fonts/rexlia_rg.otf", 30)

    def show_menu(self, event_list):
        self.display_surface.fill((18,32,45))
        # self.buttons.draw(self.display_surface)
        for button in self.buttons.sprites():
            button.draw()

        sfx_label = self.font.render("SFX", False, "white")
        sfx_rect = sfx_label.get_rect(center = (WIDTH/14*7, HEIGHT/10 * 2.4))
        self.display_surface.blit(sfx_label, sfx_rect)

        sfx_label = self.font.render(str(self.settings.sfx), False, "white")
        sfx_rect = sfx_label.get_rect(center = (WIDTH/14*7, HEIGHT/10 * 3))
        self.display_surface.blit(sfx_label, sfx_rect)

        sfx_label = self.font.render("MUSIC", False, "white")
        sfx_rect = sfx_label.get_rect(center = (WIDTH/14*7, HEIGHT/10 * 4.4))
        self.display_surface.blit(sfx_label, sfx_rect)
        sfx_label = self.font.render(str(self.settings.music), False, "white")
        sfx_rect = sfx_label.get_rect(center = (WIDTH/14*7, HEIGHT/10 * 5))
        self.display_surface.blit(sfx_label, sfx_rect)

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = get_mouse_pos(self.display)
                # print(pos)
                for x in self.buttons:
                    if x.rect.collidepoint(pos):
                        # print("Clicked %s", x.type)
                        if x.type != "volume":
                            self.change_status(x.type)
                        else:
                            if x.displayed == "+":
                                self.settings.set_sfx(10)
                            elif x.displayed == "-":
                                self.settings.set_sfx(-10)
                            elif x.displayed == "m+":
                                self.settings.set_song(10)
                            elif x.displayed == "m-":
                                self.settings.set_song(-10)

class StartAbout:
    def __init__(self, surface, change_status, display):
        self.display_surface = surface
        self.display = display
        self.change_status = change_status
        self.buttons = pygame.sprite.Group()
        self.buttons.add(Button((WIDTH/10 * 8, HEIGHT/10 * 9), self.display_surface, "start_menu", metrics=(150,50), image="/buttons/back"))
        self.font = pygame.font.Font("./fonts/Calibri Regular.ttf", 15)
        
        self.text = []
        self.read_file()

    def read_file(self):
        with open('./licences.txt') as f:
            for line in f:
                self.text.append(line.strip())

    def show_menu(self, event_list):
        self.display_surface.fill((18,32,45))
        for button in self.buttons.sprites():
            button.draw()

        for i, line in enumerate(self.text):
            sfx_label = self.font.render(line, False, "white")
            sfx_rect = sfx_label.get_rect(midleft = (10, HEIGHT/len(self.text) * i +10))
            self.display_surface.blit(sfx_label, sfx_rect)

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = get_mouse_pos(self.display)
                # print(pos)
                for x in self.buttons:
                    if x.rect.collidepoint(pos):
                        # print("Clicked %s", x.type)
                        self.change_status(x.type)