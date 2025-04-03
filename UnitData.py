from enum import Enum, auto
from UnitData import Attack, Special 
class UnitData:
    name: str
    cost: int
    move: list
    attack: Attack
    death: list
    special: Special
    moveCostFirst:int = 0
    moveCostSecond:int = 1
    attackCost:int = 1
    specialCost: int = 1

    def __init__(self, name, cost, move, attack = None, special = None, death = ""):
        self.name = name
        self.cost = cost
        self.move = move
        self.attack = attack
        self.special = special
        self.death = death

    def getMaxAttack(self):
        if (self.attack != None):
            return self.attack.attackMax
        return -1
    
    #so you dont have to call attack variable
    def getAttack(self, index):
        if (self.attack != None):
            return self.attack.getAttack(index)
        return None
    
    def getMaxSpecial(self):
        if (self.s != None):
            return self.special.specialMax
        return -1
    
    #so you dont have to call attack variable
    def getSpecial(self, index):
        if (self.attack != None):
            return self.special.getSpecial(index)
        return None
    
class AttackType(Enum):
    ATTACK_SINGLE = auto()
    ATTACK_GROUP = auto()

class Attack:
    attackType: AttackType
    attacks: list
    modifier: str
    attackMax:int

    def __init__(self, type, attackList, mod):
        #try to cast 
        self.attackType = AttackType[type]
        self.attacks = attackList
        self.modifier = mod
        self.attackMax = len(attackList)

    def getAttack(self, index)-> list[tuple[int,int]]:
        return self.attacks[index]
    
class SpecialType(Enum):
    pass
class Special:
    specialType: SpecialType
    specials: list
    modifier: str
    specialMax:int

    def __init__(self, type, specialList, mod):
        #try to cast 
        self.specialType = SpecialType[type]
        self.specials = specialList
        self.modifier = mod
        self.specialMax = len(specialList)

    def getSpecial(self, index)-> list[tuple[int,int]]:
        return self.specials[index]
