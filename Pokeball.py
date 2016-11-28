from pico2d import *

class Pokeball:
    def __init__(self):
        self.x,self.y= 750, 300
        self.hp =1000
        self.image=load_image('resource/etc/Pokeball.gif')
        self.font = load_font('ENCR10B.TTF')

    def draw(self):
        self.image.draw(self.x,self.y)
        self.font.draw(self.x-50, self.y + 50, 'HP: %3.2f' % self.hp)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x-50, self.y-50, self.x+50, self.y+50