from UnitData import SpecialType 
from ActiveBoardPiece import ActiveBoardPiece
from EventHolder import EventHolder
from GameInstance import GameInstance

class SpecialMoves:
    def runModifier(self, gameInstance:GameInstance, unit:ActiveBoardPiece, location:tuple[int, int], type: SpecialType):
        if (SpecialType[type] == SpecialType.EXPLODE):
            self.explode(gameInstance, unit, location)

    def explode(self, gameInstance:GameInstance, activeUnit, location):
        attacks:list[tuple[int,int]] = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        #creeper kills everything around it and itself
        gameInstance.boardData.deadUnit(location)
        gameInstance.handleAttackUnits(activeUnit, attacks)