WIDTH = 500
HEIGHT = 1000
fps = 60

import pygame

class Settings:
    def __init__(self):
        self.music = 100
        self.sfx = 10

    def set_music(self, volume):
        self.music += volume
        if self.music < 0:
            self.music = 0
        elif self.music > 100:
            self.music = 100

    def set_sfx(self, volume):
        self.sfx += volume
        if self.sfx < 0:
            self.sfx = 0
        elif self.sfx > 100:
            self.sfx = 100

        print(self.sfx)

    def enemy_air_die(self):
        sound = pygame.mixer.Sound("./audio/enemy_dies.wav")
        sound.set_volume(self.sfx/1000)
        sound.play()
    
    def player_jump(self):
        sound = pygame.mixer.Sound("./audio/jump.wav")
        sound.set_volume(self.sfx/1000)
        sound.play()
    
    def player_shoot(self):
        sound = pygame.mixer.Sound("./audio/shoot.wav")
        sound.set_volume(self.sfx/1000)
        sound.play()