import random
from pico2d import *

global a,b
class Pokemon:
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 10.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 60.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    ASLEEP =8
    RIGHT_IDLE, LEFT_IDLE, UP_IDLE, DOWN_IDLE = 0,1,2,3
    RIGHT_RUN, LEFT_RUN,  UP_RUN, DOWN_RUN = 4,5,6,7
    RIGHT_ATTACK, LEFT_ATTACK, UP_ATTACK, DOWN_ATTACK = 4,5,6,7

    def __init__(self, type):
        self.type = type
        self.selection = True
        self.x, self.y = random.randint(50, 600), random.randint(50, 500)

        self.frame = random.randint(0, 2)
        self.idle_frames = 0
        self.timer = 0

        # self.attack_frames=0
        #projectile = list()

        self.state = random.randint(self.RIGHT_IDLE, self.ASLEEP)
        if self.type == 0:
            self.image = load_image('resource/pokemon/marill.png')
        elif self.type == 1:
            self.image = load_image('resource/pokemon/bayleaf.png')
        elif self.type == 2:
            self.image = load_image('resource/pokemon/piri.png')
        elif self.type == 3:
            self.image = load_image('resource/pokemon/digda.png')




    def handle_asleep(self):

        self.idle_frames += 1
        if self.idle_frames == 20:
            self.state = random.randint(0, 7)
            self.idle_frames = 0

    def handle_left_idle(self):
        self.x -= 2 * self.distance
        timer = SDL_GetTicks()
        #self.idle_frames += 1

        if SDL_GetTicks() - timer > 3000:
            self.state =  random.randint(0,8)
            timer = SDL_GetTicks()
            #self.idle_frames=0

    def handle_right_idle(self):
        self.x +=2 *  self.distance
        self.idle_frames += 1

        if self.idle_frames == 20:
            self.state = random.randint(0,8)
            self.idle_frames = 0

    def handle_up_idle(self):
        self.y +=2 *  self.distance
        self.idle_frames += 1

        if self.idle_frames == 20:
            self.state = random.randint(0,8)
            self.idle_frames = 0

    def handle_down_idle(self):
        self.y -= 2 * self.distance

        if self.idle_frames == 20:
            self.state = random.randint(0,8)
            self.idle_frames = 0

    def handle_left_run(self):
        self.x -=  5 * self.distance
        self.idle_frames += 1

        if self.idle_frames == 20:
            self.state = random.randint(0, 8)
            self.idle_frames = 0
        if self.x < 50:
            self.state= self.RIGHT_RUN

    def handle_right_run(self):
        self.x +=  5 * self.distance
        if self.x > 750:
            self.state= self.LEFT_RUN


    def handle_up_run(self):
        self.y += 5 * self.distance

        if self.y > 450:
            self.state= self.DOWN_RUN

    def handle_down_run(self):
        self.y -= 5 * self.distance

        if self.y < 50:
            self.state= self.UP_RUN


    handle_state = {
        ASLEEP : handle_asleep,
        LEFT_IDLE : handle_left_idle,
        RIGHT_IDLE: handle_right_idle,
        UP_IDLE: handle_up_idle,
        DOWN_IDLE: handle_down_idle,
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        UP_RUN: handle_up_run,
        DOWN_RUN: handle_down_run,

    }

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.ASLEEP, self.LEFT_IDLE, self.RIGHT_IDLE, self.UP_IDLE, self.DOWN_IDLE,
                              self.RIGHT_RUN, self.UP_RUN, self.DOWN_RUN):
                self.state = self.LEFT_RUN
                self.x -= self.distance
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.ASLEEP, self.LEFT_IDLE, self.RIGHT_IDLE, self.UP_IDLE, self.DOWN_IDLE,
                              self.LEFT_RUN, self.UP_RUN, self.DOWN_RUN):
                self.state = self.RIGHT_RUN
                self.x +=  self.distance
        elif (event.type, event.key) == ( SDL_KEYDOWN, SDLK_UP):
            if self.state in (self.ASLEEP,self.LEFT_IDLE, self.RIGHT_IDLE, self.UP_IDLE, self.DOWN_IDLE,
                              self.LEFT_RUN, self.RIGHT_RUN, self.DOWN_RUN):
                self.state = self.UP_RUN
                self.y += self.distance
        elif (event.type, event.key) == ( SDL_KEYDOWN, SDLK_DOWN):
            if self.state in (self.ASLEEP,self.LEFT_IDLE, self.RIGHT_IDLE, self.UP_IDLE, self.DOWN_IDLE,
                              self.LEFT_RUN, self.RIGHT_RUN, self.UP_RUN):
                self.state = self.DOWN_RUN
                self.y -= self.distance
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.LEFT_RUN,):
                self.state = self.LEFT_IDLE
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.RIGHT_RUN,):
                self.state = self.RIGHT_IDLE
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_UP):
            if self.state in (self.UP_RUN,):
                self.state = self.UP_IDLE
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            if self.state in (self.DOWN_RUN,):
                self.state = self.DOWN_IDLE




   # def skill(self,state):
    #    global projectiles
     #   projectiles.append(Projectile(self))

    def update(self,frame_time):
        self.distance = Pokemon.RUN_SPEED_PPS * frame_time

        self.frame = (self.frame + 1) % 3
        self.handle_state[self.state](self)

        if(self.selection==True):
            print(self.state)
        #delay(0.02)




    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

    def draw(self):
        if self.state== self.ASLEEP:
            self.image.clip_draw(0, 5+self.state * 55, 53, 53, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 59, self.state * 57, 59, 57, self.x, self.y)




class Projectile:

    PIXEL_PER_METER = (10.0 / 0.25)  # 10pixel이 25cm임
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 200.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    LEFT, RIGHT, UP, DOWN = 0, 1, 2, 3

    image =None

    def __init__(self, Pokemon):
        self.x,self.y = Pokemon.x,Pokemon.y
        self.frame=0
        if Projectile. image == None:
            self.image = load_image('poison.png')
        self.state = random.randint(self.LEFT, self.DOWN)


        if Pokemon.state in (Pokemon.LEFT_RUN, Pokemon.LEFT_IDLE):
            self.state = self.LEFT
        elif Pokemon.state in (Pokemon.RIGHT_RUN, Pokemon.RIGHT_IDLE):
            self.state = self.RIGHT
        elif Pokemon.state in (Pokemon.UP_RUN, Pokemon.UP_IDLE):
            self.state = self.UP
        elif Pokemon.state in (Pokemon.DOWN_RUN, Pokemon.DOWN_IDLE):
            self.state = self.DOWN

    def create_left(self):
        self.x -= 5 * self.distance

    def create_right(self):
        self.x +=5 * self.distance

    def create_up(self):
        self.y += 5*self.distance

    def create_down(self):
        self.y -=5*self.distance

    handle_state = {
        LEFT: create_left,
        RIGHT: create_right,
        UP: create_up,
        DOWN: create_down

    }

    def update(self,frame_time):
        self.distance = Projectile.RUN_SPEED_PPS * frame_time
        self.frame = (self.frame + 1) % 4
        self.handle_state[self.state](self)
        if self.frame >5:
            Projectile.remove()


    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.clip_draw(self.frame * 32, 0, 32, 20, self.x, self.y)

