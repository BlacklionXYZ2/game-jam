import pygame

from sprite import Sprite

class Player:
    def __init__(self):
        self.pos=pygame.math.Vector2()
        self.sprite=Sprite("player_sprite.png", 32, 32, [2, 2, 2, 2, 2, 2, 2, 2], [10, 10, 10, 10, 10, 10, 10, 10])
        self.speed=2
        

    def move(self, key):
        direction=pygame.math.Vector2()
        direction+=pygame.math.Vector2(0,-1)*key[pygame.K_w]
        direction+=pygame.math.Vector2(-1,0)*key[pygame.K_a]
        direction+=pygame.math.Vector2(0,1)*key[pygame.K_s]
        direction+=pygame.math.Vector2(1,0)*key[pygame.K_d]
        
        if direction!=pygame.math.Vector2():
            direction=direction.normalize()
            animation=int((direction.as_polar()[1]/45+2)%8)
            if animation!=self.sprite.animation_num:
                self.sprite.change_animation(animation)
        
        self.pos+=direction*self.speed
        
        

    def draw(self,screen):
        self.sprite.draw(screen, self.pos, 3)

    def update(self, screen, key):
        self.move(key)
        self.draw(screen)
        self.sprite.update()

