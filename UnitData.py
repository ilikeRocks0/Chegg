from enum import Enum, auto
from UnitData import Attack 
class UnitData:
    name: str
    cost: int
    move: list
    attack: Attack
    death: list
    moveCostFirst:int = 0
    moveCostSecond:int = 1
    attackCost:int = 1
    specialCost: int = 1

    def __init__(self, name, cost, move, attack, death):
        self.name = name
        self.cost = cost
        self.move = move
        self.attack = attack
        self.death = death

    def getMaxAttack(self):
        return self.attack.maxAttack
    
    #so you dont have to call attack variable
    def getAttack(self, index):
        return self.attack.getAttack(index)
    
class AttackType(Enum):
    ATTACK_SINGLE = auto()
    ATTACK_GROUP = auto()

class Attack:
    attackType: AttackType
    attacks: list
    modifier: str
    maxAttack:int

    def __init__(self, type, attackList, mod):
        #try to cast 
        self.attackType = AttackType[type]
        self.attacks = attackList
        self.modifier = mod
        self.maxAttack = len(attackList)

    def getAttack(self, index)-> list[tuple[int,int]]:
        return self.attacks[index]
