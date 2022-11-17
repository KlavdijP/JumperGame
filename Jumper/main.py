import pygame, sys
from player import Player
from functions import *
from settings import *
from level import Level

pygame.init()

#BACKGROUND
# bg = load_image('./assets/bck.png', 500,800)

#PLAYER
# player = Player(WIDTH/5, 600)

#PLATFORMS
platforms = [[WIDTH/2-70/2,700, 70, 10]]

#ENEMIES
# enemy = pygame.transform.scale(pygame.image.load('./assets/enemy-fly1.png'), (100,100))
# enemy2 = pygame.transform.scale(pygame.image.load('./assets/enemy-stick1.png'), (100,150))


#GAME
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
level = Level(0, screen)
pygame.display.set_caption("Doodle Jumper")

while True:
    blocks = []

    level.run()
    # screen.blit(load_image('./assets/bck.png', 500,800), (0,0))
    # screen.fill('black')    
    # for i in range(len(platforms)):
    #     block = pygame.draw.rect(screen, (0, 0, 0), platforms[i])
    #     blocks.append(block)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(fps)