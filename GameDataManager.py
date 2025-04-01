import EventHolder
class GameDataManager:
    PLAYER1 = 1
    PLAYER2 = 2
    MAX_DECK_SIZE = 15
    MAX_MANA = 6
    
    gameTurn: int 
    player1Mana: int
    player2Mana: int
    event: EventHolder

    def __init__(self, EH:EventHolder):
        self.gameTurn = 1
        self.player1Mana = 1
        self.player2Mana = 1
        self.event = EH

    def getMana(self, playerID) -> int:
        if (playerID == self.PLAYER1):
            return self.player1Mana         
        if (playerID == self.PLAYER2):
            return self.player2Mana
    
    #after player 2s turn
    def endRound(self) -> int:
        self.gameTurn+=1
        
        if (self.gameTurn <= self.MAX_MANA):
            self.player1Mana+=self.gameTurn
            self.player2Mana+=self.gameTurn
        else:
            self.player1Mana = self.MAX_MANA
            self.player1Mana = self.MAX_MANA