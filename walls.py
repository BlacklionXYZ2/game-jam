import pygame

from sprite import Sprite

wall_textue_names={
    "dark_NE":(0,0),
    "dark_NW":(1,0),
    "dark_SE":(2,0),
    "dark_SW":(3,0),

    "light_NE":(0,1),
    "light_NW":(1,1),
    "light_SE":(2,1),
    "light_SW":(3,1),

    "dark_E":(0,2),
    "light_E":(1,2),
    "fade_bot_E":(2,2),
    "fade_top_E":(3,2),

    "dark_N":(0,3),
    "light_N":(1,3),
    "fade_bot_N":(2,3),
    "fade_top_N":(3,3),

    "dark_S":(0,4),
    "light_S":(1,4),
    "fade_bot_S":(2,4),
    "fade_top_S":(3,4),

    "dark_W":(0,5),
    "light_W":(1,5),
    "fade_bot_W":(2,5),
    "fade_top_W":(3,5)
}


class Wall:
    def __init__(self, x, y, texture):
        self.scale=8
        self.pixels=16
        self.rect=pygame.Rect(x*self.pixels*self.scale, y*self.pixels*self.scale, self.pixels*self.scale, self.pixels*self.scale,)
        self.sprite=Sprite("walls_spritesheet.png", self.pixels, self.pixels, [4, 4, 4, 4, 4, 4], [1, 1, 1, 1, 1, 1], wall_textue_names[texture][1])
        self.sprite.change_frame(wall_textue_names[texture][0])
        
    def draw(self, screen, player_pos, screen_x, screen_y, player_scale, player_pixels):
        if self.is_on_screen(player_pos, screen_x, screen_y):#draw-actual=offset
            draw_pos=(screen_x/2-(player_pixels/2)*player_scale-player_pos.x+self.rect.left, screen_y/2-(player_pixels/2)*player_scale-player_pos.y+self.rect.top)
            self.sprite.draw(screen, draw_pos, self.scale)   #screen_x-16*scale, screen_y-16*scale
    def is_on_screen(self, player_pos, screen_x, screen_y):
        return True
        return self.rect.x<player_pos.x-screen_x/2-self.scale and self.rect.x>player_pos.x+screen_x/2 and self.rect.y<player_pos.y-screen_y/2-self.scale and  self.rect.y>player_pos.y+screen_y/2

