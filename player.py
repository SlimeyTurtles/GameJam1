import pygame
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
        if self.rect.top <= 75:
            self.rect.top = 75
        if self.rect.bottom >= 375:
            self.rect.bottom = 375
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= 800:
            self.rect.right = 800

    def update(self, dialogue):
        self.player_input(dialogue)
        self.boundaries()