import pygame
import glob

class NPCs(pygame.sprite.Sprite):
    def __init__(self, type, scene, items):
        super().__init__()

        self.frames = []
        if type == 'Alice':
            for frame in glob.glob('Static/Alice/*.png'):
                self.frames.append(pygame.image.load(frame).convert_alpha())

            if scene == 2:
                self.xpos = 75
                self.ypos = 325

                self.text = ["*mumble*",
                             "mmm... yes...",
                             "*mumble*... pot of greed... *mumble*",
                             "AH! When'd you get here!",
                             ""]

                if items[0] == 1:
                    self.text.remove(4)
                    self.text.append("Interested in my wares are you?",
                                     "Bring this item to the guy u just talked to",
                                     "You obtained an unnamed item", "")

            if scene == 4:
                self.xpos = 100
                self.ypos = 300
                self.text = ["I am Alice",
                             "how do i make a game out of that",
                             "i dont even know how to code a normal game", ""]

        elif type == 'Charlotte':
            for frame in glob.glob('Static/Character/walk_left/*.png'):
                self.frames.append(pygame.image.load(frame).convert_alpha())

            if scene == 3:
                self.xpos = 100
                self.ypos = 300
                self.text = ["I am Charlotte",
                             "how do i make a game out of that",
                             "i dont even know how to code a normal game", ""]

            if scene == 4:
                self.xpos = 100
                self.ypos = 300
                self.text = ["I am Charlotte",
                             "how do i make a game out of that",
                             "i dont even know how to code a normal game", ""]

        elif type == 'Elanor':
            for frame in glob.glob('Static/Elanor/*.png'):
                self.frames.append(pygame.image.load(frame).convert_alpha())

            if scene == 3:
                self.xpos = 100
                self.ypos = 300
                self.text = ["I am Elanor",
                             "how do i make a game out of that",
                             "i dont even know how to code a normal game", ""]

            if scene == 4:
                self.xpos = 100
                self.ypos = 300
                self.text = ["I am Elanor",
                             "how do i make a game out of that",
                             "i dont even know how to code a normal game", ""]

        elif type == 'Francis':
            for frame in glob.glob('Static/Character/walk_left/*.png'):
                self.frames.append(pygame.image.load(frame).convert_alpha())

            if scene == 2:
                self.xpos = 500
                self.ypos = 150
                self.text = ["I am Francis",
                             "how do i make a game out of that",
                             "i dont even know how to code a normal game", ""]

        elif type == 'Isabella':
            for frame in glob.glob('Static/Isabella/*.png'):
                self.frames.append(pygame.image.load(frame).convert_alpha())

            if scene == 2:
                self.xpos = 700
                self.ypos = 175
                self.text = ["I am Isabella",
                             "how do i make a game out of that",
                             "i dont even know how to code a normal game", ""]

            if scene == 3:
                self.xpos = 100
                self.ypos = 300
                self.text = ["I am Isabella",
                             "how do i make a game out of that",
                             "i dont even know how to code a normal game", ""]

        elif type == 'Jeffrey':
            for frame in glob.glob('Static/Character/walk_left/*.png'):
                self.frames.append(pygame.image.load(frame).convert_alpha())

            if scene == 4:
                self.xpos = 100
                self.ypos = 300
                self.text = ["I am Jeffrey",
                             "how do i make a game out of that",
                             "i dont even know how to code a normal game", ""]

        elif type == 'Oliver':
            for frame in glob.glob('Static/Character/walk_left/*.png'):
                self.frames.append(pygame.image.load(frame).convert_alpha())

            if scene == 2:
                self.xpos = 680
                self.ypos = 350
                self.text = ["I am oliver",
                             "how do i make a game out of that",
                             "i dont even know how to code a normal game", ""]

            if scene == 3:
                self.xpos = 100
                self.ypos = 300
                self.text = ["I am oliver",
                             "how do i make a game out of that",
                             "i dont even know how to code a normal game", ""]

            if scene == 4:
                self.xpos = 100
                self.ypos = 300
                self.text = ["I am oliver",
                             "how do i make a game out of that",
                             "i dont even know how to code a normal game", ""]

        elif type == 'Quirrel':
            for frame in glob.glob('Static/Character/walk_left/*.png'):
                self.frames.append(pygame.image.load(frame).convert_alpha())

        elif type == 'Theodore':
            for frame in glob.glob('Static/Character/walk_left/*.png'):
                self.frames.append(pygame.image.load(frame).convert_alpha())

            if scene == 3:
                self.xpos = 100
                self.ypos = 300
                self.text = ["I am Theodore",
                             "how do i make a game out of that",
                             "i dont even know how to code a normal game", ""]

        elif type == 'Todd':
            for frame in glob.glob('Static/Character/walk_left/*.png'):
                self.frames.append(pygame.image.load(frame).convert_alpha())

            if scene == 2:
                self.xpos = 100
                self.ypos = 175
                self.text = ["hey bud can ya help me",
                             "i want to learn about witchcraft and stuff",
                             "can ya go talk to her about it", ""]

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

    def update(self, items):
        self.animation()
        self.text_index