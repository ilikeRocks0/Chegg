from GameInstance import GameInstance
from GameDataManager import GameDataManager
from GameStateManager import GameStateManager
from UnitDataManager import UnitDataManager
from enum import Enum, auto

class GameMessageManager:
    class TurnAction(Enum):
        PLACE = auto()
        ATTACK = auto()
        SPECIAL_ATTACK = auto()
        MOVE = auto()

    def __init__(self, gameState:GameStateManager, gameInstance:GameInstance, gameData:GameDataManager, unitData:UnitDataManager):
        self.gameState = gameState
        self.gameInstance = gameInstance
        self.gameData = gameData
        self.unitData = unitData

    
    def loadDataFromServer(self, playerID:int, p1Deck:dict[str], p2Deck:dict[str]):
        if(self.gameState.canGameStart()):
            self.gameInstance.loadData(playerID, p1Deck, p2Deck)
            self.gameState.gameStart()
            return True
        
        return False
    

    def __playerTurnAction(self, actionType:TurnAction, playerID:int, unit:str, posX:int, posY:int, *arg):
        validAction = False

        if(self.gameState.isP1Turn() and playerID == self.gameData.PLAYER1):
            validAction = True
        elif(self.gameState.isP2Turn() and playerID == self.gameData.PLAYER2):
            validAction = True

        if(validAction):
            if(actionType == self.TurnAction.PLACE):
                self.gameInstance.placeUnit(playerID, unit, posX, posY)
            elif(actionType == self.TurnAction.ATTACK):
                attackID = arg[0]
                self.gameInstance.attackUnit(playerID, unit, posX, posY, attackID)
            elif(actionType == self.TurnAction.SPECIAL_ATTACK):
                attackID = arg[0]
                self.gameInstance.specialAttackUnit(playerID, unit, posX, posY, attackID)
            elif(actionType == self.TurnAction.MOVE):
                newPosX = arg[0]
                newPosY = arg[1]
                self.gameInstance.moveUnit(playerID, unit, posX, posY, newPosX, newPosY)
            else:
                validAction = False

        return validAction

    
    def placeUnit(self, playerID:int, unit:str, posX:int, posY:int):
        # special case placing the villager
        if(self.gameState.canP1PlaceVillager() and playerID == self.gameData.PLAYER1 and unit == self.unitData.Villager):
            self.gameInstance.placeUnit(playerID, unit, posX, posY)
            self.gameState.p1PlaceVillager()
            return True
        elif(self.gameState.canP1PlaceVillager() and playerID == self.gameData.PLAYER2 and unit == self.unitData.Villager):
            self.gameInstance.placeUnit(playerID, unit, posX, posY)
            self.gameState.p2PlaceVillager()
            return True
        
        return self.__playerTurnAction(self.TurnAction.PLACE, playerID, unit, posX, posY)
    

    def attackUnit(self, playerID:int, unit:str, posX:int, posY:int, attackID:int):
        return self.__playerTurnAction(self.TurnAction.ATTACK, playerID, unit, posX, posY, attackID)

    def specialAttackUnit(self, playerID:int, unit:str, posX:int, posY:int, attackID:int):
        return self.__playerTurnAction(self.TurnAction.SPECIAL_ATTACK, playerID, unit, posX, posY, attackID)

    def moveUnit(self, playerID:int, unit:str, posX:int, posY:int, newPosX:int, newPosY:int):
        return self.__playerTurnAction(self.TurnAction.SPECIAL_ATTACK, playerID, unit, posX, posY, newPosX, newPosY)


    def endTurn(self, playerID:int):
        if(playerID == self.gameData.PLAYER1):
            self.gameState.p1EndTurn()
            return True
        elif(playerID == self.gameData.PLAYER2):
            self.gameState.p2EndTurn()
            return True

        return False
    