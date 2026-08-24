import pygame

from sprite import Sprite

class Player:
    def __init__(self):
        self.pos=pygame.math.Vector2()
        self.pixles=16
        # self.sprite=Sprite("temp_player_sprite.png", self.pixles, self.pixles, [2, 2, 2, 2, 2, 2, 2, 2], [10, 10, 10, 10, 10, 10, 10, 10], 0)
        self.sprite=Sprite("player_spritesheet.png", self.pixles, self.pixles, [1, 1, 1, 1], [10, 10, 10, 10], 0)
        self.speed=2
        self.scale=3
        

    def move(self, key):
        direction=pygame.math.Vector2()
        direction+=pygame.math.Vector2(0,-1)*key[pygame.K_w]
        direction+=pygame.math.Vector2(-1,0)*key[pygame.K_a]
        direction+=pygame.math.Vector2(0,1)*key[pygame.K_s]
        direction+=pygame.math.Vector2(1,0)*key[pygame.K_d]
        
        if direction!=pygame.math.Vector2():
            direction=direction.normalize()
            animation=int((direction.as_polar()[1]/45+2)%8//2)
            if animation!=self.sprite.animation_num:
                self.sprite.change_animation(animation)
        
        self.pos+=direction*self.speed
        
        

    def draw(self,screen, screen_x, screen_y):
        self.sprite.draw(screen, (screen_x/2-16*self.scale, screen_y/2-16*self.scale), self.scale)

    def update(self, screen, screen_x, screen_y, key):
        self.move(key)
        self.draw(screen, screen_x, screen_y)
        self.sprite.update()

