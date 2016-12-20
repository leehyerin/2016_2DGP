from pico2d import *

class Inventory:
    image = None


    def __init__(self, type):
        self.type = type
        self.count=0
        self.font = load_font('ENCR10B.TTF')

        if Inventory.image == None:
            if self.type == 'w':
                self.x, self.y = 600, 50
                self.image = load_image('resource/item/water.png')
            elif self.type == 'l':
                self.x, self.y = 640, 50
                self.image = load_image('resource/item/lightning.png')
            elif self.type == 'f':
                self.x, self.y = 680, 50
                self.image = load_image('resource/item/fire.png')
            elif self.type == 'e':
                self.x, self.y = 720, 50
                self.image = load_image('resource/item/earth.png')
            elif self.type == 't':
                self.x, self.y = 760, 50
                self.image = load_image('resource/item/tree.png')



    def draw(self):
        self.image.draw(self.x, self.y)
        self.font.draw(self.x-5,self.y-30,'%d' %self.count)

    def update(self,type):
        if self.type == type:
           self.count += 1

