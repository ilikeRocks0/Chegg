import UnitDataManager
import BoardStateManager
import GameDataManager
import CardStateManager
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
        unitPlace = MessageUnitPlace(playerID, unit, posX, posY)

        if(not self.__checkPlayerAndUnit(playerID, unit, posX, posY)):
            return None
        
        if(not self.cardData.hasCard(playerID, unit)):
            return None
        
        if(self.gameData.getMana(playerID) < self.unitData.getManaCost(unit)):
            return None
        
        if(not self.boardData.isEmpty(posX, posY)):
            return None

        return unitPlace
    
    
    def loadMessageMove(self, playerID:int, unit:str, posX:int, posY:int, newPosX:int, newPosY:int):
        unitMove = MessageUnitMove(playerID, unit, posX, posY, newPosX, newPosY)

        if(not self.__checkPlayerAndUnit(playerID, unit, posX, posY)):
            return None
        
        if(self.boardData.getUnitOnSpace(unit, playerID, posX, posY) == None):
            return None
        
        if(not self.boardData.getUnitOnSpace(unit, playerID, posX, posY).movedThisTurn 
           and self.gameData.getMana(playerID) < self.unitData.getMoveCostFirst(unit)):
            return None

        if(self.boardData.getUnitOnSpace(unit, playerID, posX, posY).movedThisTurn
           and self.gameData.getMana(playerID) < self.unitData.getMoveCostSecond(unit)):
            return None
        
        return unitMove
