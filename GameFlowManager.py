from GameStateManager import GameStateManager
from GameInputManager import GameInputManager
from GameDataManager import GameDataManager
from BoardStateManager import BoardStateManager
from UnitDataManager import UnitDataManager
from CardStateManager import CardStateManager
from GameInstance import GameInstance
from EventHolder import EventHolder

class GameFlowManager:
    def __init__(self, units:dict[str:dict], eventHolder:EventHolder):
        self.gameState = GameStateManager()
        self.unitData = UnitDataManager(units)
        self.gameData = GameDataManager(eventHolder)
        self.cardState = CardStateManager(self.unitData, self.gameData)
        self.boardState = BoardStateManager()
        self.input = GameInputManager(self.unitData, self.boardState, self.gameData, self.cardState)
        self.game = GameInstance(self.cardState, self.boardState, self.gameData, self.unitData)


    def loadDataFromServer(self, messageType:str, p1Deck:str, p2Deck:str):
        if(self.gameState.canGameStart()):
            initMessage = self.input.loadMessageInit(messageType, p1Deck, p2Deck)

            if(initMessage == None):
                return False
            
            self.game.loadData(initMessage.player1Deck, initMessage.player2Deck)

            self.gameState.gameStart()


    def __placeUnit(self, messageType:str, playerID:int, unit:str, posX:int, posY:int):
        placeMessage = self.input.loadMessagePlace(messageType, playerID, unit, posX, posY)

        if(placeMessage == None):
            return False
        
        self.game.placeUnit(placeMessage.playerID, placeMessage.unit, placeMessage.posX, placeMessage.posY)


    def p1VillagerPlacement(self, messageType:str, playerID:int, unit:str, posX:int, posY:int):
        if(self.gameState.canP1PlaceVillager()):
            self.__placeUnit(messageType, playerID, unit, posX, posY)
            self.gameState.p1PlaceVillager()

    
    def p2VillagerPlacement(self, messageType:str, playerID:int, unit:str, posX:int, posY:int):
        if(self.gameState.canP2PlaceVillager()):
            self.__placeUnit(messageType, playerID, unit, posX, posY)
            self.gameState.p2PlaceVillager()


    def __playerTurn(self, messageType:str, *arg):
        # do some stuff here depending on message type
        # also change game state if end turn
        pass


    def p1Turn(self, messageType:str, *arg):
        if(self.gameState.isP1Turn()):
            self.__playerTurn(messageType, arg)
            

    def p2Turn(self, messageType:str, *arg):
        if(self.gameState.isP2Turn()):
            self.__playerTurn(messageType, arg)
