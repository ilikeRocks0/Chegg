from UnitData import UnitData

class ActiveBoardPiece(UnitData):
    def __init__(self, playerID:int):
        self.owner = playerID
        self.movedOnce = False
        self.movedTwice = False


