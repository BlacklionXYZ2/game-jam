import pygame
import torch

from sprite import Sprite
from utility import Entity

class Player(Entity):
    def __init__(self):
        # self.sprite=Sprite("temp_player_sprite.png", self.pixels, self.pixels, [2, 2, 2, 2, 2, 2, 2, 2], [10, 10, 10, 10, 10, 10, 10, 10], 0)
        self.sprite=Sprite("player_spritesheet.png", self.pixels, self.pixels, [1, 1, 1, 1], [10, 10, 10, 10], 0)
        self.speed=2
        super().__init__(scale = 3, pixels = 16, pos = torch.zeros(2), sprite = self.sprite)

    def get_rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.pixels, self.pixels)
        

    def move(self, key):
        direction=torch.zeros(2)
        direction+=torch.tensor((0,-1))*key[pygame.K_w]
        direction+=torch.tensor((-1,0))*key[pygame.K_a]
        direction+=torch.tensor((0,1))*key[pygame.K_s]
        direction+=torch.tensor((1,0))*key[pygame.K_d]
        
        if direction!=torch.tensor():
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
