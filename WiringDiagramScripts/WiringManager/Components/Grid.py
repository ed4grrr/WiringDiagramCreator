
from Coordinates import Coordinates
from math import sqrt, pow

class CellAlreadySetError(Exception):
    """ Exception raised when a cell is already set. """
    def __init__(self, message:str):
        self.message = message
        super().__init__(self.message)

class Grid:
    """ this class uses a sparse matrix to store only the used pixels of the grid. """
    def __init__(self, width:int, height:int):
        """
        Creates a new Grid object.
        Args:
            width (int): The width of the grid.
            height (int): The height of the grid.
        """
        self.width = width
        self.height = height
        self.centerPixel = (width//2, height//2)
        self.grid = {}

    def isLongestPath(self, start:Coordinates, end:Coordinates) -> bool:
        """
        Given two points, determines the which of the two (distance to x end or distance to y end) is longer.
        Args:
            start (Coordinates): The starting coordinates.
            end (Coordinates): The ending coordinates.
            Returns:
            true if the x distance is longer than the y distance, false otherwise."""
        return abs(end.x - start.x) > abs(end.y - start.y)
    
    
    def setPixelLine(self, start:Coordinates, end:Coordinates, label:str):
        """
        Sets a line of pixels on the grid.
        Args:
            start (Coordinates): The starting coordinates of the line.
            end (Coordinates): The ending coordinates of the line.
        """
        # create every point between start and end
        xSlope = int((end.y - start.y))
        ySlope =int((end.x - start.x))

        distanceBetweenPoints = int(sqrt(pow(end.x - start.x, 2) + pow(end.y - start.y, 2)))

        points = [start]
        for i in range(1, distanceBetweenPoints):
            points.append(Coordinates("Point", start.x + int(i * ySlope / distanceBetweenPoints), start.y + int(i * xSlope / distanceBetweenPoints))
            )
        for point in points:
            self.setPixel(point)


    def setPixel(self, coord:Coordinates):
        """
        Sets a pixel on the grid. If the pixel is already set, an exception is raised.
        Args:
            x (int): The x coordinate of the pixel.
            y (int): The y coordinate of the pixel.
        """
        x=coord.x
        y=coord.y
        if x < 0 or x > self.width or y < 0 or y > self.height:
            raise ValueError(f"The pixel ({x}, {y}) is out of the grid bounds.")
        if x not in self.grid:
            self.grid[x] = {}
        if y in self.grid[x]:
            pass
            #raise CellAlreadySetError(f"The pixel ({x}, {y}) is already set.")
        self.grid[x][y] = True
   

    def setPixels(self, pixels:list[Coordinates]):
        """
        Sets multiple pixels on the grid.
        Args:
            pixels (list): A list of pixel coordinates to set.
        """
        for pixel in pixels:
            self.setPixel(pixel)
    
    def clearPixel(self, coord:Coordinates):
        """
        Clears a pixel on the grid.
        Args:
            x (int): The x coordinate of the pixel.
            y (int): The y coordinate of the pixel.
        """
        x=coord.x
        y=coord.y

        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            raise ValueError(f"The pixel ({x}, {y}) is out of the grid bounds.")
        if x in self.grid and y in self.grid[x]:
            del self.grid[x][y]
    
    def isPixelSet(self, coord:Coordinates) -> bool:
        """
        Checks if a pixel is set on the grid.
        Args:
            x (int): The x coordinate of the pixel.
            y (int): The y coordinate of the pixel.
        Returns:
            bool: True if the pixel is set, False otherwise.
        """
        x=coord.x
        y=coord.y
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            raise ValueError(f"The pixel ({x}, {y}) is out of the grid bounds.")
        if x in self.grid and y in self.grid[x]:
            return True
        return False
    
    def getGrid(self) -> dict[int, dict[int, bool]]:
        """
        Returns the grid.
        Returns:
            dict: The grid.
        """
        return self.grid
    
    def getWidth(self) -> int:
        """
        Returns the width of the grid.
        Returns:
            int: The width of the grid.
        """
        return self.width
    
    def getHeight(self) -> int:
        """
        Returns the height of the grid.
        Returns:
            int: The height of the grid.
        """
        return self.height
    

