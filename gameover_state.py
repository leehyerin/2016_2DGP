import game_framework
from pico2d import *

import title_state

name = "GameOverState"
image = None

def enter():
    global image
    image = load_image('resource/background/kpu_credit.png')


def exit():
    global image
    del(image)


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE): #restart
                game_framework.change_state(title_state)


def update(frame_time):
    global name
    global logo_time

    if (logo_time > 0.5):
        logo_time = 0
        game_framework.change_state(title_state)
        #game_framework.quit()
    logo_time += frame_time

def draw(frame_time):
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def pause(): pass
def resume(): pass




