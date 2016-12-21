from pico2d import *
from Pokemon import*



class Skill_WideDamage_W:

    PIXEL_PER_METER = (10.0 / 0.25)  # 10pixel이 25cm임
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 200.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    LEFT, RIGHT, UP, DOWN = 0, 1, 2, 3

    image = None

    def __init__(self, Pokemon: object) -> object:
        self.time=Time()
        self.x,self.y = Pokemon.x,Pokemon.y
        self.frame = 0
        self.dead = 10
        if Skill_WideDamage_W. image == None:
            self.image = load_image('resource/skill/wide_damage.png')

        if Pokemon.state in (Pokemon.LEFT_RUN, Pokemon.LEFT_IDLE):
            self.state = self.LEFT
        elif Pokemon.state in (Pokemon.RIGHT_RUN, Pokemon.RIGHT_IDLE):
            self.state = self.RIGHT
        elif Pokemon.state in (Pokemon.UP_RUN, Pokemon.UP_IDLE):
            self.state = self.UP
        elif Pokemon.state in (Pokemon.DOWN_RUN, Pokemon.DOWN_IDLE):
            self.state = self.DOWN

    def create_left(self):
        self.x -= 10 * self.distance

    def create_right(self):
        self.x += 10 * self.distance

    def create_up(self):
        self.y += 10 * self.distance

    def create_down(self):
        self.y -= 10 * self.distance

    handle_state = {
        LEFT: create_left,
        RIGHT: create_right,
        UP: create_up,
        DOWN: create_down

    }

    def update(self,frame_time):
        self.distance = Projectile.RUN_SPEED_PPS * frame_time
        self.frame = (self.frame + 1) % 4
        self.dead -=1
        self.handle_state[self.state](self)

        # if self.time.passed_time() > 300:
        #     Skill_WideDamage_W.remove()


    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.clip_draw(self.frame * 50, 0, 50, 99, self.x, self.y)

#######################################################





class Skill_Button:
    def __init__(self,number):
        if number == 1:
            self.x, self.y = 100,550
            self.image = load_image('resource/skill/skill_water.png')
        elif number == 2:
            self.x, self.y = 140,550
            self.image = load_image('resource/skill/skill_lightning.png')
        elif number == 3:
            self.x, self.y = 180,550
            self.image = load_image('resource/skill/skill_fire.png')
        elif number == 4:
            self.x, self.y = 220,550
            self.image = load_image('resource/skill/skill_earth.png')
        else:
            self.x, self.y = 260,550
            self.image = load_image('resource/skill/skill_tree.png')

    def draw(self):
        self.image.draw(self.x, self.y)