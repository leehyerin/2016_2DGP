
from pico2d import *

class Time:
    def __init__(self):
        self.font = load_font('ENCR10B.ttf',40)

    def update(self,frame_time):
        self.time = get_time()

    def draw(self):
        self.font.draw(500,550,"Time : %f " % self.time)
