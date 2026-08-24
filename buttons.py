import pygame

from utility import write_text

class Button:
    def __init__(self, pos, size, colour1, colour2, text, text_colour, text_size):
        self.rect=pygame.Rect(pos, size)
        self.colour1=colour1
        self.colour2=colour2
        self.colour=self.colour1
        self.text=text
        self.text_colour=text_colour
        self.text_size=text_size

    def above(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def swap_colour(self):
        if self.colour==self.colour1:
            self.colour=self.colour2
        else:
            self.colour=self.colour1

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.rect, border_radius=int(min(self.rect.height, self.rect.width) / 4))
        write_text(screen, self.rect.center, self.text, self.text_colour, self.text_size, 0, "center")
