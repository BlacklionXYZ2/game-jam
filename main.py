import asyncio
import pygame

from utility import colour, write_text
from menu import Menu
from player import Player
from walls import Wall

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
            walls=[Wall(1, 0, "S"), Wall(0, 1, "E"), Wall(2, 1, "W"), Wall(1, 2, "N")]
            game_state="Game"

        elif game_state=="Game":
            screen.fill(colour["white"])
            player.update(screen, screen_x, screen_y, key)
            for i in walls:
                i.draw(screen, player.pos, screen_x, screen_y, player.scale, player.pixles)
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
