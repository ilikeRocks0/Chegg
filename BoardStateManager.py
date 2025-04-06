from BoardTile import BoardTile
from ActiveBoardPiece import ActiveBoardPiece
from UnitData import AttackType
class BoardStateManager:
    MIN_X = 0
    MAX_X = 10
    MIN_Y = 0
    MAX_Y = 8
    
    def __init__(self):
        self.allunits:list[ActiveBoardPiece] = []
        # Board holds type 'BoardTile'
        self.board = [[None] * self.MAX_Y] * self.MAX_X


    def attackUnit(self, attackType:AttackType, posX:int, posY:int, attacks):
        if (AttackType.ATTACK_SINGLE == attackType):
            return self.attackUnitSingle(posX, posY, attacks)
        if (AttackType.ATTACK_GROUP == attackType):
            return self.attackUnitList(posX, posY, attacks)

    def attackUnitList(self, posX:int, posY:int, attacks:list):
        attackingUnit:ActiveBoardPiece = self.board[posX][posY]
        attackedUnits = list()
        for attackPos in attacks:
            if(self.MIN_X < posX < self.MAX_X and self.MIN_Y < posY < self.MAX_Y):
                attackPosX = posX + attackPos[0]
                attackPosY = posY + attackPos[1]
                self.board[attackPosX][attackPosY] = None
                attackedUnits.append(tuple(attackPosX, attackPosY))
        
        return attackedUnits
    
    def attackUnitSingle(self, posX:int, posY:int, attacks:tuple[int, int]):
        attackingUnit:ActiveBoardPiece = self.board[posX][posY]
        attackedUnits = list()
        if(self.MIN_X < posX < self.MAX_X and self.MIN_Y < posY < self.MAX_Y):
            attackPosX = posX + attacks[0]
            attackPosY = posY + attacks[1]
            self.board[attackPosX][attackPosY] = None
            attackedUnits.append(tuple(attackPosX, attackPosY))
        
        return attackedUnits
    

    def moveUnit(self, posX:int, posY:int, newPosX:int, newPosY:int):
        movedUnit:ActiveBoardPiece = self.board[posX][posY]
        self.board[posX][posY] = None
        self.board[newPosX][newPosY] = movedUnit

    def placeUnit(self, unit:ActiveBoardPiece, posX:int, posY:int):
        self.board[posX][posY] = unit
        self.allunits.append(unit)
        unit.unitPlaced(posX, posY)


    def isEmpty(self, posX:int, posY:int):
        return self.board[posX][posY] == None
    

    def getUnitOnSpace(self, posX:int, posY:int):
        return self.board[posX][posY]
    
    
    def deadUnit(self, posX:int, posY:int):
        #dont remove unit position in activeBoardPiece
        unit:ActiveBoardPiece = self.getUnitOnSpace(posX, posY)
        self.allunits.remove(unit)
        self.board[posX][posY] = None