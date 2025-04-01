from enum import Enum, auto

class GameState(Enum):
    SERVER_WAIT = auto()
    P1_VILL_PLACE = auto()
    P2_VILL_PLACE = auto()
    P1_TURN = auto()
    P2_TURN = auto()
    P1_WIN = auto()
    P2_WIN = auto()
