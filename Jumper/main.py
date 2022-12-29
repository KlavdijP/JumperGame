import pygame, sys
from player import Player
from functions import *
from settings import *
from level import Level
from ui import UI
from pause_menu import PauseMenu

pygame.init()
#GAME

class Game:
    def __init__(self):
        self.status = "ingame"
        
        self.score = 0
        self.level = Level(0,screen, self.update_score)
        self.ui = UI(screen)
        self.pause_menu = PauseMenu(screen)

        self.font = pygame.font.Font("./fonts/rexlia_rg.otf", 30)        #Score

    def run(self, event_list):
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p and self.status == "ingame":
                    self.status="pause"
                elif event.key == pygame.K_p and self.status == "pause":
                    self.status="ingame"
        
        if self.status == "ingame":
            self.level.run(event_list)
            self.ui.show_score(self.score)
        elif self.status == "pause":
            self.pause_menu.show_pause_menu()

    def update_score(self, amount):
        self.score += amount

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
game = Game()
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