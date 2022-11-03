import pygame
from player import Player

pygame.init()

WIDTH = 500
HEIGHT = 800

#BACKGROUND
bg = pygame.transform.scale(pygame.image.load('./assets/bck.png'), (500,800))


#PLAYER
player = Player(50,50)


#PLATFORMS
platforms = [[150,30, 100, 400]]

#ENEMIES
enemy = pygame.transform.scale(pygame.image.load('./assets/enemy-fly1.png'), (100,100))
enemy2 = pygame.transform.scale(pygame.image.load('./assets/enemy-stick1.png'), (100,150))


#GAME
fps = 60
timer = pygame.time.Clock()
screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption("Doodle Jumper")

running = True

while running:
    timer.tick(fps)
    screen.blit(bg, (0,0))
    screen.blit(player.image, (160, 250))
    screen.blit(enemy, (0,0))
    screen.blit(enemy2, (300,300))

    for plaftorm in platforms:
        screen.blit(pygame.transform.scale(pygame.image.load('./assets/normal-block.png'), (plaftorm[0],plaftorm[1])), (plaftorm[2], plaftorm[3]))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()