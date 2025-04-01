from UnitDataManager import UnitDataManager 
from UnitData import UnitData
from BoardStateManager import BoardStateManager
from GameDataManager import GameDataManager
from CardStateManager import CardStateManager
from MessageObjects import *
import json

class GameInputManager:
    def __init__(self, udm:UnitDataManager, bdm:BoardStateManager, gdm:GameDataManager, csm:CardStateManager):
        self.unitData = udm
        self.boardData = bdm
        self.gameData = gdm
        self.cardData = csm

    def __validateDeck(self, deck:dict[str]):
        # validate units are real and cards add up to 15
        cardCount = 0
        containsVillager = False
        for key in deck.keys():
            if(self.unitData.checkUnit(key)):
               if(deck[key] == self.unitData.Villager):
                   containsVillager = True

               cardCount = cardCount + deck[key]
            else:
                return False
            
        if(not containsVillager):
            return False
        if(cardCount != self.gameData.MAX_DECK_SIZE):
            return False
        
        return True


    def loadMessageInit(self, messageType:str, p1Deck:str, p2Deck:str):
        init = None
        
        if(messageType == "GameStart"):
            player1Deck = json.loads(p1Deck)
            player2Deck = json.loads(p2Deck)

            if(self.__validateDeck(player1Deck) and self.__validateDeck(player2Deck)):
                init = MessageInit(messageType, player1Deck, player2Deck)

            
        return init


    def __checkPlayerAndUnit(self, playerID:int, unit:str, posX:int, posY:int):
        if(playerID != self.gameData.PLAYER1 or playerID != self.gameData.PLAYER2):
            return False
        
        if(self.unitData.checkUnit(unit)):
            return False
        
        if(self.boardData.MAX_X < posX or self.boardData.MIN_X > posX):
            return False
        
        if(self.boardData.MAX_Y < posY or self.boardData.MIN_Y > posY):
            return False
        
        return True


    def loadMessagePlace(self, playerID:int, unit:str, posX:int, posY:int):
        if(not self.__checkPlayerAndUnit(playerID, unit, posX, posY)):
            return None
        
        if(not self.cardData.hasCard(playerID, unit)):
            return None
        
        if(self.gameData.getMana(playerID) < self.unitData.getUnit(unit).cost):
            return None
        
        if(not self.boardData.isEmpty(posX, posY)):
            return None

        return MessageUnitPlace(playerID, unit, posX, posY)
    
    
    def loadMessageMove(self, playerID:int, unit:str, posX:int, posY:int, newPosX:int, newPosY:int):
        if(not self.__checkPlayerAndUnit(playerID, unit, posX, posY)):
            return None
        
        boardUnit = self.boardData.getUnitOnSpace(posX, posY)
        
        if(boardUnit == None):
            return None
        
        if(boardUnit.name != unit):
            return None
        
        if(boardUnit.owner != playerID):
            return None

        if(not unit.movedThisTurn 
           and self.gameData.getMana(playerID) < self.unitData.getUnit(unit).moveCostFirst):
            return None

        if(unit.movedThisTurn
           and self.gameData.getMana(playerID) < self.unitData.getUnit(unit).moveCostSecond):
            return None
        
        return MessageUnitMove(playerID, unit, posX, posY, newPosX, newPosY)
