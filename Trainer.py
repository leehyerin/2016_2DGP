import random
from pico2d import *
from TIme import*

class Trainer():

    PIXEL_PER_METER = (10.0 / 0.3)   #10pixel이 30cm임
    RUN_SPEED_KMPH = 10.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 100.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    RIGHT_RUN, LEFT_RUN, DOWN_RUN, UP_RUN = 0, 1, 2, 3
    image = None

    JIWOO, YISEUL, WOONG = 0,1,2

    def __init__(self, stage: object) -> object:
        self.stage=stage
        global distance
        self.type = random.choice('wlfte')
        if self.stage == 1:
            self.x, self.y= 20,300
            self.state = self.RIGHT_RUN
        elif self.stage == 2:
            self.x, self.y= 180,10
            self.state = self.UP_RUN
            self.box0 = Turn_dir(200,290)
            self.box1 = Turn_dir(560,290)

        self.hp = 1000
        self.frame =0
        self.total_frames = 0.0
        self.dir = 1
        self.font = load_font('ENCR10B.TTF')
        self.isflame=False
        self.isstun =False

        if Trainer.image == None:
            if self.type == 'l': #lightning'
                self.image = load_image('resource/trainer/jiwoo.png')
            elif self.type == 'w': #water':
                self.image = load_image('resource/trainer/yiseul.png')
            elif self.type == 't': #tree
                self.image = load_image('resource/trainer/woong.png')
            elif self.type == 'f': #fire
                self.image = load_image('resource/trainer/woong.png')
            elif self.type == 'e': #earth
                self.image = load_image('resource/trainer/woong.png')

        self.flame_image = load_image('resource/skill/flame.png')
        self.stem_image  = load_image('resource/skill/stem_chain.png')


    def handle_left_run(self,distance):
        self.x -= 6.5 * distance
        if self.x <10:
            self.state = self.RIGHT_RUN
            self.x = 10

    def handle_right_run(self,distance):
        self.x += 6.5 * distance

        if self.x > 800:
            self.state = self.LEFT_RUN
            self.x = 800

    def handle_up_run(self,distance):
        if True == self.isstun:
            pass
        else:
            self.y += 6.5 * distance
            if self.y > 600:
                self.state = self.DOWN_RUN
                self.y = 600

    def handle_down_run(self,distance):
        self.y -= 6.5 * distance
        if self.y < 0:
            self.state = self.UP_RUN
            self.y = 60

    handle_state = {
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        UP_RUN : handle_up_run,
        DOWN_RUN : handle_down_run
    }

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.font.draw(self.x-50, self.y + 50, 'HP: %3.2f' % self.hp)
        if True == self.isflame:
            self.flame_image.clip_draw(self.frame * 34, 0, 34, 49, self.x, self.y,60,60)

        self.image.clip_draw(88 + self.frame * 51, 2 + self.state*60, 48,58, self.x, self.y)

        if True == self.isstun:
            self.stem_image.clip_draw(0, self.frame * 50, 42, 50, self.x, self.y)
            self.draw_bb()

        if self.stage == 2:
            self.box0.draw()
            self.box1.draw()

    def flame(self):
        self.timer = Time()
        self.isflame=True

    def flame_update(self):
        self.hp -= 1
        if self.timer.passed_time() > 5000:
            self.isflame = False
            self.state = self.LEFT_RUN

    def stun(self):
        self.stimer=Time()
        self.isstun = True
        self.state = self.UP_RUN

    def stun_update(self):
        self.hp -= 1
        if self.stimer.passed_time() > 3000:
            self.isstun = False



    def update(self, frame_time):
        distance = Trainer.RUN_SPEED_PPS * frame_time
        self.frame = (self.frame + 1) % 3
        self.handle_state[self.state](self, distance)
        if True == self.isflame:
            self.flame_update()
        if True == self.isstun:
            self.stun_update()

        if self.stage == 2:
            if collide(self, self.box0):
                if self.state == self.UP_RUN:
                    self.state = self.RIGHT_RUN
                elif self.state == self.LEFT_RUN:
                    self.state = self.DOWN_RUN
            if collide(self, self.box1):
                if self.state == self.RIGHT_RUN:
                    self.state = self. UP_RUN
                elif self.state == self.DOWN_RUN:
                    self.state = self.LEFT_RUN


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


class Turn_dir():
    def __init__(self,x,y):
        self.x, self.y = x, y

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw(self):
        self.draw_bb()



class Resource():
    image = None

    def __init__(self,Trainer):
        self.type = Trainer.type
        self.x, self.y = Trainer.x, Trainer.y

        if Resource.image == None:
            if self.type == 'w':
                self.image  = load_image('resource/item/water.png')
            elif self.type == 'l':
                self.image  = load_image('resource/item/lightning.png')
            elif self.type == 'f':
                self.image  = load_image('resource/item/fire.png')
            elif self.type == 'e':
                self.image  = load_image('resource/item/earth.png')
            elif self.type == 't':
                self.image  = load_image('resource/item/tree.png')


    def draw(self):
        self.image.draw(self.x,self.y)


    def update(self):
        pass