from pico2d import *
global stage

class Pokeball:
    def __init__(self,stage):
        self.stage = stage
        if self.stage == 1:
            self.x, self.y = 750, 300
            self.hp = 700
        elif self.stage == 2:
            self.x, self.y = 200, 480
            self.hp = 1500

        self.image=load_image('resource/etc/Pokeball.gif')
        self.font = load_font('ENCR10B.TTF')

    def draw(self):
        self.image.draw(self.x,self.y)
        self.font.draw(self.x-60, self.y - 50, 'HP: %d' % self.hp)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x-50, self.y-50, self.x+50, self.y+50