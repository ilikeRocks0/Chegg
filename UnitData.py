from BoardTile import BoardTile
from enum import Enum, auto
from UnitData import Attack 
class UnitData(BoardTile):
    name: str
    cost: int
    move: list
    attack: Attack
    death: list
    moveCostFirst:int = 0
    moveCostSecond:int = 1

    def __init__(self, name, cost, move, attack, death):
        self.name = name
        self.cost = cost
        self.move = move
        self.attack = attack
        self.death = death

class AttackType:
    ATTACK_SINGLE = auto()
    ATTACK_GROUP = auto()

class Attack:
    attackType: AttackType
    attacks: list
    modifier: str