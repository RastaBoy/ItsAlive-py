import math
from dataclasses import dataclass


@dataclass
class Position:
    x:int
    y:int


@dataclass
class Circle:
    pos:Position
    r:int

def position_distance(pos1:Position, pos2:Position):
    return (pos1.x - pos2.x, pos1.y - pos2.y)

def distance(pos1:Position, pos2:Position):
    pos_dis = position_distance(pos1, pos2)
    return math.sqrt(pos_dis[0] ** 2 + pos_dis[1] ** 2)

def direction(pos1:Position, pos2:Position):
    norm = distance(pos1, pos2)
    pos_dis = position_distance(pos1, pos2)
    return (pos_dis[0]/norm, pos_dis[1]/norm)

def collision(obj1:Circle, obj2:Circle):
    if  distance(obj1.pos, obj2.pos) <= obj1.r + obj2.r:
        return True
    return False

class Edible:
    energy_bonus = 100
