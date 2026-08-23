import pygame

from utility import write_text

class Button:
    def __init__(self, pos, size, colour, text, text_colour, text_size):
        self.rect=pygame.Rect(pos, size)
        self.colour=colour
        self.text=text
        self.text_colour=text_colour
        self.text_size=text_size

    def above(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())
    
    def clicked(self):
        return self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed(3)[0]

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.rect, border_radius=int(min(self.rect.height, self.rect.width) / 4))
        write_text(screen, self.rect.center, self.text, self.text_colour, self.text_size, 0, "center")