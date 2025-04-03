class MessageBase:
    def __init__(self, mt:str):
        self.messageType = mt


class MessageInit(MessageBase):
    def __init__(self, mt:str, p1Deck:dict[str], p2Deck:dict[str]):
        super(mt)
        self.player1Deck = p1Deck
        self.player2Deck = p2Deck

class MessageUnit(MessageBase):
    def __init__(self, mt:str, pID:int, unit:str, posX:int, posY:int):
        super(mt)
        self.playerID = pID
        self.unit = unit
        self.posX = posX
        self.posY = posY


#name is just for representation
class MessageUnitPlace(MessageUnit):
    pass


class MessageUnitMove(MessageUnit):
    def __init__(self, mt:str, pID:int, unit:str, posX:int, posY:int, newPosX:int, newPosY:int):
        super(mt, pID, unit, posX, posY)
        self.newPosX = newPosX
        self.newPosY = newPosY

class MessageUnitAttack(MessageUnit):
    def __init__(self, mt:str, pID:int, unit:str, posX:int, posY:int, attackNum:int):
        super(mt, pID, unit, posX, posY)
        self.attackNum = attackNum

class MessageUnitSpecial(MessageUnit):
    def __init__(self, mt:str, pID:int, unit:str, posX:int, posY:int, specialNum:int):
        super(mt, pID, unit, posX, posY)
        self.specialNum = specialNum
         