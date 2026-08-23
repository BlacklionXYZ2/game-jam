import asyncio
import pygame

from utility import colour, write_text
async def main():
    pygame.init()
    screen_x=800
    screen_y=800
    screen=pygame.display.set_mode([screen_x,screen_y])
    clock = pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(colour["white"])
        write_text(screen, (0,0), "hi", colour["black"], 48, 0)
        clock.tick(60)
        pygame.display.flip()
        await asyncio.sleep(0)
asyncio.run(main())