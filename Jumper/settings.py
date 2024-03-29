import pygame

WIDTH = 500
HEIGHT = 700
fps = 60

import pygame

class Settings:
    def __init__(self):
        self.music = 0
        self.sfx = 100

        self.enemyAirDie = pygame.mixer.Sound("./audio/enemy_dies.wav")
        self.playerJump = pygame.mixer.Sound("./audio/jump.wav")
        self.playerShoot = pygame.mixer.Sound("./audio/shoot.wav")
        self.enemyFan = pygame.mixer.Sound("./audio/fan.wav")
        self.glassBreak = pygame.mixer.Sound("./audio/glass_breaks.wav")
        self.song = pygame.mixer_music.load("./audio/music.wav")

    def set_song(self, volume):
        self.music += volume
        if self.music < 0:
            self.music = 0
        elif self.music > 100:
            self.music = 100
        pygame.mixer.music.set_volume(self.music/100)


    def set_sfx(self, volume):
        self.sfx += volume
        if self.sfx < 0:
            self.sfx = 0
        elif self.sfx > 100:
            self.sfx = 100

        # print(self.sfx)
    
    def start_song(self):
        pygame.mixer.music.play(-1)

    def enemy_air_die(self):
        self.enemyAirDie.set_volume(self.sfx/100)
        self.enemyAirDie.play()
    
    def player_jump(self):
        self.playerJump.set_volume(self.sfx/100)
        self.playerJump.play()
    
    def player_shoot(self):
        self.playerShoot.set_volume(self.sfx/100)
        self.playerShoot.play()
    
    def enemy_fan(self):
        self.enemyFan.set_volume(self.sfx/100)
        self.enemyFan.play()
    
    def enemy_fan_stop(self):
        self.enemyFan.stop()

    def glass_break(self):
        self.glassBreak.set_volume(self.sfx/100)
        self.glassBreak.play()