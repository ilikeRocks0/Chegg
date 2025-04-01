from UnitData import UnitData

class ActiveBoardPiece(UnitData):
    def __init__(self, playerID:int, parent:UnitData):
        self.owner = playerID
        self.movedOnce = False
        self.movedTwice = False
        self.name = parent.name
        self.cost = parent.cost
        self.move = parent.move
        self.attack = parent.attack
        self.death = parent.death
        self.attack = parent.attack



