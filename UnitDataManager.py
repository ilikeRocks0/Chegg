from UnitData import UnitData, Attack, Special
from ActiveBoardPiece import ActiveBoardPiece
class UnitDataManager:
    VILLAGER:str = "villager" 
    unitList: dict[str, UnitData]
    

    def __init__(self, units: dict[str, dict]):
        for unit in units:
            if ("attacks" in unit): 
                newAttacks = Attack(unit["attacks"]["attackType"], unit["attacks"]["attacksList"], unit["attacks"]["modifiers"]) 
            if ("special" in unit):
                newSpecial = Special(unit["special"]["specialType"], unit["specials"]["specialsList"], unit["specials"]["modifiers"]) 

            newUnit = UnitData(unit["name"], unit["cost"], unit["moves"], newAttacks, newSpecial, unit["death"])
            
            if(unit["modifiers"] == "extra_move_cost"):
                newUnit.moveCostFirst+=1
                newUnit.moveCostSecond+=1
            self.unitList[newUnit.name, newUnit]
        
    def checkUnit(self, unitName: str):
        for unit in self.unitList.keys():
            if (unit == unitName):
                return True
        return False
    
    def getUnit(self, unitName:str):
        for unit in self.unitList.keys():
            if (unit == unitName):
                return self.unitList[unit]
        return None
    
    def getActiveUnit(self, playerID, unitName:str):
        for unit in self.unitList.keys():
            if (unit == unitName):
                return ActiveBoardPiece(playerID, self.unitList[unit])
        return None