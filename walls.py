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

    "E":(0,2),
    "light_E":(1,2),
    "fade_bot_E":(2,2),
    "fade_top_E":(3,2),

    "N":(0,3),
    "dark_N":(1,3),
    "fade_bot_N":(2,3),
    "fade_top_N":(3,3),

    "S":(0,4),
    "dark_S":(1,4),
    "fade_bot_S":(2,4),
    "fade_top_S":(3,4),

    "W":(0,5),
    "dark_W":(1,5),
    "fade_bot_W":(2,5),
    "fade_top_W":(3,5)
}


class Wall:
    def __init__(self, x, y, texture):
        self.scale=8
        self.pixles=16
        self.rect=pygame.Rect(x*self.pixles*self.scale, y*self.pixles*self.scale, self.pixles*self.scale, self.pixles*self.scale,)
        self.sprite=Sprite("walls_spritesheet.png", self.pixles, self.pixles, [4, 4, 4, 4, 4, 4], [1, 1, 1, 1, 1, 1], wall_textue_names[texture][1])
        self.sprite.change_frame(wall_textue_names[texture][0])
        
    def draw(self, screen, player_pos, screen_x, screen_y, player_scale, player_pixles):
        if self.is_on_screen(player_pos, screen_x, screen_y):#draw-actual=offset
            draw_pos=(screen_x/2-(player_pixles/2)*player_scale-player_pos.x+self.rect.left, screen_y/2-(player_pixles/2)*player_scale-player_pos.y+self.rect.top)
            self.sprite.draw(screen, draw_pos, self.scale)   #screen_x-16*scale, screen_y-16*scale
    def is_on_screen(self, player_pos, screen_x, screen_y):
        return True
        return self.rect.x<player_pos.x-screen_x/2-self.scale and self.rect.x>player_pos.x+screen_x/2 and self.rect.y<player_pos.y-screen_y/2-self.scale and  self.rect.y>player_pos.y+screen_y/2

