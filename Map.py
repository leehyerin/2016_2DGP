from pico2d import *



class Map:
    def __init__(self):
        self.image = load_image('stage1map.png')

    def draw(self):
        self.image.clip_draw_to_origin(0, 0, 800, 600, 0, 0)
