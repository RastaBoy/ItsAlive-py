import pygame
import random

from settings import *
from utils import Circle, collision, Position, Edible

class Bacterium(Edible):

    def __init__(self, x, y, size, isHerbivore:bool, isCarnivore:bool):
        self.pos:Position = Position(x,y)
        self.size = size
        self.isHerbivore = isHerbivore
        self.isCarnivore = isCarnivore
        self.energy = 100000
        self.target:Position = None

    @property
    def isAlive(self):
        return self.energy > 0

    @property
    def fieldOfView(self):
        return self.size + self.size*10.5

    def look(self, world:list):
        items = []
        for i in world:     
            if collision(Circle(Position(i.pos.x, i.pos.y), i.size), Circle(Position(self.pos.x, self.pos.y), self.fieldOfView)):
                if id(self) != id(i):
                    items.append(i)
        return items

    def brain(self, world:list):
        if not self.isAlive:
            return
        self.energy -= STEP_COST
        for obj in self.look(world):
            if self.isCarnivore and obj.__class__ == Bacterium:
                if collision(Circle(Position(obj.pos.x, obj.pos.y), obj.size), Circle(Position(self.pos.x, self.pos.y), self.size)):
                    self.eat(obj)
                else:
                    self.move(obj.pos)

    
    def move(self, target:Position):
        self.target = target

    def eat(self, food:Edible):
        self.energy += food.energy_bonus
        #self.size += food.energy_bonus/10
        food.die()

    def die(self):
        self.energy = 0

    def render(self):
        pygame.draw.circle(screen, WHITE, (self.pos.x, self.pos.y), self.fieldOfView, 1)
        
        if self.isCarnivore and self.isHerbivore:
            pygame.draw.circle(screen, (random.randint(150, 255), 100, random.randint(150, 255)), (self.pos.x, self.pos.y), self.size)
        elif self.isCarnivore:
            pygame.draw.circle(screen, (random.randint(150, 255), 100, 0), (self.pos.x, self.pos.y), self.size)
        else: 
            pygame.draw.circle(screen, (0, 100, random.randint(150, 255)), (self.pos.x, self.pos.y), self.size)

        