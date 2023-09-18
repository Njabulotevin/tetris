from block import Block
from position import Position

positions = {
        0 : Position(0,0),
        1 : Position(0,1),
        2 : Position(0,2),
        3 : Position(1,0),
        4 : Position(1,1),
        5 : Position(1,2),
        6 : Position(2,0),
        7 : Position(2,1),
        8 : Position(2,2),
    }


class LBlock(Block):
    def __init__(self) -> None:
        super().__init__(id=1)
        self.cells = {
            0:[positions[2], positions[3], positions[4], positions[5]],
            1:[positions[1], positions[4], positions[7], positions[8]],
            2:[positions[3], positions[4], positions[5], positions[6]],
            3:[positions[0], positions[1], positions[4], positions[7]],
        }
        self.move(0, 3)



class JBlock(Block):
    def __init__(self) -> None:
        super().__init__ (id = 2)
        self.cells = {
            0:[positions[0], positions[3], positions[4], positions[5]],
            1:[positions[1], positions[2], positions[4], positions[7]],
            2:[positions[2], positions[3], positions[4], positions[5]],
            3:[positions[1], positions[4], positions[7], positions[8]],
        }
        self.move(0, 3)



class IBlock(Block):
    def __init__(self) -> None:
        super().__init__(id=3)
        self.cells = {
            0:[Position(1,0), Position(1,1), Position(1,2), Position(1,3)],
            1:[Position(0,2), Position(1,2), Position(2,2), Position(3,2)],
            2:[Position(2,0), Position(2,1), Position(2,2), Position(2,3)],
            3:[Position(0,0), Position(1,0), Position(2,0), Position(3,0)],
        }
        self.move(-1, 3)


class OBlock(Block):
    def __init__(self) -> None:
        super().__init__(id=4)
        self.cells = {
            0:[Position(0,0), Position(0,1), Position(1,0), Position(1,1)],
            1:[Position(0,0), Position(0,1), Position(1,0), Position(1,1)],
            2:[Position(0,0), Position(0,1), Position(1,0), Position(1,1)],
            3:[Position(0,0), Position(0,1), Position(1,0), Position(1,1)],
        }
        self.move(0, 3)

# TODO fix rotation
class SBlock(Block):
    def __init__(self) -> None:
        super().__init__(id=5)
        self.cells = {
            0:[positions[1], positions[2], positions[4], positions[5]],
            1:[positions[2], positions[4], positions[5], positions[6]],
            2:[positions[0], positions[4], positions[5], positions[8]],
            3:[positions[2], positions[3], positions[4], positions[6]],
        }
        self.move(0, 3)

class TBlock(Block):
    def __init__(self) -> None:
        super().__init__(id=6)
        self.cells = {
            0:[positions[1], positions[3], positions[4], positions[5]],
            1:[positions[1], positions[4], positions[5], positions[7]],
            2:[positions[3], positions[4], positions[5], positions[7]],
            3:[positions[1], positions[3], positions[4], positions[7]],
        }
        self.move(0, 3)      

class ZBlock(Block):
    def __init__(self) -> None:
        super().__init__(id=7)
        self.cells = {
            0:[positions[0], positions[1], positions[4], positions[5]],
            1:[positions[2], positions[4], positions[5], positions[7]],
            2:[positions[3], positions[4], positions[7], positions[8]],
            3:[positions[1], positions[3], positions[4], positions[6]],
        }
        self.move(0, 3)