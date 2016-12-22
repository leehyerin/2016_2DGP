
from pico2d import *

class Time:
    def __init__(self):
        self.font = load_font('ENCR10B.ttf',40)
        self.init_time = SDL_GetTicks()

    def passed_time(self):
        return (SDL_GetTicks()-self.init_time)

    def initialize(self):
        self.init_time = SDL_GetTicks()

        # print(self.passed_time())
