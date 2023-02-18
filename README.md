    def draw_background(self, scroll):
        self.display_surface.blit(background, (0, 0 + scroll))
        self.display_surface.blit(background, (0, -1*HEIGHT + scroll))

    def run(self, event_list):
        if self.bck_scroll >= HEIGHT:
            self.bck_scroll = 0
        self.draw_background(self.bck_scroll)

    def stop_object(self, object):
        for sprite in object.sprites():
            sprite.speed = 0

    def move_object(self, object, speed):
        for sprite in object.sprites():
            sprite.speed = speed

    def objects_speed(self):
        player = self.player.sprite
        if player.rect.y > HEIGHT/2:
            self.stop_object(self.platforms)
            self.stop_object(self.pickups)
            self.stop_object(self.enemyFan)
        else:
            if player.direction.y < 0:
                speed = player.direction.y * -1
                self.move_object(self.platforms, speed)
                self.move_object(self.pickups, speed)
                self.move_object(self.enemyFan, speed)

                self.bck_scroll += speed



# Links
Menu buttons
https://www.freepik.com/free-vector/game-buttons-frames-sci-fi-style-design-elements-menu-assets-user-interface-vector-ca_19454303.htm#page=2&query=game%20menu%20button&position=0&from_view=keyword&track=ais

Background moving
https://www.youtube.com/watch?v=_E7kE3Zuf3A


# TODO
Sound
    Background music https://www.chosic.com/download-audio/45407/
    Enemy flying
    Platform break

Animations

New images, template, theme

Meniji (3x5*)
    Pause menu edit
    Start menu
    Settings menu

Progression
<!-- 
Level 1: Normal blocks no enemies
Level 2: Normal blocks enemies
Level 3: All blocks enemies
-->

# IN PROGRESS


# DONE
Enemies Upgrade enemy to odzivni agent s stanji Update stanja enemyAir

Platform generation

Bullet

name changes

Shooting Projectile In clicked direction | upwards

Kontrolni elementi grafičnega uporabniškega vmesnika (3x5*)
    1. Score 

1.1.2023 - Sound
    Jump
    Laser shoot
    Enemy dies
