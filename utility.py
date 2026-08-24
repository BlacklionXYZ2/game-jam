import pygame

colour={
    "black":(0, 0, 0),
    "white":(255, 255, 255),
    "red":(255, 0, 0),
    "green":(0, 255, 0),
    "blue":(0, 0, 255),
    "l_blue":(144, 213, 255),
    "yellow":(255, 255, 0),
    "d_grey":(120, 120, 120),
    "l_grey":(172, 172, 172),
    "pink":(255, 192, 203),
    "orange":(255, 165, 0),
    "purple":(128, 0, 128),
    "gold":(240, 183, 76),
    "brown":(165, 42, 42),
    "silver":(192, 192, 192),
    "bronze":(205, 127, 50),
    "d_green":(0, 128, 0)
}

def write_text(screen, location, text, colour, size, angle, draw_point):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, colour)
    angled_text=pygame.transform.rotate(text_surface, angle)
    text_rect = angled_text.get_rect()
    if draw_point=="center":
        text_rect.center = location
    elif draw_point=="topleft":
        text_rect.topleft = location 
    elif draw_point=="topright":
        text_rect.topright = location
    elif draw_point=="bottomleft":
        text_rect.bottomleft = location
    elif draw_point=="bottomright":
        text_rect.bottomright = location
    screen.blit(angled_text, text_rect)

def remove_value(iterable, value):
    while value in iterable:
        iterable.remove(value)
    return iterable

class Entity:
    def __init__(self, scale, pixels, pos, sprite, is_moveable):
        self.scale = scale
        self.pixels = pixels
        self.pos = pos
        self.sprite = sprite
        self.is_moveable = is_moveable