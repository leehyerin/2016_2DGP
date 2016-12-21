
from pico2d import *

class Time:
    def __init__(self):
        self.font = load_font('ENCR10B.ttf',40)
        self.init_time = SDL_GetTicks()


    def passed_time(self):
        return (self.init_time-SDL_GetTicks())

    def update(self):
        print(self.passed_time())
