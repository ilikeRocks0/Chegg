
from UnitData import DeathType 
from ActiveBoardPiece import ActiveBoardPiece
from EventHolder import EventHolder
from GameInstance import GameInstance
#holds all the modifier codes
class DeathModifiers:

    def runModifier(self, gameInstance:GameInstance, unit:ActiveBoardPiece, type: DeathType):
        if (DeathType[type] == DeathType.EXPLODE):
            self.explode(gameInstance, unit)
        

    def explode(self, gameInstance:GameInstance, activeUnit:ActiveBoardPiece):
        attacks:list[tuple[int,int]] = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        #creeper kills everything around it
        gameInstance.handleAttackUnits(activeUnit, attacks)
