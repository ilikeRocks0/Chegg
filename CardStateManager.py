from UnitData import UnitData
from UnitDataManager import UnitDataManager
from GameDataManager import GameDataManager
import random
class CardStateManager:
    MAX_HAND_SIZE = 15
    unitManager: UnitDataManager
    gameManager: GameDataManager

    player1Deck: list[UnitData]
    player2Deck: list[UnitData]
    player1Hand: list[UnitData]
    player2Hand: list[UnitData]

    def __init__(self, UDM, GDM):
        self.unitManager = UDM
        self.gameManager = GDM
        self.player1Deck = list()
        self.player2Deck = list()
        self.player1Hand = list()
        self.player2Hand = list()

        
        
    def loadDataFromServer(self, p1D:list[str], p2D:list[str]):
        for unitName in p1D:
            self.player1Deck.append(self.unitManager.getUnit(unitName))

        for unitName in p2D:
            self.player2Deck.append(self.unitManager.getUnit(unitName))
        
        random.shuffle(self.player1Deck)
        random.shuffle(self.player2Deck)

    def drawCard(self, playerID) -> UnitData: 
        deck = None
        hand = None
        if (playerID == self.gameManager.PLAYER1):
            deck = self.player1Deck
            hand = self.player1Hand
        elif (playerID == self.gameManager.PLAYER2):
            deck = self.player2Deck
            hand = self.player2Hand

        if(len(deck) <= 0):
            return None
        else:
            unit = deck.pop()
            hand.append(unit)
            return unit
            # self.event.addEvent(Event.DRAW_CARD_NONE, playerID, unit)

    def drawCardForce(self, playerID, unit:str) -> UnitData: 
        deck = None
        if (playerID == self.gameManager.PLAYER1):
            deck = self.player1Deck
        elif (playerID == self.gameManager.PLAYER2):
            deck = self.player2Deck

        return self.__locateCard(deck, unit)
        
    #locates a card within the deck
    def __locateCard(self, deck:list[UnitData], unitName:str):
        for unit in deck:
            if (unit.name == unitName):
                return unit
        return None
        
    def hasCard(self, playerID, unitName:str) -> bool:
        hand = None
        if (playerID == self.gameManager.PLAYER1):
            hand = self.player1Hand
        elif (playerID == self.gameManager.PLAYER2):
            hand = self.player2Hand
        
        for unit in hand:
            if (unit.name == unitName):
                return True
        return False

        
