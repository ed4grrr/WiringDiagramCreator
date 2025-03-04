import math

class Coordinates:
    def __init__(self, label:str, x: int | float, y: int | float):
        """
        Creates a new Coordinates object representing a set of coordinates.
        
        Args:
        
            x (int): The x-coordinate.
            y (int): The y-coordinate.
        """
        self.label = label
        self.x = x
        self.y = y

    def returnLabel(self):
        """
        Returns the label of the Coordinates object.
        
        Returns:
        
            str: The label.
        """
        return self.label
    
    def setLabel(self, newLabel:str):
        """
        Sets the label of the Coordinates object.
        
        Args:
        
            newLabel (str): The new label.
        """
        self.label = newLabel

    def returnCoordinates(self):
        """
        Returns the coordinates object's attributes within a dictionary.
        
        Returns:
        
            dict: The coordinates object's attributes.
        """
        return {"x": self.x, "y": self.y}
    
    def returnCoordinatesTuple(self):
        """
        Returns the coordinates object's attributes within a tuple.
        
        Returns:
        
            tuple: The coordinates object's attributes.
        """
        return (self.x, self.y)
    
    def returnYCoordinate(self):
        """
        Returns the y-coordinate of the Coordinates object.
        
        Returns:
        
            int: The y-coordinate.
        """
        return self.y   
    
    def returnXCoordinate(self):
        """
        Returns the x-coordinate of the Coordinates object.
        
        Returns:
        
            int: The x-coordinate.
        """
        return self.x
    
    def setCoordinates(self, newX: int | float, newY: int | float):
        """
        Sets the coordinates of the Coordinates object.
        
        Args:
        
            newX (int): The new x-coordinate.
            newY (int): The new y-coordinate.
        """
        self.x = newX
        self.y
    
    def setYCoordinate(self, newY: int | float):
        """
        Edits the y-coordinate of the Coordinates object.
        
        Args:
        
            newY (int): The new y-coordinate.
        """
        self.y = newY

    def setXCoordinate(self, newX: int | float):
        """
        Edits the x-coordinate of the Coordinates object.
        
        Args:
        
            newX (int): The new x-coordinate.
        """
        self.x = newX
    def __eq__(self, other):
        
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, other):
        
        return self.x != other.x or self.y != other.y
    
    def __repr__(self):
        return f"Coordinates({self.x}, {self.y})"
    
    def __str__(self):
        return f"Coordinates: ({self.x}, {self.y})"
    
    def __hash__(self): 
        return hash((self.x, self.y))
    
    def _checkXYExistence(self, other:dict[str, int | float]):
        if not "x" in other.keys():
            other["x"] = 0
        if not "y" in other.keys():
            other["y"] = 0
    
    def _modifyUnaccceptableZeros(self, other:dict[str, int | float]):
        if other["x"] == 0:
            other["x"] = 1
        if other["y"] == 0:
            other["y"] = 1

    def __add__(self, other:dict[str, int | float]):
        
        self._checkXYExistence(other)
    
        return Coordinates(self.x + other["x"], self.y + other["y"])
    
    def __sub__(self, other:dict[str, int | float]):
        
        self._checkXYExistence(other)
    
        return Coordinates(self.x - other["x"], self.y - other["y"])
    
    def __mul__(self, other:dict[str, int | float]):
        
        self._checkXYExistence(other)
        self._modifyUnaccceptableZeros(other)
    
        return Coordinates(self.x * other["x"], self.y * other["y"])
    def __truediv__(self, other:dict[str, int | float]):
        
        self._checkXYExistence(other)
        self._modifyUnaccceptableZeros(other)
        return Coordinates(self.x / other["x"], self.y / other["y"])
    
    def __floordiv__(self, other:dict[str, int | float]):
        
        self._checkXYExistence(other)
        self._modifyUnaccceptableZeros(other)
        return Coordinates(self.x // other["x"], self.y // other["y"])
    
    def __mod__(self, other:dict[str, int | float]):
        
        self._checkXYExistence(other)
        self._modifyUnaccceptableZeros(other)

        return Coordinates(self.x % other["x"], self.y % other["y"])
    
    def __pow__(self, other:dict[str, int | float]):
        
        self._checkXYExistence(other)
        self._modifyUnaccceptableZeros(other)

        return Coordinates(self.x ** other["x"], self.y ** other["y"])
    
    def __neg__(self):
        return Coordinates(-self.x, -self.y)
    
    def __pos__(self):
        return Coordinates(+self.x, +self.y)
    
    def __abs__(self):
        return Coordinates(abs(self.x), abs(self.y))
    
    def __round__(self, n:int):
        return Coordinates(round(self.x, n), round(self.y, n))
    
    def __floor__(self):
        return Coordinates(math.floor(self.x), math.floor(self.y))
    def __ceil__(self):
        return Coordinates(math.ceil(self.x), math.ceil(self.y))
    