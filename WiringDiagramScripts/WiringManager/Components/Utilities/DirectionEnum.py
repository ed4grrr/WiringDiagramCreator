from enum import Enum

class DirectionEnum(Enum):
    """
    Enum for the direction of a connection.
    """
    
    LEFT = "left"
    RIGHT = "right"
    TOP = "top"
    BOTTOM = "bottom"
    UP = "up"
    DOWN = "down"
    


    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__class__.__name__

    def __eq__(self, other):
        return self.__class__.__name__ == other.__class__.__name__

    def __ne__(self, other):
        return self.__class__.__name__ != other.__class__.__name__
DOWN = DirectionEnum.DOWN
UP = DirectionEnum.UP
LEFT = DirectionEnum.LEFT
RIGHT = DirectionEnum.RIGHT
TOP = DirectionEnum.TOP
BOTTOM = DirectionEnum.BOTTOM