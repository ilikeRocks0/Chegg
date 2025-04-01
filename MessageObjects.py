class MessageBase:
    def __init__(self, mt:str):
        self.messageType = mt


class MessageInit(MessageBase):
    def __init__(self, mt:str, p1Deck:dict[str], p2Deck:dict[str]):
        super(mt)
        self.player1Deck = p1Deck
        self.player2Deck = p2Deck


class MessageUnitPlace(MessageBase):
    def __init__(self, mt:str, pID:int, unit:str, posX:int, posY:int):
        super(mt)
        self.playerID = pID
        self.posX = posX
        self.posY = posY


class MessageUnitMove(MessageBase):
    def __init__(self, mt:str, newPosX:int, newPosY:int):
        super(mt)
        self.newPosX = newPosX
        self.newPosY = newPosY
