import pygame
from sys import exit
from sprite_sheet import Spritesheet
from npcs import NPCs
from player import Player

# initialization shenanigans
pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('GameJam1 Avinh')
clock = pygame.time.Clock()
text_font = pygame.font.Font(None, 50)

dialogue = False
scene = 2
items = [0, 0, 0, 0, 0, 0, 0, 0, 0]
energy = 5

# Groups

player = pygame.sprite.GroupSingle()
player.add(Player())

npc_group = pygame.sprite.Group()

# Objects

inventory_surf = pygame.Surface((800, 125))
inventory_surf.fill('Red')

text_surface = text_font.render('My game', False, 'Green')
text = ''

# Initializing Sprite Sheets

buildings_spritesheet = Spritesheet('./Static/buildings_sprite_sheet.png')
terrain_spritesheet = Spritesheet('./Static/tiles.png')

# game loop
while True:

    screen.fill((175, 175, 255))

    if scene == 0:
        while scene == 0:  # Home
            floor = buildings_spritesheet.get_sprite(160, 144, 16, 50)
            floor = pygame.transform.scale(floor, (500, 500))
            screen.blit(floor, (0, 0))

            screen.blit(inventory_surf, (0, 375))
            screen.blit(text_font.render(text, False, 'Green'), (0, 375))

            npc_group.draw(screen)
            npc_group.update()

            player.draw(screen)
            player.update(dialogue)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if pygame.sprite.spritecollide(player.sprite, npc_group, False):
                        dialogue = True
                        character = pygame.sprite.spritecollide(player.sprite, npc_group, False)[0]
                        text = character.dialogue()
                        if character.text_index >= len(character.text)-1:
                            dialogue = False

            pygame.display.update()
            clock.tick(60)

    elif scene == 1:
        while scene == 1:  # Home
            floor = pygame.image.load('Static/Scene_1.png').convert()
            floor = pygame.transform.scale(floor, (800, 375))
            screen.blit(floor, (0, 0))

    elif scene == 2:
        npc_group.empty()
        npc_group.add(
            NPCs('Oliver', 2, items),
            NPCs('Todd', 2, items),
            NPCs('Isabella', 2, items),
            NPCs('Francis', 2, items),
            NPCs('Alice', 2, items)
        )

        while scene == 2:
            floor = pygame.image.load('./Static/Scene_2.png').convert()
            floor = pygame.transform.scale(floor, (800, 375))
            screen.blit(floor, (0, 0))

            screen.blit(inventory_surf, (0, 375))
            screen.blit(text_font.render(text, False, 'Green'), (0, 375))

            npc_group.draw(screen)
            npc_group.update(items)

            player.draw(screen)
            player.update(dialogue, items)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if pygame.sprite.spritecollide(player.sprite, npc_group, False):
                        dialogue = True
                        character = pygame.sprite.spritecollide(player.sprite, npc_group, False)[0]
                        text = character.dialogue()

                        if text == "hey bud can ya help me":
                            energy -= 1
                            items[0] == 1

                        if text == "you obtained an unnamed item":
                            energy -= 1
                            print(energy)

                        if character.text_index >= len(character.text)-1:
                            dialogue = False

            if energy <= 0:
                energy = 5
                scene += 1

            pygame.display.update()
            clock.tick(60)

    elif scene == 3:
        npc_group.empty()
        npc_group.add(
            NPCs('Oliver', 3, items),
            NPCs('Theodore', 3, items),
            NPCs('Isabella', 3, items),
            NPCs('Charlotte', 3, items),
            NPCs('Elanor', 3, items)
        )

        while scene == 3:
            floor = pygame.image.load('./Static/Scene_3.png').convert()
            floor = pygame.transform.scale(floor, (800, 375))
            screen.blit(floor, (0, 0))

            screen.blit(inventory_surf, (0, 375))
            screen.blit(text_font.render(text, False, 'Green'), (0, 375))

            npc_group.draw(screen)
            npc_group.update()

            player.draw(screen)
            player.update(dialogue)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if pygame.sprite.spritecollide(player.sprite, npc_group, False):
                        dialogue = True
                        character = pygame.sprite.spritecollide(player.sprite, npc_group, False)[0]
                        text = character.dialogue()
                        if character.text_index >= len(character.text)-1:
                            dialogue = False

            if energy <= 0:
                energy = 5
                scene += 1

            pygame.display.update()
            clock.tick(60)

    elif scene == 4:
        npc_group.empty()
        npc_group.add(
            NPCs('Oliver', 4, items),
            NPCs('Jeffrey', 4, items),
            NPCs('Alice', 4, items),
            NPCs('Charlotte', 4, items),
            NPCs('Elanor', 4, items)
        )

        while scene == 4:  # Period 2
            floor = pygame.image.load('./Static/Scene_4.png').convert()
            floor = pygame.transform.scale(floor, (800, 300))
            screen.blit(floor, (0, 75))

            tree = terrain_spritesheet.get_sprite(32, 384, 43, 32)
            tree = pygame.transform.scale(tree, (150, 2000))

            tree_x = -35
            while tree_x < 800:
                screen.blit(tree, (tree_x, -55))
                tree_x += 130

            tree_x = -100
            while tree_x < 800:
                screen.blit(tree, (tree_x, -50))
                tree_x += 130

            screen.blit(inventory_surf, (0, 375))
            screen.blit(text_font.render(text, False, 'Green'), (0, 375))

            npc_group.draw(screen)
            npc_group.update()

            player.draw(screen)
            player.update(dialogue)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if pygame.sprite.spritecollide(player.sprite, npc_group, False):
                        dialogue = True
                        character = pygame.sprite.spritecollide(player.sprite, npc_group, False)[0]
                        text = character.dialogue()
                        if character.text_index >= len(character.text)-1:
                            dialogue = False

            pygame.display.update()
            clock.tick(60)