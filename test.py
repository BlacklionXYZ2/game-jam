from walls import Wall as wall
import pygame
pygame.init()
screen_x=800
screen_y=800
screen=pygame.display.set_mode([screen_x,screen_y])
wall1 = wall(0, 0, 'E')
print(wall1.rect[0])