from pico2d import *


class Skill__W:
    def __init__(self):
        self.x, self.y = 100, 550
        self.image = load_image('resource/skill/skill_water.png')

    def draw(self):
        self.image.draw(self.x, self.y)


class Skill__L:
    def __init__(self):
        self.x, self.y = 140, 550
        self.image = load_image('resource/skill/skill_lightning.png')

    def draw(self):
        self.image.draw(self.x, self.y)


class Skill__F:
    def __init__(self):
        self.x, self.y = 180, 550
        self.image = load_image('resource/skill/skill_water.png')


    def draw(self):
        self.image.draw(self.x, self.y)


class Skill__E:
    def __init__(self):
        self.x, self.y = 220, 550
        self.image = load_image('resource/skill/skill_earth.png')


    def draw(self):
        self.image.draw(self.x, self.y)


class Skill__T:
    def __init__(self):
        self.x, self.y = 260, 550
        self.image = load_image('resource/skill/skill_tree.png')

    def draw(self):
        self.image.draw(self.x, self.y)


