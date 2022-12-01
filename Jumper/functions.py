import pygame

def load_image(src, sc1, sc2):
    return pygame.transform.scale(pygame.image.load("./assets/" + src), (sc1, sc2))