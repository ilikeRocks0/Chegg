from BoardTile import BoardTile

class BoardStateManager:
    MIN_X = 0
    MAX_X = 10
    MIN_Y = 0
    MAX_Y = 8

    def __init__(self):
        # Board holds type 'BoardTile'
        self.board = [[None] * self.MAX_Y] * self.MAX_X


    def attackUnit(self, posX:int, posY:int, attacks:list):
        attackedUnits = list()
        for attackPos in attacks:
            attackPosX = posX + attackPos[0]
            attackPosY = posY + attackPos[1]
            self.board[attackPosX][attackPosY] = None
            attackedUnits.append(tuple(attackPosX, attackPosY))

        return attackedUnits
    

    def moveUnit(self, posX:int, posY:int, newPosX:int, newPosY:int):
        movedUnit = self.board[posX][posY]
        self.board[posX][posY] = None
        self.board[newPosX][newPosY] = movedUnit

        if(not movedUnit.movedOnce):
            movedUnit.movedOnce = True
        elif(not movedUnit.movedTwice):
            movedUnit.movedTwice = True


    def placeUnit(self, unit:BoardTile, posX:int, posY:int):
        self.board[posX][posY] = unit


    def isEmpty(self, posX:int, posY:int):
        return self.board[posX][posY] == None
    

    def getUnitOnSpace(self, posX:int, posY:int):
        return self.board[posX][posY]