import asyncio
import pygame

from menu import Menu

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if game_state=="Menu":
            game_state=menu.update(screen)
        clock.tick(60)
        pygame.display.flip()
        await asyncio.sleep(0)
asyncio.run(main())