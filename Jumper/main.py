import pygame, sys
from player import Player
from functions import *
from settings import *
from level import Level
from ui import UI
from menus import PauseMenu, StartMenu, SettingsMenuMenu, SettingsMenuPause

pygame.init()
#GAME

class Game:
    def __init__(self, settings):
        self.status = "start_menu"
        self.settings = settings
        self.level = Level(screen, self.settings, self.change_status)

        self.start_menu = StartMenu(screen, self.change_status)
        self.pause_menu = PauseMenu(screen, self.change_status)
        self.settings_menu_menu = SettingsMenuMenu(screen, self.change_status, settings)
        self.settings_menu_pause = SettingsMenuPause(screen, self.change_status, settings)
        
    def run(self, event_list):
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
            self.start_menu.show_menu(event_list)
        elif self.status == "settings_menu":
            self.settings_menu_menu.show_menu(event_list)
        elif self.status == "settings_pause":
            self.settings_menu_pause.show_menu(event_list)
        elif self.status == "newgame":
            self.new_game()

    def change_status(self, new_status):
        self.status = new_status
    
    def new_game(self):
        # self.score = 0
        self.level = Level(screen, self.settings, self.change_status)
        self.status = "play"

screen = pygame.display.set_mode((WIDTH,HEIGHT))
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

    pygame.display.update()
    clock.tick(fps)