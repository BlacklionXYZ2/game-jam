import asyncio
import pygame
import torch

from utility import colour, write_text, remove_value
from menu import Menu
from player import Player
from walls import Wall

collision_entities = []

async def main():
    global collision_entities

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
            collision_entities.append(player)
            walls=[Wall(1, 0, "S"), Wall(0, 1, "E"), Wall(2, 1, "W"), Wall(1, 2, "N")]
            entities = walls.append(player)
            game_state="Game"

        elif game_state=="Game":
            screen.fill(colour["white"])
            player.update(screen, screen_x, screen_y, key)
            for i in walls:
                i.draw(screen, player.pos, screen_x, screen_y, player.scale, player.pixels)
            if mouse_click:
                game_state="Menu"
            check_collisions(entities)

        else:
            screen.fill(colour["black"])
            write_text(screen, (400, 400), "game state not found", colour["white"], 64, 0, "center")

            if mouse_click:
                game_state="Menu"

        clock.tick(60)
        pygame.display.flip()
        await asyncio.sleep(0)

asyncio.run(main())

def check_collisions(entities):
    num_ents = len(entities)
    max = torch.zeros((num_ents, 2))
    min = torch.zeros((num_ents, 2))

    for obj, idx in enumerate(entities):
        if type(obj) == Wall:
            min[idx, :] = [obj.rect[0], obj.rect[1]]
            max[idx, :] = [obj.rect[0] + obj.pixels, obj.rect[1] + obj.pixels]
        elif type(obj) == Player:
            min[idx, :] = obj.pos
            max[idx, :] = obj.pos + obj.pixels

    max_A = max.unsqueeze(1)
    min_A = min.unsqueeze(1)
    max_B = max.unsqueeze(0)
    min_B = min.unsqueeze(0)

    overlap = (max_A > min_B) & (max_B > min_A)
    overlap_mask = torch.all(overlap, dim = 2)
    collisions = overlap_mask & torch.triu(torch.ones(num_ents, num_ents), dtype = torch.bool)
    index_A, index_B = torch.where(collisions)

    collision_list = [(entities[x], entities[y]) for x, y in zip(index_A.tolist(), index_B.tolist())]
    player_collisions = [pair if any(collision_entities) in pair else None for pair in collision_list]
    remove_value(player_collisions, None)

    return player_collisions