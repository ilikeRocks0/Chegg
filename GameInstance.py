from GameDataManager import GameDataManager
from UnitDataManager import UnitDataManager
from CardStateManager import CardStateManager
from BoardStateManager import BoardStateManager
from enum import Enum, auto

class GameInstance:
    def __init__(self, cardData:CardStateManager, boardData:BoardStateManager, gameData:GameDataManager, unitData:UnitDataManager):
        self.gameData = gameData
        self.unitData = unitData
        self.cardData = cardData
        self.boardData = boardData

    def loadData(self, playerID, p1Deck, p2Deck):
        pass

    def placeUnit(self):
        pass

    def attackUnit(self):
        pass

    def specialAttackUnit(self):
        pass

    def moveUnit(self):
        pass