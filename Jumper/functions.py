import pygame

def load_image(src, sc1, sc2, flipped=False):
    if flipped:
        return pygame.transform.flip(pygame.transform.scale(pygame.image.load("./assets/" + src + ".png"), (sc1, sc2)), True, False)
    return pygame.transform.scale(pygame.image.load("./assets/" + src + ".png"), (sc1, sc2))