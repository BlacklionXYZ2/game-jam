import asyncio
import pygame

from utility import colour, write_text
from menu import Menu
from player import Player
from walls import Wall
from sprite import Sprite

async def main():

    pygame.init()

    screen_x=800
    screen_y=800
    screen=pygame.display.set_mode([screen_x,screen_y])

    game_state="Menu"
    menu=Menu()


    clock = pygame.time.Clock()

    running=True

    while running:
        mouse_click=False
        key=pygame.key.get_pressed()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    mouse_click=True

        if game_state=="Menu":
            game_state=menu.update(screen, mouse_click)

        elif game_state=="Pre-Game":
            player=Player()
            background=Sprite("background.png", 144, 144, [1], [1], 0)
            walls=[Wall(1, 0, "dark_S"), Wall(0, 1, "dark_E"), Wall(2, 1, "dark_W"), Wall(1, 2, "dark_N"), Wall(0, 0, "dark_SE"), Wall(2, 0, "dark_SW"), Wall(0, 2, "dark_NE"), Wall(2, 2, "dark_NW")]
            game_state="Game"

        elif game_state=="Game":
            screen.fill(colour["white"])
            player.update(key)
            background.draw(screen,(-(player.pos.x%128), -(player.pos.y%128)), 8)
            player.draw(screen, screen_x, screen_y)
            for i in walls:
                i.draw(screen, player.pos, screen_x, screen_y, player.scale, player.pixels)
            if mouse_click:
                game_state="Menu"

        else:
            screen.fill(colour["black"])
            write_text(screen, (400, 400), "game state not found", colour["white"], 64, 0, "center")

            if mouse_click:
                game_state="Menu"

        clock.tick(60)
        pygame.display.flip()
        await asyncio.sleep(0)

asyncio.run(main())
