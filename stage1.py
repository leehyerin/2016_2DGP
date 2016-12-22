import game_framework
import stage2
import title_state
import gameover_state
from Map import Map
from Pokeball import *
from Projectile import *
from Skill import*
from Time import*
from Trainer import *
from resource_inven import*


name = "Stage1"

map = None
pokeball = None
font = None
pokemons = None
selection = None
######skill#######
projectiles = None
wide_damage = None
flame = None
stem = None

timing = None
fix_times = None
resources = None
invens = None


def create_world():
    global map, pokeball, trainers, font, pokemons, selection,\
        projectiles,wide_damage,flame,stem, timing, fix_time, resources, invens, skill_buttons
    timing = Time()
    fix_time = Time()
    map = Map()

    pokeball = Pokeball(1)
    trainers = list()
    trainers.append(Trainer(1))
    projectiles = list()
    wide_damage = list()
    flame = list()
    stem = list()
    resources = list()
    invens = []
    invens.append(Inventory('w'))
    invens.append(Inventory('l'))
    invens.append(Inventory('t'))
    invens.append(Inventory('e'))
    invens.append(Inventory('f'))
    skill_buttons = [Skill_Button(i) for i in range(5)]
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
            elif (event.type ,event.key)==(SDL_KEYDOWN,SDLK_LSHIFT):
                for pokemon in pokemons:
                    if pokemon.selection == True:
                        Meele_Attack(pokemon)

            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                for pokemon in pokemons:
                    if pokemon.selection == True:
                        if pokemon.fix == False:
                            pokemon.fix = True
                            fix_time.init_time = SDL_GetTicks()
                            Fix_Attack(pokemon)
                        else:
                            pokemon.fix = False

            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_1): #water
                for pokemon in pokemons:
                    if pokemon.selection == True:
                        if skill_1() == True:
                             WideDamage(pokemon)

            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_2):
                for pokemon in pokemons:
                    if pokemon.selection == True:
                        if skill_2() == True:
                            Flame(pokemon)

            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_3):
                for pokemon in pokemons:
                    if pokemon.selection == True:
                        # if pokemon.type == 0:
                            if skill_3() == True:
                                Stem_Chain(pokemon)

            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_n):  # go to next stage
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
                    if pokemon.selection:
                        pokemon.handle_event(event)

                if pokeball.hp <= 0:
                    game_framework.change_state(gameover_state)


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


def skill_1(): #rulili
    global flag
    flag= False
    for inven in invens:
        if inven.type == 'w':
            if inven.count > 0:
                inven.count -= 1
                return True


def skill_2(): #fire
    global flag
    flag = False
    for inven in invens:
        if inven.type == 'f':
            if inven.count > 0:
                inven.count-=1
                return True

def skill_3(): #tree
    global flag
    flag = False
    for inven in invens:
        if inven.type == 't':
            if inven.count > 0:
                inven.count-=1
                return True

def Fix_Attack(Pokemon):
    if fix_time.passed_time() > 1000:
        Meele_Attack(Pokemon)
        fix_time.init_time = SDL_GetTicks()


def Meele_Attack(Pokemon):
    global projectiles
    projectiles.append(Projectile(Pokemon))


def WideDamage(Pokemon):
    wide_damage.append(Skill_WideDamage_W(Pokemon))


def Flame(Pokemon):
    flame.append(Skill_Flame_F(Pokemon))

def Stem_Chain(Pokemon):
    stem.append(Skill_Stem_Chain(Pokemon))


def create_item(Trainer):
    resources.append(Resource(Trainer))


def trainer_ai(time):
    if timing.passed_time()>time and timing.passed_time()<time+48:
        trainers.append(Trainer(1))


def update(frame_time):
    for trainer in trainers:
        trainer.update(frame_time)
    for i in range (20):
        trainer_ai(i*3000)    #use jason

    for trainer in trainers:
        if collide(trainer, pokeball):
            # if pokeball.hp <= 0:
            #     game_framework.change_state(gameover_state)
            # else:
                pokeball.hp-=10
        if trainer.hp <= 0:
            create_item(trainer)
            trainers.remove(trainer)


    for pokemon in pokemons:
        pokemon.update(frame_time)
        if pokemon.fix == True:
            Fix_Attack(pokemon)

    for projectile in projectiles:
        projectile.update(frame_time)
        for trainer in trainers:
            if collide(projectile, trainer) :
                # projectiles.remove(projectile)
                trainer.hp -= 250

    for skill in wide_damage:
        skill.update(frame_time)
        for trainer in trainers:
            if collide(skill, trainer) :
                # wide_damage.remove(skill)
                trainer.hp -= 250

    for skill in flame:
        skill.update(frame_time)
        for trainer in trainers:

            if collide(skill, trainer) :
                trainer.flame()
                flame.remove(skill)

    for trainer_i in trainers:
        for trainer_j in trainers:
            if trainer_i is not trainer_j:
                if True == trainer_j.isflame or True == trainer_i.isflame:
                    if collide(trainer_i,trainer_j):
                        trainer_i.flame()
                        trainer_j.flame()

    for skill in stem:
        skill.update(frame_time)
        for trainer in trainers:
            if collide(skill, trainer) :
                stem.remove(skill)
                trainer.stun()
    delay(0.07)


def draw(frame_time):
    clear_canvas()
    map.draw()
    pokeball.draw()
    for trainer in trainers:
        trainer.draw()
    # for button in skill_buttons:
    #     button.draw()
    for inven in invens:
        inven.draw()
    for pokemon in pokemons:
        pokemon.draw()
    for projectile in projectiles:
        projectile.draw()
    for skill in wide_damage:
        skill.draw()
    for skill in flame:
        skill.draw()
    for skill in stem:
        skill.draw()
    for resource in resources:
        resource.draw()
    update_canvas()



