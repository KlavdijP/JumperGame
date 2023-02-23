import pygame, sys
from player import Player
from functions import *
from settings import *
from level import Level
from ui import UI
from menus import PauseMenu, StartMenu, SettingsMenuMenu, SettingsMenuPause, ShopMenu


pygame.init()
#GAME

class Game:
    def __init__(self, settings):
        self.player_name = ""
        self.status = "start_menu"
        self.settings = settings
        self.level = Level(screen, self.settings, self.change_status, display)
        self.new_player()
        self.start_menu = StartMenu(screen, self.change_status, display)
        self.shop_menu = ShopMenu(screen, self.change_status, display)
        self.pause_menu = PauseMenu(screen, self.change_status, display)
        self.settings_menu_menu = SettingsMenuMenu(screen, self.change_status, settings, display)
        self.settings_menu_pause = SettingsMenuPause(screen, self.change_status, settings, display)
        self.money = 0
        self.builds = 0
        self.timer = 0

    def new_player(self):
        data = return_json_data()
        self.builds = data["builds"]
        self.money = 0
    
    def mining(self):
        self.money += self.builds * 0.0003
        self.timer += 1
        if self.timer > 60:
            self.timer = 0
            self.save_earning()
            self.new_player()

    def save_earning(self):
        # print(self.money)
        update_stock("money", self.money)

    def run(self, event_list): 
        ## MINING BITCOIN
        self.mining()
        # Rigs running at all time
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p and self.status == "play":
                    self.status="pause"
                elif event.key == pygame.K_p and self.status == "pause":
                    self.status="play"
        if self.status == "play":
            self.level.run(event_list)
        elif self.status == "pause":
            self.pause_menu.show_menu(event_list)
        elif self.status == "start_menu":
            self.level.end()
            self.start_menu.show_menu(event_list)
        elif self.status == "settings_menu":
            self.settings_menu_menu.show_menu(event_list)
        elif self.status == "shop_menu":
            self.shop_menu.update()
            self.shop_menu.show_menu(event_list)
        elif self.status == "settings_pause":
            self.settings_menu_pause.show_menu(event_list)
        elif self.status == "newgame":
            self.new_game()
        elif self.status == "exit":
            pygame.quit()
            sys.exit()

    def change_status(self, new_status):
        self.status = new_status
        if self.status == "start_menu":
            self.start_menu.update_score()
    
    def new_game(self):
        self.level = Level(screen, self.settings, self.change_status, display)
        self.status = "play"

display = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
screen = pygame.Surface((WIDTH, HEIGHT))
clock = pygame.time.Clock()
settings = Settings()
game = Game(settings)
pygame.display.set_caption("SKYFRIK")

while True:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    game.run(event_list)

    display.blit(pygame.transform.scale(screen, (display.get_width(), display.get_height())), (0, 0))
    pygame.display.update()
    clock.tick(fps)