from UnitData import UnitData

class ActiveBoardPiece(UnitData):
    def __init__(self, playerID: int, parent: UnitData):
        # Calls the constructor of UnitData to initialize attributes
        super().__init__(  
            parent.name,
            parent.cost,
            parent.move,
            parent.attack,
            parent.special,
            parent.death
        )
        
        self.owner = playerID
        self.movedOnce = False
        self.movedTwice = False
        self.attacked = False



