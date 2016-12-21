from pico2d import *

import game_framework
import title_state
from Map import *

from Trainer import *
from Pokemon import *
from Projectile import *
from Pokeball import *
from TIme import*

map=None
pokeball=None
font=None
pokemons =None
selection = None
projectiles = None
timing=None


name = "Stage2"
image = None

def create_world():
    global map, pokeball, trainer1, font,pokemons, selection, projectiles, timing
    timing=Time()
    map = Map2()

    pokeball = Pokeball(2)
    trainer1 = Trainer(2)

    projectiles=list()
    pokemons = [Pokemon(i) for i in range(3)]



def destroy_world():
    global map, pokeball, trainer1, pokemons, timing
    del(map)
    del(pokeball)
    del(trainer1)
    del(pokemons)
    del(timing)


#image = load_image('stage2.png')


def enter():
    global image
    game_framework.reset_time()
    create_world()

def exit():
    destroy_world()


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(title_state)
            elif (event.type ,event.key)==(SDL_KEYDOWN,SDLK_SPACE):
                for pokemon in pokemons:
                    if pokemon.selection == True:
                        skill(pokemon)
            elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
                for pokemon in pokemons:
                    if point_collide(pokemon,event.x,event.y):
                        pokemon.selection = True
                    else:
                        pokemon.selection = False
            else:
                for pokemon in pokemons:
                    if pokemon.selection == True:
                        pokemon.handle_event(event)


def skill(Pokemon):
    global projectiles
    projectiles.append(Projectile(Pokemon))


def exit():
    global image
    del(image)

import stage1

def pause():
    pass

def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(title_state)
           # elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_n):
            #    game_framework.change_state(stage3)

            elif (event.type ,event.key)==(SDL_KEYDOWN,SDLK_SPACE):
                for pokemon in pokemons:
                    if pokemon.selection == True:
                        skill(pokemon)
            elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
                for pokemon in pokemons:
                    if point_collide(pokemon,event.x,600-event.y):
                        pokemon.selection = True
                    else:
                        pokemon.selection = False
            else:
                for pokemon in pokemons:
                    if pokemon.selection == True:
                        pokemon.handle_event(event)




def point_collide(self,x,y):
    if (self.x - 30 < x and x < self.x + 30) and (self.y - 30 < y and y < self.y + 30):
        print("collide")
        return True


def collide(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b:return False
    if top_a < bottom_b:return False
    if bottom_a > top_b:return False

    return True




def update(frame_time):
    global trainer1,trainer2, trainer3

    trainer1.update(frame_time)
    if collide(trainer1, pokeball):
         pokeball.hp-=10
    elif trainer1.hp <= 0:
        trainer1.x=-100
    delay(0.05)
    timing.update(frame_time)


    for pokemon in pokemons:
        pokemon.update(frame_time)
    for projectile in projectiles:
        projectile.update(frame_time)
        if collide(projectile, trainer1) :
            trainer1.hp -= 25
            projectiles.remove(projectile)



def draw(frame_time):
    clear_canvas()
    timing.draw()
    map.draw()
    pokeball.draw()
    trainer1.draw()
    for pokemon in pokemons:
        pokemon.draw()
    for projectile in projectiles:
        projectile.draw()
    update_canvas()


