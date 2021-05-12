from utils import Position, direction
import pygame
import sys
from settings import *
from objects.bacterium import Bacterium
from objects.world import world

Game = True

# Initialize
world.append(Bacterium(60, 80, 10, False, True))
world.append(Bacterium(20, 40, 10, True, False))
world.append(Bacterium(150, 20, 10, True, False))




while Game:

    # Events
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            Game = False
            sys.exit()

    # Drawing
    screen.fill(BLACK)
    for obj in world:
        obj.render()
    pygame.display.update()



    # Logic
    bacteriums = []
    for obj in world:
        if obj.__class__ == Bacterium:
            obj.brain(world)
            bacteriums.append(obj)

    for obj in bacteriums:
        if not obj.isAlive:
            world.remove(obj)
            continue
        if obj.target != None:
            dir = direction(obj.target, obj.pos)

            pos:Position = Position(obj.pos.x, obj.pos.y)
            pos.x += dir[0] * STEP
            pos.y += dir[1] * STEP
            obj.pos = pos

    clock.tick(FPS)

