import asyncio
import pygame

from utility import colour, write_text
from menu import Menu
from player import Player

async def main():

    pygame.init()

    screen_x=800
    screen_y=800
    screen=pygame.display.set_mode([screen_x,screen_y])

    game_state="Menu"
    menu=Menu()
    player=Player()

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

        elif game_state=="Game":
            screen.fill(colour["white"])
            player.update(screen, key)


        else:
            screen.fill(colour["black"])
            write_text(screen, (400, 400), "game state not found", colour["white"], 64, 0, "center")

            if mouse_click:
                game_state="Menu"

        clock.tick(60)
        pygame.display.flip()
        await asyncio.sleep(0)

asyncio.run(main())
