import GameState

class GameStateManager:
    def __init__(self):
        self.currState = GameState.SERVER_WAIT


    def canGameStart(self):
        return self.currState == GameState.SERVER_WAIT

    def canP1PlaceVillager(self):
        return self.currState == GameState.P1_VILL_PLACE
  
    def canP2PlaceVillager(self):
        return self.currState == GameState.P2_VILL_PLACE
    
    def isP1Turn(self):
        return self.currState == GameState.P1_TURN
    
    def isP2Turn(self):
        return self.currState == GameState.P2_TURN
    

    def gameStart(self):
        if(self.canGameStart()):
            self.currState = GameState.P1_VILL_PLACE

    def p1PlaceVillager(self):
        if(self.canP1PlaceVillager()):
            self.currState = GameState.P2_VILL_PLACE

    def p2PlaceVillager(self):
        if(self.canP2PlaceVillager()):
            self.currState = GameState.P1_TURN

    def p1EndTurn(self):
        if(self.isP1Turn()):
            self.currState = GameState.P2_TURN

    def p2EndTurn(self):
        if(self.isP2Turn()):
            self.currState = GameState.P1_TURN
            