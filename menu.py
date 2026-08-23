import pygame

from utility import colour, write_text
from buttons import Button

class Menu:
    def __init__(self):
        self.menu_type="Main"
        self.buttons={
            "Main":[
                Button((300, 200), (200, 100),colour["l_blue"], "Play", colour["black"], 48), 
                Button((300, 350), (200, 100),colour["l_blue"], "Tutorial", colour["black"], 48), 
                Button((300, 500), (200, 100),colour["l_blue"], "Settings", colour["black"], 48),
                Button((300, 650), (200, 100),colour["l_blue"], "Credits", colour["black"], 48)
                ],
            "Settings":[],
            "Credits":[],
        }
    def update(self, screen):
        self.draw(screen)
        clicked_button=self.check_buttons()
        if clicked_button:
            if clicked_button.text=="Play":
                return "Game"
            elif clicked_button.text=="Tutorial":
                return "Tutorial"
            elif clicked_button.text=="Settings":
                self.menu_type="Settings"
            elif clicked_button.text=="Credits":
                self.menu_type="Credits"
        return "Menu"

    def draw(self, screen):
        screen.fill(colour["white"])
        self.draw_buttons(screen)
        if self.menu_type=="Main":
            self.draw_main(screen)
        elif self.menu_type=="Settings":
            self.draw_settings(screen)
        elif self.menu_type=="Credits":
            self.draw_credits(screen)
    
    def draw_main(self, screen):
        write_text(screen, (400, 100), "Title", colour["black"], 128, 0, "center")

    def draw_settings(self, screen):
        write_text(screen, (400, 100), "Settings", colour["black"], 128, 0, "center")

    def draw_credits(self, screen):
        write_text(screen, (400, 100), "Credits", colour["black"], 128, 0, "center")

    def check_buttons(self):
        for i in self.buttons[self.menu_type]:
            if i.clicked():
                return i
        return False

    def draw_buttons(self, screen):
        above=False
        for i in self.buttons[self.menu_type]:
            i.draw(screen)
            if i.above():
                above=True
        if above:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
