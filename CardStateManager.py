from UnitData import UnitData
import UnitDataManager
import GameDataManager
import EventHolder
import random
from EventData import Event
class CardStateManager:
    unitManager: UnitDataManager
    gameManager: GameDataManager
    event: EventHolder

    MAX_HAND_SIZE = 15
    player1Deck: list[UnitData]
    player2Deck: list[UnitData]
    player1Hand: list[UnitData]
    player2Hand: list[UnitData]

    def __init__(self, UDM, GDM, EH,p1D:list[str], p2D:list[str]):
        self.unitManager = UDM
        self.gameManager = GDM
        self.event = EH
        self.player1Deck = list()
        self.player2Deck = list()
        self.player1Hand = list()
        self.player2Hand = list()

        for unitName in p1D:
            self.player1Deck.append(UDM.getUnit(unitName))

        for unitName in p2D:
            self.player2Deck.append(UDM.getUnit(unitName))
        
        random.shuffle(self.player1Deck)
        random.shuffle(self.player2Deck)
        

    def drawCard(self, playerID, amount): 
        deck = None
        hand = None
        if (playerID == self.gameManager.PLAYER1):
            deck = self.player1Deck
            hand = self.player1Hand
        elif (playerID == self.gameManager.PLAYER2):
            deck = self.player2Deck
            hand = self.player2Hand

        for num in range(amount):
            if(len(deck) <= 0):
                self.event.addEvent(Event.DRAW_CARD_NONE, playerID)
            else:
                unit = deck.pop()
                hand.append(unit)
                self.event.addEvent(Event.DRAW_CARD_NONE, playerID, unit)


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

        
