from pico2d import *

import game_framework
import title_state
import stage2

from Trainer import *
from Pokemon import *
from Projectile import *
from Pokeball import *
from TIme import*
from Map import Map
from resource_inven import*
from Skill import*

name = "Stage1"

map = None
pokeball = None
font = None
pokemons = None
selection = None
projectiles = None
timing = None
resources = None
invens = None

def create_world():
    global map, pokeball, trainers, font, pokemons, selection,\
        projectiles, timing, resources, invens, skill_buttons
    timing = Time()
    map = Map()
    pokeball = Pokeball(1)
    trainers = list()
    trainers.append(Trainer(1))
    projectiles=list()
    resources=list()
    invens = []
    invens.append(Inventory('w'))
    invens.append(Inventory('l'))
    invens.append(Inventory('t'))
    invens.append(Inventory('e'))
    invens.append(Inventory('f'))
    skill_buttons = []
    skill_buttons.append(Skill__W())
    skill_buttons.append(Skill__L())
    skill_buttons.append(Skill__T())
    skill_buttons.append(Skill__E())
    skill_buttons.append(Skill__F())

    pokemons = [Pokemon(i) for i in range(4)]



def destroy_world():
    global map, pokeball, trainers, pokemons, timing, resources, invens
    del(map)
    del(pokeball)
    del(trainers)
    del(pokemons)
    del(timing)
    del(resources)
    del(invens)


def skill(Pokemon):
    global projectiles
    projectiles.append(Projectile(Pokemon))

def create_item(Trainer):
    resources.append(Resource(Trainer))


def enter():
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
            elif (event.type ,event.key)==(SDL_KEYDOWN,SDLK_n):          #go to next stage
                game_framework.change_state(stage2)
            elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
                for pokemon in pokemons:
                    if point_collide(pokemon,event.x, 600 - event.y):
                        pokemon.selection = True
                    else:
                        pokemon.selection = False
                for resource in resources:
                    if point_collide(resource,event.x, 600 - event.y):
                        resources.remove(resource)
                        for inven in invens:
                            inven.get_resource(resource.type)

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

def trainer_ai(time):
    if timing.passed_time()>time and timing.passed_time()<time+48:
        trainers.append(Trainer(1))

def update(frame_time):
    for trainer in trainers:
        trainer.update(frame_time)
    timing.update()
    for i in range (4):
        trainer_ai(i*2000)    #use jason


    for trainer in trainers:
        if collide(trainer, pokeball):
             pokeball.hp-=10
        elif trainer.hp <= 0:
            create_item(trainer)
            trainers.remove(trainer)
        for pokemon in pokemons:
            if collide(trainer, pokemon):
                pokemon.hp-=10

    for pokemon in pokemons:
        pokemon.update(frame_time)
    for projectile in projectiles:
        projectile.update(frame_time)
        for trainer in trainers:
            if collide(projectile, trainer) :
                projectiles.remove(projectile)
                trainer.hp -= 250


    delay(0.05)

def draw(frame_time):
    clear_canvas()
    map.draw()
    pokeball.draw()
    for trainer in trainers:
        trainer.draw()
    for button in skill_buttons:
        button.draw()
    for inven in invens:
        inven.draw()
    for pokemon in pokemons:
        pokemon.draw()
    for projectile in projectiles:
        projectile.draw()
    for resource in resources:
        resource.draw()
    update_canvas()



