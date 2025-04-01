from enum import Enum, auto
from UnitData import Attack 
class UnitData:
    name: str
    cost: int
    move: list
    attack: Attack
    death: list
    place: list


class AttackType:
    ATTACK_SINGLE = auto()
    ATTACK_GROUP = auto()

class Attack:
    attackType: AttackType
    attacks: list
    modifier: str