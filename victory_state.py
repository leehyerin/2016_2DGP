import game_framework
from pico2d import *


name = "VictoryState"
image = None



def enter():
    global image
    image = load_image('resource/background/victory.png')
    bgm = load_music('resource/sound/victory.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()

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


def update(frame_time):
    pass

def draw(frame_time):
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def pause(): pass
def resume(): pass




