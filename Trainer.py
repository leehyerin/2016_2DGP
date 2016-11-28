import random
from pico2d import *


class Trainer:

    PIXEL_PER_METER = (10.0 / 0.3)   #10pixel이 30cm임
    RUN_SPEED_KMPH = 10.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 100.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    RIGHT_RUN, LEFT_RUN, DOWN_RUN, UP_RUN = 0, 1, 2, 3
    JIWOO, YISEUL, WOONG = 0,1,2

    def handle_left_run(self):
        self.x -= 5
        if self.x <10:
            self.state = self.RIGHT_RUN
            self.x = 10

    def handle_right_run(self):
        self.x += 5

        if self.x > 800:
            self.state = self.LEFT_RUN
            self.x = 800


    def handle_up_run(self):
        self.y += 5
        if self.y > 600:
            self.state = self.DOWN_RUN
            self.y = 600

    def handle_down_run(self):
        self.y -= 5
        if self.y < 0:
            self.state = self.UP_RUN
            self.y = 60

    handle_state = {
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        UP_RUN : handle_up_run,
        DOWN_RUN : handle_down_run
    }

    def update(self,frame_time):
        distance = Trainer.RUN_SPEED_PPS * frame_time
        self.frame = (self.frame + 1) % 3
        self.handle_state[self.state](self)

    def __init__(self,stage):
        self.stage=stage
        self.type = random.randint( 0,2)
        if self.stage == 1:
            self.x, self.y= 20,300
            self.state = self.RIGHT_RUN
        elif self.stage == 2:
            self.x, self.y= 180,10
            self.state = self.UP_RUN

        self.hp = 1000
        self.frame =0
        self.total_frames = 0.0
        self.dir = 1
        self.font = load_font('ENCR10B.TTF')


        if self.type == self.JIWOO:
            self.image = load_image('resource/trainer/jiwoo.png')
        elif self.type == self.YISEUL:
            self.image = load_image('resource/trainer/yiseul.png')
        elif self.type == self.WOONG:
            self.image = load_image('resource/trainer/woong.png')

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.font.draw(self.x-50, self.y + 50, 'HP: %3.2f' % self.hp)
        self.image.clip_draw(88 + self.frame * 51, 2 + self.state*60, 48,58, self.x, self.y)
