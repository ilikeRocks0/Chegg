from GameDataManager import GameDataManager
from UnitDataManager import UnitDataManager
from CardStateManager import CardStateManager
from BoardStateManager import BoardStateManager

class GameInstance:
    def __init__(self, cardData:CardStateManager, boardData:BoardStateManager, gameData:GameDataManager, unitData:UnitDataManager):
        self.gameData = gameData
        self.unitData = unitData
        self.cardData = cardData
        self.boardData = boardData

    def loadData(self, p1Deck, p2Deck):
        self.cardData.loadDataFromServer(p1Deck, p2Deck)

    def placeUnit(self, playerID, unit, posX, posY):
        newUnit = self.unitData.getActiveUnit(unit)

        self.boardData.placeUnit(newUnit, posX, posY)

        pass

    def attackUnit(self):
        pass

    def specialAttackUnit(self):
        pass

    def moveUnit(self):
        pass