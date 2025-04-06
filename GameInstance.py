from GameDataManager import GameDataManager
from UnitDataManager import UnitDataManager
from CardStateManager import CardStateManager
from BoardStateManager import BoardStateManager
from ActiveBoardPiece import ActiveBoardPiece
from DeathModifiers import DeathModifiers
from SpecialMoves import SpecialMoves
class GameInstance:
    def __init__(self, cardData:CardStateManager, boardData:BoardStateManager, gameData:GameDataManager, unitData:UnitDataManager):
        self.gameData = gameData
        self.unitData = unitData
        self.cardData = cardData
        self.boardData = boardData

        #components for easier state management
        self.deathMod = DeathModifiers()
        self.specialMov = SpecialMoves()

    def loadData(self, p1Deck, p2Deck):
        self.cardData.loadDataFromServer(p1Deck, p2Deck)

    def placeUnit(self, playerID, unit, posX, posY):
        newUnit:ActiveBoardPiece = self.unitData.getActiveUnit(unit)
        self.boardData.placeUnit(newUnit, posX, posY)   
        newUnit.unitPlaced(posX, posY)

        #attack interface for users
    def attackUnit(self, playerID, unit, posX, posY, attackID):
        activeUnit:ActiveBoardPiece = self.boardData.getUnitOnSpace(posX, posY)
        attack = activeUnit.getAttack(attackID)
        self.handleAttackUnits(activeUnit, attack)
        activeUnit.unitAttacked()
        
    def specialAttackUnit(self, playerID, unit, posX, posY, specialID):
        activeUnit:ActiveBoardPiece = self.boardData.getUnitOnSpace(posX, posY)
        special = activeUnit.getSpecial(specialID)
        self.specialMov.runModifier(self, activeUnit, special, activeUnit.special.specialType)
        activeUnit.unitSpecialed()

    def moveUnit(self):
        pass

    def handleAttackUnits(self, activeUnit:ActiveBoardPiece, attack):
        #can either be int or list[int]
        attackedUnits:list[ActiveBoardPiece] = self.boardData.attackUnit(activeUnit.attack.attackType, activeUnit.posX, activeUnit.posY, attack)
        self.handleDeathUnits(attackedUnits)


    def handleDeathUnits(self, attackedUnits:list[ActiveBoardPiece]):
        #remove them from board
        for unit in attackedUnits:
            self.boardData.deadUnit(unit.posX, unit.posX)
        
        for unit in attackedUnits:
            self.deathMod.runModifier(self, unit, unit.death)