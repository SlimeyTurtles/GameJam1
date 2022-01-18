import pygame
from sys import exit
import glob

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_walk_right = []
        self.player_walk_left = []
        self.player_walk = self.player_walk_left
        for player_frame in glob.glob('Static/Character/walk_right/*.png'):
            self.player_walk_right.append(pygame.image.load(player_frame).convert_alpha())
        for player_frame in glob.glob('Static/Character/walk_left/*.png'):
            self.player_walk_left.append(pygame.image.load(player_frame).convert_alpha())

        self.player_index = 0

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (300, 400))

    def player_input(self, dialogue):
        keys = pygame.key.get_pressed()
        if not dialogue:
            if keys[pygame.K_UP]:
                self.rect.y -= 4
            if keys[pygame.K_DOWN]:
                self.rect.y += 4
            if keys[pygame.K_LEFT]:
                self.rect.x -= 4
                self.player_walk = self.player_walk_left
            if keys[pygame.K_RIGHT]:
                self.rect.x += 4
                self.player_walk = self.player_walk_right
            if keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                self.player_index += 0.2
                if self.player_index >= len(self.player_walk): self.player_index = 0
                self.image = self.player_walk[int(self.player_index)]

    def boundaries(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 375:
            self.rect.bottom = 375
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= 800:
            self.rect.right = 800

    def update(self, dialogue):
        self.player_input(dialogue)
        self.boundaries()

class NPCs(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        self.frames = []
        if type == 'cat':
            for frame in glob.glob('Static/Character/walk_left/*.png'):
                self.frames.append(pygame.image.load(frame).convert_alpha())
            self.xpos = 100
            self.ypos = 300
            self.text = ["cat1", "cat2", "cat3"]
        elif type == 'dog':
            for frame in glob.glob('Static/Character/walk_left/*.png'):
                self.frames.append(pygame.image.load(frame).convert_alpha())
            self.xpos = 200
            self.ypos = 200
            self.text = ["dog1", "dog2", "dog3"]
        else:
            for frame in glob.glob('Static/Character/walk_left/*.png'):
                self.frames.append(pygame.image.load(frame).convert_alpha())
            self.xpos = 300
            self.ypos = 300
            self.text = ["fish1", "fish2", "fish3"]

        self.text_index = -1
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (self.xpos, self.ypos))

    def animation(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def dialogue(self):
        self.text_index += 1
        if self.text_index > len(self.text)-1: self.text_index = 0
        return self.text[self.text_index]

    def update(self):
        self.animation()
        self.text_index


pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('GameJam1 Avinh')
clock = pygame.time.Clock()
text_font = pygame.font.Font(None, 50)
dialogue = False

# objects

player = pygame.sprite.GroupSingle()
player.add(Player())

npc = pygame.sprite.Group()

npc.add(NPCs('cat'))
cat = NPCs('cat')

npc.add(NPCs('dog'))
dog = NPCs('dog')

npc.add(NPCs('fish'))
fish = NPCs('fish')

inventory_surf = pygame.Surface((800, 125))
inventory_surf.fill('Red')

text_surface = text_font.render('My game', False, 'Green')
text = ''

# game loop
while True:

    screen.blit(inventory_surf, (0, 375))

    screen.blit(text_font.render(text, False, 'Green'), (0, 375))

    player.draw(screen)
    player.update(dialogue)

    npc.draw(screen)
    npc.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if pygame.sprite.spritecollide(player.sprite, npc, False):
                dialogue = True
                character = pygame.sprite.spritecollide(player.sprite, npc, False)[0]
                text = character.dialogue()
                if character.text_index >= len(character.text)-1:
                    dialogue = False

    pygame.display.update()
    clock.tick(60)