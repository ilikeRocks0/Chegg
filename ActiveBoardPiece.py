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
        self.specialed = False
        self.posX = -1
        self.posY = -1

    def unitPlaced(self, posX, posY):
        self.posX = posX
        self.posY = posY

    def unitMoved(self, posX, posY):
        self.posX = posX
        self.posY = posY
        
        if(not self.movedOnce):
            self.movedOnce = True
        elif (not self.movedTwice):
            self.moveCostSecond = True

    def unitAttacked(self):
        self.attacked = True
    
    def unitSpecialed(self):
        self.special = True

    def endTurn(self):
        self.attacked = False
        self.movedOnce = False
        self.movedTwice = False
        self.special = False